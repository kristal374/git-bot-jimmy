import discord

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(int(733230754817114166))
    await channel.send('Reconecting Complite!')

tok = "NzMzMjM3NDQ1MTcyMzk2MDQ0"
en = ".XxAOlQ.A6_McAUlhRfFvJuDE7IloQe98tc"
client.run(str(tok+en))
