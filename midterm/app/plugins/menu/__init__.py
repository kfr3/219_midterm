from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self):
        print(f'Here is a list of the commands you can use:')
        print(f'add')
        print(f'subtract')
        print(f'multiply')
        print(f'divide')
        print(f'menu')
        print(f'clear')
        
