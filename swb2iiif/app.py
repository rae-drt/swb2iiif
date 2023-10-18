import pandas as pd

def read_csv(file_name):
    for row in pd.read_csv(file_name, iterator=True):
        yield row

for row in read_csv("../export/solrwayback_2023-10-18_15-30-22.csv"):
    print(row)

