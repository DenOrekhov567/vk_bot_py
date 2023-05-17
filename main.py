from utils.utils import get_token
from vk_bot import VKBot

class Main:
    
    if __name__ == '__main__':
        print("Бот запускается...")
        bot = VKBot(token=get_token())
        bot.run()