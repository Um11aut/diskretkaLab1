def first13():
    name = input()
    surname = input()
    phone = input()

    if len(phone) != 0:
        try:
            int(phone) # phone number can be converted to int
        except:
            return "Неправильний номер телефону, введіть цифри"
    
    if len(name) == 0:
        name = "false"
    if len(surname) == 0:
        surname = "false"
    if len(phone) == 0:
        phone = "false"
    print(name, surname, phone)

    if name != "false" and surname != "false" and phone != "false":
        return "Спасибі"
    else:
        return "Не залишайте жодні поля порожніми"

def second13():
    name = input()
    surname = input()
    phone = input()

    if len(phone) != 0:
        try:
            int(phone) # phone number can be converted to int
        except:
            return "Неправильний номер телефону, введіть цифри"
        
    if len(name) == 0:
        name = "false"
    if len(surname) == 0:
        surname = "false"
    if len(phone) == 0:
        phone = "false"
    print(name, surname, phone)

    if name != "false" or surname != "false" or phone != "false":
        return "Спасибі"
    else:
        return "Не залишайте всі поля порожніми"

def third13():
    name = input()
    surname = input()
    phone = input()

    
    if len(name) == 0:
        name = "false"
    if len(surname) == 0:
        surname = "false"
    if len(phone) == 0:
        phone = "false"
    print(name, surname, phone)
    
    if name != "false" or surname != "false":
        return "Спасибі"
    else:
        return "Не залишайте всі поля порожніми"
    
