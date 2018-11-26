def add_value(key, value):


    with open("example.db", "r") as file:
        for line in file:
            if key + ":" in line:                                           #Проверяем, существует ли уже ключ
                raise "KeyError" ("You can't use the same key many times!") #Если да - вызываем исключение
    with open("example.db", "a") as file:
        file.write(f"{key}:{value}\n")                                      #Если исключение не вызвалось - всё в порядке, добавляем


add_value("name2", "Anton")    #Записываем в файл example.db "name2:Anton"

def modify_value(key, value):  #Позволяет добавить другое значение с уже существующим ключём


    with open("example.db", "a") as file: 
        file.write(f"{key}:{value}\n")


modify_value("name2", "Kenny")   #Теперь файл выглядит следующим образом #name2:Anton
                                                                         #name2:Kenny
def get_value(key):    #Выведет только значение, с последним упоминанием ключа в файле


    with open("example.db", "r") as file:
        for line in file:
            if key + ":" in line:
                result = line                           #Находим последнее упоминание ключа
        return result.split(":")[1].replace("\n", "")   #Выводим значение ключа (ключ:значение)
    
print(get_value("name2"))    #output: "Kenny"
