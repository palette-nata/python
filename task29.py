# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
import xml.etree.ElementTree as ET
from typing import List
import codecs

class Person:
    def __init__(self, id, fio, tel, age, description):
        self.id = id
        self.fio = fio
        self.tel = tel
        self.age = age
        self.description = description

    def to_csv_str(self)->str:
        return self.id + ',' + self.fio + ',' + self.tel + ',' + self.age + ',' + self.description + '\n'

    def to_xml_str(self)->str:
        personStart = "  <person>\n"
        id = f"    <id>{self.id}</id>\n"
        fio = f"    <fio>{self.fio}</fio>\n"
        tel = f"    <tel>{self.tel}</tel>\n"
        age = f"    <age>{self.age}</age>\n"
        description = f"    <description>{self.description}</description>\n"
        personEnd = "  </person>\n"
        s = personStart + id + fio + tel + age + description + personEnd
        return s


def load_from_xml(xml_file)->List[Person]:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    sprav :List[Person] =[]
    for person in root:
        sprav.append(Person(person.find("id").text, person.find("fio").text, person.find("tel").text, person.find("age").text, person.find("description").text ))
    return sprav

def load_from_csv(csv_file)->List[Person]:
    sprav :List[Person] =[]
    with open(csv_file) as f:
        lines = f.readlines()
        for line in lines:
            person_data = line.rstrip().split(',')
            sprav.append(Person(person_data[0],person_data[1],person_data[2],person_data[3],person_data[4]))
    return sprav

def save_to_csv(sprav:List[Person] , file):
    data = ""
    for person in sprav:
        data += person.to_csv_str()
    with open(file, "w") as text_file:
        text_file.write(data)
    print(data)

def save_to_xml(sprav:List[Person] , file):
    data = "<data>\n"
    for person in sprav:
        data += person.to_xml_str()
    data += "</data>"
    with codecs.open(file, "w", "utf-8-sig") as text_file:
        text_file.write(data)

sprav = load_from_xml("ps.xml")
save_to_csv(sprav,"ps.csv")

sprav2 = load_from_csv("ps.csv")
save_to_xml(sprav2,"ps1.xml")

print(f"количество записей {len(sprav)}")