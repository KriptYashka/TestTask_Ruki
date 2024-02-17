from search_number.controller import SearchController


class Application:
	def __init__(self):
		self.controller = SearchController()
		self.handler = None

	def start(self):
		self.controller.welcome()
		self.controller.read()


def main():
	app = Application()
	app.start()


if __name__ == '__main__':
	main()
