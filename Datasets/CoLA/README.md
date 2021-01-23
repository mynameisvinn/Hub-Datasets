# CoLA
The Corpus of Linguistic Acceptability (CoLA) in its full form consists of 10657 sentences from 23 linguistics publications, expertly annotated for acceptability (grammaticality) by their original authors. The [public version](https://nyu-mll.github.io/CoLA/) provided here contains 9594 sentences belonging to training and development sets, and excludes 1063 sentences belonging to a held out test set. 

## Quickstart
The script `download.py` downloads the CoLA dataset and pushes it to `activeloop/CoLA`.

```python
url = 'https://nyu-mll.github.io/CoLA/cola_public_1.1.zip'
tag = "activeloop/CoLA"

schema = {
    'sentence': Text(shape=(None, ), max_shape=(500, )),
    'labels': Primitive(dtype="int64")
}
```