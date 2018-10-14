from tkinter import Tk

try:
	from word_look_up import LookUp
except ModuleNotFoundError:
	print("`word_look_up.py` not found \nPlease place it in the same folder as `main.py`")
	exit()

try:
	from system_tools import SystemTools
except ModuleNotFoundError:
	print("`system_tools.py` not found \nPlease place it in the same folder as `main.py`")
	exit()


class Main:
	def __init__(self, *args, **kwargs):
		SystemTools().run()

	def get_clipboard_text(self):
		# Initializing `tkinter` and hiding the default window
		root = Tk()
		root.withdraw()
		# Returning text from clipboard
		return root.clipboard_get()

	def run_look_up(self):
		text = self.get_clipboard_text()

		if text != "":
			print("Searching for ===> " + text, end="\r")
			LookUp().get_meaning(text)
		else:
			print("No text copied. \nPlease select a text and copy it to find a meaning.")


Main().run_look_up()

input("\nPress enter to close...")
