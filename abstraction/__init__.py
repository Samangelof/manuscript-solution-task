from database_handler import DatabaseHandler
from data_processing import DataProcessor


if __name__ == '__main__':
    db_handler = DatabaseHandler('base.sqlite')
    db_handler.connect()

    data_processor = DataProcessor(db_handler, 'products')

    # data_processor.insert_data('data.xlsx')
    # data_processor.process_data()

    db_handler.disconnect()



#! Samangelof !#