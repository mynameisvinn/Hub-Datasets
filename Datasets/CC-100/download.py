from cc100 import Retrieve


def main(url):
	print(">>")
    R = Retrieve()
    R.fetch(url)


if __name__ == "__main__":
    url = 'http://data.statmt.org/cc-100/en.txt.xz'
    main(url)