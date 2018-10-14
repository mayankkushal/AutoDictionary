from tkinter import Tk

from word_look_up import LookUp

def get_clipboard_text():
	# Initializing `tkinter` and hiding the default window
	root = Tk()
	root.withdraw()
	# Returning text from clipboard
	return root.clipboard_get()

text = get_clipboard_text()

if text != "":
	print("Searching for ===> " + text, end="\r")
	LookUp().get_meaning(text)
else:
	print("No text copied. \nPlease select a text and copy it to find a meaning.")

input("\nPress enter to close...")
