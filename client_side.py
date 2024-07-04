import requests
import json
from pprint import pprint


def add_visual_separator():
    print()
    print('--------------------------------------------------------')
    print('♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ')
    print()

def display_classes():
    result = requests.get('http://localhost:5000/classes')
    # returning the data receive from the api
    return result.json()

def regist_to_class(class_id):
    requests.put(f'http://localhost:5000/classes/{class_id}')


def add_new_student(name, surname, email, phone, disability_req):
    student = {
        'first_name': name,
        'last_name':surname
        , 'email_address': email,
        'phone_number': phone,
        'disability_requirements': disability_req
    }
    response = requests.put(
        'http://localhost:5000/students',
        headers={'content-type':'application/json'},
        data=json.dumps(student)
    )

    return student


def run():
    print()
    print('♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ')
    print()
    print('Hi there! Welcome to CFG Drums!')
    add_visual_separator()
    input("Press enter to start:")
    add_visual_separator()
    start_choice = input('If you are an existing student and want to register for one of our drum classes, welcome back! Please type 1 and press enter\nIf you want to register as a student, welcome to our school! Please type 2 and press enter. ')
    add_visual_separator()

    if start_choice != '1' and start_choice != '2':
         print('\n Invalid option. Please re-run the program and select a valid option!')

    elif start_choice == '1':
        classes = display_classes()
        for c in classes:
            pprint(c)

        add_visual_separator()

        class_choice = input('Please enter the class number of the class you wish to register for: ')
        regist_to_class(class_choice)
        print(f"Yay! You have been registered to class number{class_choice}! We look forward to playing some drums with you!")
        add_visual_separator()
        print('Take a look at the updated available classes:\n')
        pprint(display_classes())

    elif start_choice == '2':
        name = input('Please enter your name: ')
        surname = input('Please enter your surname: ')
        email = input('Please enter your email address: ')
        phone = input('Please enter your phone number: ')
        disability_req = input('Do you have any disability requirements? If so, feel free to type your request, otherwise type NULL and press enter: ')

        new_stud = add_new_student(name, surname, email, phone, disability_req)
        print()
        print('------------------------')
        print()
        pprint(f'Registration completed for student:{new_stud}')
        print()
        print('------------------------')
        print()
        print(f'Welcome on board {name}! \nYou are officially a CFG Drummer, we look forward to playing some drums together')
        print()

    print('############################')
    print('♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ')
    print()
    print()
    print('See you soon!')
    print()
    print()
    print('♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ')
    print('############################')



if __name__ == '__main__':
        run()