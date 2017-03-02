'''

'''
import os

'''
how often we scrape wuxiaworld.com
1000: 20 minutes
'''
SLEEP_INTERVAL = 1000

# This is the token that allows us to send messages to Slack
# user must set the token as an environmental variable
SLACK_TOKEN = os.getenv("WUXIA_BOT_TOKEN", "")

# channel we're posting the updates to
SLACK_CHANNEL = "#wuxia_update"
CHROMEDRIVER = os.path.join(os.path.dirname(__file__), 'drivers/chromedriver')
# novel update filtering var
TIME_CRITERIA = [
	'1 second ago',
	'30 seconds ago',
	'1 minute ago',
	'2 minutes ago',
	'5 minutes ago',
	'10 minutes ago',
	'30 minutes ago',
	'1 hour ago',
	'2 hours ago']
# titles we want updates for
NOVELS = [
	'Against the Gods',
	'Absolute Choice',
	'Battle Through the Heavens',
	'Desolate Era',
	'I Shall Seal the Heavens']
