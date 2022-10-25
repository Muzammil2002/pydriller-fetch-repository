# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# import datetime
# import mysql.connector
#
# studentname = input("Enter Your Name : ")
# english = int(input("Enter English Subject Nmuber : "))
# math = int(input("Enter Math Subject Nmuber : "))
# urdu = int(input("Enter Urdu Subject Nmuber : "))
# totalnumber = english + math + urdu
# print(f"{studentname} Your Total Number {totalnumber}")
# pre = (totalnumber * 100) / 300
# print(f"{studentname} Your Precantage is {pre}")
# curr = datetime.datetime.now()
# # data save in file
#
# f = open("studentdata.txt",mode = "a")
# f.write(f"{studentname}\n Your English Nmuber {english}\n Your Math Nmuber {math}\n Your Urdu Nmuber {urdu}\n {studentname} Your Total Number Is {totalnumber} \n {studentname} Your Precantage {pre}\t {curr}  ")
#
# dbcon = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="student",
# )
#
# cursos = dbcon.cursor()
# insert_query = "INSERT INTO `studentdata`( `Name`, `English`, `Math`, `Urdu`, `Total_Number`, `Percentage`, `curr`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# my_value = [studentname,english,math,urdu,totalnumber,pre,curr]
#
# cursos.execute(insert_query,my_value)
# dbcon.commit()
# dbcon.close()

# #22 oct 2022
# import pandas
# from openpyxl.workbook import Workbook
# import lxml
#
# khaadi = {
#     "suitname": ["Fabrics 3 Piece Suit","Fabrics 2 Piece","Fabrics 3 Piece Suit","Flared Kameez","Classic Kameez","Classic Kurta","Flared Kameez","Drop Shoulder"],
#     "des" : ["Essentials Dyed Embroidered Top Bottoms Dupatta","Essentials Dyed Embroidered Top Bottoms","Essentials Dyed Embroidered Top Bottoms Shawl","Signature Dyed Embroidered Kurta","Signature Printed Embroidered Kurta","Signature Dyed Embroidered Kurta","Signature Printed Embroidered Kurta","Essentials Dyed"],
#     "price" : ["Rs. 4,490","Rs. 2,990","Rs. 4,690","Rs. 5,593","Rs. 6,392","Rs. 3,843","Rs. 5,912","Rs. 6,392"]
# }
#
# convertable = pandas.DataFrame(khaadi)
# print(convertable)
#
#
# # save data in excel
# convertable.to_excel("muzammil.xlsx")
# # save data in csv
# convertable.to_csv("muzammil.csv")
# # save data in xml
# convertable.to_xml("muzammil.xml")
# # save data in json
# convertable.to_json("muzammil.js")

#25-10-2022
# reposition label github sa data fetch karna ka liye use hote ha
# pandas label data ko table from main leta ha

from pydriller import Repository
import pandas
import lxml

Nm , date , masg = [] , [] , []

for ms in Repository(path_to_repo="https://github.com/microsoft/calculator.git").traverse_commits():
    Nm.append(ms.committer.name)
    date.append(ms.committer_date)
    masg.append(ms.msg)

# dictionaryo
github = {
    "n" : Nm,
    "n" : date,
    "n" : masg,
}
#save data into cvs xlsx

convert_to_table = pandas.DataFrame(github)
convert_to_table.to_csv("Repository.csv",index=False)
convert_to_table.to_xml("Repository.xml")

print("Data Save")

