from model.record import Record
import pymongo
from pymongo import MongoClient
from operator import attrgetter
from datetime import datetime


class DataManager:
    """
    A class used to manage data operations related to travel records using MongoDB.

    This class provides functionality to read and manipulate travel records stored in a MongoDB database.
    It allows reading data from the database, inserting new records, updating existing records, 
    and deleting records.

    Attributes
    ----------
    MAX_RECORDS : int
        The maximum number of records to be read from the database.
    client : MongoClient
        MongoDB client for database interaction.
    db : Database
        MongoDB database instance.
    collection : Collection
        MongoDB collection to store travel records.

    Methods
    -------
    read_data_from_db():
        Reads travel records from MongoDB and returns them as a list of Record objects.
    insert_record(record):
        Inserts a new travel record into the MongoDB collection.
    update_record(ref_number, updated_details):
        Updates an existing travel record in the MongoDB collection.
    delete_record(ref_number):
        Deletes a travel record from the MongoDB collection based on its reference number.
    save_records_to_db(records):
        Saves multiple travel records to the MongoDB collection.
    """

    MAX_RECORDS = 100

    def __init__(self):
        # Initialize MongoDB Client
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['CST8333']
        self.collection = self.db['records']

    def read_data_from_db(self):
        """
        Reads the travel data from MongoDB and converts it into a list of Record objects.

        This method queries the MongoDB database to retrieve travel records and converts them 
        into a list of Record objects. It limits the number of records retrieved to MAX_RECORDS.

        Returns
        -------
        list of Record
            A list containing the travel records as Record objects.
        """
        mongo_records = self.collection.find().limit(self.MAX_RECORDS)
        allowed_keys = {'ref_number', 'title_en', 'purpose_en', 'start_date', 'end_date',
                        'airfare', 'other_transport', 'lodging', 'meals', 'other_expenses', 'total'}
        records = [Record(**{k: v for k, v in record.items()
                            if k in allowed_keys}) for record in mongo_records]
        return records

    def insert_record(self, record):
        """
        Inserts a new travel record into the MongoDB collection.

        Parameters
        ----------
        record : Record
            The Record object to be inserted into the database.
        """
        self.collection.insert_one(record.__dict__)

    def update_record(self, ref_number, updated_details):
        """
        Updates an existing travel record in the MongoDB collection.

        Parameters
        ----------
        ref_number : str
            The reference number of the travel record to be updated.
        updated_details : dict
            A dictionary containing the updated details of the record.
        """
        self.collection.update_one({'ref_number': ref_number}, {
                                    '$set': updated_details}, upsert=True)

    def delete_record(self, ref_number):
        """
        Deletes a travel record from the MongoDB collection based on its reference number.

        Parameters
        ----------
        ref_number : str
            The reference number of the travel record to be deleted.
        """
        self.collection.delete_one({'ref_number': ref_number})

    def save_records_to_db(self, records):
        """
        Saves multiple travel records to the MongoDB collection.

        Parameters
        ----------
        records : list of Record
            A list of Record objects to be saved to the database.
        """
        for record in records:
            self.update_record(record.ref_number, record.__dict__)

    def get_sorted_records(self, sort_criteria):
        """
        Fetches travel records from the database and sorts them in memory based on given criteria.

        Parameters
        ----------
        sort_criteria : list of tuples
            Each tuple contains a column name and a sorting order ('asc' or 'desc').

        Returns
        -------
        list of Record
            Sorted list of travel records.
        """
        # Fetch records from MongoDB
        records = list(self.collection.find().limit(self.MAX_RECORDS))

        # Convert to Record objects
        record_objects = []
        for record in records:
            # Map MongoDB fields to Record class constructor arguments
            record_args = {
                'ref_number': record.get('ref_number'),
                'title_en': record.get('title_en'),
                'purpose_en': record.get('purpose_en'),
                'start_date': record.get('start_date').strftime('%Y-%m-%d') if record.get('start_date') else None,
                'end_date': record.get('end_date').strftime('%Y-%m-%d') if record.get('end_date') else None,
                'airfare': record.get('airfare', 0.0),
                'other_transport': record.get('other_transport', 0.0),
                'lodging': record.get('lodging', 0.0),
                'meals': record.get('meals', 0.0),
                'other_expenses': record.get('other_expenses', 0.0),
                'total': record.get('total', 0.0),
            }
            record_objects.append(Record(**record_args))


        # Sort records in memory
        for field, order in sort_criteria:
            reverse = order == 'desc'
            record_objects = sorted(record_objects, key=attrgetter(field), reverse=reverse)

        return record_objects