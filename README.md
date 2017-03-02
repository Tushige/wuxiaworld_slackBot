# wuxiaworld_slackBot
A Slack bot that scrapes www.wuxiaworld.com for novel updates. You can
filter the updates by novel titles and update time. The bot posts
the title of the novel and the time it was updated to the specified Slack channel.
You can enable desktop notifications on Slack for convenience.

## SETUP
In order to use this bot, you need to create
    1. Slack Team
    2. Slack channel - where the bot will post
    3. Test API token - add it to your environment variables as `WUXIA_BOT_TOKEN`

## Settings
For the bot to work, you need to do the following in `settings.py`
    1. Modify `SLACK_CHANNEL` to contain the channel you've created
    2. Modify `NOVELS` to contain titles of novels you're interested
    3. Modify `TIME_CRITERIA` to specify search condition
    4. Modify `SLEEP_INTERVAL` to specify how often to check for updates
## installing dependencies
    run `pip install -r requirements.txt` to install all the dependencies

## How to run
    run `python loop.py` to begin the program
