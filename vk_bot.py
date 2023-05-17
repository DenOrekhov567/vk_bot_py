import vk_api
from vk_api.longpoll import VkLongPoll
from logger.logger import Logger
from database.connection import Connection
from database.model.user import User
from handler.event_handler import EventHandler
from command.command_manager import CommandManager

class VKBot:

    def __init__(self, token):
        self.token = token

    def run(self):
        self.init_components()
        
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk_api = self.vk_session.get_api()
        self.longpoll = VkLongPoll(self.vk_session)

        self.listen_longpoll()

    def init_components(self):
        self.logger = Logger()
        self.init_database()
        self.get_logger().execute(
            message="База данных инициализирована"
        )
        self.command_manager = CommandManager(vk_bot=self)
        self.event_handler = EventHandler(vk_bot=self)
        self.get_logger().execute(
            message="Идет прослушивание событий..."
        )

    def listen_longpoll(self):
        for event in self.longpoll.listen():
            self.event_handler.handle_event(event)

    def send_message(self, user_id, message):
        self.vk_api.messages.send(
            user_id=user_id,
            message=message,
            random_id=vk_api.utils.get_random_id()
        )

    def get_logger(self):
        return self.logger

    def init_database(self):
        connection = Connection()

        with connection.db:
            connection.db.create_tables([User])
            self.database = connection.db
        
    def get_database(self):
        return self.database