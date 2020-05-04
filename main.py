import cx_Oracle
import chart_studio
import re
chart_studio.tools.set_credentials_file(username='kseniia.yurieva', api_key='AOaMNFhahzGFJDyAVESS')
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

def GetId(url):
    name = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return name.replace('/', ':')

username = 'DBLAB'
password = 'system'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

print("Вивести країни та загальну кількість зареєстрованих у них випадків Covid-19.\n")
сountries1 = []
values1 = []
query1 = '''
SELECT
    Total.country,
    Total.total_cases
 FROM
    Total
ORDER BY
    total_cases DESC
'''
cursor.execute(query1)

for row in cursor.fetchall():
    сountries1.append (row[0])
    values1.append(row[1])
bar = go.Bar (x = сountries1, y = values1)
bar = py.plot([bar],auto_open = True, file_name = "Plot1")

#QUERY 2
print("\nВивести країну та % зареєстрованих у ній випадків відносно усіх зареєстрованих у світі.\n")
сountries2 = []
values2 = []
query2 = '''
SELECT
    Total.country,
	round((Total.total_cases + 0.0) * 100 / t.total, 2) as persent
FROM
    Total,
    (SELECT
        SUM(Total.total_cases) AS total
     FROM
        Total
    ) t
'''

cursor.execute(query2)

for row in cursor.fetchall():
    сountries2.append (row[0])
    values2.append(row[1])
pie = go.Pie (labels = сountries2, values = values2)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)

#QUERY 3
print("\nДинаміка залежності кількості летальних випадків від загальної кількості зареєстрованих.\n")
cases = []
deaths = []
query3 = '''
 SELECT
    Total.total_cases,
    Total.total_deaths
 FROM
    Total
ORDER BY
    total_cases DESC
'''

cursor.execute(query3)
for row in cursor.fetchall():
    cases.append (row[0])
    deaths.append(row[1])
scatter = go.Scatter (x = cases, y = deaths)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")

my_dboard = dash.Dashboard()
bar_id = GetId(bar)
pie_id = GetId(pie)
scatter_id = GetId(scatter)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Запит 1: Країни та загальна кількість зареєстрованих у них випадків Covid-19.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'Запит 2: Країни та % зареєстрованих у них випадків відносно усіх зареєстрованих у світі.'

}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'Запит 3: Динаміка залежності кількості летальних випадків від загальної кількості зареєстрованих.'
}


my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'DBlab2')


cursor.close()
connection.close()
