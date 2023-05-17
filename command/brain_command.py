from command.icommand import ICommand
from database.model.user import User
import datetime
import random

class BrainCommand(ICommand):

    def __init__(self, name, cooldown, vk_bot):
        self.vk_bot = vk_bot
        super().__init__(name, cooldown)
        
    # Метод, вызываемый при написании команды
    def execute(self, source):
        user_data = User.get_or_none(
            User.vk_id==source.user_id
        )

        # Если пользователя нет в таблице
        if user_data == None:
            User.create(
                vk_id=source.user_id, 
                brain_size=0, 
                brain_size_last_update=datetime.date.today()
            )
            message = "Ура! Победа! Твой мозг... сейчас он — 0²"
        else:
            user_data = User.get(
                User.vk_id==source.user_id
            )

            brain_size = user_data.brain_size
            brain_size_last_update = user_data.brain_size_last_update

            if not brain_size_last_update == datetime.date.today():
                rand_int = random.randint(1, 5)
    
                if rand_int >= brain_size:
                    brain_size += rand_int
    
                    message = 'Твой мозг увеличился на ' + str(rand_int) + '², сейчас он — ' + str(brain_size) + '²'
                        
                if random.randint(1, 2) == 1:
                    brain_size += rand_int
    
                    message = 'Твой мозг увеличился на ' + str(rand_int) + '², сейчас он — ' + str(brain_size) + '²'
                else:
                    # Переинициализируем запись пользователя
                    brain_size -= rand_int
    
                    message = 'Твой мозг уменьшился на ' + str(rand_int) + '², сейчас он — ' + str(brain_size) + '²'
    
                User.update(
                    brain_size=brain_size,
                    brain_size_last_update=datetime.date.today()
                ).where(
                    User.vk_id==source.user_id
                ).execute()
            else:
                message = "Сегодня ты уже не можешь прокачать свой мозг..."
            
        self.vk_bot.send_message(source.user_id, message)