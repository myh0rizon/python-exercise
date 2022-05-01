import sqlite3


def check_record_exists(db=None, table=None, id=None):

    conn = sqlite3.connect(f'db/{db}.sqlite')

    if conn.execute(f'SELECT * from {table} WHERE id="{id}"').fetchone() is None:
        conn.close()
        return False

    conn.close()
    return True
