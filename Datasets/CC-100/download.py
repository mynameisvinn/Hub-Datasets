from cc100 import Retrieve


def main(url):
    R = Retrieve()
    R.fetch(url)


if __name__ == "__main__":
    url = 'https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases/cord-19_2020-03-13.tar.gz'
    main(url)