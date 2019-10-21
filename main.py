#Ecrire en python  le code (en utilisant flask) permettan
#ecouter sur le port 5000 et de répondre "Hello world"
#quand l'utilisateur se connecte dessus
#!/usr/bin/python
# -*- coding: <encoding name> -*-
""" fichier main test"""
from flask import Flask
APP = Flask(__name__)
@APP.route("/")
def hello():
    """ doc """
    return "Hello"
# LISTEN
if __name__ == '__main__':
    APP.run(host="0.0.0.0")
