###########################################
#      This project is made with <3       #
#                for TUMS                 #
###########################################


#requirements


import os, sys
import ast
import re
import copy
import getpass
import smtplib
import ssl
from time import sleep
from email.message import EmailMessage
from datetime import datetime

patients_list=[]
tests_list=[]
test_results=[]
company_name=""
company_email=""
email_pass=""


#Functions


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def incorrect_input():
    print("The entered input is not correct!\n"
          "Returning...")
    sleep(2)
    clean()


def green(x):
    colored=f'\033[0;32m'+x+f'\033[0m'
    return colored


def is_email(x):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,x):
      return True
   return False


def enter_company_info():
    clean()
    company_name=input("Enter the name of this organization: ")
    while True:
        company_email=input("Enter the email address associated with your orgnization: ")
        if is_email(company_email):
            break
        else:
            print("The entered input doesn't have a correct format")        
    while True:
        email_pass=getpass.getpass("Enter the app password for this organization\n"
                                   "(You can see instrustions on how to get app passwords on the web): ")
        if email_pass!=getpass.getpass("Enter your app password again: "):
            print("Passwords do not match!")
        else:
            break
    clean()
    print(f'System name: {company_name}')
    print(f'Organization email: {company_email}')
    confirm=input("Are the displayed information correct?\n"
                  "1. Yes, proceed\n"
                  "0. No, try again\n"
                  "Input the operation number: ")
    if confirm=="1":
        with open(r'./Database/Info.py', 'w') as inf:
            print("Saving info...")
            inf.write("company_name='%s'\n" % company_name)
            inf.write("company_email='%s'\n" % company_email)
            inf.write("email_pass='%s'\n" % email_pass)
            sleep(1)
            print('Done!')
            sleep(1)
            return True
    elif confirm=="0":
        return False
    else:
        incorrect_input()
        return False


def read_patients_database():
    if os.path.isfile("./Database/Patients.txt") is True:
        with open(r'./Database/Patients.txt', 'r') as p_db: # 'r' indicates reading the file
            for line in p_db:
                x = ast.literal_eval((line[:-1]))
                patients_list.append(x)
    else:
        p_db = open("./Database/Patients.txt", "x") # 'x' indicates creation of a new file


def read_tests_database():
    if os.path.isfile("./Database/Tests.txt") is True:
        with open(r'./Database/Tests.txt', 'r') as t_db:
            for line in t_db:
                x = ast.literal_eval((line[:-1]))
                tests_list.append(x)
    else:
        t_db = open("./Database/Tests.txt", "x")
   

def read_results_database():
    if os.path.isfile("./Database/Results.txt") is True:
        with open(r'./Database/Results.txt', 'r') as r_db:
            for line in r_db:
                x = ast.literal_eval((line[:-1]))
                test_results.append(x)
    else:
        r_db = open("./Database/Results.txt", "x")


def save_patients():
    with open(r'./Database/Patients.txt', 'w') as p_db: # 'w' indicates overwriting all the context in the opened file
        print("Saving Patients' database...")
        for item in patients_list:
            p_db.write("%s\n" % item)
        sleep(1)
        print('Done!')
        sleep(1)


def save_tests():
    with open(r'./Database/Tests.txt', 'w') as t_db:
        print("Saving Tests database...")
        for item in tests_list:
            t_db.write("%s\n" % item)
        sleep(1)
        print('Done!')
        sleep(1)


def save_results():
    with open(r'./Database/Results.txt', 'w') as r_db:
        print("Saving Results database...")
        for item in test_results:
            r_db.write("%s\n" % item)
        sleep(1)
        print('Done!')
        sleep(1)


def main_menu():
    clean()
    print('\033[94m'+company_name+' Laboratory Information System\033[0m\n'
          "1. Patients' menu\n"
          "2. Tests menu\n"
          "3. Results menu\n"
          "0. exit")
    a=input("Input the operation number: ")
    return a


