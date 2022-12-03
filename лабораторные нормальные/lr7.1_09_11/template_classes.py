from msilib.schema import Class
import pickle
from typing import NamedTuple    
from collections import namedtuple
from typing import TypeVar, Generic, List

class Otdelbl(): #Класс - отдел с переменными, Класс "Отделы" с переменными: название отдела, этаж, телефон, начальник отдела.
    def __init__(self, nazv_otd, floor, phone, nath_otd):
        self.nazv_otd = nazv_otd
        self.floor = floor
        self.phone = phone
        self.nath_otd = nath_otd


    def Nachalinik(self):
        print(f"Начальник данного отдела - {self.nath_otd}")

    #Деструктор
    #def __del__(self): #Уничтожение экземпляра
        #print(f"На этаж с названием отделом {self.nazv_otd} влетела ракета Калибр")

#Сериализация
    def serialize(self): # Сериализация модели телефона
        with open('D:\\Code_all\\MDK_0101\\лабораторные нормальные\\lr4_12_10\\cock.pkl', 'wb') as f:
            pickle.dump(self.phone, f)
        f.closed

#Десериализация
    def deserialize(self): #Десериализация модели телефона
        with open('D:\\Code_all\\MDK_0101\\лабораторные нормальные\\lr4_12_10\\cock.pkl', 'rb') as f:
            cock = pickle.load(f)
        f.closed
        print (cock)

class Sotrydniki(): #Класс "Сотрудники" с переменными: название отдела, этаж, телефон, начальник отдела.
    def __init__(self, FIO, doljnost, nomer_otdela, pol_M_or_J, adress, date_birth):
        self.FIO = FIO
        self.doljnost = doljnost #Допустимые должности: (конструкторы,инженеры, техники, лаборанты, 
                                 #прочий обслуживающий персонал)
        self.nomer_otdela = nomer_otdela
        self.pol_M_or_J = pol_M_or_J
        self.adress = adress
        self.date_birth = date_birth 
        
    def Nama(self):
        return self.FIO

class Organizatsia(): #Класс "Организация" с переменными: название организации, тип деятельности, страна, город, адрес, ФИО директора.
    def __init__(self, nazvanie_org, type_deyatelnosti, country, city, adres, FIO_directora):
        self.nazvanie_org = nazvanie_org
        self.type_deyatelnosti = type_deyatelnosti
        self.country = country
        self.city = city
        self.adres = adres
        self.FIO_directora = FIO_directora
    def Name(self):
        print(f'Тип деятельности:{self.type_deyatelnosti}')

class Dogovor(): #Класс "Договор" с переменными: номер договора, дата заключения договора, организация, стоимость договора.
    def __init__(self, nomer_dogovora, data_zakl, organizatsia, stoimost_dogovora):
        self.nomer_dogovora = nomer_dogovora
        self.data_zakl = data_zakl
        self.organizatsia = organizatsia
        self.stoimost_dogovora = stoimost_dogovora

#Начало обобщённого класса

T = TypeVar('T')
class Add_Documentologist(Generic[T]):
    """Класс для составителей договоров. Переменная: список с типом данных T"""
    def __init__(self) -> None:
    # Создание пустого списка с объетами типа T
        self.items: List[T] = []

    #Вывод выбора читательного зала
    def __call__(self, nm):
        print(f'Заполнение списка документоведов в организации - {nm.organizatsia}')

    # Ввод в stack
    def push(self, item: T) -> None:
        self.items.append(item)
    # Метод для удаления объекта по индексу
    def pop(self, x) -> T:
        return self.items.pop(x)
    # Пустой или с чем-то(true/false)
    def empty(self) -> bool:
        print(not self.items)
    #Вывод информации о введенном в stack
    def info(self) -> None:
        print(self.items)
#Конец обобщённого класса



# Начало namedtuple
Journale = namedtuple('Journale', 'name pages type')
Jour1 = Journale(name="Forbes", pages=210, type="Economic")
Jour2 = Journale(name="Economic analysis", pages=160, type="Finance")
Jour3 = Journale(name="Funny pictures", pages=80, type="Funny")
Jour4 = Journale(name="Culinary magazine Gastronomy", pages=55, type="Food")
print(Jour1.name, Jour2, Jour3.pages, Jour4, sep='\n')
#Конец namedtuple


#Применение кортежей для реализации структуры
    #Данный кортеж приписан к классу <<Журнал>>
#class Journal(NamedTuple):
    # """Класс "журнал" с переменными: номер журнала, номер страницы, номер строки, номер ячейки в журнале"""
    # number_journal: int
     #number_page: int
    # number_lines: int
     #number_cell: int


#def Get_Journal() -> Journal:
     #return 'Журнал'

#def Get_Journal() -> Journal:
     #return 

    #Окончание примения кортежа длля реализации структуры

class Proekt_rab(): #Класс "Проектная работа" с переменными: дата начала проектной работы, дата завершения проектной работы, номер договора, отдел, осуществляющий разработку.
    def __init__(self, data_nachala_rabot, data_zaversheniya_rabot, nomer_dogovor, otdel_razrabotki):
        self.data_nachala_rabot = data_nachala_rabot
        self.data_zaversheniya_rabot = data_zaversheniya_rabot
        self.nomer_dogovor = nomer_dogovor
        self.otdel_razrabotki = otdel_razrabotki

#Наследование
 
class Budget(Organizatsia):
    def __init__(self,nazvanie_org,type_deyatelnosti,country,city,adres,FIO_directora,size): 
        super().__init__(nazvanie_org,type_deyatelnosti,country,city,adres,FIO_directora)
        self.size = size
    def Name(self):  
        print(f'Название организации:{self.nazvanie_org}')

    

#Экземпляры

o1 = Otdelbl("Calibr",4,"Redmi","Зимин Виктор Анатольевич")
o2 = Otdelbl("Bread", 1, "Xiaomi", "Лесовой Василий Батькович")
r1 = Organizatsia("Хлебопекарня","Повар","Россия","Новодвинск","Мира 13","Шарипов Никита Олегович")
#r1.Name()
r1 = Budget(r1.nazvanie_org,r1.type_deyatelnosti,r1.country,r1.city,r1.adres,r1.FIO_directora,5)
s1 = Sotrydniki("Зимин Данила Викторович","Лаборант", 2 ,"М","Пушкина 25", "07.07.2002")
d1 = Dogovor("90080706","17.12.2003",r1.nazvanie_org,25000)
#print(s1.Nama())
#o1.Nachalinik()
#o2.Nachalinik()
#del o1

#o2.serialize()
#o2.deserialize()

#Полиморфизм
#r1.Name()

#Использование обобщённого класса
stack = Add_Documentologist[str]()
stack(d1)
stack.push("Данила")
stack.push(7)
stack.empty()
stack.push("Филипп")
stack.push("Никита")
stack.pop(1)
stack.info()
#Окончание использования обобщённого класса    


#Использование кортежей
#Journal1 = Journal(57, 98, 480, 1500)
#Journal2 = Journal(12, 300, 740, 3424)
#print(f"Расположение ячейки:", Journal1)
#print(f"Журнал:", Journal1.number_journal)
#print(f"Страница:", Journal1.number_page) 
#print(f"Строка:", Journal1.number_lines) 
#print(f"Ячейка:", Journal1.number_cell) 
#print(f"Расположение ячейки:", Journal2)

#Окончание использования кортежей


