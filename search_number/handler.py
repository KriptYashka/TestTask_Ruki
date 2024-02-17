import re
import requests

from bs4 import BeautifulSoup as bs

from search_number.re_number import re_rus_number


class SearchHandler:
	def __init__(self, url):
		self.url = url
		self.data = None

	def get_number(self, text):
		number = "".join([symbol for symbol in text if symbol.isdigit() or symbol == "+"]).replace("+7", "8")
		if len(number) not in [7, 11]:
			return None
		if len(number) == 7:
			return "8495" + number
		return number
	def get_nums(self):
		request = requests.get(self.url, allow_redirects=False)
		if request.status_code != 200:
			return None
		soup = bs(request.text, "html.parser")
		# data = re.findall(r'([a-z]+)(\d*)', r'foo3, im12, go, 24buz42')
		data = re.finditer(re_rus_number, soup.text)
		res = set()
		for item in data:
			number = self.get_number(soup.text[item.start():item.end()])
			if number is not None:
				res.add(number)
		return res


def main():
	# sh = SearchHandler("https://hands.ru/company/about/")
	sh = SearchHandler("https://repetitors.info/")
	sh = SearchHandler("https://loft-zavod.ru/")
	nums = sh.get_nums()
	for num in nums:
		print(num)


if __name__ == "__main__":
	main()
