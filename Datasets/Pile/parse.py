from hub.schema import Text
import hub

import ijson
from tqdm import tqdm


my_schema = {'text': Text(shape=(None, ), max_shape=(10000000, ))}
url = "mynameisvinn/pile" #instead write your {username}/{dataset} to make it public
ds = hub.Dataset(url, shape=(101,), schema=my_schema, mode='w')

data = ijson.parse(open("val.jsonl", 'r'), multiple_values=True)  # https://stackoverflow.com/questions/59346164/ijson-fails-with-trailing-garbage-parse-error

counter = 0

for prefix in tqdm(data):
    if prefix[0] == "text":
        print(">>", counter)
        ds["text", counter] = prefix[2]
        counter += 1

    if counter > 100:
    	break
ds.commit()