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
    query = 'SELECT DISTINCT(cities.name) FROM cities\
 JOIN states ON states.id = cities.state_id WHERE states.name = %s'
    cur.execute(query, (sys.argv[4], ))
    lists = cur.fetchall()
    print(', '.join([row[0] for row in lists]))
