class Record:
    """
    A class used to represent a travel record.

    This class encapsulates all the attributes related to a travel record,
    providing a structured format to store and manipulate travel data.

    Attributes
    ----------
    ref_number : str
        The reference number of the travel record.
    title_en : str
        The title of the travel record in English.
    purpose_en : str
        The purpose of the travel, described in English.
    start_date : str
        The start date of the travel in 'YYYY-MM-DD' format.
    end_date : str
        The end date of the travel in 'YYYY-MM-DD' format.
    airfare : float
        The cost of airfare.
    other_transport : float
        The cost of other transportation.
    lodging : float
        The cost of lodging.
    meals : float
        The cost of meals.
    other_expenses : float
        The cost of other miscellaneous expenses.
    total : float
        The total cost of the travel.

    Methods
    -------
    No methods are defined for this class.
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
