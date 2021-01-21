from dota import Retrieve


def main(url):
	print(">> downloading")
    R = Retrieve()
    R.fetch(url)


if __name__ == "__main__":
    url = 'https://drive.google.com/uc?id=1fwiTNqRRen09E-O9VSpcMV2e6_d4GGVK'
    main(url)