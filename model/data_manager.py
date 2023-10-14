import pandas as pd
from model.record import Record

class DataManager:
    MAX_RECORDS = 100
    CSV_FILE_NAME = 'data/travelq.csv'

    @staticmethod
    def read_csv_data():
        try:
            df = pd.read_csv(DataManager.CSV_FILE_NAME)
            records = [
                Record(
                    row['ref_number'],
                    row['title_en'],
                    row['purpose_en'],
                    row['start_date'],
                    row['end_date'],
                    row['airfare'],
                    row['other_transport'],
                    row['lodging'],
                    row['meals'],
                    row['other_expenses'],
                    row['total'])
                for _, row in df.head(DataManager.MAX_RECORDS).iterrows()
            ]
            return records
        except FileNotFoundError:
            raise FileNotFoundError(f"File {DataManager.CSV_FILE_NAME} not found!")
        except pd.errors.EmptyDataError:
            raise ValueError(f"File {DataManager.CSV_FILE_NAME} is empty!")
        except Exception as e:
            raise Exception(f"Error reading the CSV file: {e}")
