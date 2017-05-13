import random
import pyodbc

def gengroups():
    conn = pyodbc.connect(
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER=localhost;'
        r'DATABASE=test;'
        r'Trusted_Connection=yes;'
        )
    cursor=conn.cursor()
    cursor.execute("select * from employee")
    empn=[]
    for row in cursor:
        emp_no=row[0]
        empn.append(emp_no)

    #groupsize=grpsize(len(empn))
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
    conn.close()
    return

gengroups()



