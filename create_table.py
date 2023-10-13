import sqlite3
import pandas


class CreateTable:
    def __init__(self, name_table) -> None:
        self.data_users = {}
        self.name_table = name_table
        self.connection = sqlite3.connect('base.sqlite')
        self.cursor = self.connection.cursor()

    def create_table(self):
        print(f'[INFO] Таблица {self.name_table} создана')
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name_table} (
                ID INTEGER PRIMARY KEY,
                ID_TOVAR INTEGER,
                TOVAR TEXT,
                ID_ISG INTEGER,
                ISG TEXT,
                COUNTRY TEXT,
                BARCOD TEXT
            );
        """)

    def insert_data(self, xlsx_file):
        data_frame = pandas.read_excel(xlsx_file)
        data_frame.to_sql(self.name_table, self.connection, if_exists="replace", index=False)
        print(f'[INFO] Данные из {xlsx_file} вставлены в таблицу {self.name_table}')
        self.connection.commit()
    
        
    def process_data(self):
        query = f"""
            SELECT COUNTRY, COUNT(*) AS COUNT
            FROM {self.name_table}
            GROUP BY COUNTRY;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        with open('data.tsv', 'w', encoding='utf-8') as file:
            for country, count in results:
                file.write(f"{country} - {count}\n")


if __name__ == '__main__':
    table = CreateTable('products')
    # table.create_table()          # create table
    # table.insert_data('data.xlsx')  # insert in db
    # table.process_data()          # create tsv 