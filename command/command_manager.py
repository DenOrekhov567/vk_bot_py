from command.test_command import TestCommand
from command.brain_command import BrainCommand
from command.top_brain_command import TopBrainCommand

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
        self.pool_commands["топ_мозг"] = TopBrainCommand(
            name="топ_мозг", cooldown=0, vk_bot=self.vk_bot
        )