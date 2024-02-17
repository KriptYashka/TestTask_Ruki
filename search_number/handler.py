import re
import requests

from bs4 import BeautifulSoup as bs

from search_number.re_number import re_rus_number


class SearchHandler:
	def __init__(self, url):
		self.url = url
		self.data = None

	def get_page(self):
		request = requests.get(self.url, allow_redirects=False)
		if request.status_code != 200:
			return None
		soup = bs(request.text, "html.parser")
		data = re.search(re_rus_number, soup.text)
		print(data)


def main():
	# sh = SearchHandler("https://hands.ru/company/about/")
	sh = SearchHandler("https://repetitors.info/")
	sh = SearchHandler("https://loft-zavod.ru/")
	sh.get_page()


if __name__ == "__main__":
	main()
