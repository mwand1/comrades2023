#get comrades results 2023

#default link: https://results.finishtime.co.za/results.aspx?CId=35&RId=30203
#pages: https://results.finishtime.co.za/results.aspx?CId=35&RId=30203&EId=1&dt=0&PageNo=2

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import pyodbc

url = "https://results.finishtime.co.za/results.aspx?CId=35&RId=30203"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

#get the number of pages 
pages = 1
links = soup.find_all('a', href=True)
for link in links: 
    if ('PageNo=' in link['href'] and int(link.get_text()) > pages):
        pages = int(link.get_text()) 


conn = pyodbc.connect('Driver={SQL Server};'

                     'Server=MWAMWA;'
                     'Database=Comrades;'
                     'UID=db_dev;'
                     'PWD=db_dev;'
                     'Trusted_Connection=no')
cursor = conn.cursor() 


for i in range(pages):
    url = "https://results.finishtime.co.za/results.aspx?CId=35&RId=30203&EId=1&dt=0&PageNo=" + str(i+1)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    table_tag = soup.select('.table')[0]
    
    for row_data in table_tag.select("tr")[1:]:
        sql = """INSERT INTO [dbo].[Race_Results]
            ([Event_Year]
            ,[Race_Number]
            ,[Runner_Name]
            ,[Overall_Position]
            ,[Finish_Time]
            ,[Category]
            ,[Category_Position]
            ,[Gender]
            ,[Gender_Position]
            ,[Club]
            ,[Country]
            ,[Wave]
            ,[Lynnfield_Park_Time]
            ,[Cato_Ridge_Time]
            ,[Drummond_Time]
            ,[Winston_Park_Time]
            ,[Pinetown_Time]
            ,[Sherwood_Time])     
            VALUES
            (2023\n"""
        sql = sql + "," + row_data.select("th,td")[2].text + "\n"
        sql = sql + ",'" + row_data.select("th,td")[5].text.replace("'", "''") + "'\n"
        sql = sql + "," + (row_data.select("th,td")[1].text if row_data.select("th,td")[1].text else "NULL") + "\n"
        sql = sql + "," + ("NULL" if row_data.select("th,td")[7].text in ("DNS", "Not started") else ("'" + row_data.select("th,td")[7].text.replace("DNF", "0:00:00") + "'")) + "\n"
        sql = sql + ",'" + row_data.select("th,td")[10].text + "'\n"
        sql = sql + "," + (row_data.select("th,td")[11].text if row_data.select("th,td")[11].text else "NULL") + "\n"
        sql = sql + ",'" + row_data.select("th,td")[12].text + "'\n"
        sql = sql + "," + (row_data.select("th,td")[13].text if row_data.select("th,td")[13].text else "NULL") + "\n"
        sql = sql + ",'" + row_data.select("th,td")[14].text.replace("'", "''") + "'\n"
        sql = sql + ",'" + row_data.select("th,td")[15].text + "'\n"
        sql = sql + ",'" + row_data.select("th,td")[16].text + "'\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[17].text + "'") if row_data.select("th,td")[17].text else "NULL")  + "\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[18].text + "'") if row_data.select("th,td")[18].text else "NULL")  + "\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[19].text + "'") if row_data.select("th,td")[19].text else "NULL")  + "\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[20].text + "'") if row_data.select("th,td")[20].text else "NULL")  + "\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[21].text + "'") if row_data.select("th,td")[21].text else "NULL") + "\n"
        sql = sql + "," + (("'" + row_data.select("th,td")[22].text + "'") if row_data.select("th,td")[22].text else "NULL") + ")" 
            
        #print(sql)
        cursor.execute(sql) 

conn.commit()