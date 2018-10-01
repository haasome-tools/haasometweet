import time
import config

from haasometweet.util.Util import Util
from haasometweet.util.RepeatedTimer import RepeatedTimer

from haasometweet.managers.TwitterManager import TwitterManager
from haasometweet.managers.DiscordManager import *


def update_twitter_screenshot():
    try:
        Util.take_screenshot("./haasomescreenshot.png")
        time.sleep(1)
        TwitterManager.send_screenshot_tweet("Current Haas Version: v3.2.3 Beta - EMAGod Forward Testing - Phase 2", "./haasomescreenshot.png")
    except Exception as e:
        Util.get_logger().debug(e)

if __name__ == "__main__":

    print(Util.banner)
    
    Util.get_logger().debug('Starting Haasome Tweet Process')

    rt = RepeatedTimer(3600, update_twitter_screenshot)

    Util.get_logger().debug("Posting first screenshot")
    
    update_twitter_screenshot()

    try:

        bot.run(config.CONFIG['DISCORD_BOT_TOKEN'])

        while True:
            print("derp")
            time.sleep(5)


    finally:
        rt.stop()