import discord
client = discord.Client()
@client.event
async def on_message(message):
  await message.channel.send("fhjfks")
tok = "NzMzMjM3NDQ1MTcyMzk2MDQ0"
en = ".XxAOlQ.A6_McAUlhRfFvJuDE7IloQe98tc"
client.run(str(tok+en))
