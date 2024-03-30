from app.commands import Command
import logging
import csv
import argparse

class ClearCommand(Command):
    def execute(self):
        try:
        # Open the file in write mode, which clears its contents
            with open('./data/history.csv', 'w', newline='') as file:
                pass  # Just open and close the file to clear its contents
            return True  # Return True if the operation is successful
            logging.info(f'Cleared csv file')
            print(f'You cleared the csv file.')
        except Exception as e:
            print(f"Error clearing history: {e}")
            logging.error(f'Failed to clear history')
            return False

            file_path = './data/history.csv'
            if clear_history(file_path):
                print("History cleared successfully.")
            else:
                print("Failed to clear history.")
