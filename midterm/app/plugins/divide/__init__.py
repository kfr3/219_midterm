from app.commands import Command
import logging
import csv

class DivideCommand(Command):
    def execute(self):
        n1 = float(input("Enter the first number for the division operation: "))
        n2 = float(input("Enter the second number for the division operation: "))
        try:
            n1 = float(n1)
            n2 = float(n2)

            if n2 == 0:
                logging.error(f'User inputted zero as second number in division function.')
                print(f"You cannot divide by zero. Please enter a different number")
                return
            
            answer = n1 / n2
            logging.info(f'{n1} divided by {n2} is {answer}')
            print(f"{n1} divided by {n2} is {answer}")

        except ValueError:
            print("Please enter valid numbers.")
            logging.error(f'User entered invalid number')

        with open('./data/history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['divide', n1, n2, answer])