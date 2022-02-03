from sec_module import mycon
from sec_module import validation1

ob1=mycon()
ob2=validation1
#_insert_
print("==== WELCOME TO CYBROM STUDENT DATA TABLE ====")
print("insert(1)||update(2)||display(3)||search(4)||delete record(5)")
ch = input("Enter Your Choice ==> ")
print()
if ch == "1":
    ob1.studisplay()
    ob2.inputinsert()
#_update_
elif ch=="2" :
    print("====Update Record====")
    print
    ob1.studisplay()
    ob2.upD()
#_display_
elif ch=="3" :
    print("==== STUDENT TABLE ====")
    ob1.studisplay()
#_search_
elif ch=="4" :
    print("== Search for Student ==")
    ob2.roll()
#_delete_
elif ch=="5" :
    ob1.studisplay()
    ob2.dele()
else:
    print("Invalid Choice")