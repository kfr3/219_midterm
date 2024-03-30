from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self):
        logging.info(f'Here is a list of the commands you can use:')
        logging.info(f'add')
        logging.info(f'subtract')
        logging.info(f'multiply')
        logging.info(f'divide')
        logging.info(f'menu')
        
