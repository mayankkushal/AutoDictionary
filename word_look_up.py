import requests
from simplejson.errors import JSONDecodeError
from colorama import init
from colorama import Fore, Back, Style

init()

class LookUp:
	url = "https://googledictionaryapi.eu-gb.mybluemix.net/?define="

	def get_url(self):
		return f"{self.url}{self.word}"

	def get_meaning_json(self, word=None):
		""" Requests the API and returns JSON or [] """

		if word is not None:
			self.word = word

		url = self.get_url()
		r = requests.get(url)

		try:
			meaning = r.json()
		except JSONDecodeError:
			print(Fore.RED + "OOPS, couldn't find your word")
			meaning = []
		return meaning

	def pretty_print(self):
		""" Prints the contents to the terminal in a nice way """

		# Setting the size of terminal to 25X150
		import sys
		sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=25, cols=150))

		try:
			print("The word you looked for is " + Fore.RED + self.meaning['word'].upper())
		except TypeError:
			print("Error.")
			return
		print(Fore.WHITE)
		for key, value in self.meaning['meaning'].items():
			print(Fore.YELLOW + key.capitalize(), "\n")
			counter = 1
			for sub in value:
				print(f"{Fore.RED}{counter})", end="")
				for k,v in sub.items():
					print(f"\t{Fore.GREEN}{k.capitalize()}: {Fore.WHITE}{v}")
				print()
				counter += 1
			print("--------------------\n")

	def get_meaning(self, word):
		""" Combines all the methods, and takes care of everything """
		self.word = word
		self.meaning = self.get_meaning_json()
		if self.meaning is not []:
			self.pretty_print()


if __name__ == "__main__":
	lu = LookUp()
	lu.get_meaning("man up")