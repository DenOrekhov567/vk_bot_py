from command.icommand import ICommand

class TestCommand(ICommand):

    def __init__(self, name, cooldown, vk_bot):
        # super().__init__(name, cooldown)
        self.vk_bot = vk_bot
        super().__init__(name, cooldown)
        
    # Метод, вызываемый при написании команды
    def execute(self, source):
        self.vk_bot.send_message(source.user_id, "Тестовая команда")