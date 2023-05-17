from command.icommand import ICommand
import random

class BrainCommand(ICommand):

    def __init__(self, name, cooldown, vk_bot):
        self.vk_bot = vk_bot
        self.lst_users = {}
        super().__init__(name, cooldown)
        
    # Метод, вызываемый при написании команды
    def execute(self, source):
    # Если словарь пуст или пользователя нет в словаре
        if self.lst_users == {} or self.lst_users.get(source.user_id) == False:
            # Инициализируем запись пользователя
            self.lst_users[source.user_id] = 10;

            message = 'Ты активировал свой мозг, сейчас он — 10 см²'
        else:
            rand_int = random.randint(1, 10)

            if rand_int >= self.lst_users[source.user_id]:
                # Переинициализируем запись пользователя
                self.lst_users[source.user_id] += rand_int

                message = 'Твой мозг увеличился на ' + str(rand_int) + '², сейчас он — ' + str(self.lst_users[source.user_id]) + '²'
                    
            if random.randint(1, 2) == 1:
                # Переинициализируем запись пользователя
                self.lst_users[source.user_id] += rand_int

                message = 'Твой мозг увеличился на ' + str(rand_int) + '², сейчас он — ' + str(self.lst_users[source.user_id]) + '²'
            else:
                # Переинициализируем запись пользователя
                self.lst_users[source.user_id] -= rand_int

                message = 'Твой мозг уменьшился на ' + str(rand_int) + '², сейчас он — ' + str(self.lst_users[source.user_id]) + '²'
                
        self.vk_bot.send_message(source.user_id, message)