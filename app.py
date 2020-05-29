#!/usr/bin/python3
from flask import Flask, render_template, request
from model.Lunh import Lunh
import socket

app = Flask(__name__)
lunh = Lunh()

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/checksum", methods=["POST"])
def checksum():
	valid = lunh.checksum(request.form["number"])
	if not valid: message = "Credit card number is invalid"
	else: message = "Credit card number is valid"
	return render_template("index.html", message=message)

if __name__ == "__main__":
	app.run()
