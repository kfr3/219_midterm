from app.commands import Command
import logging
import csv

class SubtractCommand(Command):
    def execute(self):
        n1 = float(input("Enter the first number for the subtraction operation: "))
        n2 = float(input("Enter the second number for the subtraction operation: "))
        try:
            n1 = float(n1)
            n2 = float(n2)
            answer = n1 - n2
            logging.info(f'{n1} minus {n2} is {answer}')
            print(f"{n1} minus {n2} is {answer}")

        except ValueError:
            print("Please enter valid numbers.")
            logging.error(f'User entered invalid number')

        with open('./data/history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['subtract', n1, n2, answer])
            
