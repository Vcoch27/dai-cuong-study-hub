"""Check bank integrity and report superficial answer cues, not item difficulty."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
CUES = re.compile(r"\b(?:chỉ(?!\s+(?:đạo|ra|tiêu)\b)|hoàn toàn|tuyệt đối|duy nhất|luôn luôn|mọi)\b", re.I)


def metrics(questions):
    longest = shortest = 0.0
    uniquely_longest = 0
    cue_ids, length_ids = [], []
    for q in questions:
        lengths = [len(c) for c in q["choices"]]
        key = lengths[q["answer"]]
        if key == max(lengths):
            longest += 1 / lengths.count(key)
            uniquely_longest += lengths.count(key) == 1
        if key == min(lengths):
            shortest += 1 / lengths.count(key)
        if any(CUES.search(c) for i, c in enumerate(q["choices"]) if i != q["answer"]):
            cue_ids.append(q["id"])
        others = [n for i, n in enumerate(lengths) if i != q["answer"]]
        if key > 1.5 * max(others) or max(lengths) > 2 * min(lengths):
            length_ids.append(q["id"])
    return {
        "questions": len(questions),
        "correct_uniquely_longest": uniquely_longest,
        "pick_longest_accuracy_percent": round(100 * longest / len(questions), 2),
        "pick_shortest_accuracy_percent": round(100 * shortest / len(questions), 2),
        "distractor_cue_ids": cue_ids,
        "length_review_ids": length_ids,
    }


def audit(data):
    questions, forms = data["questions"], data["examForms"]
    by_id = {q["id"]: q for q in questions}
    assert len(questions) == len(by_id) == 249
    assert len({q["question"] for q in questions}) == len(questions)
    slides = {(s["file"], s["slide"]): s["text"] for s in data["slidePages"]}
    slide_pages = {(s["file"], s["slide"]): s for s in data["slidePages"]}
    assert len(slide_pages) == 125
    for page in slide_pages.values():
        assert page["image"].startswith(f"/slides/chapter-{page['chapter']}/")
        assert page["image"].endswith(f"page-{page['slide']:03}.webp")
        assert (ROOT / "dist" / page["image"].lstrip("/")).is_file()
        assert page["imageWidth"] > 1000 and page["imageHeight"] > 500
    for q in questions:
        assert q["chapter"] in (1, 2, 3, 4), q["id"]
        assert len(q["choices"]) == len(set(q["choices"])) == 4, q["id"]
        assert 0 <= q["answer"] < 4 and q["explanation"].strip(), q["id"]
        source = q["source"]
        assert source["evidence"].strip(), q["id"]
        if source["kind"] == "doc":
            assert source["evidence"] == data["docLines"][source["line"] - 1].strip(), q["id"]
        else:
            assert source["kind"] == "slide", q["id"]
            assert source["evidence"] == slides[(source["file"], source["page"])], q["id"]
            page = slide_pages[(source["file"], source["page"])]
            assert source["image"] == page["image"] and page["chapter"] == q["chapter"], q["id"]
    assert len(forms) == 8
    used = []
    for form in forms:
        ids = form["questionIds"]
        assert len(ids) == len(set(ids)) == 30 and form["durationSeconds"] == 900
        assert all(qid in by_id for qid in ids)
        assert {by_id[qid]["chapter"] for qid in ids} == {1, 2, 3, 4}
        assert {by_id[qid]["source"]["kind"] for qid in ids} == {"doc", "slide"}
        used.extend(ids)
    assert len(used) == len(set(used)) == 240
    result = metrics(questions)
    assert not result["length_review_ids"], result["length_review_ids"]
    assert not result["distractor_cue_ids"], result["distractor_cue_ids"]
    # Random selection has expected accuracy 25%; ties are selected uniformly.
    # This is a bank-level heuristic check, not evidence of individual difficulty.
    assert 20 <= result["pick_longest_accuracy_percent"] <= 30
    assert 20 <= result["pick_shortest_accuracy_percent"] <= 30
    result["chapters"] = dict(sorted(Counter(q["chapter"] for q in questions).items()))
    result["sources"] = dict(Counter(q["source"]["kind"] for q in questions))
    result["exam_forms"] = len(forms)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", type=Path)
    args = parser.parse_args()
    current = json.loads((ROOT / "dist/data.json").read_text(encoding="utf-8"))
    result = {"after": audit(current)}
    if args.before:
        before = json.loads(args.before.read_text(encoding="utf-8"))
        original = {q["id"]: q for q in before["questions"]}
        assert set(original) == {q["id"] for q in current["questions"]}
        assert before["examForms"] == current["examForms"], "Existing forms must remain stable"
        for q in current["questions"]:
            assert all(q["source"].get(key) == value for key,value in original[q["id"]]["source"].items())
            assert original[q["id"]]["answer"] == q["answer"]
        result["before"] = metrics(before["questions"])
        result["edited_question_or_choices"] = sum(
            q["question"] != original[q["id"]]["question"] or q["choices"] != original[q["id"]]["choices"]
            for q in current["questions"]
        )
        result["edited_explanations"] = sum(
            q["explanation"] != original[q["id"]]["explanation"] for q in current["questions"]
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))
