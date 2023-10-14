from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

class Display:
    
    def display_records(self, records):
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
        print(Fore.BLUE + "\nCreated by: Gurarman Singh")

    def display_message(self, message):
        print(Fore.BLUE + message)
        
    def display_error_message(self, message):
        print(Fore.RED + message)
