# Red-Hat-assignment

In order to run this program you'll have to use Python and verify that you own sqlite3 package (you should have it if you use Python 3).

The program was tested on Windows 10.

I have created 3 python files (which contain SQL queries as well):
1.	main.py
2.	queries.py
3.	change_name.py

The first two files are located in the main branch, as they're the answers for sections 2 and 3. 

The third file is located in the 'section 4' branch, which I created a pull request with. This is the answer for section 4.

Follow the next steps in order to run this program:

  1.	In the command line, navigate to this Red-Hat-assignment folder.
  
  2.	run: py main.py
            
  This command will create a local database, a table ('Airlines') and will inject the required data (section 2).
  
  3.	run: py queries.py
            
  This command will display the output for the required queries of section 3.

After merging 'section 4' branch with the main branch, you'll be able to run the full program.
The addition for the program will take place by following the next step:

   4.	run: py change_name.py
            
   This command will commit the requried change by creating a new table - 'Changes' and by updating 'Airlines'.
   
   'Changes' table contains the columns Changecode, OldName, NewName (foreign key references Airlines(name)) and the date of changing.
   
   In addition, this command will display the changes that were done.

Assumptions:
1.	Changing an airline name in the database isn't always Synchronous with the day the airline actually changed its name, so there is no reason to use the current date       when inserting the relevant details to the 'Changes' table. 
2.	We only care about the last change that an airline made. So, 'Changes' table has only one row per airline at most.
