import mysql.connector
import requests
import json

mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='anything', database='data_work')
mycursor = mydb.cursor()
mycursor.execute('select id, request_data from database_table')
mydata = mycursor.fetchall()

url = 'https://0.0.0.0:8000/my/web'
header = {'content-type':'application/json'}

for i in mydata:
    try:
        data = i[1]
        r = requests.post(url,data,header)
        response = json.loads(r.text)
        print(response)
    except Exception as e:
        print(e)