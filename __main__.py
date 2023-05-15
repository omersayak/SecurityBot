from bot.my_bot import MyBot

if __name__ == "__main__":
    api_id = 2103305
    api_hash = '10dccb903ef15ce08d67a38cd8afa680'
    bot_token = "6240902231:AAGw8pd27ZUxeyPUrwI8Fn1w4RJlV2z4Z-c"
    group = "supersssw"  # Grup kimliğini veya kullanıcı adını buraya girin

    bot = MyBot(api_id, api_hash, bot_token, group)
    bot.run()
