from pyrogram import Client, filters
import random

class MyBot:
    def __init__(self, api_id, api_hash, bot_token, group):
        self.bot = Client(
            "my_first_project",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token
        )
        self.group = group
        self.register_handlers()

    def register_handlers(self):
        self.bot.on_message(filters.command('start') & filters.private)(self.command_start)
        self.bot.on_message(filters.command('help'))(self.command_help)
        self.bot.on_message(filters.command('photo'))(self.command_photo)
        self.bot.on_message(filters.chat(self.group) & filters.new_chat_members)(self.welcome_message)

    async def command_start(self, client, message):
        await client.send_message(message.chat.id, "Heya, I am a simple test bot.")

    async def command_help(self, client, message):
        await message.reply_text("This is the test bot's help section.")

    async def command_photo(self, client, message):
        photo_link = [
            "https://imgur.com/gallery/KWvtdg0",
            "https://imgur.com/gallery/wYTCtRu",
            "https://imgur.com/gallery/dw3mC",
            "https://imgur.com/gallery/8zdXp",
        ]
        random_link = random.choice(photo_link)
        await client.send_photo(message.chat.id, random_link)

    async def welcome_message(self, client, message):
        await message.reply_text("Hello, Welcome to the group chat!")

    def run(self):
        print("I AM ALIVE")
        self.bot.run()
