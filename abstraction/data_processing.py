import pandas


class DataProcessor:
    def __init__(self, database, table_name):
        self.database = database
        self.table_name = table_name

    def insert_data(self, xlsx_file):
        data_frame = pandas.read_excel(xlsx_file)
        data_frame.to_sql(self.table_name, self.database.connection, if_exists="replace", index=False)

    def process_data(self):
        query = f"""
            SELECT COUNTRY, COUNT(*) AS COUNT
            FROM {self.table_name}
            GROUP BY COUNTRY;
        """
        self.database.execute_query(query)
        results = self.database.fetch_all()

        with open('data.tsv', 'w', encoding='utf-8') as file:
            for country, count in results:
                file.write(f"{country} - {count}\n")