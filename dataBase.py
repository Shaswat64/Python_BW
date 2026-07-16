import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = 3306,
    database = "broadways"
)


#insert
terminal = db.cursor()
# query = "INSERT INTO fifa (name, address, phone) VALUES ('Shitole', 'South_Africa', 78963);"
# terminal.execute(query)
# db.commit()



#update
# query = "UPDATE `fifa` SET `address` = 'South Africa' WHERE `fifa`.`id` = 9;"
# terminal.execute(query)
# db.commit()
# print(db)



#fetch data
query = "Select * from fifa"
terminal.execute(query)
result = terminal.fetchall()

# print(result)
for i in result:
    print(list(i))