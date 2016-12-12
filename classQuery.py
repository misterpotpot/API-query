# -*- coding: utf8 -*-

import sqlite3


class Url():
	"""Classe définissant une Url. Elle contient
	- ID
	- href
	- categories
	- lectures 
	- qs
	- qs_0
	- site
	- lang
	- date_push"""
	nb_Url = 0

	def __init__(self, ID, href, categories, lectures, qs, qs_0, site, lang, date_push):
		self._ID = ID
		self._href = href
		self._categories = categories
		self._lectures = lectures
		self._qs = qs
		self._qs_0 = qs_0
		self._site = site
		self._lang = lang
		self._date_push = date_push

	def get_ID(self):
		return self._ID
	def get_href(self):
		return self._href
	def get_categories(self):
		return self._categories
	def get_lectures(self):
		return self._lectures
	def get_qs(self):
		return self._qs
	def get_qs_0(self):
		return self._qs_0
	def get_site(self):
		return self._site
	def get_lang(self):
		return self._lang
	def get_date_push(self):
		return self._date_push
	def set_ID(self, input):
		self._ID = input
	def set_href(self, input):
		self._href = input
	def set_categories(self, input):
		self._categories = input
	def set_lectures(self, input):
		self._lectures = input
	def set_qs(self, input):
		self._qs = input
	def set_qs_0(self, input):
		self._qs_0 = input
	def set_site(self, input):
		self._site = input
	def set_lang(self, input):
		self._lang = input
	def set_date_push(self, input):
		self._date_push = input

	ID = property(get_ID, set_ID)
	href = property(get_href, set_href)
	categories = property(get_categories, set_categories)
	lectures = property(get_lectures, set_lectures)
	qs = property(get_qs, set_qs)
	qs_0 = property(get_qs_0, set_qs_0)
	site = property(get_site, set_site)
	lang = property(get_lang, set_lang)
	date_push = property(get_date_push, set_date_push)



class User():
	"""Classe définissant un User. Elle contient
	- ID
	- navigateur
	- preferences_categories
	- preferences_site 
	- urls_vu
	- lang"""

	def __init__(self, key, bdd = "../zapking.db"):
		self.key = str(key)
		conn = sqlite3.connect(bdd)
		conn.text_factory = str
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users WHERE key = ?", (self.key,))
		for x in cursor.fetchall():
			self._ID = x[0]
			self._navigateur = x[2]
			self._preferences_categories = x[3]
			self._preferences_site = x[4]
			self._urls_vu = x[5]
			self._lang = x[6]
		cursor.close()
		conn.close()

	def get_ID(self):
		return self._ID
	def get_navigateur(self):
		return self._navigateur
	def get_preferences_categories(self):
		return self._preferences_categories
	def get_preferences_site(self):
		return self._preferences_site
	def get_urls_vu(self):
		return self._urls_vu
	def get_lang(self):
		return self._lang
	def set_ID(self, input):
		self._ID = input
	def set_navigateur(self, input):
		self._navigateur = input
	def set_preferences_categories(self, input):
		self._preferences_categories = input
	def set_preferences_site(self, input):
		self._preferences_site = input
	def set_urls_vu(self, input):
		self._urls_vu = input
	def set_lang(self, input):
		self._lang = input

	ID = property(get_ID, set_ID)
	navigateur = property(get_navigateur, set_navigateur)
	preferences_categories = property(get_preferences_categories, set_preferences_categories)
	preferences_site = property(get_preferences_site, set_preferences_site)
	urls_vu = property(get_urls_vu, set_urls_vu)
	lang = property(get_lang, set_lang)