#This must be run sever times at different ranges, or set to go off on a timer, since google blocks access after ~60 hits for a while
import requests
import mechanize
import sys
import re
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver


senate=pd.read_csv('names.csv')

#senate['dem_count']=999
#senate['rep_count']=999



#The function to collect results for a given candidate first and last name and year
def collect(first,last,year):

	more=True
	
	#The basic search string which examines news articles in a given year (before November) which includes a specific candidate's
	#full name and Minnesota
	test_url='https://www.google.com/search?q=%22'+first+'+'+last+'%22++%22minnesota%22&hl=en&gl=us&authuser=0&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F1%2F'+year+'%2Ccd_max%3A11%2F1%2F'+year+'&tbm=nws'

	
	HTTP_REQUESTS = "requests"
	HTTP_MECHANIZE = "mechanize"
	
	
	driver = webdriver.Firefox()
	
	articles=0
	count=0

	while more==True and count<1: #Tentitively only looking at the first page of results

	
		driver.get( test_url )
	
		test_html = driver.page_source
	
	
		soup = BeautifulSoup( test_html, "html5lib" )
	
	
		count=count+1
	
		new_articles=len(soup.find_all("h3", class_='r')) #getting the number of articles
		articles=articles+new_articles

		print(new_articles)
	

		next=soup.find_all("td", class_='b')
	
		old_url=test_url
	
		for element in next: #finding the next button and getting its link
			if element.get_text()=='Next':
				nexta=element.find('a')
				test_url='https://www.google.com'+nexta.get('href')
		if new_articles==0 or old_url==test_url: #google 
			top=soup.find_all("div", id='topstuff')
			more=False
			if 'did not match' in str(top): #A solution to the fact that it seems to display articles even if no results found
				articles=0
				print('nada')
		if more==True:
			print('found more')
		driver.close()	
	return articles

for i in range(1,60):
	print(i)
	#For each case, retrieve results for the Democrat and Republican
	if str((senate['First_D'][i]))!='nan':
		try:
			dem=collect(senate['First_D'][i],senate['Last_D'][i],str(senate['year'][i]))
			senate['dem_count'][i]=dem
		except:
			print('failure')
			senate['dem_count'][i]=555
	if str((senate['First_R'][i]))!='nan':
		try:
			rep=collect(senate['First_R'][i],senate['Last_R'][i],str(senate['year'][i]))
			senate['rep_count'][i]=rep
		except:
			print('failure')
			senate['rep_count'][i]=555


#senate.to_csv('names.csv',index=False)
#collect('katie','sieben','2012')

#first='katie'

#last='sieben'


