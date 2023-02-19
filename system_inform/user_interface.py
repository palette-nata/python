from import_data import *
from menu import *

#import ui_enum

def main_menu():
    choose = 0
    while choose != MenuItems.exit:
        clear_screen()        
        print('''Добро пожаловать в справочник школы! 
                    Выберите действие:  
                    1. Работа с классами
                    2. Работа с учениками
                    3. Вывести справочник в консоль
                    4. Экспорт справочника
                    5. Импорт справочника 
                    6. Выход''')
        choose = Menu.main_menu(input("Введите цифру выбора: "))
        match choose:
            case MenuItems.classes:
                classes_menu()
            case MenuItems.students:
                students_menu()
            case MenuItems.print_to_console:
                print_students()
            case MenuItems.export:
                save_to_xml()
            case MenuItems.importxml:
                load_from_xml()

def classes_menu():
    choose = 0
    while choose != MenuItems.exit:
        clear_screen()
        print('''Выберите действие для классов:
                    1. Вывести список на экран
                    2. Добавить
                    4. Удалить классы без студентов
                    5. Выход в главное меню''')
        choose = Menu.Item_menu(input("Введите цифру выбора: "))
        match choose:
            case MenuItems.print_to_console:
                print_classes()
            case MenuItems.create:
                create_class()
            case MenuItems.delete:
                delete_empty_classes()


def students_menu():
    choose = 0
    while choose != MenuItems.exit:
        clear_screen()
        print('''Выберите действие для студентов:
                    1. Вывести список на экран
                    2. Добавить
                    3. Редактировать
                    4. Удалить
                    5. Выход в главное меню''')
        choose = Menu.Item_menu(input("Введите цифру выбора: "))
        match choose:
            case MenuItems.print_to_console:
                print_students()
            case MenuItems.create:
                create_student()
            case MenuItems.update:
                update_student()
            case MenuItems.delete:
                delete_student()
