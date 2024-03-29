from app.commands import Command
import logging

class DivideCommand(Command):
    def execute(self):
        n1 = float(input("Enter the first number for the division operation: "))
        n2 = float(input("Enter the second number for the division operation: "))
        try:
            n1 = float(n1)
            n2 = float(n2)
            answer = n1 / n2
            logging.info(f'{n1} divided by {n2} is {answer}')

        except ValueError:
            print("Please enter valid numbers.")