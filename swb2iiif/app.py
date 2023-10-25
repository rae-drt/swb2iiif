import click
import pandas as pd
from configparser import ConfigParser
from iiif_prezi3 import Manifest, Canvas, AnnotationPage, Annotation, ResourceItem, ResourceItem1

config_ini = ConfigParser()
config_ini.read("config.ini")

@click.command()
@click.option("--csv", required=True, help="csv file to parse.")
@click.option("--domain", required=True, help="filter by domain.")
@click.option("--search-service", required=False, show_default=True, default=config_ini.get("swb2iiif", "SEARCH_SERVICE"), help="content search service.")
@click.option("--uri-prefix", required=False, default=config_ini.get("swb2iiif", "URI_PREFIX"), help="used to form URI id.")
@click.option("--label", required=False, default=config_ini.get("swb2iiif", "LABEL"), help="manifest label.")
@click.version_option(prog_name=config_ini.get("main", "NAME"), version=config_ini.get("main", "VERSION"))


def run(csv, search_service, domain, uri_prefix, label):
    manifest = Manifest(id=f"{uri_prefix}/manifest.json", label={"en":[label]})
    manifest.make_service(id=search_service, type="SearchService2")
    df = pd.read_csv(csv)
    dedup_df = df.drop_duplicates(subset=['description'])
    for row in dedup_df.itertuples(index=True, name='Pandas'):
        url = getattr(row, "url")
        id = getattr(row, "id")
        export_domain = getattr(row, "domain")
        description = getattr(row, "description")
        if pd.notnull(description) and domain == export_domain:
            painting_resource_item = ResourceItem(id=url, type="Image", height="3024", width="4032")
            annotation_page = AnnotationPage(id=f"{uri_prefix}/annotation-page/{id}")
            painting_item = Annotation(id=f"{uri_prefix}/painting/{id}", body=painting_resource_item, target=f"{uri_prefix}/canvas-{id}", motivation="painting")
            annotation_page.add_item(painting_item)
            canvas = Canvas(id=f"{uri_prefix}/canvas/{id}", height="3024", width="4032")
            canvas.add_item(annotation_page)
            manifest.add_item(canvas)
            commenting_resource_item = ResourceItem1(id=f"{uri_prefix}/text/{id}", type="TextualBody", value=description)
            commenting_item = Annotation(id=f"{uri_prefix}/comment/{id}", body=commenting_resource_item, target=f"{uri_prefix}/canvas-{id}", motivation="commenting")
            canvas.add_annotation(commenting_item)
    print(manifest.json(indent=2))


if __name__ == "__main__":
    run()

