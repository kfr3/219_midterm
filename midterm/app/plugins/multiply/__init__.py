from app.commands import Command
import logging

class MultiplyCommand(Command):
    def execute(self):
        n1 = float(input("Enter the first number for the multiplication operation: "))
        n2 = float(input("Enter the second number for the multiplication operation: "))
        try:
            n1 = float(n1)
            n2 = float(n2)
            answer = n1 * n2
            logging.info(f'{n1} multipied by {n2} is {answer}')

        except ValueError:
            print("Please enter valid numbers.")