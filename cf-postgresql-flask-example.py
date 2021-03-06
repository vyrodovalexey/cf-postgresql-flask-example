from flask import Flask
import time
import datetime
import sys
import os
import psycopg2
import json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    s=[]
    ltime = str(datetime.datetime.now())
    s=pgsql_insel(ltime)
    line=str(s)
    for char in line:
	if char in "\",()'":
	    line=line.replace(char,"")
    return '<HTML><BODY>Hello World!' + line + ' h</BODY><HTML>'

def pgsql_insel(ltime):
    if 'VCAP_SERVICES' in os.environ:
	services = json.loads(os.getenv('VCAP_SERVICES'))
	""" Change this in according of env service name """
	pgsql_env = services['postgres-2.0'][0]['credentials']
	""" end """
    else:
	""" For static """
	uname = "your_userbame"
	password = "your_password"
	database = "your_database"
	hostname = "hosname"
	""" end """
    hostname = pgsql_env['hostname']
    password = pgsql_env['password']
    database = pgsql_env['database']
    uname = pgsql_env['username']
    sres = []
    db1 = psycopg2.connect(host=hostname, dbname=database, user=uname, password=password)
    db1.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = db1.cursor()
    cur.execute("create table IF NOT EXISTS ips (date varchar);")
    cur.execute("insert into ips VALUES (%s)", (ltime,))
    cur.execute("select * from ips;")
    row_c=0
    for row in cur:
        row_c += 1
        sres.append('<P>user ' + str(row_c) + ': access time ' + str(row))

    cur.close()
    db1.close()
    return sres                        
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
