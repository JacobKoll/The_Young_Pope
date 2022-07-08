#!/bin/bash

filepath="$(pwd)"
dirname="$(basename $(pwd))""-venv"

function activate () {
	cd "$filepath"
	rm -rf $dirname
	python3 -m venv $dirname
	source $dirname/bin/activate
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt
}
activate
