import json
from student_staff import main
from student_staff import empty_checking
from admin import admin

Master_List=[]
Targeted_List=[]
Administrator_List=[{'name':'li','password':'12345678'},{'name':'john','password':'21101226d'}]


filename = 'Master_List.json'
try:
    with open(filename) as f:
        Master_List = json.load(f)
except:
    with open(filename,'w') as f:
        json.dump([],f)

   
while True:
    user = input('\nAre you a student or staff or the admin, enter "q" to quit')
    user = empty_checking(user)
    if user.lower() == "q":
        break

    if user.lower() == 'student' or user.lower() == 'staff':
        main(Master_List,Targeted_List,user.lower())
        while Targeted_List:
            current = Targeted_List.pop(0)
            start = 0
            end = len(Master_List)
            while True:
                if abs(start - end) <= 1:
                    break
                if current['id'] in [Master_List[x]['id'] for x in range(start, (end + start) // 2)]:
                    end = (end + start) // 2
                elif current['id'] in [Master_List[x]['id'] for x in range((end + start) // 2, end)]:
                    start = (end + start) // 2
                else:
                    break

            index = start
            Master_List[index] = current

    elif user.lower() == "admin":
        x = input("please enter your name")
        y = input("please enter your password")

        dict1 = {'name':x,'password':y}
        if Administrator_List.count(dict1) != 0:
            admin(Master_List,Targeted_List)
        else:
            print("Invaild admin username/password,please try again\n")

    else:
        print('Error: invalid input, please try again\n')




filename = 'Master_List.json'
with open(filename,'w') as f:
    json.dump(Master_List, f)



    
