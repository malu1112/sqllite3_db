from sqlite3 import connect

with connect('test.db') as con:
    cur = con.cursor()
    cur.execute('create table if not exists my_table (id int, name text, age int)')
    print("Table Created")
    insert_list = [(1, "Tom", 20),(2, "David", 22),(3, "Linda", 35),(4, "Rabit", 40),(5, "Cat", 34)]
    cur.executemany('insert into my_table values(?,?,?)',insert_list)
    #cur.execute('insert into my_table values(1, "Tom", 20)')
    print("Record Inserted")
    cur.execute('select * from my_table')
    print("Records Fetched")
    all_records = cur.fetchall()
    print("Number of records: {0} All Records: {1}".format(len(all_records), all_records))
    cur.execute('drop table my_table')
    print("Table dropped")

