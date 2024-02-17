class SearchController:
	def __init__(self):
		self.url = None

	@staticmethod
	def welcome():
		with open("welcome") as fin:
			print(fin.read())

	def read(self):
		self.url = input("Введите URL сайта: ")


def main():
	print("Новый файл, юху!")


if __name__ == "__main__":
	main()
