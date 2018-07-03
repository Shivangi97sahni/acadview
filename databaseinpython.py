import sqlite3

conn = sqlite3.connect('test2.db')
print("Opened database successfully")

#conn.execute('''CREATE TABLE BOOKKSS
             #(BOOKID INT PRIMARY KEY  NOT NULL,
             # TITLEID       INT       NOT NULL,
             # LOCATION       CHAR(50),
              #GENRE          TEXT      NOT NULL)''')

#print("Table1 created successfully")

#conn.execute('''CREATE TABLE TITLEES
            #(TITLEID INT PRIMARY KEY    NOT NULL,
             #TITLES                TEXT   NOT NULL,
             #ISBN                  INT    NOT NULL,
             #PUBLISHERID            INT    NOT NULL,
             #PUBLISHERYEAR        INT    NOT NULL)''')

#print("Table2 created successfully")

#conn.execute('''CREATE TABLE PUBLISHERRS
            #(PUBLISHERID INT PRIMARY KEY    NOT NULL,
            # NAME                     TEXT   NOT NULL,
            # STREETADDRESS           INT    NOT NULL,
            # SUITENUMBER             INT    NOT NULL,
            # ZIPCODEID              INT    NOT NULL)''')

#print("Table3 created successfully")

#conn.execute('''CREATE TABLE ZIPCODE
             #(ZIPCODEID INT PRIMARY KEY    NOT NULL,
              #CITY                CHAR(20),
             # STATE               CHAR(20),
             # ZIPCODE             INT        NOT NULL)''')

#print("Table4 created successfully")

#conn.execute('''CREATE TABLE AUTHORSTITLES
            #(AUTHORTITLEID INT PRIMARY KEY    NOT NULL,
             #AUTHORID       INT   NOT NULL,
             #TITLEID        INT    NOT NULL)''')

#print("Table5 created successfully")

#conn.execute('''CREATE TABLE AUTHORS
           # (AUTHORID INT PRIMARY KEY    NOT NULL,
            # FIRSTNAME           TEXT   NOT NULL,
            # MIDDLENAME          TEXT    NOT NULL,
            # LASTNAME            INT     NOT NULL)''')

#print("Table6 created successfully")

#conn.execute("INSERT INTO BOOKKSS(BOOKID,TITLEID,LOCATION,GENRE) VALUES(1, 24, 'Agra', 'Inspiration')")
#conn.execute("INSERT INTO BOOKKSS(BOOKID,TITLEID,LOCATION,GENRE) VALUES(2, 25, 'Chandigarh', 'Love')")
#conn.commit()
#print("Record1 created successfully")


#cursor = conn.execute("SELECT BOOKID, TITLEID, LOCATiON, GENRE from BOOKKSS")
#for row in cursor:
    #print("BOOKID = ",row[0])
   # print("TITLEID = ",row[1])
   # print("LOCATION = ",row[2])
   # print("GENRE = ",row[3], "\n")

#print("Operation1 done successfully")

#conn.execute("INSERT INTO TITLEES(TITLEID, TITLES, ISBN, PUBLISHERID, PUBLISHERYEAR) VALUES(1, 'The Alchemist', 35456, 456, 2005)")
#conn.execute("INSERT INTO TITLEES(TITLEID, TITLES, ISBN, PUBLISHERID, PUBLISHERYEAR ) VALUES(2, 'Two States', 35457, 457, 2005)")
#conn.commit()
#print("Record2 created successfully")

conn.execute("UPDATE TITLEES set PUBLISHERYEAR = 2009 where TITLEID = 2")
conn.commit()
print("Total number of rows updated : ", conn.total_changes)
print("The original value is 2005")
print("The updated value is 2009")

cursor = conn.execute("SELECT TITLEID, TITLES, ISBN, PUBLISHERID, PUBLISHERYEAR from TITLEES")
for row in cursor:
    print("TITLEID = ",row[0])
    print("TITLES = ",row[1])
    print("ISBN = ",row[2])
    print("PUBLISHERID = ", row[3])
    print("PUBLISHERYEAR = ",row[4], "\n")

#print("Operation2 done successfully")

#conn.execute("INSERT INTO PUBLISHERRS(PUBLISHERID, NAME, STREETADDRESS, SUITENUMBER, ZIPCODEID) VALUES(456, 'HarperCollins', 'Agra', 201301, 275)")
#conn.execute("INSERT INTO PUBLISHERRS(PUBLISHERID, NAME, STREETADDRESS, SUITENUMBER, ZIPCODEID) VALUES(457, 'Rupa', 'Chandigarh', 209302, 328)")
#conn.commit()
#print("Record3 created successfully")

#cursor = conn.execute("SELECT PUBLISHERID, NAME, STREETADDRESS, SUITENUMBER, ZIPCODEID from PUBLISHERRS")
#for row in cursor:
    #print("PUBLISHERID = ",row[0])
    #print("NAME = ",row[1])
    #print("STREETADDRESS = ", row[2])
    #print("SUITENUMBER = ", row[3])
    #print("ZIPCODEID = ",row[4], "\n")

#print("Operation3 done successfully")

#conn.execute("INSERT INTO ZIPCODE(ZIPCODEID, CITY, STATE, ZIPCODE) VALUES(275, 'Agra', 'Uttar Pradesh', 5678)")
#conn.execute("INSERT INTO ZIPCODE(ZIPCODEID, CITY, STATE, ZIPCODE) VALUES(328, 'Chandigarh', 'Punjab', 6789)")
#conn.commit()
#print("Record4 created successfully")



#cursor = conn.execute("SELECT ZIPCODEID, CITY, STATE, ZIPCODE from ZIPCODE")
#for row in cursor:
   #print("ZIPCODEID = ",row[0])
   #print("CITY = ",row[1])
   #print("STATE = ", row[2])
  # print("ZIPCODE = ",row[3], "\n")

#print("Operation4 done successfully")

#conn.execute("INSERT INTO AUTHORSTITLES(AUTHORTITLEID, AUTHORID, TITLEID) VALUES(344, 678,5678)")
#conn.execute("INSERT INTO AUTHORSTITLES(AUTHORTITLEID, AUTHORID, TITLEID) VALUES(434, 786, 7865)")
#conn.commit()
#print("Record4 created successfully")


#cursor = conn.execute("SELECT AUTHORTITLEID, AUTHORID, TITLEID from AUTHORSTITLES")
#for row in cursor:
 #   print("AUTHORTITLEID = ",row[0])
  #  print("AUTHORID = ",row[1])
   # print("TITLEID = ",row[2], "\n")

#print("Operation5 done successfully")

#conn.execute("INSERT INTO AUTHORS(AUTHORID, FIRSTNAME, MIDDLENAME, LASTNAME) VALUES(678,'Paulo', ' ', 'Coelho')")
#conn.execute("INSERT INTO AUTHORS(AUTHORID, FIRSTNAME, MIDDLENAME, LASTNAME) VALUES(786, 'Chetan', ' ', 'Bhaghat')")
#conn.commit()
#print("Record5 created successfully")

#cursor = conn.execute("SELECT AUTHORID, FIRSTNAME, MIDDLENAME, LASTNAME from AUTHORS")
#for row in cursor:
 #print("AUTHORID = ",row[0])
 #print("FIRSTNAME = ",row[1])
 #print("MIDDLENAME = ",row[2])
 #print("LASTNAME = ",row[3], "\n")


#print("Operation6 done successfully")

conn.close()
