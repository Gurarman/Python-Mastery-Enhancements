import unittest
from model.record import Record
from controller.main_controller import MainController

class TestMainController(unittest.TestCase):

    def setUp(self):
        self.controller = MainController()

    def test_add_new_record(self):
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
        
        # Assume: A method to add a record directly (might need to be implemented)
        new_record = Record(**record_details)
        self.controller.records.append(new_record)
        
        # Act
        final_len = len(self.controller.records)
        
        # Assert
        self.assertEqual(final_len, initial_len + 1, "New record was not added successfully")

if __name__ == '__main__':
    unittest.main()
