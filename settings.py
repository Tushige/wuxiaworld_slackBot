import os

'''
how often we scrape wuxiaworld.com
1000: 20 minutes
'''
SLEEP_INTERVAL = 1000

#This is the token that allows us to send messages to Slack
#It's inputted from the user as an environmental variable
SLACK_TOKEN = os.getenv("WUXIA_BOT_TOKEN", "")
#where we're posting the updates to
SLACK_CHANNEL = "#wuxia_update"


#novel update filtering var
TIME_CRITERIA = ['0 minute ago', '1 minute ago', "2 minutes ago", "1 hour ago", "17 hours ago"];

#import private settings here
'''
try:
		from private import *
except Exception:
		pass
'''

# Any external private settings are imported from here.
'''
try:
    from config.private import *
except Exception:
    pass
'''