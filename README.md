# swb2iiif

Generate a IIIF manifest from a Solrwayback csv export

```
❯ python app.py --help
Usage: app.py [OPTIONS]

Options:
  --csv TEXT              csv file to parse.  [required]
  --domain TEXT           filter by domain.  [required]
  --image-height INTEGER  image height.  [default: 3024]
  --image-width INTEGER   image width.  [default: 4032]
  --search-service TEXT   content search service.  [default:
                          https://example.com/iiif/search]
  --uri-prefix TEXT       used to form URI id.  [default:
                          https://example.com/iiif]
  --label TEXT            manifest label.  [default: Example export from
                          Solrwayback]
  --version               Show the version and exit.
  --help                  Show this message and exit.
  ```
