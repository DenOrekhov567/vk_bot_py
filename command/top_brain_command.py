from command.icommand import ICommand
from database.model.user import User

class TopBrainCommand(ICommand):

    def __init__(self, name, cooldown, vk_bot):
        self.vk_bot = vk_bot
        super().__init__(name, cooldown)
        
    # Метод, вызываемый при написании команды
    def execute(self, source):
        self.vk_bot.send_message(source.user_id, 'l')
        lol = User.select()
        print(lol)