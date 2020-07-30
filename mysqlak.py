#!/usr/bin/python3

import mysql.connector
import uuid


def do_batch(size=10):
    batch_uuid = uuid.uuid4()

    print('Starting batch {0}, size {1}'.format(batch_uuid, size))
    print('   Connecting to database...')
    conn = mysql.connector.connect(user='mario', 
                                host='xen-mysql-percona.lxd',
                                database='mysqlak')
    conn.autocommit = False

    curs = conn.cursor()

    curs.execute("INSERT INTO batches (batch_uuid) VALUES ('{0}');".format(batch_uuid))
    conn.commit()

    for i in range(1,size):
        sql = "INSERT INTO t1 (batch_uuid, data_value) VALUES ('{0}', 'data-{1}');".format(batch_uuid, i)
        curs.execute(sql)
        conn.commit()

    conn.close()
    print('   Completed.')

for i in range(1,100, 10):
    do_batch(i*100)