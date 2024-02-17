import logging
import re
import requests

from bs4 import BeautifulSoup as bs

from search_number.re_number import re_rus_number


class SearchHandler:
	def __init__(self, url=None):
		self.url = url

	@staticmethod
	def get_number(text):
		number = "".join([symbol for symbol in text if symbol.isdigit() or symbol == "+"]).replace("+7", "8")
		if len(number) not in [7, 10, 11]:
			return None
		if len(number) == 7:
			return "8495" + number
		if len(number) == 10:
			return "8" + number
		return "8" + number[1:]

	def get_nums(self):
		if self.url is None:
			raise NotImplementedError("Не передано URL")
		request = requests.get(self.url, allow_redirects=False)
		if request.status_code != 200:
			return None
		soup = bs(request.text, "html.parser")
		text = soup.text
		data = re.finditer(re_rus_number, text)
		res = set()
		for item in data:
			logging.debug(item)
			number = self.get_number(text[item.start():item.end()])
			if number is not None:
				res.add(number)
		return res


def main():
	logging.basicConfig(level=logging.DEBUG)
	urls = [
		"https://repetitors.info/",
		"https://loft-zavod.ru/",
		"https://informatics.ru/",
		"https://habr.com/ru/articles/110731/",
		"https://almazcinema.ru/myt/p/contacts/"
	]
	sh = SearchHandler(urls[-1])
	nums = sh.get_nums()
	if nums is None:
		print("Нет номеров")
	else:
		for num in nums:
			print(num)


if __name__ == "__main__":
	main()
