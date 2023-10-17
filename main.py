import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, yourtodos

st.set_page_config(
	page_title = "KASIRA HOUSE TODOs List"
)

class KASIRA:

	def __init__(self) -> None:
		self.app = []

	def add_app(self, title, function):
		self.app.append({
			"title": title,
			"function": function
		})
	
	def run():
		with st.sidebar:
			app = option_menu(
				menu_title = 'KASIRA HOUSE TODOs List',
				options = ['Home', 'Account', 'Your TODOs', 'About'],
				icons = ['house-fill', 'person-circle', 'chat-fill', 'info-circle-fill'],
				menu_icon = 'chat-text-fill',
				default_index = 1,
				styles = {
					"container": {"padding": "5!important", "background-color":'black'},
					"icon": {"color": "white", "font-size": "23px"}, 
					"nav-link": {"color":"white", "font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
					"nav-link-selected": {"background-color": "#02ab21"},
				}
			)
		
		if app == 'Home':
			home.app()
		if app == 'Account':
			account.app()
		if app == 'About':
			about.app()
		if app == 'Your TODOs':
			yourtodos.app()

	run()