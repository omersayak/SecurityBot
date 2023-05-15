from pyrogram import Client, filters

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
        await client.send_photo(message.chat.id, "https://imgur.com/gallery/wYTCtRu")

    async def welcome_message(self, client, message):
        await message.reply_text("Hello, Welcome to the group chat!")

    def run(self):
        print("I AM ALIVE")
        self.bot.run()

if __name__ == "__main__":
    api_id = 2103305
    api_hash = '10dccb903ef15ce08d67a38cd8afa680'
    bot_token = "6240902231:AAGw8pd27ZUxeyPUrwI8Fn1w4RJlV2z4Z-c"
    group = "supersssw"  # Grup kimliğini veya kullanıcı adını buraya girin
    
    bot = MyBot(api_id, api_hash, bot_token, group)
    bot.run()
