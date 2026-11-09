import os
import discord

from dotenv import load_dotenv
from ai.client import generate_response

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# ユーザーごとの会話履歴
histories = {}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):

    if message.author.bot:
        return

    # Botへのメンション、またはDMだけに反応
    if (
        bot.user not in message.mentions
        and not isinstance(message.channel, discord.DMChannel)
    ):
        return

    user_id = message.author.id

    if user_id not in histories:
        histories[user_id] = []

    history = histories[user_id]

    history.append({
        "role": "user",
        "content": message.content
    })

    async with message.channel.typing():

        try:
            reply = await generate_response(history)

            history.append({
                "role": "assistant",
                "content": reply
            })

            await message.reply(reply)

        except Exception as e:
            print(f"Error: {e}")
            await message.reply("ごめんね、ちょっと調子が悪いみたい……")


bot.run(os.getenv("DISCORD_TOKEN"))