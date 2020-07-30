#!/usr/bin/python3

import mysql.connector
import uuid


def do_batch(size=10):
    batch_uuid = uuid.uuid4()

    print(f'Starting batch {batch_uuid}, size {size}')
    print('   Connecting to database...')
    conn = mysql.connector.connect(user='mario', 
                                host='xen-mysql-percona.lxd',
                                database='mysqlak')
    conn.autocommit = False

    curs = conn.cursor()

    curs.execute("INSERT INTO batches (batch_uuid) VALUES ('{0}');".format(batch_uuid))
    conn.commit()

    for i in range(1,size):
        sql = f"INSERT INTO t1 (batch_uuid, data_value) VALUES ('{batch_uuid}', 'data-{i}');"
        curs.execute(sql)
        conn.commit()

    conn.close()
    print('   Completed.')

for i in range(1,100, 10):
    do_batch(i*100)