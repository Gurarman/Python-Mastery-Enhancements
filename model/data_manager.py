import pandas as pd
from model.record import Record

class DataManager:
    """
    A class used to manage data operations related to travel records.

    This class provides functionality to read travel records from a CSV file
    and convert them into a list of Record objects.

    Attributes
    ----------
    MAX_RECORDS : int
        The maximum number of records to be read from the CSV file.
    CSV_FILE_NAME : str
        The name of the CSV file containing the travel records.

    Methods
    -------
    read_csv_data():
        Reads the travel data from the CSV file and returns a list of Record objects.
    """

    MAX_RECORDS = 100
    CSV_FILE_NAME = 'data/travelq.csv'

    @staticmethod
    def read_csv_data():
        """
        Reads the travel data from the CSV file and converts it into a list of Record objects.

        This method reads the travel data from the CSV file specified by `CSV_FILE_NAME`,
        converts each record into a Record object, and returns a list of these objects.
        It reads a maximum of `MAX_RECORDS` records from the file.

        Returns
        -------
        list of Record
            A list containing the travel records as Record objects.

        Raises
        ------
        FileNotFoundError
            If the specified CSV file is not found.
        ValueError
            If the CSV file is empty.
        Exception
            If an error occurs while reading the CSV file.
        """
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
