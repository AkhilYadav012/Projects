import mysql.connector as msc
import datetime
def addbook():
    name=input("enter book name")
    writer=input("enter writer name")
    qty=int(input("enter quantity"))
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="insert into books(name,writer,qty)values('{}','{}',{})".format(name,writer,qty)
    cursor.execute(query)
    conn.commit()
    conn.close()
def searchbook():
    writer=input("enter writer name")
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="select * from books where writer='{}'".format(writer)
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
    conn.close()
def addcustomer():
    name=input("enter customer name")
    phone_no=input("enter phone_no")
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="insert into customers(name,phone_no)values('{}','{}')".format(name,phone_no)
    cursor.execute(query)
    conn.commit()
    conn.close()      
def searchcustomer():
    id=int(input("enter id"))
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="select * from customers where id={}".format(id)
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
    conn.close()
    
def deccopy(bid):
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="update books set qty=qty+1 where id={}".format(bid) 
    cursor.execute(query)
    conn.commit()
    conn.close()
    
def inccopy(bid):
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="update books set qty=qty-1 where id={}".format(bid) 
    cursor.execute(query)
    conn.commit()
    conn.close()    
def isavailable(bid):
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="select * from Books where id={} and qty>0".format(bid)
    cursor.execute(query)
    records=cursor.fetchall()
    conn.close()
    if len(records)==0:
       return False
    else:
        return True

def issuebook():
     bid=int(input("enter book id"))
     cid=int(input("enter customer id"))
     date=datetime.datetime.now()
     if isavailable(bid)==True:
        deccopy(bid)
        conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
        cursor=conn.cursor()        
        query="insert into transactions(bid,cid,doi) values({},{},'{}')".format(bid,cid,date)
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("Issued")
     else:
         print("false")
def returnbook():
    tid=int(input("enter transaction ID"))
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="select * from transactions where id={}".format(tid)
    cursor.execute(query)
    records=cursor.fetchall()
    row=records[0]
    bid=row[1]
    inccopy(bid)
    date=datetime.datetime.now()
    query="update transactions set dor='{}' where id={}".format(date,tid)
    cursor.execute(query)
    conn.commit()
    conn.close()
def viewdefaulters():
    conn=msc.connect(host="localhost",user="root",password="India@123",database="lms")
    cursor=conn.cursor()        
    query="select t.id,c.name,c.phone_no,t.doi from transactions t,customers c where t.cid=c.id and dor is null"
    cursor.execute(query)
    records=cursor.fetchall()
    print("TID","\t\t","CNAME","\t\t\t","Phone No","\t\t\t","DOI","\t\t")
    for row in records:
        print(row[0],"\t\t",row[1],"\t\t",row[2],"\t\t",row[3],"\t\t")
    conn.close()



ch=1
while ch!=8:
     print ("press 1 to add a new book")
     print("press 2 to search a book")
     print ("press 3 to add a customer")
     print ("press 4 to search a customer")
     print ("press 5 to issue a book")
     print ("press 6  to return a book")
     print ("press 7  to see defaulters")
     print ("press 8 to exit")
     ch=int(input("enter choice"))
     if ch==1:
          addbook()
     elif ch==2:
          searchbook()
     elif ch==3:
          addcustomer()
     elif ch==4:
          searchcustomer()
     elif ch==5:
          issuebook()
     elif ch==6:
          returnbook()
     elif ch==7:
          viewdefaulters()
     
