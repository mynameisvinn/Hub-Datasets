import hub
from hub.schema import Text, Tensor

import pandas as pd

from tqdm import tqdm
import argparse


def up(url: str):
    """Push Cord-19 embeddings to Hub.
    """

    df = pd.read_csv('cord_19_embeddings_2021-01-04.csv', header=None)

    my_schema = {
        'label': Text(shape=(None,), max_shape=(1000,)),
        'embedding': Tensor((768,), "float64")
        }

    ds = hub.Dataset(url, shape=(df.shape[0],), schema=my_schema, mode="w")

    for i, row in tqdm(df.iterrows()):
        ds['label', i] = row.values[0]  # unique article identifier
        ds["embedding", i] = row.values[1:]  # 768 dim embedding
    ds.commit()


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--url', type=int, help='hub url')
    args = my_parser.parse_args()
    url = args.url
