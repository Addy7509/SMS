
#===========================================================================================


class mycon():
    def __init__(self):
        import mysql.connector
        self.mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="school"
			)
        self.mycursor=self.mydb.cursor()
    
        
#_update
    def stuupdate(self, rno, nm, clas, mrks, adds):
        self.rno = rno
        self.nm = nm
        self.clas = clas
        self.mrks = mrks
        self.adds = adds
        pre_sql = "select count(rollno) from student where rollno=%s"
        pre_value = [self.rno]
        self.mycursor.execute(pre_sql, pre_value)
        pre_data = self.mycursor.fetchall()
        pre_data1 = list(pre_data)
        for x in pre_data1:
           for y in x:
               if y == 0:
                   print("### Roll Number Not Matched Please Re-enter ###")
                   ob2.upD()

               else:
                    sql = "update student set name=%s,class=%s,marks=%s,address=%s where rollno=%s"
                    value = (self.nm, self.clas, self.mrks, self.adds, self.rno)
                    self.mycursor.execute(sql,value)
                    self.mydb.commit()
                    print("Record Successfully Updated!!!!")
        
#_display_table
    def studisplay(self):
        self.mycursor.execute("select * from student")
        sql = self.mycursor.fetchall()
        self.mydb.commit()
        for x in sql:
            print("ROLL >",x[0],"NAME >",x[1],"CLASS >",x[2],"MARKS >",x[3],"ADDRS >",x[4])
#_student_details
    def studetails(self,rno):
        self.rno = rno 
        sql = "select name,class,marks,address from student where rollno=%s"
        value =[self.rno]
        self.mycursor.execute(sql,value)
        data1 = self.mycursor.fetchall()
        data2 = list(data1)
        if data2 == []:
            print("### Roll Number Not Found Please re-enter ###")
            ob2.roll()

        else:
            print("==== STUDENT DETAILS ====")
            for i in data2:
                print("  name   = ",i[0])
                print("  class  = ",i[1])
                print("  marks  = ",i[2])
                print(" address = ",i[3])
#_delete      
    def stuRecDel(self, rno):
        self.rno = rno
        pre_sql = "select count(rollno) from student where rollno=%s"
        pre_value = [self.rno]
        self.mycursor.execute(pre_sql,pre_value)
        pre_data = self.mycursor.fetchall()
        pre_data1 = list(pre_data)
        for x in pre_data1:
           for y in x :
                if y==0:
                   print("Record Not Found Please Re-enter !!")
                   ob2.dele()
                else: #ask yes or no to delete record 
                    ch1 = input("Are you sure you want to delete ? y/n  ")
                    if ch1==y:
                        sql = "delete from student where rollno=%s"
                        value = [self.rno]
                        self.mycursor.execute(sql,value)
                        self.mydb.commit()
                        print("!!! Record successfully Deleted !!!")
                    else:
                        print("Aborted!!!")
#_insert_
    def stuInsert(self, rno, nm, clas, mrks, adds):
        self.rno = rno
        self.nm = nm
        self.clas = clas
        self.mrks = mrks
        self.adds = adds
        pre_sql = "select count(rollno) from student where rollno=%s"
        pre_value = [self.rno]
        self.mycursor.execute(pre_sql, pre_value)
        pre_data = self.mycursor.fetchall()
        pre_data1 = list(pre_data)
        for x in pre_data1:
            for y in x:
                if y==1 :
                    print("!!! No Duplicate RollNumber Allowed !!!")
                    ob2.inputinsert()
            
                else:
                    sql = "insert into student(rollno,name,class,marks,address) values (%s,%s,%s,%s,%s)"
                    value=(self.rno,self.nm,self.clas,self.mrks,self.adds)
                    self.mycursor.execute(sql,value)
                    self.mydb.commit()
                    print("Record Inserted Successfully!!")
#####################################################################################
#___validations___
class validation1(mycon):
    
    #insert validation
    def inputinsert():
        print("====Insert New Record====")
        rno = input("Enter Roll No: ")
        name = input("Enter Name: ")
        clas = input("Enter Class: ")
        marks = input("Enter Marks: ")
        address = input("Enter Address: ")
        if rno == "" or name == "" or clas == "" or marks == "" or address == "":
            print("--> Values Can't Be Null Please Re-enter <--")
            ob2.inputinsert()
        else:
            ob1.stuInsert(rno, name, clas, marks, address)
    #_student details validation
    def roll():
        rno = input("Enter Roll No: ")
        ob1.studetails(rno)
    #_update validation
    def upD():
        rno = input("Enter Roll No: ")
        name = input("Enter Name: ")
        clas = input("Enter Class: ")
        marks = input("Enter Marks: ")
        address = input("Enter Address: ")
        ob1.stuupdate(rno, name, clas, marks, address)
    #_delete _validation
    def dele():
        rno = input("Enter Roll No: ")
        ob1.stuRecDel(rno)
ob1 = mycon()
ob2 = validation1






       




