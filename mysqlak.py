#!/usr/bin/python3

import mysql.connector
import uuid

TABLE_DEFINITION = """
    CREATE TABLE batches (
        batch_uuid text primary key,
        time_created timestamp
    );

    CREATE TABLE t1 (
        id integer primary key auto_increment,
        batch_uuid text NOT NULL REFERENCES batches (batch_uuid),
        data_value text NOT NULL,
        time_created timestamp
    );
"""



def prepare_database()
