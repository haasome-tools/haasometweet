import config
import tweepy
from haasometweet.util.Util import Util

class TwitterManager():

    @staticmethod
    def send_tweet(message):

        Util.get_logger().debug('Sending Tweet')

        consumer_key = config.CONFIG['TWITTER_CONSUMER_KEY']
        consumer_secret = config.CONFIG['TWITTER_CONSUMER_SECRET']
        access_token = config.CONFIG['TWITTER_ACCESS_TOKEN']
        access_token_secret = config.CONFIG['TWITTER_ACCESS_SECRET']
         
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
         
        api = tweepy.API(auth)

        api.update_status(message)
        
        Util.get_logger().debug('Sent Tweet')

    @staticmethod
    def send_screenshot_tweet(message, imagepath):
        
        Util.get_logger().debug('Sending Screenshot Tweet')

        consumer_key = config.CONFIG['TWITTER_CONSUMER_KEY']
        consumer_secret = config.CONFIG['TWITTER_CONSUMER_SECRET']
        access_token = config.CONFIG['TWITTER_ACCESS_TOKEN']
        access_token_secret = config.CONFIG['TWITTER_ACCESS_SECRET']
         
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
         

        api = tweepy.API(auth)

        api.update_with_media(imagepath, message)

        Util.get_logger().debug('Sent Screenshot Update')