from Conn import *

mycursor = mydb.cursor()

Name = input('Enter Your Name: ')


# mycursor.execute("INSERT INTO `clients` (`ID`, `Name`, `Email`, `Age (years)`) VALUES (NULL, '{}', '{}', '{}')".format(Name, Email, Age))

mycursor.execute("INSERT INTO `clients` (`ID`, `Name`, `Email`, `Age (years)`) VALUES (NULL, '"+Name+"', '"+Email+"', '"+str(Age)+"')")

mydb.commit()


# sql = "INSERT INTO `usr` (`ID`, `Name`, `Surname`, `Email`) VALUES (NULL, %s, %s, %s)"
# val = ('A', 'B', 'c@d.com')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")