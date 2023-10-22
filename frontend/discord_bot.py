import discord
from discord import Intents
import responses


async def send_msg(msg, user_msg, priv):
    try:
        response =  responses.get_responses(user_msg)
        await msg.author.send(response) if priv else await msg.channel.send(response)
    except Exception as e:
        #Change latr
        print(e)

def run_bot():
    TOKEN = 'MTE2NTU1MjE3NTQ2MDY2NzQyMg.Gu_BjN.23GCXKcZ-TdrCh1cr1BX2rxk40amkdCP62h0Fs'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f'{username} said: "{user_msg}"({channel})')

        if user_msg[0] == '!':
            user_msg = user_msg[1:]
            await send_msg(msg, user_msg, priv=True)
        else:
            await send_msg(msg, user_msg, priv=False)

    client.run(TOKEN)