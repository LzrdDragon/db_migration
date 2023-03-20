from __future__ import annotations
from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker, Session

# DEFINE THE DATABASE CREDENTIALS
user = ''
password = ''
host = '127.0.0.1'
port = 3306
database_1 = 'crypto_wp'
database_2 = 'crypto_new'

engines = dict(
    wp=create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database_1
        ), pool_pre_ping=True,
        poolclass=NullPool
    ),
    new=create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database_2), pool_pre_ping=True,
        poolclass=NullPool
    )
)


if __name__ == '__main__':
    print('sqlalchemy_connection has ran')
