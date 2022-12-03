from msilib.schema import Class
import pickle
from typing import NamedTuple    


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

#Применение кортежей для реализации структуры
    #Данный кортеж приписан к классу <<Журнал>>
class Journal(NamedTuple):
     """Класс "журнал" с переменными: номер журнала, номер страницы, номер строки, номер ячейки в журнале"""
     number_journal: int
     number_page: int
     number_lines: int
     number_cell: int


def Get_Journal() -> Journal:
     return 'Журнал'

def Get_Journal() -> Journal:
     return 

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
#print(s1.Nama())
#o1.Nachalinik()
#o2.Nachalinik()
#del o1

#o2.serialize()
#o2.deserialize()

#Полиморфизм
#r1.Name()

    


#Использование кортежей
Journal1 = Journal(57, 98, 480, 1500)
Journal2 = Journal(12, 300, 740, 3424)
print(f"Расположение ячейки:", Journal1)
print(f"Журнал:", Journal1.number_journal)
print(f"Страница:", Journal1.number_page) 
print(f"Строка:", Journal1.number_lines) 
print(f"Ячейка:", Journal1.number_cell) 
print(f"Расположение ячейки:", Journal2)

#Окончание использования кортежей

