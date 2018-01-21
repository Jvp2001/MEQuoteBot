import discord
from discord.ext import commands
class Quotes:
    file = "./Files/Quotes.txt"

    @classmethod
    async def add(cls,quote:str() ,author: str, updateQuotes, callback):
        with open(cls.file,"a+") as file:
            author = str(author).split("#")
            q = quote+"\n-"+"("+author[0]+")"
            quotes = cls.GetQuotes()
            #print("\n\n"str(quotes)+"\n\n")
            if q not in  quotes:
                file.write(q)
                file.write("\n")
                await updateQuotes()

    @classmethod
    def makeQuote(cls,quoteArr) -> str:
        quote = ""
        for word in quoteArr:
            quote+=word+" "
        return quote

    @classmethod
    def GetQuotes(cls) -> set:
        allQuotes = set()
        with open(cls.file,"r",newline="\n") as quotes:

           #print(quotes.read().split("|"))
            for quote in quotes.read().split("|"):

                allQuotes.add(quote)
        return allQuotes


    @classmethod
    def randomSetItem(cls,theSet: set):
        print(theSet)
        from random import choice
        setList = []
        for i in theSet:
            setList.append(i)
        return choice(setList)