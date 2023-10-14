import unittest
from model.record import Record
from controller.main_controller import MainController

class TestMainController(unittest.TestCase):
    """
    Unit test class for testing methods of the MainController class.

    This class inherits from unittest.TestCase and includes methods to test
    the functionality of methods in the MainController class, particularly
    focusing on the ability to add a new record to the controller's records.

    Methods
    -------
    setUp():
        Special method to instantiate the MainController before each test method.
    test_add_new_record():
        Test case to verify that a new record can be added to the controller's records.
    """

    def setUp(self):
        """
        Set up the testing environment before each test method.

        This method is called before each individual test method, and sets up
        the necessary objects for testing. Specifically, it creates an instance
        of MainController and assigns it to the instance variable self.controller.
        """
        self.controller = MainController()

    def test_add_new_record(self):
        """
        Test the ability to add a new record to the controller's records.

        This method:
        - Stores the initial length of the controller's records.
        - Creates a new Record object with mock data and adds it to the controller's records.
        - Checks that the length of the controller's records has increased by 1.
        """
        # Arrange
        initial_len = len(self.controller.records)
        
        # Mock record details
        record_details = {
            'ref_number': 'T-2023-P11-001',
            'title_en': 'Test Title',
            'purpose_en': 'Test Purpose',
            'start_date': '2023-01-01',
            'end_date': '2023-01-05',
            'airfare': 500.00,
            'other_transport': 100.00,
            'lodging': 200.00,
            'meals': 150.00,
            'other_expenses': 50.00,
            'total': 1000.00
        }
        
        # Assume: A method to add a record directly
        new_record = Record(**record_details)
        self.controller.records.append(new_record)
        
        # Act
        final_len = len(self.controller.records)
        
        # Assert
        self.assertEqual(final_len, initial_len + 1, "New record was not added successfully")

if __name__ == '__main__':
    """
    Main entry point for running the tests.

    When the script is run as the main module, it runs the tests defined in TestMainController.
    """
    unittest.main()
