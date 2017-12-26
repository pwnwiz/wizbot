#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql
import os,time

def developer() :
	string='pwnWiz\n'
	string+='Email : pwnWiz@gmail.com\n'
	string+='Github : https://github.com/pwnwiz/wizbot\n'
	return string