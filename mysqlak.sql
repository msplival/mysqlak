DROP DATABASE IF EXISTS mysqlak;
CREATE DATABASE mysqlak;
USE mysqlak;

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
