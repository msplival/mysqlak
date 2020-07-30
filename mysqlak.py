#!/usr/bin/python3

import mysql.connector
import uuid
import argparse

TABLE_DEFINITION = """
    CREATE TABLE batches (
        batch_uuid char(36) primary key,
        time_created timestamp
    );

    CREATE TABLE t1 (
        id integer primary key auto_increment,
        batch_uuid char(36) NOT NULL REFERENCES batches (batch_uuid),
        data_value text NOT NULL,
        time_created timestamp
    );
"""



def prepare_database():
    print('Preparing the database...')
    conn = mysql.connector.connect(user='mario', 
                                   host='xen-mysql-percona.lxd')
    curs = conn.cursor()
    try:
        curs.execute('DROP DATABASE IF EXISTS mysqlak;')
        curs.execute('CREATE DATABASE mysqlak;')
        curs.execute('USE mysqlak;')
        curs.execute(TABLE_DEFINITION) 
    except Exception as e:
        print('e:'+ str(e))

    conn.close()

def run_me():
    pass

parser = argparse.ArgumentParser()
parser.add_argument('--init', action='store_true', dest='init', default=False)
parsed = parser.parse_args()

#if parsed.init == True or 1==1:
if 1 == 1:
    prepare_database()