import sqlite3

connection = sqlite3.connect("resources\school.db")
#sqlite3.connect("..\\resources\school.db")


cursor = connection.cursor()
create_query = 'CREATE TABLE IF NOT EXISTS students (id int UNIQUE, first_name text, last_name text, Class text, Address text)'
insert_query = 'INSERT INTO students values (?, ?, ?, ?, ?)'
select_query = 'SELECT * FROM students'

cursor.execute(create_query)

student_list = [
    (101, 'FNAME1', 'LNAME2', 'CLASSA', '14 Sam Lane PIN- 801425'),
    (102, 'FNAME2', 'LNAME3', 'CLASSA', '15 Sam Lane PIN 801426'),
    (103, 'FNAME3', 'LNAME4', 'CLASSA', '16 Sam Lane PIN 801427'),
    (104, 'FNAME4', 'LNAME5', 'CLASSA', '17 Sam Lane PIN 801428'),
    (105, 'FNAME5', 'LNAME6', 'CLASSA', '18 Sam Lane PIN 801429'),
    (106, 'FNAME6', 'LNAME7', 'CLASSA', '19 Sam Lane PIN 801430'),
    (107, 'FNAME7', 'LNAME8', 'CLASSA', '20 Sam Lane PIN 801431'),
    (208, 'FNAME8', 'LNAME9', 'CLASSB', '21 Sam Lane PIN 801432'),
    (209, 'FNAME9', 'LNAME10', 'CLASSB', '22 Sam Lane PIN 801433'),
    (210, 'FNAME10', 'LNAME11', 'CLASSB', '23 Sam Lane PIN 801434'),
    (211, 'FNAME11', 'LNAME12', 'CLASSB', '24 Sam Lane PIN 801435'),
    (212, 'FNAME12', 'LNAME13', 'CLASSB', '25 Sam Lane PIN 801436'),
    (213, 'FNAME13', 'LNAME14', 'CLASSB', '26 Sam Lane PIN 801437'),
    (214, 'FNAME14', 'LNAME15', 'CLASSB', '27 Sam Lane PIN 801438'),
    (115, 'FNAME15', 'LNAME16', 'CLASSA', '28 Sam Lane PIN 801439'),
    (116, 'FNAME16', 'LNAME17', 'CLASSA', '29 Sam Lane PIN 801440'),
    (117, 'FNAME17', 'LNAME18', 'CLASSA', '30 Sam Lane PIN 801441'),
    ]

cursor.executemany(insert_query, student_list)


'''
update_query = 'UPDATE students SET Address=? WHERE id=?'
cursor.execute(update_query, ('56 Sam Lane PIN 001426', 110))
'''
results = cursor.execute(select_query)
for result in results:
    print(result)

connection.commit()
connection.close()
