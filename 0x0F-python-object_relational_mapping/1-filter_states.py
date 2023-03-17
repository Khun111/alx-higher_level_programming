#!/usr/bin/python3
'''Module for listing states'''
import sys
import MySQLdb
con = MySQLdb.connect(
    host='localhost', port=3306,
    user=sys.argv[1], passwd=sys.argv[2],
    db=sys.argv[3])
cur = con.cursor()
query = 'SELECT * FROM states WHERE states.name LIKE "N%"'
cur.execute(query)
lists = cur.fetchall()
for row in lists:
    print(row)
