# swb2iiif

## Generate a IIIF manifest from a Solrwayback CSV export

Select the image type facet and make sure your export includes the following fields:
```
id,description,url,domain
```

### usage

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

### installation
```
git clone https://github.com/rae-drt/swb2iiif.git
cd swb2iiif
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd swb2iiif
```

### example command
```
python app.py --csv ../export/solrwayback_2023-10-18_15-30-22.csv --domain iwm.org.uk --uri-prefix https://miiifystore.s3.eu-west-2.amazonaws.com/swb --label 'Export of iwm.org.uk from Solrwayback' --search-service http://pi.zedstar.org:5555/search
```

### example output

https://projectmirador.org/embed/?iiif-content=https://miiifystore.s3.eu-west-2.amazonaws.com/swb/iwm.json

