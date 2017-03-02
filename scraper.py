import settings
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from slackclient import SlackClient

slack = SlackClient(settings.SLACK_TOKEN)

def scrape_wuxia():
	driver = webdriver.Chrome(settings.CHROMEDRIVER)
	driver.get('http://www.wuxiaworld.com')
	page = driver.page_source
	soup = BeautifulSoup(page, 'lxml')
	# @titles: dict of {novel name: released date}
	titles = {};
	for entry in soup.find_all('div', class_="ww_action_click"):
		title = entry.find("span", class_="title")
		titles[title.text] = entry.find("span", class_="ww_elapsed_time").text
	'''
	At this point, we have the data we need
	Now, we check if novels have updates
	'''
	# dict of all updated novels
	updated = {}
	slack_msg = ""
	for name, release_date in titles.items():
		if(release_date in settings.TIME_CRITERIA and name in settings.NOVELS):
			print("new update available")
			slack_msg = str(name) + " was updated " + release_date + "!"
			slack.api_call(
				"chat.postMessage", channel=settings.SLACK_CHANNEL, text = slack_msg,
				username='wuxia_bot', icon_emoji=':robot_face:'
			)
			updated[name] = release_date
