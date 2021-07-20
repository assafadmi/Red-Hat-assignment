import os
from main import excute_query as excute_query_
from main import create_connection
from queries import excute_query as excute_query
  

def main():
    path = os.path.join(os.path.dirname(__file__),"db.sqlite")


    query1 = """CREATE TABLE IF NOT EXISTS Changes (
                    Changecode INT NOT NULL,
					OldName VARCHAR(45) NOT NULL,
                    NewName VARCHAR(45) NOT NULL,
                    Year YEAR NOT NULL,
                    PRIMARY KEY(Changecode),
                    FOREIGN KEY (NewName) REFERENCES Airlines (Name)
                    );"""
    
    query2 = """UPDATE Airlines
                SET Name = 'Lufthansa Airways'
                WHERE Name ='Lufthansa'"""
    
    query3 = """INSERT INTO Changes
                    VALUES  (1,'Lufthansa', 'Lufthansa Airways', 2009);"""
    
    
    query4 = "SELECT * FROM Airlines;"

    query5 = "SELECT * FROM Changes;"

    # create a database connection
    conn = create_connection(path)
    
    if conn is not None:
        # create Changes table
        excute_query_(conn, query1)

        # update Airlines table
        excute_query_(conn, query2)

        # insert the change to Changes table
        excute_query_(conn, query3)

        # display updated Airlines table
        print("4. Here is the updated Airlines table:")
        excute_query(conn, query4)
        
        # display new table 
        print("Here is the new table - 'Changes':")
        excute_query(conn, query5)

    else:
        print("Error! cannot create the database connection.")    
    
    

if __name__ == '__main__':
    main()