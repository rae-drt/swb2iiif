import pandas as pd
from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem

def read_csv(file_name):
    for row in pd.read_csv(file_name, iterator=True):
        yield row


manifest = Manifest(id="https://example.com/iiif/manifest.json", label={"en":["Example Manifest"]}, behavior="paged")

for row in pd.read_csv("../export/solrwayback_2023-10-18_15-30-22.csv", chunksize=1):
    url = row['url'].values[0]
    id = row['id'].values[0]
    resource_item = ResourceItem(id=url, type="Image", height="3024", width="4032")
    annotation_page = AnnotationPage(id=f"https://example.com/iiif/annopage-{id}")
    item = Annotation(id=f"https://example.com/iiif/anno-{id}", body=resource_item, target=f"https://example.com/iiif/canvas-{id}", motivation="painting")
    annotation_page.add_item(item)
    canvas = Canvas(id=f"https://example.com/iiif/canvas-{id}", height="3024", width="4032")
    canvas.add_item(annotation_page)
    manifest.add_item(canvas)


print(manifest.json(indent=2))


