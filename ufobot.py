import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.Member):
    # Check if the reaction was added to a message in the designated channel
    if reaction.message.channel.name == "dochazka":
        # Check if the reaction is the one we're looking for
        if str(reaction.emoji) == "✅":
            # Create a new role
            new_role = await reaction.message.guild.create_role(name="Dochazka Yes")
            # Add the role to the user who reacted to the message
            await user.add_roles(new_role)


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    # Check if the reaction was removed from a message in the designated channel
    if payload.channel_id == "dochazka":
        # Get the associated guild and member objects
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        # Get the role that corresponds to the reaction
        role = discord.utils.get(guild.roles, name="Dochazka yes")
        # Remove the role from the member who removed the reaction
        await member.remove_roles(role)
