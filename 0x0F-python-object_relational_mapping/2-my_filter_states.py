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
    query = "SELECT * FROM states WHERE BINARY name\
 = '{}' ORDER BY id".format(sys.argv[4])
    cur.execute(query)
    lists = cur.fetchall()
    for row in lists:
        print(row)
