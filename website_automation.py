# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:19:55 2019

@author: Somil
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import random
import pandas as pd

comments = ["Great!","Amazing!","Good Work!","Keep it up!"]
#Usernames
opts = Options()
opts.set_headless()
assert opts.headless
browser = Chrome(executable_path='C:/chromedriver/chromedriver.exe')
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

username = browser.find_element_by_xpath("//input[@name='username']")
password = browser.find_element_by_xpath("//input[@name='password']")

username.send_keys('strength_and_motivation_')
password.send_keys('Somil@112')

login = browser.find_element_by_xpath("//button[@type='submit']")
login.click()

time.sleep(5)
tags = ['strength','success',"motivation","motivationalquotes","fitness","money","inspire","mentalstrength","lifestyle","life","joerogan","ripped","health"]
random.shuffle(tags)

for tag in tags:
	browser.get('https://www.instagram.com/explore/tags/{}'.format(tag))

	acc_links = []
	num = 6000
	while True:
		acc_links = []
		browser.execute_script("window.scrollTo(0, {})".format(num)) 
		time.sleep(5)
		images = browser.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']//a")
		for links in images:
			acc_links.append(links.get_attribute('href'))
		print(len(acc_links))

		if len(acc_links) > 40:
			break
		num = num*2

	random.shuffle(acc_links)
	i = 0
	for link in acc_links:
		browser.get(link)
		time.sleep(5)
		like = browser.find_element_by_xpath("//span[@class='fr66n']//button")
		like.click()
		#Comment
		browser.find_element_by_xpath("//span[@class='_15y0l']//button").click()
		time.sleep(5)
		if i%3 == 0:
			browser.find_element_by_xpath("//textarea").send_keys("{}".format(random.choice(comments)))
			browser.find_element_by_xpath("//button[@type='submit']").click()
		browser.execute_script("window.scrollTo(0, 0)")
		time.sleep(5)
		try:
			browser.find_element_by_xpath("//button[@class='oW_lN _0mzm- sqdOP yWX7d        ']").click()
		except:
			pass
		i += 1