def exit_program():
    clean()
    print("Saving all changes...")
    save_patients()
    save_tests()
    save_results()
    print("Exiting program...")
    exit()


def register_patient():
    clean()
    answer=input("Do you want to add a new patient?\n"
                 "1. Add a new paient\n"
                 "0. Return to the main menu\n"
                 "Input the operation number: ")
    if answer=="1":
        checklist=[]
        for d in patients_list:
            nid=d["National ID"]
            checklist.append(nid)            
        id=input("Please enter patient's national ID code: ")
        if id in checklist:
            print("This patient's data exists in the database!\n"
                  "(Or the entered National ID is incorrect)")
            sleep(3)
        else:
            first_name=input("Please enter patient's first name: ")
            last_name=input("Please enter patient's last name: ")
            father_name=input("Please enter patient's father name: ")
            age=input("Please enter patient's age: ")
            gender=input("Please enter patient's gender: ")
            email=""
            while True:
                email=input("Please enter patient's Email address: ")
                if is_email(email):
                    break
                else:
                    print("The entered input doesn't have a correct format")
            d={"First name":first_name , "Last name": last_name , "Father name": father_name , "Age": age , "Gender": gender , "National ID": id , "Email address": email}
            patients_list.append(d)
            save_patients()
            print("Patient info saved successfully!")
            sleep(2)
            clean()
            return False
    elif answer=="0":
        clean()
        return True
    else:
        incorrect_input()
        return False


def show_patients():
    clean()
    for p in patients_list:
        print(f'First name: {p["First name"]}, Last name: {p["Last name"]}, Father name: {p["Father name"]}, Age: {p["Age"]}, Gender: {p["Gender"]}, ID: {p["National ID"]}, Email: {p["Email address"]}')


def show_tests():
    clean()
    for t in tests_list:
            print(f'Test name: {t["Name"]} with values names being: {list(t.keys())}')


def highlight():
    clean()
    highlighted=""
    look=input("What are you looking for? ")
    target=re.compile(look, re.IGNORECASE)
    for p in patients_list:
        highlighted+=(f'First name: {p["First name"]}, Last name: {p["Last name"]}, Father name: {p["Father name"]}, Age: {p["Age"]}, Gender: {p["Gender"]}, ID: {p["National ID"]}, Email: {p["Email address"]}\n')
    nocolor=target.sub("SOMETHINGTHATNOONEEVERUSESINADATABASE", highlighted)
    print(nocolor.replace("SOMETHINGTHATNOONEEVERUSESINADATABASE", green(look)))


def edit_patient_info():
    clean()
    answer=input("Do you want to edit a patient's info?\n"
                 "1. Enter a patient's ID\n"
                 "0. Return to the main menu\n"
                 "Input the operation number: ")
    if answer=="1":
        get_id=input("Enter patient's ID: ")
        clean()
        checklist=[]
        for d in patients_list:
            nid=d["National ID"]
            checklist.append(nid)
        if get_id in checklist:
            while True:
                clean()
                for d in patients_list:
                    for k,v in d.items():
                        if v == get_id:
                            print(f'First name: {d["First name"]}\n'
                                  f'Last name: {d["Last name"]}\n'
                                  f'Father name: {d["Father name"]}\n'
                                  f'Age: {d["Age"]}\n'
                                  f'Gender: {d["Gender"]}\n'
                                  f'ID: {d["National ID"]}\n'
                                  f'Email: {d["Email address"]}')
                            edit=input("Which data do you want to edit?\n"
                                       "1. First name\n"
                                       "2. Last name\n"
                                       "3. Father name\n"
                                       "4. Age\n"
                                       "5. Gender\n"
                                       "6. National ID\n"
                                       "7. Email address\n"
                                       "0. abort\n"
                                       "Input the operation number: ")
                            num={"0","1","2","3","4","5","6","7"}
                            if edit not in num:
                                incorrect_input()
                                return False
                            else:
                                if edit=="0":
                                    clean()
                                    return True
                                index=(list(d)[int(edit)-1])
                                new_value=input(f'Enter the new value for {index}: ')
                                if edit=="6":
                                    if new_value in checklist:
                                        print("The entered ID is already associated to another patient!")
                                        sleep(2)
                                        break
                                d.update({index: new_value})
                                save_patients()
                                return False
        else:
            print("The entered ID is not found within the database")
            sleep(1)
            return False
    elif answer=="0":
        return True
    else:
        incorrect_input()
        return False


