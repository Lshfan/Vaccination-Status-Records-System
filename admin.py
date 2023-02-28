from student_staff import gender_checking,digit_checking,empty_checking,printing_info
func_list=['add','delete','edit','view','quit']

def add(Master_list):
    """Adding a users' information"""
    id = empty_checking(input('\nPlease enter the id of the person to be added'))
    start=0
    end=len(Master_List)
    while not abs(start-end)<=1:
        if id in [Master_List[x]['id'] for x in range (start,(end+start)//2)]:
            end = (end+start)//2
        elif id in [Master_List[x]['id'] for x in range ((end+start)//2,end)]:
            start = (end+start)//2
        else:
            name = empty_checking(input('Please input the name of the person'))
            age = digit_checking(input('Please input the age of the person'))
            gender = gender_checking(input('Please input the gender of the person'))
            occupation = empty_checking(input('Please input whether that person is a student or staff'))
            department = empty_checking(input('Please input the department that person is in'))
            vac_dose = digit_checking(input('Please input the dose of vaccination that person has take so far'))
            new_person = {"id": id, "occupation": occupation,
                          "department": department.upper(), "name": name.title(),
                          "sex": gender, "age": age, "vac_dose": vac_dose}
            Master_list.append(new_person)
            print(f"\nThe information of {new_person['name']} has uploaded successfully")
            break
    else:
        print("\nError: The information of that person has already uploaded, please try again")

def delete(Master_List):
    """Deleting a users' information"""
    id = empty_checking(input('\nPlease enter the id of the person to be deleted'))
    start = 0
    end = len(Master_List)
    while not abs(start - end) <= 1:
        if id in [Master_List[x]['id'] for x in range(start, (end + start) // 2)]:
            end = (end + start) // 2
        elif id in [Master_List[x]['id'] for x in range((end + start) // 2, end)]:
            start = (end + start) // 2
        else:
            print(f"Error: The person with the id \"{id}\" has not being founded, please try again")
            break
    else:
        i = start
        print("Are you sure you are going to remove the person with following information? y/n\n")
        printing_info(**Master_List[i])
        choice = input('\n').lower()
        if choice == 'y' or 'yes':
            del Master_List[i]
            print(f'\nThe person with id "{id}" has been removed successfully')

def edit(Master_List):
    """Editing a users' information"""
    id = empty_checking(input('\nPlease enter the id of the person to be edited'))
    start = 0
    end = len(Master_List)
    while not abs(start - end) <= 1:
        if id in [Master_List[x]['id'] for x in range(start, (end + start) // 2)]:
            end = (end + start) // 2
        elif id in [Master_List[x]['id'] for x in range((end + start) // 2, end)]:
            start = (end + start) // 2
        else:
            print(f"Error: The person with the id \"{id}\" has not being founded, please try again")
            break

    else:
        i = start
        while True:
            print('Which would the following section you want to change: ')
            printing_info(**Master_List[i])
            change = input("\n").lower()
            key_list=[key for key in Master_List[i].keys()]
            while change not in key_list:
                change = input("The section you want to update is invalid,please try again\n").lower()
            else:
                for key in Master_List[i].keys():
                    if change == 'vac_dose':
                        new_value = digit_checking((input("Please enter the new value")))
                        Master_List[i][key] = new_value

                    elif change == 'name':
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = empty_checking(new_value).title()

                    elif change == 'age':
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = digit_checking(new_value)

                    elif change == 'id':
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = empty_checking(new_value)

                    elif change == 'department':
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = empty_checking(new_value).upper()

                    elif change == 'occupation':
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = empty_checking(new_value).title()

                    else:
                        new_value = input("Please enter the new value")
                        Master_List[i][key] = gender_checking(new_value)

                    print(f'"The section {key}" successfully updated as "{Master_List[i][key]}"\n')
                    break

            ask = input("Continue to update?(YES/NO)")
            if ask.lower() == 'yes' or ask.lower() == 'y':
                continue
            break




def view(Master_List,Targeted_List):
    """Either viewing an individual's information or perform vaccination state analysis"""
    print("Would you like to view the information of:")
    print("\t- An individual")
    print("\t- Certain group?")
    choice=input().lower()
    if choice == 'individual':
        id = empty_checking(input('\nPlease enter the id of the person you are looking for'))
        start = 0
        end = len(Master_List)
        while not abs(start - end) <= 1:
            if id in [Master_List[x]['id'] for x in range(start, (end + start) // 2)]:
                end = (end + start) // 2
            elif id in [Master_List[x]['id'] for x in range((end + start) // 2, end)]:
                start = (end + start) // 2
            else:
                print(f"Error: The person with the id \"{id}\" has not being founded, please try again")
                break
        else:
            print(f"The information of the person you are looking for:")
            printing_info(**Master_List[start])
            end=input(f"\n{'——————————press any key to quit——————————'}")

    elif choice == 'certain group':
        print("\n")
        criteria={"occupation": "", "department": "", "sex": "", "age": "", "vac_dose": ""}
        for i in criteria.keys():
            change=empty_checking(input(f"Please input the requirement for section \"{i}\", enter 'n' if there's no requirement for it:"))
            criteria[i] = change
        list_criteria = {(k,v)for k,v in criteria.items() if v != 'n'}
        for individual in Master_List:
            list_individual ={(x,y)for x,y in individual.items()}
            if list_individual > list_criteria:
                Targeted_List.append(individual)
        else:
            if Targeted_List:
                print(f"\n{'ID':^12}|{'Occupation':^10}|{'Department':^10}|{'Name':^12}|{'Sex':^8}|{'Age':^5}|{'Dose of vaccine taken':^25}")
                print("—"*88)
                x = 0
                y = len([i for i in Master_List if int(i['vac_dose'])>0])
                for i in Targeted_List:
                    if int(i['vac_dose']) > 0:
                        x += 1
                    print(f"{i['id']:^12}|{i['occupation']:^10}|{i['department']:^10}|{i['name']:^12}|{i['sex']:^8}|{i['age']:^5}|{i['vac_dose']:^25}")
                print(f"\n{len(Targeted_List)} results have found.")
                print(f"%{(len(Targeted_List)/x)*100:.2f} of the the sample group have received vaccination and %{((x-len(Targeted_List))/x)*100:.2f} of the sample group have not")
                print(f"%{((len(Targeted_List))/len(Master_List))*100:.2f} of the population recorded is occupied by the sample with following criteria:")
                for i in list_criteria:
                    print(f"\t{i[0]}:{i[1]:^5}")
                print(f"In addition, the number of people who received vaccine within sample occupies %{(x/y)*100} of the total number of vacinned people record")
                end=input(f"\n{'——————————press any key to quit——————————'}")
            else:
                print("\nThere is no result matches with the criteria you entered!")

    else:
        print("Invalid input!")


def admin(Master_List,Targeted_List):
    "Main page"
    while True:
        print("\nWhich of the following operation you would like to perform:")
        for i in range (len(func_list)):
            print(f"{i+1}. {func_list[i].title()}")

        choice=input().lower()

        if choice == 'add' or choice == '1':
            add(Master_List)
        elif choice == 'delete' or choice == '2':
            delete(Master_List)
        elif choice == 'edit' or choice == '3':
            edit(Master_List)
        elif choice == 'view' or choice == '4':
            view(Master_List,Targeted_List)
        elif choice == 'quit' or choice == '5':
            quit=input('\nAre you sure to quit? y/n').lower()
            if quit == 'y' or 'yes':
                break
