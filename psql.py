import json
import psycopg2

f = open('config.json', 'r')
jsonf = f.read()

config = json.loads(jsonf)

HOST = config['host']
PORT = config['port']
USER = config['user']
PASSWORD = config['password']
DBNAME = config['dbname']

def main():
    print('PSQL v1.4')

# ------ Connect to database ------

def connect():
    try:
        conn = psycopg2.connect(f'host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DBNAME}')

        return conn
    except:
        return 'Failed to connect to database'

# ------ Fetch all data ------

def get(t):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(f'SELECT * FROM {t}')
        res = cur.fetchall()

        cur.close()
        conn.close()

        return res
    except:
        return 'Error querying database'

# ------ Find all data of a condition ------

def where(t, cond):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(f'SELECT * FROM {t} WHERE {cond}')
        res = cur.fetchall()

        cur.close()
        conn.close()

        return res
    except:
        return 'Error querying database'

# ------ Search for a data by its condition ------

def find(t, cond):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(f'SELECT * FROM {t} WHERE {cond}')
        res = cur.fetchone()

        cur.close()
        conn.close()

        return res
    except:
        return 'Error querying database'

# ------ Insert into database ------

def insert(t, fields, data):
    conn = connect()
    cur = conn.cursor()

    columns = str()
    values = str()

    for h in fields:
        columns += h + ','

    for i in data:
        values += '%s,'

    columns = columns[:-1]
    values = values[:-1]

    try:
        QUERY = f'INSERT INTO {t}({columns}) VALUES ({values})'
        
        cur.execute(QUERY, data)

        conn.commit()

        cur.close()
        conn.close()

        return 'Inserted correctly'
    except:
        return 'Error querying database'

# ------ Update in database ------

def update(t, fields, data, cond):
    conn = connect()
    cur = conn.cursor()

    values = str()

    for i in fields:
        values += i + '=%s,'
    
    values = values[:-1]

    try:
        QUERY = f'UPDATE {t} SET {values} WHERE {cond}'
        
        cur.execute(QUERY, data)

        conn.commit()

        cur.close()
        conn.close()

        return 'Updated successfully'
    except:
        return 'Error querying database'

# ------ Delete in database ------

def delete(t, cond):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(f'DELETE FROM {t} WHERE {cond}')

        conn.commit()

        cur.close()
        conn.close()

        return 'Removed successfully'
    except:
        return 'Error querying database'

if __name__ == '__main__':
    main()
