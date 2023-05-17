from vk_api.longpoll import VkEventType

class EventHandler:

    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.lst_users = {}
        
    def handle_event(self, event):
        if event.type == VkEventType.MESSAGE_NEW:
            if event.text[0] == "/":
                self.handle_command(event)
            else:
                self.handle_message_new(event)

    def handle_command(self, event):
        command = self.vk_bot.command_manager.pool_commands.get(
            event.text[1:]
        )

        if not command == None:
            command.execute(source=event)
        
    def handle_message_new(self, event):
        pass