import logging
import os
from app.commands import Command
import pandas as pd


class CsvCommand(Command):
    def execute(self):
        
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")

        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return

        '''calculator_abbrevations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }'''
        
        csv_file_path = os.path.join(data_dir, 'history.csv')
        logging.info(f'the relative path to save my file is {csv_file_path}')
        absolute_path = os.path.abspath(csv_file_path)
        logging.info(f'the absolute path  to save my file is {absolute_path}')
        df_read_states = pd.read_csv(csv_file_path)
        
        try:
            print("Calculator Functions from CSV:")
            for index, row in df_read_states.iterrows():
                function_info = f"{row['Function']}: {row['N1']}, {row['N2']}"
                print(f"Record {index}: {function_info}")
                logging.info(f"Record {index}: {function_info}")
            
            # Then, iterate through each field in the row to print and log
            for field in row.index:
                field_info = f"    {field}: {row[field]}"
                print(field_info)
                logging.info(f"Index: {index}, {field_info}")

        except:
            logging.info(f'No functions have been made')

    def add(self, n1, n2):
        answer = n1 + n2
        logging.info(f'{n1} plus {n2} equals {answer}')

    def subtract(self, n1, n2):
        answer = n1 - n2
        logging.info(f'{n1} minus {n2} equals {answer}')

    def multiply(self, n1, n2):
        answer = n1 * n2
        logging.info(f'{n1} multipled by {n2} equals {answer}')

    def divide(self, n1, n2):
        answer = n1 / n2
        logging.info(f'{n1} divided by {n2} equals {answer}')

    def clear():
        logging.info(f'Cleared csv file')

    
