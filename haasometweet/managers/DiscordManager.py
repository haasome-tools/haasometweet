import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

def clean_spaces(message):
    dataToClean = message.split(' ')
    dataCleaned = []
    for data in dataToClean:
        if data is not '':
            dataCleaned.append(data)

    dataCleaned = dataCleaned[1:]

    return ' '.join(dataCleaned)

def return_clean_message(message):
    data = message['fields'][0]['value'].split('\n')

    returnData = []

    # Get The Title
    returnData.append(' '.join(data[0].split(" ")[:2]))
    returnData.append(clean_spaces(' '.join(data[2].strip().split(" "))))
    returnData.append(clean_spaces(data[3].strip()))
    returnData.append(clean_spaces(data[6].strip()))

    return returnData

@bot.event
async def on_message(message):
    if message.channel.name == "completed-orders":
        if len(message.embeds) > 0:
            for x in message.embeds:
                data = return_clean_message(x)
                tweet = "Decision: " + str(data[0]) + "\n"
                tweet = tweet + "Market: " + str(data[1]) + "\n"
                tweet = tweet + "Price: " + str(data[2]) + "\n"
                tweet = tweet + "Origin: " + str(data[3]) + "\n"
                tweet = tweet + config.CONFIG['HASHTAG_TRADE_DECISION_TEXT']
                
                send_tweet(tweet)
