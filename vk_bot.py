import vk_api
from vk_api.longpoll import VkLongPoll
from handler.event_handler import EventHandler
from command.command_manager import CommandManager

class VKBot:

    def __init__(self, token):
        self.token = token

    def run(self):
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk_api = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)
        self.command_manager = CommandManager(vk_bot=self)
        self.event_handler = EventHandler(vk_bot=self)
        self.listen_longpoll()

    def listen_longpoll(self):
        for event in self.longpoll.listen():
            self.event_handler.handle_event(event)

    def send_message(self, user_id, message):
        self.vk_api.messages.send(
            user_id=user_id,
            message=message,
            random_id=vk_api.utils.get_random_id()
        )