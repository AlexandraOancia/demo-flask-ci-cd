# Ecrire en python  le code (en utilisant flask) permettant 
# d'ecouter sur le port 5000 et de répondre "Hello world"
# quand l'utilisateur se connecte dessus

#!/usr/bin/python
# -*- coding: <encoding name> -*-


from flask import Flask 
app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello"

# LISTEN 
if __name__ == '__main__':
    app.run(host="0.0.0.0")
