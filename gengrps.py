import random
import pyodbc



conn_str= """    
    DRIVER={ODBC Driver 13 for SQL Server};
    SERVER=localhost;
    DATABASE=test;
    Trusted_Connection=yes;
    """


def gengroups():
    dbconn=pyodbc.connect(conn_str)
    cursor=dbconn.cursor()
    cursor.execute("select * from employee")
    empn=[]
    for row in cursor:
        emp_no=row[0]
        empn.append(emp_no)
    groupno=0
    while len(empn)>0:
        groupno+=1
        grplist=[]
        groupsize=random.randint(3,5)
        if len(empn)<groupsize or len(empn) < 10:
            if len(empn)==9:
                groupcnt=(len(empn))-4
            elif len(empn)>5:
                groupcnt=(len(empn))-3
            else:
                groupcnt=len(empn)
        else:
            groupcnt=groupsize
        while groupcnt>0:
            if len(empn)>0:
                x=random.choice(empn)
                grplist.append(x)
                empn.remove(x)
                groupcnt-=1
        grpsql='select emp_id, emp_name from employee where emp_id in (' + ','.join(map(str, grplist)) + ');'
        print "\n----- Group %s ---------" %(groupno)
        cursor.execute(grpsql)
        for row in cursor:
            print str(row[0]) + " " +row[1]
    dbconn.close()
    return


def addemp(emp):
    dbconn=pyodbc.connect(conn_str)
    cursor=dbconn.cursor()
    isql = "insert into employee(emp_name,picked) values(\'%s\', \'Y\')" %(emp)
    cursor.execute(isql) 
    dbconn.commit()
    dbconn.close()
    return        

def menu():
    while True:
    print "User Menu"
    print "\ta. Add Users"
    print "\tb. Generate Groups"
    print "\tq. Exit"
    n=' '
        n = raw_input("\n\n Enter your Choice: ")
        if n.lower() == 'a':
            uname = raw_input("Enter User Name: ")
            addemp(uname)           
        elif n.lower() == 'b':
            print "Generate Groups Automatically"
            gengroups()
        elif n.lower() == 'q':
            break
        else:
            print "invalid input, try again" 
    return

menu()

