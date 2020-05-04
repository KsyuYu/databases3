import csv
import cx_Oracle

username = 'DBLAB'
password = 'system'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

query = '''
SELECT
        country,
        total_cases,
        new_cases,
        total_deaths,
        new_deaths
FROM
    Total'''
cursor.execute(query)

with open("WorldometerDataset.csv", "w", newline="\n") as file:
    writer = csv.writer(file)

    writer.writerow('Country,Total Cases,New Cases,Total Deaths,New Deaths'.split(','))

    for (country, total_cases, new_cases, total_deaths, new_deaths) in cursor:

        writer.writerow([country, total_cases, new_cases, total_deaths, new_deaths])

cursor.close()
