from utils.utils import get_token
from vk_bot import VKBot

class Main:
    
    if __name__ == '__main__':
        print("Загрузка начинается...")
        bot = VKBot(token=get_token())
        bot.run()