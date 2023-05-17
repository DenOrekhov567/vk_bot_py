from command.test_command import TestCommand
from command.brain_command import BrainCommand

class CommandManager:

    pool_commands = {}
    
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.init_commands()

    def init_commands(self):
        self.pool_commands["тест"] = TestCommand(
            name="тест", cooldown=0, vk_bot=self.vk_bot
        )
        
        self.pool_commands["мозг"] = BrainCommand(
            name="мозг", cooldown=0, vk_bot=self.vk_bot
        )