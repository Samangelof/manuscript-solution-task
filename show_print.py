import pandas as pd


def view_rows(file):
    show_data = pd.read_excel(file, engine='openpyxl')
    return print(show_data)

view_rows('data.xlsx')