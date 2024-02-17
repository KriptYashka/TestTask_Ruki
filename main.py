from search_number.controller import SearchController
from search_number.handler import SearchHandler


class Application:
	def __init__(self):
		self.controller = SearchController()
		self.handler = SearchHandler()

	def start(self):
		self.controller.welcome()
		self.handler.url = self.controller.read()
		nums = self.handler.get_nums()
		if nums is None:
			print("Номера не найдены")
		else:
			print(*nums, sep="\n")


def main():
	app = Application()
	app.start()


if __name__ == '__main__':
	main()
