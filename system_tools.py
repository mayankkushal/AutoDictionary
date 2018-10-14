import time

import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

from pykeyboard import PyKeyboard



class SystemTools:

	def __init__(self, *args, **kwargs):
		self.k = PyKeyboard()
		self.screen = Wnck.Screen.get_default()
		self.screen.force_update()
		self.active_window = self.screen.get_active_window()

	def activate_previous_window(self):
		self.window_list = self.screen.get_windows_stacked()
		self.window_list[-2].activate(0)

	def copy_text(self):
		self.k.press_keys([self.k.control_key, 'c'])

	def run_for_terminal(self):
		self.activate_previous_window()
		self.copy_text()

	def run_for_other(self):
		self.copy_text()
		self.activate_previous_window()

	def run(self):
		if self.active_window.get_name() == "Terminal":
			self.run_for_terminal()
		else:
			self.run_for_other()


if __name__=="__main__":
	st = SystemTools()
	st.run()
	input("enter")