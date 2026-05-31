import discord
from discord import app_commands
from discord.ext import tasks

import datetime

####################################################################################################

# to get these, make sure discord developer mode is enabled, and then just right click on a user or channel to copy the id
LibraryServerId = 465227088002154526
FrontDeskChannelId = 1144367171212939404
AlertsAndRolesChannelId = 599736045709557763
LogsChannelId = 725045035044831243

NotificationsMessageId = 599745222792183808
PronounsMessageId = 1087090519731077241
CommissionMessageId = 1121794581646803015
EventMessageId = 1121885276793491536
RulesMessageId = 465766450691440645

SierraUserId = 175264618644635648
MalUserId = 179394925685637120
FloUserId = 157319368655634433

AllArtRoleId = 599732332114608139
FinishedPiecesRoleId = 599742216151367701
TransformationArtRoleId = 599733029740478485
NonTransformationArtRoleId = 599744199230881812
SketchesRoleId = 599733568268402701
ComicsRoleId = 599733660278849546
WorksInProgressRoleId = 599733069783760907
AnimationsRoleId = 599733715945652224
LivestreamsRoleId = 599739888673357829
OneYearTillMidnightRoleId = 804806291008651264
MacroRoleId = 1121789161771372615
NonMacroRoleId = 1121788987661635645
HeHimRoleId = 1087083102704238763
SheHerRoleId = 1087083232127897670
TheyThemRoleId = 1087083285601075280
CommissionsRoleId = 1121793404637040720
DonoDoodlesRoleId = 1121792988092313690
VrChatRoleId = 1096409375825989682
JackboxRoleId = 1096409490645069934
VerifiedRoleId = 1145359302656278599

TokenFile = "token.txt"

####################################################################################################

# intents are like permissions for twitch bots
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# set up bot client + command support
client = discord.Client(intents=intents)
command_tree = app_commands.CommandTree(client)

####################################################################################################

# see https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_ready#event-reference for a list of all events

@client.event
async def on_ready():
	if client.user != None:
		print(f"Connected as {client.user.name}")

@client.event
async def on_member_join(member: discord.Member):
	front_desk_channel = await client.fetch_channel(FrontDeskChannelId)

	# put <@user_id> in a message to ping someone; put <#channel_id> in a message to link a channel
	await front_desk_channel.send(f"<@{member.id}> joined! Welcome to the library! Please be sure to read the rules, and if you want to be notified when WhenWolvesCryOut uploads art or goes live on twitch, please check the <#{AlertsAndRolesChannelId}> channel. If you have any questions, please ask <@{SierraUserId}>, <@{MalUserId}>, or <@{FloUserId}>.") # type: ignore

@client.event
async def on_raw_member_remove(payload: discord.RawMemberRemoveEvent):
	logs_channel = await client.fetch_channel(LogsChannelId)
	await logs_channel.send(f"<@{payload.user.id}> ({payload.user.name}) has left the server.") # type: ignore

@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
	if payload.message_id == NotificationsMessageId:
		if str(payload.emoji) == "1⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(AllArtRoleId)) # type: ignore
		elif str(payload.emoji) == "2⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(FinishedPiecesRoleId)) # type: ignore
		elif str(payload.emoji) == "3⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(TransformationArtRoleId)) # type: ignore
		elif str(payload.emoji) == "4⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(NonTransformationArtRoleId)) # type: ignore
		elif str(payload.emoji) == "5⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(SketchesRoleId)) # type: ignore
		elif str(payload.emoji) == "6⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(ComicsRoleId)) # type: ignore
		elif str(payload.emoji) == "7⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(WorksInProgressRoleId)) # type: ignore
		elif str(payload.emoji) == "8⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(AnimationsRoleId)) # type: ignore
		elif str(payload.emoji) == "9⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(LivestreamsRoleId)) # type: ignore
		elif str(payload.emoji) == "🔟":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(OneYearTillMidnightRoleId)) # type: ignore
		elif str(payload.emoji) == "🔼":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(MacroRoleId)) # type: ignore
		elif str(payload.emoji) == "🔽":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(NonMacroRoleId)) # type: ignore
	elif payload.message_id == PronounsMessageId:
		if str(payload.emoji) == "♂️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(HeHimRoleId)) # type: ignore
		elif str(payload.emoji) == "♀️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(SheHerRoleId)) # type: ignore
		elif str(payload.emoji) == "⚧️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(TheyThemRoleId)) # type: ignore
	elif payload.message_id == CommissionMessageId:
		if str(payload.emoji) == "🖌️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(CommissionsRoleId)) # type: ignore
		elif str(payload.emoji) == "✏️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(DonoDoodlesRoleId)) # type: ignore
	elif payload.message_id == EventMessageId:
		if str(payload.emoji) == "🗣️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(VrChatRoleId)) # type: ignore
		elif str(payload.emoji) == "📦":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(JackboxRoleId)) # type: ignore
	elif payload.message_id == RulesMessageId:
		if str(payload.emoji) == "✅":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).add_roles(discord.Object(VerifiedRoleId)) # type: ignore

@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
	if payload.message_id == NotificationsMessageId:
		if str(payload.emoji) == "1⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(AllArtRoleId)) # type: ignore
		elif str(payload.emoji) == "2⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(FinishedPiecesRoleId)) # type: ignore
		elif str(payload.emoji) == "3⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(TransformationArtRoleId)) # type: ignore
		elif str(payload.emoji) == "4⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(NonTransformationArtRoleId)) # type: ignore
		elif str(payload.emoji) == "5⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(SketchesRoleId)) # type: ignore
		elif str(payload.emoji) == "6⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(ComicsRoleId)) # type: ignore
		elif str(payload.emoji) == "7⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(WorksInProgressRoleId)) # type: ignore
		elif str(payload.emoji) == "8⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(AnimationsRoleId)) # type: ignore
		elif str(payload.emoji) == "9⃣":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(LivestreamsRoleId)) # type: ignore
		elif str(payload.emoji) == "🔟":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(OneYearTillMidnightRoleId)) # type: ignore
		elif str(payload.emoji) == "🔼":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(MacroRoleId)) # type: ignore
		elif str(payload.emoji) == "🔽":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(NonMacroRoleId)) # type: ignore
	elif payload.message_id == PronounsMessageId:
		if str(payload.emoji) == "♂️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(HeHimRoleId)) # type: ignore
		elif str(payload.emoji) == "♀️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(SheHerRoleId)) # type: ignore
		elif str(payload.emoji) == "⚧️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(TheyThemRoleId)) # type: ignore
	elif payload.message_id == CommissionMessageId:
		if str(payload.emoji) == "🖌️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(CommissionsRoleId)) # type: ignore
		elif str(payload.emoji) == "✏️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(DonoDoodlesRoleId)) # type: ignore
	elif payload.message_id == EventMessageId:
		if str(payload.emoji) == "🗣️":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(VrChatRoleId)) # type: ignore
		elif str(payload.emoji) == "📦":
			await (await client.get_guild(LibraryServerId).fetch_member(payload.user_id)).remove_roles(discord.Object(JackboxRoleId)) # type: ignore

# this code will be executed upon running this file
# this weird if statement is just a python convention; it makes sure code doesn't get executed at the wrong time
if __name__ == "__main__":
	token_file = open(TokenFile, "r")
	token = token_file.readline()
	token_file.close()

	client.run(token)
