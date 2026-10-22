"""Render the user's four original PDFs; never recreate slides from extracted text."""
import hashlib
import json
from pathlib import Path
import pymupdf
from PIL import Image

ROOT = Path(__file__).parent


def render():
    pages = []
    for chapter, count in ((1,8),(2,54),(3,69),(4,44)):
        files = list((ROOT/'sources/hcm').glob(f'C{chapter}.*.pdf'))
        assert len(files) == 1
        source = files[0]
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        document = pymupdf.open(source)
        assert len(document) == count
        folder = ROOT/f'dist/hcm-slides/chapter-{chapter}'
        folder.mkdir(parents=True, exist_ok=True)
        for number, page in enumerate(document,1):
            path = folder/f'page-{number:03}.webp'
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(1600/page.rect.width,1600/page.rect.width),alpha=False)
            Image.frombytes('RGB',(pixmap.width,pixmap.height),pixmap.samples).save(path,'WEBP',quality=88,method=5)
            pages.append({'file':source.name,'chapter':chapter,'slide':number,
                          'image':f'/hcm-slides/chapter-{chapter}/{path.name}',
                          'imageWidth':pixmap.width,'imageHeight':pixmap.height,
                          'text':page.get_text(),'sourceSha256':digest})
        print(f'Chapter {chapter}: {count} original PDF pages rendered')
    (ROOT/'content/hcm/slide-manifest.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
    assert len(pages)==175


if __name__=='__main__':
    render()
