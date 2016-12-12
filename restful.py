# -*- coding: utf8 -*-

from bottle import run, get, request
import sqlite3
from string import split
from classQuery import *



def check_parametre(url_parametre, user_parametre):
	url_parametre = str(url_parametre)
	user_parametre = str(user_parametre)
	match = False
	for user_parametre in split(user_parametre, ";"):
		for url_parametre in split(url_parametre, ";"):
			if user_parametre == url_parametre:
				match = True

	return match


def get_urls():
	conn = sqlite3.connect('../zapking.db')
	conn.text_factory = str
	cursor = conn.cursor()
	cursor.execute("""SELECT * FROM urls""")
	urls = []
	for x in cursor.fetchall():
		urls.append(Url(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])) #x[0] = ID, x[1] = href, x[2] = categories, x[3] = lectures, x[4] = qs, x[5] = qs_0, x[6] = site, x[7] = lang, x[8] = date_push
	cursor.close()
	conn.close()
	return urls


def choix_urls(nb, user, urls):
	j = 0
	url_filtrees = []
	for url in urls:
		if check_parametre(url.get_categories(), user.get_preferences_categories()) == 0: ## Si catégorie de l'url n'est pas dans les préférences catégorie du user
			compatible = False
		elif check_parametre(url.get_site(), user.get_preferences_site()) == 0: ## Si le site de l'url n'est pas dans les préférences site du user
			compatible = False
		elif check_parametre(url.get_ID(), user.get_urls_vu()) == 1: ## Si l'url a déjà été vu par le user
			compatible = False
		elif check_parametre(url.get_lang(), user.get_lang()) == 0: ## Si langue l'url n'est pas dans les langues du user
			compatible = False
		else:
			compatible = True
		if compatible:
			url_filtrees.append(url)
		j += 1

	url_triees = sorted(url_filtrees, key=lambda url: url.qs, reverse=True)
	return url_triees[:nb]


@get('/url')
def getAll():
	key, nb = str(request.query['key']), int(request.query['nb'])
	try:
		user = User(key) 
	except:
		resultat = """{"Erreur" : "Echec de l'authentification"}"""
	else:
		urls = get_urls()
		resultat_urls = choix_urls(nb, user, urls)
		resultat = "{"
		for url in resultat_urls:
			resultat += "\"" + str(url.get_ID()) + "\" : \"" + str(url.get_href()) + "\", "
		if len(resultat) == 1:
			resultat = """{"Erreur" : "Aucune url ne correspond aux parametres user"}"""
		else:
			resultat = resultat[:-2] + "}"

	return resultat

run(reloader=True, debug=True)