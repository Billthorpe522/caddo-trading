"""Generate the static archive directory; Python standard library only."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
categories = [
 ('points','Stone','Arrowheads & points','The original arrowhead catalog, with a second page of points and blades.','Arrowheads/arrowheads.htm'),
 ('pottery','Ceramics','Pottery & vessels','Jars, bottles, bowls, and other ceramics from the original catalog.','Pottery/pottery.htm'),
 ('beadwork','Beadwork','Beaded items','Moccasins, bags, and other examples of beadwork.','BeadedItems/BeadedItems.htm'),
 ('museum-quality','Sold collection','Museum Quality archive','The original site explicitly identifies this entire collection as already sold. Preserved for reference.','MuseumQuality/museumquality.htm'),
 ('beads','Beadwork','Beads','The original catalog of beads and bead strands.','Beads/beads.html'),
 ('stone','Stone','Stone artifacts','Browse the original stone artifact catalog.','Stones/Stones.htm'),
 ('books','Reference','Books','Collector guides and artifact reference books.','Books/book.html'),
 ('rare-books','Reference','Rare books','Older reference volumes from the rare-book catalog.','RareBooks/RareBooks.htm'),
 ('fossils','Natural history','Fossils','Fossils and natural-history specimens from the catalog.','Fossils/fossils.htm'),
 ('display','Display','Display frames','Cases and frames photographed for the original catalog.','DisplayFrames/DisplayFrames.htm'),
 ('framed','Display','Framed collections','The original catalog of framed pieces and groupings.','Frames/frames.htm'),
 ('minerals','Natural history','Rocks & minerals','Specimens from the rocks and minerals catalog.','RocksMin/rocksmin.htm'),
 ('diamonds','Natural history','Arkansas diamonds','Historical diamond listings; ask Sam about availability.','Diamonds/diamonds.htm'),
 ('coins','Collectibles','Coins','Original coin listings and photographs.','Coins/coins.htm'),
 ('contemporary','Contemporary','Contemporary pieces','Items identified as contemporary in the original catalog.','Contemporary/Contemporary.htm'),
 ('worldwide','International','World Wide Artifacts','The original collection of artifacts from beyond North America.','WorldWide%20Artifacts/worldwideartifacts.htm'),
 ('bone-shell','Materials','Bone & shell','The original bone and shell catalog.','Bone%20&%20Shell/Bone%20&%20Shell.htm'),
 ('under-50','Historical price range','Original $50-and-under catalog','An older price-grouped catalog. Published prices and availability need confirmation.','Artifacts%20$50.%20or%20Less/Artifacts%20$50.%20or%20Less.htm'),
 ('under-100','Historical price range','Original $50–$100 catalog','An older price-grouped catalog. Published prices and availability need confirmation.','Artifacts%20$100.%20or%20Less/artifacts$50-$100.htm'),
 ('arrivals','Historical listings','Original arrivals page','The old “New Items” page is preserved as a historical catalog, not a feed of today’s arrivals.','http://www.caddotc.com/NewItems/NewItems.htm'),
]

home=(ROOT/'index.html').read_text(encoding='utf-8')
head=home.split('<body>')[0].replace('Caddo Trading Company | Artifacts, Certification & Ka-Do-Ha','Collection Archive | Caddo Trading Company').replace('https://billthorpe522.github.io/caddo-trading/"','https://billthorpe522.github.io/caddo-trading/collection.html"').replace('Explore Caddo Trading Company in Murfreesboro, Arkansas. Shop Caddoman on eBay, browse the collection archive, and contact Sam Johnson about artifact certification.','Browse original Caddo Trading catalogs and historical photographs. See current inventory on eBay; confirm availability of older catalog entries with Sam.').replace('Caddo Trading Company — A collector’s eye. A personal connection.','The Collection Archive — Caddo Trading Company')
header=home.split('<body>')[1].split('<main id="main">')[0]
for anchor in ['certification','visit','contact']:
    header=header.replace(f'href="#{anchor}"',f'href="index.html#{anchor}"')
header=header.replace('href="collection.html">The collection','href="collection.html" aria-current="page">The collection')
footer='<footer'+home.split('<footer')[1]
footer=footer.replace('href="#contact"','href="index.html#contact"')
cards=[]
for id,group,title,description,path in categories:
    url=path if path.startswith('http') else 'http://www.caddotc.com/Catalogue/Inventory/'+path
    second='<a class="text-link" href="http://www.caddotc.com/Catalogue/Inventory/Arrowheads/arrowheads2.htm">Arrowheads · page 2 <span aria-hidden="true">↗</span></a>' if id=='points' else ''
    cards.append(f'<article class="directory-card" id="{id}"><p class="eyebrow">{escape(group)}</p><h2>{escape(title)}</h2><p>{escape(description)}</p><a class="text-link" href="{escape(url,quote=True)}" aria-label="Open the original {escape(title,quote=True)}">Original catalog <span aria-hidden="true">↗</span></a>{second}</article>')

body='''<main id="main"><div class="wrap">
<section class="archive-hero" aria-labelledby="archive-title"><p class="breadcrumb"><a href="./">Home</a> / Collection archive</p><p class="eyebrow">A record worth keeping</p><h1 id="archive-title">The collection.<br> <em>Then and now.</em></h1><p class="lead">Explore the photographs, categories, and reference material from Caddo Trading’s original website. Some pieces have sold; others may still be available. Sam can help you find out.</p><div class="actions"><a class="button" href="https://www.ebay.com/str/Caddoman/">Shop current eBay listings <span aria-hidden="true">↗</span></a><a class="text-link" href="index.html#contact">Ask about an older piece <span aria-hidden="true">→</span></a></div><div class="archive-callout"><p><strong>A collection archive, not current stock.</strong> The links below open Sam’s original catalogs. Prices and availability may have changed. The Museum Quality collection is explicitly an archive of sold pieces.</p></div></section>
<div class="archive-tools" hidden><div class="search-wrap"><label for="archive-search">Find a category</label><input id="archive-search" type="search" placeholder="Try pottery, arrowheads, books…" autocomplete="off" aria-controls="catalog-directory"></div><p class="result-count" id="result-count" role="status" aria-live="polite" aria-atomic="true">20 categories</p></div>
<div class="no-results" id="no-results" hidden><p>No categories match that search. Try a broader term or <button id="clear-search" type="button" class="button button-small">Clear search</button>.</p></div>
<section class="directory" id="catalog-directory" aria-label="Original catalog categories">'''+''.join(cards)+'''</section></div>
<section class="archive-gallery section" aria-labelledby="highlights-title"><div class="wrap"><div class="section-heading"><div><p class="eyebrow">From the sold collection</p><h2 id="highlights-title">A few pieces to remember.</h2></div></div><p class="section-intro">These photographs come from the original Museum Quality page. All three pieces have already sold. Open a photograph for a closer look.</p><div class="collection-grid">
<a class="collection-card" href="assets/images/catalog/museumq/pot1122.jpg"><div class="collection-photo"><img src="assets/images/catalog/museumq/pot1122.jpg" width="684" height="471" loading="lazy" alt="Red and cream pottery bottle from the sold collection"></div><div class="collection-label"><h3>A study in color</h3><span class="round-arrow" aria-hidden="true">↗</span></div><p>Historical photograph · Sold collection</p></a>
<a class="collection-card" href="assets/images/catalog/museumq/pot543b.jpg"><div class="collection-photo"><img src="assets/images/catalog/museumq/pot543b.jpg" width="320" height="232" loading="lazy" alt="Black and white patterned pottery vessel from the sold collection"></div><div class="collection-label"><h3>Pattern & form</h3><span class="round-arrow" aria-hidden="true">↗</span></div><p>Historical photograph · Sold collection</p></a>
<a class="collection-card" href="assets/images/catalog/museumq/1914.jpg"><div class="collection-photo"><img src="assets/images/catalog/museumq/1914.jpg" width="633" height="385" loading="lazy" alt="Stone blade from the sold collection"></div><div class="collection-label"><h3>Work in stone</h3><span class="round-arrow" aria-hidden="true">↗</span></div><p>Historical photograph · Sold collection</p></a>
</div><p class="back-top"><a class="text-link" href="#main">Back to the archive directory ↑</a></p></div></section></main>'''
(ROOT/'collection.html').write_text(head+'<body>'+header+body+footer,encoding='utf-8')

# Keep old prototype category URLs useful, too; no domain migration is performed.
redirects={'arrowheads':'points','pottery':'pottery','museumq':'museum-quality','beaded':'beadwork','books':'books','fossils':'fossils','display':'display','misc':'catalog-directory'}
for old,anchor in redirects.items():
    (ROOT/f'catalogue-{old}.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><meta http-equiv="refresh" content="0;url=collection.html#{anchor}"><link rel="canonical" href="https://billthorpe522.github.io/caddo-trading/collection.html"><title>Collection Archive | Caddo Trading Company</title></head><body><main><h1>The collection has a new home.</h1><p><a href="collection.html#{anchor}">Continue to the collection archive.</a></p></main></body></html>',encoding='utf-8')
print(f'Built collection directory: {len(categories)} categories; {len(redirects)} compatibility pages.')