def register_test():
    answer=input("Do you want to add a new test?\n"
                 "1. Yes. Add a new test\n"
                 "0. Return to main menu\n"
                 "Input the operation number: ")
    if answer=="1":
        clean()
        checklist=[]
        for d in tests_list:
            names=d["Name"]
            checklist.append(names)            
        name=input("Input the name of this test: ")
        if name in checklist:
            print("The entered name is used previously by another test!")
            sleep(2)
        else:
            index="Name"
            test={}
            test[index]=name
            while True:
                clean()
                for k,v in test.items():
                    print(green(k),':',test[k])
                answer2=input(f'Do you want to add an entry for {name}?\n'
                              "1. Add a new entry\n"
                              "0. save the test and return\n"
                              "Input the operation number: ")
                if answer2=="1":
                    clean()
                    item=input("Enter the new entry name: ")
                    item_value=""
                    test.update({item:item_value})
                elif answer2=="0":
                    tests_list.append(test)
                    save_tests()
                    clean()
                    break
                else:
                    incorrect_input()
            return False
    elif answer=="0":
        clean()
        return True
    else:
        incorrect_input()
        return False


def edit_test():
    clean()
    checklist=[]
    for d in tests_list:
        for k,v in d.items():
            print(k,':',green(d[k]))
        names=d["Name"]
        checklist.append(names)
    name=input(f'Enter test {green("name")} (Input 0 to return): ')
    clean()
    if name=="0":
        return True
    elif name in checklist:
        for d in tests_list:
            copied=copy.deepcopy(d)
            for k,v in copied.items():
                if v == name:
                    for k,v in d.items():
                        print(green(k),':',d[k])
                    answer=input("What do yo want to do?\n"
                                 f'1. Edit the name of an existing {green("key")}\n'
                                 "2. Edit the name of the selected test\n"
                                 "3. Add a new key to selected test\n"
                                 "4. Remove an existing key from the test\n"
                                 "0. Return to the previous menu\n"
                                 "Input the operation number: ")
                    if answer=="1":
                        while True:
                            edit=input(f'Which {green("key")} do you want to edit? ')
                            if edit not in d.keys():
                                print("The entered Key not in the database provided!!")
                            elif edit=="Name":
                                print("You cannot edit the 'Name' key!")
                                sleep(3)
                                clean()
                                break
                            else:
                                new_key=input(f'Enter the new value for {edit}: ')
                                td={new_key if k==edit else k:v for k,v in d.items()}
                                for d in tests_list:
                                    if edit in d.keys():
                                        tests_list.remove(d)
                                        tests_list.append(td)
                                clean()
                                break
                    elif answer=="2":
                        while True:
                            rename=input(f'Enter the new name for {name}: ')
                            if rename in checklist:
                                print("The entered name is already in use by another test!")
                            else:
                                for td in tests_list:
                                    for k,v in td.items():
                                        if td["Name"]==name:
                                            td["Name"]=rename
                                print("New name saved!")
                                sleep(1)
                                clean()
                                break
                    elif answer=="3":
                        while True:
                            new_name=input("Input the name for your new value: ")
                            d[new_name]=""
                            confirm=input("Do you want to add another value?\n"
                                          "1. Yes, add a new value\n"
                                          "0. No, return to the previous menu\n"
                                          "Input the operation number: ")
                            if confirm=="1":
                                continue
                            elif confirm=="0":
                                break
                            else:
                                incorrect_input()
                    elif answer=="4":
                        while True:
                            clean()
                            for k,v in d.items():
                                print(green(k),':',d[k])
                            remove=input(f'Enter a {green("key")} name to remove it\n'
                                         "or enter 0 to return to the privious menu: ")
                            if remove=="Name":
                                print("You can't remove the name of a test!")
                                sleep(3)
                                clean()
                            elif remove=="0":
                                break
                            else:
                                if remove not in d.keys():
                                    print("The entered name is not present in the selected test!")
                                else:
                                    confirm2=input(f'Do you really want to remove {remove}?\n'
                                                   "1. Yes\n"
                                                   "0. No, choose another key\n"
                                                   "Input the operation number: ")
                                    if confirm2=="1":
                                        d.pop(remove)
                                        save_tests
                                    elif confirm2=="0":
                                        clean()
                                        break
                                    else:
                                        incorrect_input()
                    elif answer=="0":
                        save_tests()
                        return True
                    else:
                        incorrect_input()
                        return False
    else:
        print("The entered name is not found within the database!")
        sleep(2)
        return False


