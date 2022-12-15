import sqlite3

con = sqlite3.connect("D:\Code_all\MDK_0101\лабораторные нормальные\lr28_12_12\database.db")
con.execute("PRAGMA foreign_keys = 1")

cursor = con.cursor()

def create_table_departments() -> None:
    """Таблица, хранящая название отдела,этаж,телефон,начальник отдела"""
    req = """
    CREATE TABLE IF NOT EXISTS Departments(
    name_department TEXT PRIMARY KEY,
    floor INT,
    number_phone TEXT,
    head_of_department TEXT)"""
    cursor.execute(req)

    departments_input = [("Свежий Хлеб", 1, "+7-(931)-587-32-21", "Шариков Н.О"), 
                        ("Пятёрочка", 2, "+7-(818)-734-77-77","Зимин Д.В")]
    cursor.executemany("INSERT INTO Departments (name_department, floor, number_phone,head_of_department) VALUES (?, ?, ?, ?)", departments_input)
    con.commit()
    

    
cursor.execute("INSERT INTO Departments (name_department, floor, number_phone,head_of_department) VALUES ('Магнит', 3,'+7-(911)-555-35-35','Овечкин О.О')")
con.commit()

        
cursor.execute("UPDATE Departments SET name_department='Fix Price' WHERE name_department='Магнит'")
con.commit()

        
cursor.execute("DELETE FROM Departments WHERE name_department=?", ('Fix Price',))
con.commit()


def create_table_staff() -> None:
    """Таблица, хранящая фамилию, имя, отчество должность, 
    название отдела, пол, адрес, дата рождения"""
    req ="""
    CREATE TABLE IF NOT EXISTS Staff(
    FIO TEXT, 
    post TEXT,
    name_departments TEXT,
    gender TEXT,
    adress TEXT,
    date_of_birth TEXT,
    FOREIGN KEY (name_departments) REFERENCES Departments (name_department))"""
    cursor.execute(req)
    staff_input = [("Орлов Роман Тимофеевич", "Менеджер", "Свежий Хлеб", "M", "Мира 13", "20.12.2000"), 
            ("Потапов Тихон Степанович", "Продавец", "Пятёрочка", "M", "Воронина 32/2", "17.12.2003",)]
    cursor.executemany("INSERT INTO Staff (FIO, post, name_departments, gender, adress, date_of_birth) VALUES (?, ?, ?, ?, ?, ?)",staff_input)
    con.commit()


def create_table_organization() -> None:
    """Таблица, хранящая фамилию, имя, отчество директора, 
    название организации, тип деятельности,страна, город, адрес"""
    req ="""
    CREATE TABLE IF NOT EXISTS Organization(
    FIO_directora TEXT,
    name_of_the_organization TEXT PRIMARY KEY, 
    type_of_activity TEXT,
    country TEXT,
    city TEXT,
    adress TEXT)"""
    cursor.execute(req)

    organization_input = [("Леонов Макар Фёдорович", "ЦУМ", "Торговля", "Россия", "Москва","Приморский 25"), 
                    ("Долгов Сергей Степанович", "ТЦ Макси", "Торговля", "Россия", "Псков", "Макаренко 10")]
    cursor.executemany("INSERT INTO Organization (FIO_directora, name_of_the_organization, type_of_activity,country, city, adress) VALUES (?, ?, ?, ?, ?, ?)", organization_input)
    con.commit()

def create_table_dogovor() -> None:
    """Таблица, хранящая номер договора, дата заключения, 
    организация, стоимость договора"""
    req ="""
    CREATE TABLE IF NOT EXISTS Dogovor(
    number_dogovor TEXT PRIMARY KEY,
    date_of_conclusion TEXT, 
    organization TEXT,
    the_cost_of_the_contract TEXT,
    FOREIGN KEY (organization) REFERENCES Organization (name_of_the_organization))"""
    cursor.execute(req)

    dogovor_input = [("1", "18.02.2013", "ЦУМ", "500.000$"), 
                    ("2", "19.03.1999", "ТЦ Макси", "2.000.000$")]
    cursor.executemany("INSERT INTO Dogovor (number_dogovor, date_of_conclusion, organization, the_cost_of_the_contract) VALUES (?, ?, ?, ?)", dogovor_input)
    con.commit()

def create_table_project_work() -> None:
    """Таблица, хранящая дату начала, дату завершения, номер договора, отдел - осуществляющий разработку"""
    req ="""
    CREATE TABLE IF NOT EXISTS Project_Work (
    start_date TEXT,
    completion_date TEXT, 
    number_contract TEXT,
    department_responsible_for_development TEXT,
    FOREIGN KEY (number_contract) REFERENCES Dogovor (number_dogovor),
    FOREIGN KEY (department_responsible_for_development) REFERENCES Departments(name_department))"""
    cursor.execute(req)
    
    project_work_input = [("16.02.2010", "19.05.2015", "1", "Свежий Хлеб"), 
                          ("12.01.2009", "15.12.2020", "2", "Пятёрочка")]
    cursor.executemany("INSERT INTO  Project_work (start_date, completion_date,  number_contract, department_responsible_for_development) VALUES (?, ?, ?, ?)", project_work_input)
    con.commit()


create_table_departments()
create_table_staff()
create_table_organization()
create_table_dogovor()
create_table_project_work()
