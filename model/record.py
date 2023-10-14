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