def remove_test():
    clean()
    checklist=[]
    for d in tests_list:
        test_names=d["Name"]
        print(green(test_names))
        checklist.append(test_names)
    name=input("Enter test's name\n"
               "(Enter 0 to return): ")
    if name=="0":
        return True
    else:
        if name in checklist:        
            answer=input(f'Do you really wish to remove {name}?\n'
                         "1. Yes I'm sure\n"
                         "0. No, return to main menu\n"
                         "Input the operation number: ")
            if answer=="1":
                answer2=input("Are you really really sure?\n"
                              "confirm by Typing 'YES': ")
                if answer2=="YES":
                        for d in tests_list:
                            if name in d.values():
                                tests_list.remove(d)
                                save_tests()
                                print("Test successfully deleted!")
                                sleep(1)
                                return False
                else:
                    print("Input doesn't match"
                          "confirmation aborted. returning...")
                    sleep(5)
                    clean()
                    return True
            elif answer=="0":
                print("confirmation aborted. returning...")
                sleep(2)
                clean()
                return True
            else:
                incorrect_input()
                return False
        else:
            incorrect_input()
            return False


def add_result(x):
    clean()
    names=[]
    for test_dict in tests_list:
        for k,v in test_dict.items():
            if k=="Name":
                print(k,':',green(test_dict[k]))
            test_names=test_dict["Name"]
            names.append(test_names)
    name=input(f'Which {green("test")} do you want to enter results for? ')
    if name not in names:
        print("The entered Key not in the database provided!!")
        sleep(2)
        clean()
        return False
    else:
        time=datetime.now()
        time_fingerprint=time.strftime("%Y%m%d%H%M%S")
        test_result={}
        for test_dict in tests_list:
            for k,v in test_dict.items():
                if test_dict["Name"]==name:
                    test_result["TID"]=time_fingerprint
                    test_result.update(test_dict)
        for k,v in test_result.items():
            if k not in ("TID", "Name"):
                value=input(f'enter the value for {k}: ')
                test_dict[k]=value
        for person in test_results:
            if person[2]==x:
                person.append(test_dict)
        print("Saving the test results...")
        save_results()
        print(f'Done! Test is saved with {time_fingerprint} as fingerprint')
        sleep(4)
        clean()
        return True


