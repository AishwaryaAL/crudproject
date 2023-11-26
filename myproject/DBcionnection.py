import cx_Oracle
dsn_tns = cx_Oracle.makedsn('192.168.0.98', 1521, service_name = 'orcl')
cx_Oracle.init_oracle_client("C:\\Users\\Aishwarya\\Documents\\Downloads\\instantclient-basic-windows.x64-21.12.0.0.0dbru\\instantclient_21_12")
conn = cx_Oracle.connect(user=r'learning_sql', password = 'Admin123', dsn = dsn_tns)
c = conn.cursor()
c.execute("create table Aishwarya (Name varchar(20), cell_num number(10))")
c.execute("insert into Aishwarya values ('sachin', 9900815803)")
c.execute("commit")
c.execute("select * from Aishwarya")
for row in c:
    print(row[0], '-', row[1])
c.close()
