import argparse
from cord19 import Retrieve

def main(fname, my_schema, files, url):
    R = Retrieve()
    R.fetch(fname)
    R.unpack('sink.tgz')
    R.unpack('unzipped/2020-03-13/pmc_custom_license.tar.gz')
    R.push(schema=my_schema, files=files, url=url)


if __name__ == '__main__':    

    fname = 'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-03-13.tar.gz'
    files = glob("unzipped/pmc_custom_license/*")

    my_schema = {
        'data': dict
        }

    url = "mynameisvinn/test"

    main(fname, my_schema, files, url)