def test_patient():
    clean()
    patient_id=input("Which patient do you want to add a test results for?\n"
                     "(enter '0' to return to the previous menu)\n"
                     "Input their nationl ID number: ")
    if patient_id=="0":
        clean()
        return True
    ids=[]
    for l in test_results:
        pid=l[2]
        ids.append(pid)
    if patient_id in ids:
        clean()
        print("Patient has previous test results. Adding a new entry")
        sleep(1)
        for l in test_results:
            if l[2]==patient_id:
                print(f'Patient name: {l[0]}\n'
                      f'Father name: {l[1]}\n'
                      f'National ID: {l[2]}')
        answer=input("Are the displayed information correct?\n"
                     "1. Yes\n"
                     "0. No, back to the previous menu\n"
                     "Input the operation number: ")
        if answer=="0":
            clean()
            return True
        elif answer=="1":
            while True:
                if add_result(patient_id):
                    break
            return False
        else:
            incorrect_input()
            return False
    else:
        checklist=[]
        for d in patients_list:
            nid=d["National ID"]
            checklist.append(nid)
        if patient_id not in checklist:
            print("The entered ID is not within the patients' database.\n"
                  "You may need to enter patient's details in patients list first")
            sleep(3)
            clean()
            return False
        else:
            clean()
            print("Initializing adding the first test for this patient...")
            for p in patients_list:
                if p["National ID"]==patient_id:
                    print(f'Patient name: {p["First name"]} {p["Last name"]}\n'
                          f'Father name: {p["Father name"]}\n'
                          f'National ID: {p["National ID"]}')
            answer=input("Are the displayed information correct?\n"
                         "1. Yes\n"
                         "0. No, back to the previous menu\n"
                         "Input the operation number: ")
            if answer=="0":
                clean()
                return True
            elif answer=="1":
                test_result_list=[]
                for p in patients_list:
                    if p["National ID"]==patient_id:
                        name=(f'{p["First name"]} {p["Last name"]}')
                        father=p["Father name"]
                        national_id=p["National ID"]
                        test_result_list.append(name)
                        test_result_list.append(father)
                        test_result_list.append(national_id)
                test_results.append(test_result_list)
                while True:
                    if add_result(patient_id):
                        break
                return False
            else:
                incorrect_input()
                return False


def send_results(rm,cntx):
    subject = f'{company_name} Laboratory Information System - Your test results'
    em = EmailMessage()
    em['From'] = company_email
    em['To'] = rm
    em['Subject'] = subject
    em.set_content(cntx)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(company_email, email_pass)
        smtp.sendmail(company_email, rm, em.as_string())


def view_results():
    clean()
    tid=input("Enter the test fingerprint (it should be in YYYYMMDDHHMMSS format)\n"
              "(Input 0 to return to the previous menu) :")
    if tid=="0":
        clean()
        return True
    else:
        dict_list=[]
        for l in test_results:
            for x in l:
                if type(x)==dict:
                    tid_check=x["TID"]
                    dict_list.append(tid_check)
        if tid not in dict_list:
            print("The entered fingerprint is incorrect!")
            sleep(2)
            return False
        else:
            for l in test_results:
                for x in l:
                    if type(x)==dict:
                        if x["TID"]==tid:
                            clean()
                            result=[]
                            result.append(f'Patient name: {l[0]}')
                            result.append(f'Father name: {l[1]}')
                            result.append(f'National ID: {l[2]}')
                            result.append(f'Searched test: {x}')
                            for n in result:
                                print(n)
                            send=input("Do you want to send this result to the patient?\n"
                                       "1. Yes, send the test to the patient\n"
                                       "0. Go back to the previous menu\n"
                                       "Input the operation number: ")
                            if send=="0":
                                clean()
                                return True
                            elif send=="1":
                                id=l[2]
                                checklist=[]
                                for d in patients_list:
                                    cl=d["National ID"]
                                    checklist.append(cl)
                                if id in checklist:
                                    for d in patients_list:
                                        for k,v in d.items():
                                            if v == id:
                                                ma=d["Email address"]
                                                result_string=""
                                                for k,v in x.items():
                                                    result_string += k + ' : ' + x[k] + '\n'
                                                print("Sending results as an email...")
                                                send_results(ma,result_string)
                                                print("Done!")
                                                sleep(1)
                                                clean()
                                    return False
                                else:
                                    print("The patient is not found in patients database.\n"
                                          "Maybe the recorde got removed?")
                                    sleep(3)
                                    clean()
                                    return True
                            else:
                                incorrect_input()
                                return False


