"""Check local links, fragments, image metadata and site essentials without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
import json

ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__(); self.path=path; self.ids=[]; self.refs=[]; self.images=[]; self.h1=0
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='h1': self.h1+=1
        if tag in ['a','link'] and a.get('href'): self.refs.append(a['href'])
        if tag in ['img','script'] and a.get('src'): self.refs.append(a['src'])
        if tag=='img': self.images.append(a)

pages={p:Page(p) for p in ROOT.glob('*.html')}
errors=[]; checked=0
for path,page in pages.items():
    if page.h1!=1: errors.append(f'{path.name}: expected one h1, got {page.h1}')
    if len(page.ids)!=len(set(page.ids)): errors.append(f'{path.name}: duplicate IDs')
    for img in page.images:
        if 'alt' not in img or not img.get('width') or not img.get('height'): errors.append(f'{path.name}: missing image metadata {img.get("src")}')
    for href in page.refs:
        url=urlsplit(href)
        if url.scheme or url.netloc: continue
        target=(path.parent/unquote(url.path or path.name)).resolve()
        if target.is_dir(): target=target/'index.html'
        checked+=1
        if not target.exists(): errors.append(f'{path.name}: missing {href}')
        elif url.fragment and target.suffix=='.html' and url.fragment not in pages[target].ids: errors.append(f'{path.name}: missing fragment {href}')
ET.parse(ROOT/'sitemap.xml')
report={'html_pages':len(pages),'local_references_checked':checked,'errors':errors}
print(json.dumps(report,indent=2))
raise SystemExit(bool(errors))
