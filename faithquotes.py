
import discord
import discord.ext.commands
import discord.ext.commands.bot as b

import Speeches
from Repos.QuoteBot import Quote

Quotes = Quote.Quotes
bot = b.Bot(command_prefix="!")

quotes = set()

client = discord.Client()

help_msg="!Quote for a quote."
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Mirror's Edge"))
    global quotes

    quotes = Quotes.GetQuotes()
    print(quotes)




@client.event
async def on_message(message):
    # if message.content.startswith("!"):
    #     msg = message.content[12:]
    #     await client.send_message(message.channel,msg.split(" "))
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def quote(ctx):
    global quotes
    message = ctx.message
    if(message.content.startswith("!quote")):
        msg = message.content.split(" ")
        if len(msg) == 1:
            quote = Quotes.randomSetItem(quotes)
            print(quote)
            await client.send_message(message.channel,quote)
        else:
            if msg[1] == "Jerry" or msg[1] == "jerry":
                await client.send_message(message.channel,
                                          "When a girl buys a vibrator its seen as a bit of naughty fun. BUT when a guy orders a 240 Volt FuckMaster Pro 5000 blowup latex doll with 6 speed pulsating vagina, elasticized anus with non-drip semen collection tray, together with optional built in realistic orgasm scream surround sound system, he's called a pervert?\n-(SteveGlowPlunk & Jerry)\n")

            if msg[1] == "add":

                q = " ".join(map(str,msg[2:]))

                print(q+"\n")
                done = await Quotes.add(q,message.author,
                    callback=lambda: client.send_message(message.channel,
                                                "Already a quote."),
                    updateQuotes=lambda: client.send_message(message.channel,"Added:\n"+q)
                )

@bot.command(pass_context=True)
async def speech(ctx):

    message = ctx.message
    speeches = Speeches
    if(message.content.startswith("!speech")):
        msg = message.content.split(" ")
        print(msg[1])
        if(msg[1].lower() in speeches.keys()):
            #print(speeches[msg[1]])
            await client.send_message(message.channel,speeches[msg[1]])

client.run('MzY3NTQ1NDIwOTkxNDMwNjY2.DL8_DQ.jilMs2jv9P5_rWCogxgqkSfZa1s')
