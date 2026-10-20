"""Encode native PowerPoint exports as web images without changing their content."""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
renders = ROOT / '.slide-renders'
index = json.loads((renders / 'index.json').read_text(encoding='utf-8-sig'))
records = []
for item in index:
    relative = Path('slides') / f"chapter-{item['chapter']}" / f"page-{item['slide']:03}.webp"
    destination = ROOT / 'dist' / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    source = renders / f"chapter-{item['chapter']}" / f"page-{item['slide']:03}.png"
    if not destination.exists() or destination.stat().st_mtime < source.stat().st_mtime:
        with Image.open(source) as image:
            assert image.size == (item['width'], item['height'])
            image.convert('RGB').save(destination, 'WEBP', quality=92, method=6)
    records.append({**item, 'image': '/' + relative.as_posix()})
manifest = {
    'decks': {name: hashlib.sha256((ROOT / 'slidegk' / name).read_bytes()).hexdigest() for name in sorted({p['file'] for p in index})},
    'pages': records,
}
(ROOT / 'sources/slide-images.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Encoded {len(records)} slides, {sum((ROOT / 'dist' / r['image'].lstrip('/')).stat().st_size for r in records) / 1024**2:.2f} MiB")
