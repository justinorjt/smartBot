import numpy as np
from html.parser import HTMLParser
import pandas as pd
import json
from bs4 import BeautifulSoup as bsoup
from pandas.io.html import read_html
#downloaded to deal with js loaded html. May have to look it up
from selenium import webdriver
from explore_crawl import gatherPics

def scrapeCaption(posts):
	# postUrl ='https://www.instagram.com/p/BZHE8E7FAGy/'
	i=1

	for item in posts:
		postUrl = item

		browser = webdriver.Chrome('chromedriver.exe')
		browser.get(postUrl)
		source = browser.page_source
		pretty = bsoup(source, 'html.parser')
		body = pretty.find('body')
		commentBlock = body.find('ul',{'class':'k59kT'})
		comments = commentBlock.findAll('li',{'class':'gElp9'})
		print(i,"---------------------------")
		for comment in comments:
			print(comment.find('span').get_text())

		browser.quit()
		i=i+1

scrapeCaption(gatherPics())
