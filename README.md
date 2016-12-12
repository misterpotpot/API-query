# API Query - Readme

## Project name
Crawling

## Description
Fait partie du projet Zapking, dont l'objectif est de construire un plug-in permettant à l'internaute d'accéder à des urls suceptibles de lui plaire lors du clic sur le logo du plug-in.<br/>
Cet API permet de renvoyer un nombre n d'url à l'utilsiateur qui possède la clé key


## Usage
Appel Api déclenché lors d'un appel géré par le plug-in

## Resultats
Format Json. {"id" : "href", ...}<br/>
Les n urls qui ont le plus gros qs parmi celles qui matchent avec les préférences utilisateur

## Version Python
Ecrit en python 2.7