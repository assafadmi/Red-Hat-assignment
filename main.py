import sqlite3
from sqlite3 import Error
import os


def create_connection(db_path):
    """ create a database connection to the SQLite database
        specified by db_path
    param db_path: database path
    return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)

    return conn


def excute_query(conn, query):
    """ excute query
    param conn: Connection object
    param query: a CREATE/INSERT/UPDATE statement
    return:
    """
    try: 
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)



def main():
    path = os.path.join(os.path.dirname(__file__),"db.sqlite")

    create_query = """ CREATE TABLE IF NOT EXISTS Airlines (
                    Acode INT NOT NULL,
					Name VARCHAR(45) NOT NULL,
                    Established YEAR NOT NULL,
                    Hub VARCHAR(45) NOT NULL,
                    Destinations INT NOT NULL,
                    Alliance VARCHAR(45) NOT NULL,
                    Planes INT NOT NULL,
                    AvgPrice INT NOT NULL,
                    PRIMARY KEY(Acode)
                    );"""

    insert_query = """INSERT INTO Airlines
                    VALUES 
	                (1,'Lufthansa', 1955, 'Germany', 220, 'Star', 294, 1183),
                    (2,'Swiss', 2002, 'Switzerland', 102, 'Star',89, 1674),
                    (3,'Elal', 1948, 'Israel', 60, 'Matmid', 43, 984),
                    (4,'TurkishAirlines', 1933, 'Turkia', 304, 'Star', 338, 1298),
                    (5,'AirCanada', 1937, 'Canada', 222, 'Star', 189, 1167),
                    (6,'BritishAirways', 1974, 'UK', 183, 'OneWorld', 277, 1535),
                    (7,'UnitedAirlines', 1926, 'USA', 342, 'Star', 781, 1116),
                    (8,'CathayPacific', 1946, 'China', 77, 'OneWorld', 153, 1636);"""

    # create a database connection
    conn = create_connection(path)

    
    if conn is not None:
        # create Airlines table 
        excute_query(conn, create_query)
        # inject the data
        excute_query(conn, insert_query)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
