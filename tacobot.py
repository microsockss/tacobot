import discord
import asyncio
import string

email = ('DISCORD EMAIL')
password = ('DISCORD PASSWORD')
channel = discord.Object(id='CHANNEL ID')

prefix = '!'

# Don't touch these variables
inputString = ''
scratching = False

print('Intializing . . .')
client = discord.Client()

async def commandHandler():
        scratching = False
        while not client.is_closed:
            inputString = input('> ')
            if inputString == 'scratch' and scratching == False:
                print('Starting scratch card loop')
                scratching = True
                await scratch()
            elif inputString == 'scratch' and scratching == True:
                print('Stopping scratch card loop')
                scratching = False

async def run():
        await client.wait_until_ready()
        while not client.is_closed:
                print('LOGGED IN SUCCESSFULLY')
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                botMessage = await client.send_message(channel, prefix + 'work')
                print('Sent: ' + prefix + 'work')
                await asyncio.sleep(300)
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                await asyncio.sleep(300)
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                botMessage = await client.send_message(channel, prefix + 'work')
                print('Sent: ' + prefix + 'work')

async def scratch():
        while not client.is_closed:
            if (scratching == False):
                return
            else:
                botMessage = await client.send_message(channel, prefix + 'scratch')
                print('Sent: ' + prefix + 'scratch')
                await asyncio.sleep(8)

client.loop.create_task(run())
client.run(email, password)
