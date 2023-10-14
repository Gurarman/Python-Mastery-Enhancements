from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

class Display:
    """
    A class used to manage the display of travel records and messages to the console.

    This class provides functionality to display travel records, messages, and error messages
    in a formatted and color-coded manner.

    Methods
    -------
    display_records(records):
        Displays multiple travel records in a tabulated format.
    display_single_record(record):
        Displays a single travel record in a tabulated format.
    display_creator_name():
        Displays the creator's name in blue text.
    display_message(message):
        Displays a message in blue text.
    display_error_message(message):
        Displays an error message in red text.
    """

    def display_records(self, records):
        """
        Displays multiple travel records in a tabulated format.

        Parameters
        ----------
        records : list of Record
            A list containing the travel records to be displayed.
        """
        print(Fore.CYAN + "Travel Records Table")
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

        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def display_single_record(self, record):
        """
        Displays a single travel record in a tabulated format.

        Parameters
        ----------
        record : Record
            The travel record to be displayed.
        """
        print(Fore.CYAN + "Travel Record Details")
        table = [
            [
                record.ref_number, record.title_en, record.purpose_en,
                record.start_date, record.end_date, f"${record.airfare:.2f}",
                f"${record.other_transport:.2f}", f"${record.lodging:.2f}",
                f"${record.meals:.2f}", f"${record.other_expenses:.2f}",
                f"${record.total:.2f}"
            ]
        ]
        headers = ["Ref Number", "Title", "Purpose", "Start Date", "End Date",
                    "Airfare", "Other Transport", "Lodging", "Meals", "Other Expenses", "Total"]

        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    @staticmethod
    def display_creator_name():
        """
        Displays the creator's name in blue text.
        """
        print(Fore.BLUE + "\nCreated by: Gurarman Singh")

    def display_message(self, message):
        """
        Displays a message in blue text.

        Parameters
        ----------
        message : str
            The message to be displayed.
        """
        print(Fore.BLUE + message)
        
    def display_error_message(self, message):
        """
        Displays an error message in red text.

        Parameters
        ----------
        message : str
            The error message to be displayed.
        """
        print(Fore.RED + message)
