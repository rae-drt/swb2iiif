import pandas as pd
from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem, ResourceItem1

def read_csv(file_name):
    for row in pd.read_csv(file_name, iterator=True):
        yield row


manifest = Manifest(id="https://example.com/iiif/manifest.json", label={"en":["Example export from Solrwayback"]}, behavior="paged")

manifest.make_service(id="http://localhost:5555/search", type="SearchService2")


df = pd.read_csv('../export/solrwayback_2023-10-18_15-30-22.csv')
dedup_df = df.drop_duplicates(subset=['description'])
for row in dedup_df.itertuples(index=True, name='Pandas'):
    url = getattr(row, "url")
    id = getattr(row, "id")
    description = getattr(row, "description")
    if pd.notnull(description):
        resource_item = ResourceItem(id=url, type="Image", height="3024", width="4032")
        annotation_page = AnnotationPage(id=f"https://example.com/iiif/annopage-1/{id}")
        item = Annotation(id=f"https://example.com/iiif/anno-1/{id}", body=resource_item, target=f"https://example.com/iiif/canvas-{id}", motivation="painting")
        annotation_page.add_item(item)
        canvas = Canvas(id=f"https://example.com/iiif/canvas-{id}", height="3024", width="4032")
        canvas.add_item(annotation_page)
        manifest.add_item(canvas)
        anno_resource_item = ResourceItem1(id=f"https://example.com/iiif/annopage-2/anno-1/{id}", type="TextualBody", value=description)
        anno_item = Annotation(id=f"https://example.com/iiif/anno-2/{id}", body=anno_resource_item, target=f"https://example.com/iiif/canvas-{id}", motivation="commenting")
        canvas.add_annotation(anno_item)
    

print(manifest.json(indent=2))


