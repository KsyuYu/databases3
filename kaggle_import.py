import csv
import cx_Oracle

username = 'DBLAB'
password = 'system'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

filename = "WorldometerDataset.csv"

with open(filename, newline='') as file:
    reader = csv.reader(file)
    for el in list(reader)[1:]:
        country = el[0]
        total_cases = el[1]
        new_cases = el[2]
        total_deaths = el[3]
        new_deaths = el[4]

        insert_query_country = '''INSERT INTO Countries (country)
                    VALUES (:country)'''
        cursor.execute(insert_query_country, country=country)


        insert_query_cases = '''INSERT INTO TotalCases (country, total_cases, new_cases )
                    VALUES (:country, :total_cases, :new_cases )'''
        cursor.execute(insert_query_cases, country=country, total_cases=total_cases, new_cases=new_cases)

        insert_query_deaths = '''INSERT INTO TotalDeaths
                (country, total_deaths, new_deaths)
                    VALUES (:country, :total_deaths, :new_deaths)'''
        cursor.execute(insert_query_deaths, country=country, total_deaths=total_deaths, new_deaths=new_deaths)

    connection.commit()
    cursor.close()
    connection.close()


# import csv
# filename = 'WorldometerDataset1.csv'
# new_file = 'WorldometerDataset.csv'
# with open(filename, newline='') as file:
#     with open(new_file, 'w', newline='') as n_file:
#         reader=csv.reader(file)
#         for el in reader:
#             st = ''
#             for element in el:
#                 element = element.replace(',', '')
#                 st = st+element+','
#             st=st+'\n'
#             n_file.write(st)
