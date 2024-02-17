class SearchController:
	def __init__(self):
		self.url = None

	@staticmethod
	def welcome():
		text = """Программа тестового задания для сервиса 'Руки'

Разработчик: Кучук Егор Андреевич (kriptyashka)"""
		print(text)

	def read(self):
		self.url = input("Введите URL сайта: ")
		return self.url


def main():
	pass


if __name__ == "__main__":
	main()