def view_patient_results():
    clean()
    patient_id=input("Which patient's test results do you want to view?\n"
                     "(enter '0' to return to the previous menu)\n"
                     "Input their nationl ID number: ")
    if patient_id=="0":
        clean()
        return True
    patients_ids=[]
    for l in test_results:
        ids=l[2]
        patients_ids.append(ids)
    if patient_id not in patients_ids:
        print("The entered ID has no associated test result!")
        sleep(2)
        return False
    else:
        results=[]
        for l in test_results:
            if l[2]==patient_id:
                clean()
                results.append(f'Patient name: {l[0]}')
                results.append(f'Father name: {l[1]}')
                results.append(f'National ID: {l[2]}')
                results.append("Test results:")
                for item in l:
                    if item not in (l[0], l[1], l[2]):
                        results.append(item)
                for n in results:
                    print(n)
        answer=getpass.getpass("(press 'enter' to return)")
        if answer!="":
            return False


def handle_input(c):
    if c=="0":
        exit_program()
    elif c=="1":
        while True:
            clean()
            answer=input("What do you want to do?\n"
                         "1. Register a new patient\n"
                         "2. Show patient list\n"
                         "3. Edit patients' info\n"
                         "0. Return to the main menu\n"
                         "Input operation number: ")
            if answer=="1":
                while True:
                    if register_patient():
                        break
            elif answer=="2":
                clean()
                while True:
                    answer=input("What do you want to do?\n"
                                 "1. Find a specific info\n"
                                 "2. View full list of patients\n"
                                 "0. Return to the main menu\n"
                                 "Input the operation number: ")
                    if answer=="1":
                        highlight()
                    elif answer=="2":
                        show_patients()
                    elif answer=="0":
                        clean()
                        break
                    else:
                        incorrect_input()
            elif answer=="3":
                while True:
                    clean()
                    if edit_patient_info():
                        break
            elif answer=="0":
                clean()
                break
            else:
                incorrect_input()
        handle_input(main_menu())
    elif c=="2":
        clean()
        while True:
            clean()
            answer=input("What do you want to do?\n"
                         "1. View all tests\n"
                         "2. Add a new test\n"
                         "3. Edit an existing test\n"
                         "4. Remove a registered test\n"
                         "0. Return to the main menu\n"
                         "Input operation number: ")
            if answer=="1":
                show_tests()
            elif answer=="2":            
                clean()
                while True:
                    if register_test():
                        break
            elif answer=="3":
                while True:
                    if edit_test():
                        break
            elif answer=="4":
                while True:
                    if remove_test():
                        break
            elif answer=="0":
                clean()
                break
            else:
                incorrect_input()
        handle_input(main_menu())
    elif c=="3":
        clean()
        while True:
            answer=input("What do you want to do?\n"
                         "1. Enter results of a test for a patient\n"
                         "2. View test results of a patient and/or send them\n"
                         "0. Return to the main menu\n"
                         "Input the operation number: ")
            if answer=="1":
                while True:
                    if test_patient():
                        break
            elif answer=="2":
                clean()
                while True:
                    answer=input("What do you want to do?\n"
                                 "1. Find a specific test result\n"
                                 "2. View a patient's test result list\n"
                                 "0. Return to the main menu\n"
                                 "Input the operation number: ")
                    if answer=="1":
                        while True:
                            if view_results():
                                break
                    elif answer=="2":
                        while True:
                            if view_patient_results():
                                break
                    elif answer=="0":
                        clean()
                        break
                    else:
                        incorrect_input()
            elif answer=="0":
                clean()
                break
            else:
                incorrect_input()
        save_results()
        handle_input(main_menu())
    else:
        incorrect_input()
        handle_input(main_menu())


#Main


if sys.platform == "win32":
    os.system("")

if not os.path.exists(r'./Database'):
    os.makedirs(r'./Database')

if not os.path.isfile("./Database/Info.py"):
    print("Initializing first time use...")
    sleep(2)
    inf = open("./Database/Info.py", "x")
    while True:
        if enter_company_info():
            break

sys.path.insert(1, './Database')
from Info import *

read_patients_database()
read_tests_database()
read_results_database()

handle_input(main_menu())