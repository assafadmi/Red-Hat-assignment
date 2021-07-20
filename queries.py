import os
from main import excute_query as excute_query_
from main import create_connection


def excute_query(conn, query):
    """ excute query
    param conn: Connection object
    param query: a SELECT statement 
    return:
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)   

def main():
    path = os.path.join(os.path.dirname(__file__),"db.sqlite")

    # required queries
    query1 = """SELECT Alliance FROM Airlines 
                GROUP BY Alliance
                ORDER BY COUNT(Acode) 
                LIMIT 1;"""
    
    query2 = """SELECT Name FROM Airlines
                WHERE Planes < (SELECT AVG(Planes) 
                                FROM Airlines) AND 
                    Destinations > (SELECT AVG(Destinations) 
                                FROM Airlines);"""

    query3_1 = """CREATE TABLE IF NOT EXISTS years 
                (Year YEAR NOT NULL,
                 PRIMARY KEY(Year))"""

    query3_2 = """SELECT * FROM years;"""
    
    query4 = """SELECT DISTINCT Established FROM Airlines;"""

    query5 = """SELECT Year FROM years 
                WHERE Year NOT IN (SELECT Established FROM Airlines);"""
    
    # create a database connection
    conn = create_connection(path)
    
    if conn is not None:
        # excute required queries
        print("3.1. The name of the alliance with the fewest airlines is:")
        excute_query(conn, query1)
        
        print("""3.2. The airlines with less than the average number of planes,
        but above average destinations are:""")
        excute_query(conn, query2)
        
        excute_query_(conn, query3_1)
        
        for year in range(1950,1960):
            excute_query_(conn, f"INSERT INTO years VALUES ({year});")

        print("3.3. Here is the new table - 'years':")
        excute_query(conn, query3_2)           
        
        print("3.4. The years the airlines were established:")
        excute_query(conn, query4)
        
        print("3.5. The years that appear in section 3.3 but don't appear in section 3.4 are:")
        excute_query(conn, query5)
    
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
