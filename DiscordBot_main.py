import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        game = discord.Game("On the lookout.")
        await client.change_presence(status=discord.Status.idle, activity=game)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if str(message.author) == "randomname#0730":
            pass

        if message.author != client.user:
            await message.channel.send(message.content)
            print(message.channel.id)

    async def on_member_update(self, before, after:
    channel = client.get_channel(7468824724528169xx)
    if str(before) == "Wildyoda#0296":
        if after.activity == None:
            await channel.send("Good Job Buddy! I am glad you got off. Now you can focus on your studies!")
            game = discord.Game("On the lookout.")
        else:
            await channel.send("I am disappointed. Why are you playing?")
            game = discord.Game("WildYoda is losing. He should be studying.")

    await client.change_presence(status=discord.Status.idle, activity=game)

client = MyClient()
client.run(key)