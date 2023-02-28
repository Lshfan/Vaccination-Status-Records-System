#Student staff update
def printing_info(**ARGUMENT):
    """Print users information in rows"""
    for k,v in ARGUMENT.items():
        print("{0:^20}".format(k.title())+":"+"{0:^10}".format(str(v)))

def empty_checking(new_value):
    """Checking whether user's enter is empty or not"""
    while new_value == ' ' or new_value == '':
        new_value = input('Error: the new value cannot be empty, pleas try again:')
    else:
        return new_value

def gender_checking(sex):
    """Checking whether user's enter is a valid gender"""
    sex=sex.lower()
    sex_list=['m','male','f','female']
    while empty_checking(sex) not in sex_list:
        sex = input('Error: the gender is invalid, pleas try again:')
    else:
        if sex in sex_list[0:2]:
            return 'Male'
        else:
            return 'Female'

def digit_checking(digit):
    """Checking whether user's enter is a digit"""
    while not digit.isdigit():
        digit=empty_checking(input("Error: the input should be an integer, please try again:"))
    else:
        return digit

def upload_function(**ARGUMENT):
    """Updating users' information"""
    global new_value
    printing_info(**ARGUMENT)
    change=input("\nWhich of the aboving specific section do you want to update?").lower()
    for key in ARGUMENT.keys():
        if key==change:
            if change == 'vac_dose':
                new_value=(input("Please enter the new value"))
                new_value = digit_checking(new_value)
                if int(ARGUMENT['vac_dose'])>int(new_value):
                    print("Error: You cannot 'un-vaccine' your vaccination!\n")
                    break
                elif int(new_value) < 0 or int(new_value) > 3:
                    print("Error: Unreasonable value for dose of vaccination\n")
                    break
                else:
                    ARGUMENT[key] = new_value
                    
                    
            elif change == 'name':
                new_value=input("Please enter the new value")
                ARGUMENT['name']= empty_checking(new_value).title()
                
            elif change == 'age':
                new_value=input("Please enter the new value")
                ARGUMENT['age']= digit_checking(new_value)
            
            elif change == 'id':
                print("\nWarning: You cannot change your id! Please inform the administrator to change your id if you have made a typo.")
                break
                
            elif change == 'department':
                new_value=input("Please enter the new value")
                ARGUMENT['department']=empty_checking(new_value).upper()
                
            elif change == 'occupation':
                print("\nWarning: You cannot change your occupation! Please inform the administrator to change your occupation if you have made a typo.")
                break

            elif change == 'sex':
                new_value=input("Please enter the new value")
                ARGUMENT['sex']=gender_checking(new_value)
                
            print(f'"The section {key}" successfully updated as "{ARGUMENT[change]}"\n')
            break
                
    else:
        print("The section you want to update is invalid\n")
        
    ask=input("Continue to update?(YES/NO)")
    if ask.lower() == 'yes' or ask.lower() == 'y':
        print('\n')
        ARGUMENT=upload_function(**ARGUMENT)

    return ARGUMENT

def adding(**ARGUMENT):#id=id,department=...,
    """Adding user's information"""
    name = input("Please enter your name:")
    name = empty_checking(name)
    sex = input("Please enter your gender:")
    sex = gender_checking(sex)
    age = input("Please enter your age:")
    age = digit_checking(age)
    vac_dose = input("please enter your number of vaccine you've received so far:")
    vac_dose = digit_checking(vac_dose)

    ARGUMENT['name'] = name.title()
    ARGUMENT['sex'] = sex
    ARGUMENT['age'] = age
    ARGUMENT['vac_dose'] = vac_dose
    print("\nThe user's information has uploaded succesfully:\n")
    printing_info(**ARGUMENT)

    return ARGUMENT


def main(Master_List,Targeted_List,user):
    """The Main Page of student staff page (regular user)"""
    while True:
        department=input("\nWhich department are you in?")
        department=empty_checking(department).upper()
        student_staff=user.title()

        for ARGUMENT in Master_List:
            if ARGUMENT['department'] == department and ARGUMENT['occupation'] == student_staff:

                Targeted_List.append(ARGUMENT)

        id=input("Please enter your student/staff ID:")
        id=empty_checking(id).lower()

        for i in range(len(Targeted_List)):
            ARGUMENT=Targeted_List[i]
            if ARGUMENT['id'] == id and ARGUMENT["department"] == department and ARGUMENT["occupation"] == student_staff:

                print("\nIt seems that this is your following information:")
                printing_info(**ARGUMENT)

                ask=input("\nWould you like to update your information??(y/n)")
                if ask.lower() == "y" or ask.lower() == "yes":
                    new = upload_function(**ARGUMENT)
                    Targeted_List[i] = new
                    break

                else:
                    break

        else:
            ask=input("\nIt seems that there is no record of you in the system,would you like to upload your information?(y/n)")
            if ask.lower() == "y":
                Master_List.append(adding(id=id,occupation=student_staff,department=department))

        ask=input("\nWould you like to search for another user? y/n")
        if ask.lower() == 'n' or ask.lower() == 'no':
            break




