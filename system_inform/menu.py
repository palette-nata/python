import enum

class MenuItems(enum.Enum):
    classes = 1
    students = 2
    print_to_console = 3
    export = 4
    importxml = 5
    exit = 6
    create = 7
    update = 8
    delete = 9
    
class Menu:
    def main_menu(i) -> MenuItems:
        match i:
            case '1':
                return MenuItems.classes
            case '2':
                return MenuItems.students
            case '3':
                return MenuItems.print_to_console
            case '4':
                return MenuItems.export
            case '5':
                return MenuItems.importxml
            case '6':
                return MenuItems.exit

    def Item_menu(i) -> MenuItems:
        match i:
            case '1':
                return MenuItems.print_to_console
            case '2':
                return MenuItems.create
            case '3':
                return MenuItems.update
            case '4':
                return MenuItems.delete
            case '5':
                return MenuItems.exit

