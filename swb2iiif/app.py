import pandas as pd
from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem

def read_csv(file_name):
    for row in pd.read_csv(file_name, iterator=True):
        yield row

def create_manifest():
    manifest = Manifest(id="https://example.com/iiif/manifest.json", label={"en":["Example Manifest"]}, behavior="paged")
    return manifest

def create_canvas():
    canvas = Canvas(id="https://example.com/iiif/canvas-1", height="3024", width="4032")
    return canvas

def create_annotation_page():
    annotation_page = AnnotationPage(id="https://example.com/iiif/manifest.json")
    return annotation_page

def create_annotation():
    annotation = Annotation(id="https://example.com/iiif/manifest.json", target="https://example.com/iiif/manifest.json")
    return annotation

def create_resource_item(id):
    resource_item = ResourceItem(id=id, type="Image")

manifest = create_manifest()
canvas = create_canvas()
manifest.add_item(canvas)



for row in pd.read_csv("../export/solrwayback_2023-10-18_15-30-22.csv", chunksize=1):
    url = row['url'].values[0]
    id = row['id'].values[0]
    resource_item = ResourceItem(id=url, type="Image", height="3024", width="4032")
    annotation_page = create_annotation_page()
    annotation = create_annotation()
    item = annotation.construct(id=f"https://example.com/iiif/manifest.json{id}", body=resource_item, target="https://example.com/iiif/canvas-1", motivation="painting")
    annotation_page.add_item(item)
    canvas.add_item(annotation_page)

canvas.add_item(annotation_page)
print(manifest.json(indent=2))


