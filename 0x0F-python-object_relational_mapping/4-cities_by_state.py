#!/usr/bin/python3
'''Module for listing states'''
import sys
import MySQLdb
if __name__ == '__main__':
    con = MySQLdb.connect(
        host='localhost', port=3306,
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3])
    cur = con.cursor()
    query = 'SELECT cities.id, cities.name, states.name FROM cities,\
 states WHERE states.id = cities.state_id'
    cur.execute(query)
    lists = cur.fetchall()
    for row in lists:
        print(row)
