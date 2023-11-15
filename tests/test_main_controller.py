import unittest
import sys
from unittest.mock import MagicMock
from model.data_manager import DataManager
from model.record import Record
from controller.main_controller import MainController
from unittest.mock import patch



class TestMainController(unittest.TestCase):
    """
    Unit test class for testing CRUD methods of the MainController class.

    Methods
    -------
    setUp():
        Prepare resources for testing.
    test_create_record():
        Test creating a new record.
    test_edit_record():
        Test editing an existing record.
    test_delete_record():
        Test deleting a record.
    test_save_data_to_db():
        Test saving data to the database.
    """

    def setUp(self):
        """
        Set up the testing environment before each test method.
        """
        sys.stderr.write("Tests run by: Gurarman Singh")
        self.controller = MainController()
        self.controller.data_manager.insert_record = MagicMock()
        self.controller.data_manager.update_record = MagicMock()
        self.controller.data_manager.delete_record = MagicMock()
        self.controller.data_manager.save_records_to_db = MagicMock()
        self.controller.input.get_record_details = MagicMock(return_value={
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
        })

    def test_create_record(self):
        """
        Test the ability to create a new record.
        """
        # Act
        self.controller.create_record()

        # Assert
        self.controller.data_manager.insert_record.assert_called_once()

    @patch('builtins.input', side_effect=['T-2023-P11-001'])
    def test_delete_record(self, mock_input):
        """
        Test the ability to delete a record.
        """
        # Arrange
        ref_number_to_delete = 'T-2023-P11-001'
        self.controller.records = [Record(ref_number=ref_number_to_delete, title_en='Test Title', purpose_en='Test Purpose', start_date='2023-01-01', end_date='2023-01-05', airfare=500.00, other_transport=100.00, lodging=200.00, meals=150.00, other_expenses=50.00, total=1000.00)]

        # Act
        self.controller.delete_record()

        # Assert
        self.controller.data_manager.delete_record.assert_called_once_with(ref_number_to_delete)

    @patch('builtins.input', side_effect=['T-2023-P11-001'])
    def test_edit_record(self, mock_input):
        """
        Test the ability to edit an existing record.
        """
        # Arrange
        ref_number_to_edit = 'T-2023-P11-001'
        self.controller.records = [Record(ref_number=ref_number_to_edit, title_en='Old Title', purpose_en='Old Purpose', start_date='2023-01-01', end_date='2023-01-05', airfare=400.00, other_transport=90.00, lodging=180.00, meals=120.00, other_expenses=40.00, total=830.00)]
        
        updated_details = {
            'title_en': 'Updated Title',
            'purpose_en': 'Updated Purpose',
            'airfare': 550.00,
            'other_transport': 110.00,
            'lodging': 250.00,
            'meals': 160.00,
            'other_expenses': 60.00,
            'total': 1130.00
        }
        
        self.controller.input.get_record_details.return_value = updated_details

        # Act
        self.controller.edit_record()

        # Assert
        self.controller.data_manager.update_record.assert_called_once_with(ref_number_to_edit, updated_details)


    def test_save_data_to_db(self):
        """
        Test saving records to the database.
        """
        # Arrange
        self.controller.records = [Record('T-2023-P11-001', 'Test Title', 'Test Purpose', '2023-01-01', '2023-01-05', 500.00, 100.00, 200.00, 150.00, 50.00, 1000.00)]

        # Act
        self.controller.save_data_to_db()

        # Assert
        self.controller.data_manager.save_records_to_db.assert_called_once_with(self.controller.records)


if __name__ == '__main__':
    print(f"Tests run by: Gurarman Singh")
    unittest.main()
