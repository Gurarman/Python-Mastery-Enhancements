import pandas as pd
from tabulate import tabulate
from colorama import init, Fore

# Initialize colorama for colored terminal output.
init(autoreset=True)

# Constants for default CSV file name and number of records to display.
# CSV is the dataset used Proactive Disclosure - Travel Expenses retrieved from the Open Government of Canada, published by The Treasury Board, Canada.
CSV_FILE_NAME = 'travelq.csv'
MAX_RECORDS = 5

    
class Record:
    """
    Represents a record from the travel data CSV.

    Attributes:
    - ref_number: Reference number of the record.
    - title_en: Title in English.
    - purpose_en: Purpose of travel in English.
    - start_date: Start date of travel.
    - end_date: End date of travel.
    - airfare: Cost of airfare.
    - other_transport: Cost of other transportation.
    - lodging: Cost of lodging.
    - meals: Cost of meals.
    - other_expenses: Cost of other miscellaneous expenses.
    - total: Total cost.
    """

    # Initialize the attributes from the provided parameters.
    def __init__(self, ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total):
        self.ref_number = ref_number
        self.title_en = title_en
        self.purpose_en = purpose_en
        self.start_date = start_date
        self.end_date = end_date
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total


def read_csv_data(file_name):
    """
    Reads the CSV data and returns a list of Record objects.

    Args:
    - file_name: Name of the CSV file.

    Returns:
    List of Record objects.
    """
    try:
        df = pd.read_csv(file_name)
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
            for _, row in df.head(MAX_RECORDS).iterrows()
        ]
        return records

    except FileNotFoundError:
        print(f"File {file_name} not found!")
        return []
    except pd.errors.EmptyDataError:
        print(f"File {file_name} is empty!")
        return []
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []


def display_records(records):
    """
    Displays the list of records in a tabular format.

    Args:
    - records: List of Record objects to display.
    """

    print(Fore.CYAN + "Travel Records Table")

    # Create a list of rows for tabulation
    table = [
        [
            record.ref_number, record.title_en, record.purpose_en,
            record.start_date, record.end_date, f"${record.airfare:.2f}",
            f"${record.other_transport:.2f}", f"${record.lodging:.2f}",
            f"${record.meals:.2f}", f"${record.other_expenses:.2f}",
            f"${record.total:.2f}"
        ]
        for record in records
    ]

    headers = ["Ref Number", "Title", "Purpose", "Start Date", "End Date",
                "Airfare", "Other Transport", "Lodging", "Meals", "Other Expenses", "Total"]

    print(tabulate(table, headers=headers, tablefmt="grid"))

    print(Fore.BLUE + "\nCreated by: Gurarman Singh")


def main():
    """
    Main function to orchestrate reading and displaying of records.
    """
    records = read_csv_data(CSV_FILE_NAME)
    display_records(records)


if __name__ == '__main__':
    main()
