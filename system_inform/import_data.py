
import os
from pyautogui import typewrite
from collections import namedtuple
from typing import List
import xml.etree.ElementTree as ET
import codecs

Person = namedtuple('Person',['id','firstname','lastname','patronymic','birthdate','phonenumber','address','classnumber'])

all_classes = []
all_students :List[Person] = []
id_student = 1

def delete_empty_classes():
    global all_classes
    for cl in all_classes:
        if [st for st in all_students if st.classnumber==cl].__len__() == 0:
            all_classes.remove(cl)

def create_class(name_class=False):
    clear_screen()
    if not name_class:
        name_class = input("Введите номер класса: ")
        all_classes.append(name_class)
        print('Класс ' + name_class + ' добавлен в справочник.')
        input('нажмите Enter для перехода в меню')
    else:
        all_classes.append(name_class)

def print_classes():
    clear_screen()
    print("-= Классы в справочнике =-")
    for el in all_classes:
        print(el)
    print()
    input('нажмите Enter для перехода в меню')

def print_students(classname = False):
    clear_screen()
    print("-= Список учеников по классам =-")
    for cl in all_classes if classname == False else all_classes[classname]:
        print("\n---------------------- Класс " + cl + " ----------------------")
        for student in [st for st in all_students if st.classnumber==cl]:
            st:Person = student
            print(str(st.id) + ' ' + st.lastname + ' ' + st.firstname + ' ' + st.patronymic + ' ' + st.birthdate + ' ' + st.phonenumber + ' ' + st.address + ' ' + st.classnumber)
    input('\nнажмите Enter для перехода в меню')

def create_student():
    global id_student
    clear_screen()
    print("-= Заведение нового студента =-")
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите номер класса ученика: ")
    pers = Person(id=id_student, firstname=name, lastname=surname,patronymic=otch, birthdate=birth, phonenumber=tel, address=adress, classnumber=class_name)
    global all_classes
    if class_name not in all_classes:
        create_class(class_name)
    global all_students
    all_students.append(pers)
    id_student += 1

def update_student():
    global id_student
    global all_students
    clear_screen()
    print("-= Редактирование записи студента =-")
    student_id = input("Введите id ученика: ")
    students =[st for st in all_students if st[0]==int(student_id)]
    if students.__len__() == 0:
        input("Ученик с данным id отсутствует")
        return
    student:Person = students[0]
    
    print("Введите фамилию ученика:")
    typewrite(student.lastname)
    lastname = input()

    print("Введите имя ученика: ")
    typewrite(student.firstname)
    firstname = input()

    print("Введите отчество ученика: ")
    typewrite(student.patronymic)
    patronymic = input()

    print("Введите дату рождения ученика: ")
    typewrite(student.birthdate)
    birthdate = input()

    print("Введите телефон ученика: ")
    typewrite(student.phonenumber)
    phonenumber = input()

    print("Введите адрес ученика: ")
    typewrite(student.address)
    address = input()

    print("Введите класс ученика: ")
    typewrite(student.classnumber)
    classnumber = input()
    global all_classes
    if classnumber not in all_classes:
        create_class(classnumber)
    
    all_students.remove(student)
    student = Person(id=int(student_id), firstname=firstname, lastname=lastname,patronymic=patronymic, birthdate=birthdate, phonenumber=phonenumber, address=address, classnumber=classnumber)
    all_students.append(student)
    delete_empty_classes()
    print(str(student.id) + ' ' + student.lastname + ' ' + student.firstname + ' ' + student.patronymic + ' ' + student.birthdate + ' ' + student.phonenumber + ' ' + student.address + ' ' + student.classnumber +'\n')
    input('нажмите Enter для перехода в меню')

def delete_student():
    print("-= Удаление студента =-")
    student_id = int(input("Введите id студента."))
    students =[st for st in all_students if st[0]==int(student_id)]
    if students.__len__() == 0:
        input("Ученик с данным id отсутствует")
        return
    student:Person = students[0]
    all_students.remove(student)
    delete_empty_classes()

def to_xml_str(person:Person)->str:
    personStart = "  <person>\n"
    id = f"    <id>{person.id}</id>\n"
    lastname = f"    <lastname>{person.lastname}</lastname>\n"
    firstname = f"    <firstname>{person.firstname}</firstname>\n"
    patronymic = f"    <patronymic>{person.patronymic}</patronymic>\n"
    birthdate = f"    <birthdate>{person.birthdate}</birthdate>\n"
    phonenumber = f"    <phonenumber>{person.phonenumber}</phonenumber>\n"
    address = f"    <address>{person.address}</address>\n"
    classnumber = f"    <classnumber>{person.classnumber}</classnumber>\n"
    personEnd = "  </person>\n"
    s = personStart + id + lastname + firstname + patronymic + birthdate + phonenumber + address + classnumber + personEnd
    return s

def load_from_xml():
    global all_students
    xml_file = input("Укажите путь к файлу для импорта: ")
    all_students.clear()
    tree = ET.parse(xml_file)
    root = tree.getroot()
    global all_classes
    for person in root:
        if person.find("classnumber").text not in all_classes:
            create_class(person.find("classnumber").text)
        all_students.append(Person(id=int(person.find("id").text), firstname=person.find("firstname").text, lastname=person.find("lastname").text,patronymic=person.find("patronymic").text, birthdate=person.find("birthdate").text, phonenumber=person.find("phonenumber").text, address=person.find("address").text, classnumber=person.find("classnumber").text))

def save_to_xml():
    file = input("Укажите путь к файлу для экспорта: ")
    data = "<data>\n"
    for person in all_students:
        data += to_xml_str(person)
    data += "</data>"
    with codecs.open(file, "w", "utf-8-sig") as text_file:
        text_file.write(data)

def clear_screen():
    os.system('clear') if os.name == 'posix' else os.system('cls')
   
