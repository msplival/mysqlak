#!/usr/bin/python3

import mysql.connector
import uuid
import time


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

    with open(f'batch-{batch_uuid}.txt', 'a') as logFile:
        for i in range(1,size):
            sql = f"INSERT INTO t1 (batch_uuid, data_value) VALUES ('{batch_uuid}', 'data-{i}');"
            tic = time.perf_counter()
            curs.execute(sql)
            conn.commit()
            toc = time.perf_counter()
            logFile.write(f'Counter: {i}, duration: {toc - tic} seconds. \n')

    conn.close()
    print('   Completed.')

for i in range(1,2, 10):
    do_batch(i*100)