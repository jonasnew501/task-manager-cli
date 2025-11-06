
from abc import ABC, abstractmethod

class CommandHandler(ABC):
    def match(command: str) -> bool:
        pass


class AddCommand(CommandHandler):
    def __init__(self, command) -> None:
        self.command = command
    
    def match(command: str) -> bool:
        pass