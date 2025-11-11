
# SQL Learning Project - From Excel to SQLite

# This procejt shows the basis SQL operations with Python.


import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Configuration for better diagrams
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class SQLLearnproject:
    """
    Main class for the SQL Project.
    This class create the connection to the database and all SQL operations.
    
    """
    
    def __init__(self, db_name='learningproject.db'):
        """
        Initializes the database connection.
        
        Parameter:
        db_name (str): SQL-database
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print(f"Database connection established: {db_name}")
    
    def excel_zu_sql(self, excel_file, table_name='Fragebogen_A'):
        """
        1. Import Data
          Loads Excel data and creates a SQL table.
        
        Parameter:
        excel_file (str): Path to the Excel file
        tabellen_name (str): Name of the SQL table to be created
        """
        print(f"Load Excel-file: {excel_file}")
        
        # Read Excel-file with pandas
        
        try:
            if not os.path.exists(excel_file):
                raise FileNotFoundError(f"Excel-Datei nicht gefunden: {excel_file}")
            df = pd.read_excel(excel_file)
        
        except Exception as e:
        
            raise
        
        # Save data in SQL-Table
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)
        
        print(f"   Table '{table_name}' created")
        print(f"   Number rows: {len(df)}")
        print(f"   Columns: {', '.join(df.columns)}")
        
        return df
    
    # def create_example_data(self):
    #     """
    #     IF there would be no data, this would create data for an example to learn

    #     """
    #     print("Create example data...")
        
    #     # Example for employees.
    #     employee_data = {
    #         'id': range(1, 21),
    #         'name': [
    #             'Anna Schmidt', 'Ben Müller', 'Clara Wagner', 'David Koch',
    #             'Emma Weber', 'Felix Becker', 'Greta Hoffmann', 'Hans Schulz',
    #             'Ida Fischer', 'Jonas Richter', 'Klara Braun', 'Leon Wolf',
    #             'Maria Klein', 'Noah Schröder', 'Olivia Neumann', 'Paul Schwarz',
    #             'Quinn Zimmermann', 'Rosa Krüger', 'Simon Hartmann', 'Tina Lange'
    #         ],
    #         'department': [
    #             'IT', 'HR', 'IT', 'Vertrieb', 'IT', 'Vertrieb', 'HR', 'IT',
    #             'Vertrieb', 'IT', 'HR', 'Vertrieb', 'IT', 'Vertrieb', 'HR',
    #             'IT', 'Vertrieb', 'IT', 'HR', 'Vertrieb'
    #         ],
    #         'salary': [
    #             55000, 48000, 62000, 51000, 58000, 49000, 47000, 65000,
    #             52000, 59000, 46000, 50000, 61000, 53000, 45000, 67000,
    #             54000, 63000, 44000, 56000
    #         ],
    #         'date of hire': [
    #             '2020-03-15', '2019-07-22', '2021-01-10', '2018-11-05',
    #             '2020-09-30', '2019-04-18', '2021-06-12', '2017-08-25',
    #             '2019-12-03', '2020-05-20', '2021-03-08', '2018-09-15',
    #             '2020-11-22', '2019-02-14', '2021-07-30', '2017-05-11',
    #             '2019-10-28', '2020-02-17', '2021-04-05', '2018-12-20'
    #         ],
    #         'active': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
    #     }
        
    #     df = pd.DataFrame(employee_data)
    #     df.to_sql('employee', self.conn, if_exists='replace', index=False)
        
    #     print(" Example data created: 20 Employees in the table 'employee_data'")
    #     return df
    #
    
# Basic SQL Operations
    
    
    def select_all_data(self, table='Fragebogen_A'):
        """
        SELECT - All data is read
        Basic SQL Operation.
        """
        print(f"\nSELECT: All data from '{table}'")
        
        query = f"SELECT * FROM {table}"
        df = pd.read_sql_query(query, self.conn)
        
        print(f"\n{df.to_string()}\n")
        return df
    
    def select_special_columns(self, columns, table='Fragebogen_A'):
        """
        SELECT special columns
        
        """
        print(f"\n SELECT: Only Colums {columns}")
        
        columns_str = ', '.join(columns)
        query = f"SELECT {columns_str} FROM {table}"
        df = pd.read_sql_query(query, self.conn)
        
        print(f"\n{df.to_string()}\n")
        return df
    
    def select_where(self, condition, table='Fragebogen_A'):
        """
        SELECT Where - filter data.
        To select only specific rows from a table.
        """
        print(f"\nSELECT with WHERE: {condition}")
    
        query = "SELECT * FROM ? WHERE ?"
        df = pd.read_sql_query(query, self.conn)
    
        print(f"Rows found: {len(df)}")
        print(f"\n{df.to_string()}\n")
        return df

    
    def select_with_order_by(self, column, direction='ASC', table='Fragebogen_A'):
        """
        ORDER BY - Sort data.
        ASC = ascending (small to large), DESC = descending (large to small).
        """
        print(f"\nSELECT with ORDER BY: {column} {direction}")
    
        query = f"SELECT * FROM {table} ORDER BY {column} {direction}"
        df = pd.read_sql_query(query, self.conn)
    
        print(f"\n{df.head(10).to_string()}\n")
        return df


    def select_with_limit(self, amount, table='Fragebogen_A'):
        """
        LIMIT - Retrieve only a specific number of rows.
        """
        print(f"\nSELECT with LIMIT: First {amount} rows")
    
        query = f"SELECT * FROM {table} LIMIT {amount}"
        df = pd.read_sql_query(query, self.conn)
    
        print(f"\n{df.to_string()}\n")
        return df
