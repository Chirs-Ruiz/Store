import mysql.connector as c
con=c.connect(host="localhost",user="root",password="mint",database="school")
if con.is_connected():
    print("Successfully Connected...")
else:
    print("Connectivty issues...")

mycursor=con.cursor()
mycursor.execute("desc account")
for i in mycursor:
    print(i)

