from abc import ABC, abstractmethod

class ICommand(ABC):

    # При реализации интерфейса ICommand необходимо обязательно использовать
    # конструктор со следующим содержимым:
    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown

    # Метод интерфейса ICommand, который необходимо обязательно реализовать в 
    # классе-наследнике
    @abstractmethod
    def execute(self):
        pass