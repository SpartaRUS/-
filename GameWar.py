import random

def team_selection():
    selection = 0
    while selection != 1 or selection != 2:
        selection = int(input("За какую команду вы будете играть? Нежить или Жить? Напишите 1 или 2, для выбора:"))
        if selection == 1:
            return selection
        elif selection == 2:
            return selection
        else:
            print("Неверное число!")

def army_unded():
    global Skeleton
    global Zombie
    global Ghosts
    global Vampires
    global Lychee
    global Banshee
    global Bone_Dragon
    Skeleton = {'name':'Скелеты','hp': random.randint(2,5),'Attack' : random.randint(1,2) , 'Defense' : random.randint(1,2) , 'Damage': random.randint(1,2) }
    Zombie = {'name':'Зомби','hp': random.randint(3,10),'Attack' : random.randint(3,5) , 'Defense' : random.randint(3,5) , 'Damage': random.randint(2,4) }
    Ghosts = {'name':'Призраки','hp': random.randint(5,15),'Attack' : random.randint(5,8) , 'Defense' : random.randint(5,8) , 'Damage': random.randint(4,6) }
    Vampires = {'name':'Вампиры','hp': random.randint(20,40),'Attack' : random.randint(10,14) , 'Defense' : random.randint(10,14) , 'Damage': random.randint(6,8) }
    Lychee = {'name':'Личи','hp': random.randint(40,80),'Attack' : random.randint(15,20) , 'Defense' : random.randint(15,20) , 'Damage': random.randint(12,16) }
    Banshee = {'name':'Баньши','hp': random.randint(80,120),'Attack' : random.randint(20,26) , 'Defense' : random.randint(20,26) , 'Damage': random.randint(16,20) }
    Bone_Dragon = {'name':'Костяные драконы','hp': random.randint(100,150),'Attack' : random.randint(25,32) , 'Defense' : random.randint(25,32) , 'Damage': random.randint(20,24)}
    global undead_unit
    undead_unit = Skeleton 
def print_unded():
    print("Армия нежити. Подробные характеристики войска.")
    print (Skeleton)
    print (Zombie)
    print (Ghosts)
    print (Vampires)
    print (Lychee)
    print (Banshee)
    print (Bone_Dragon)

def Live():
    global Peasants
    global Archers
    global swordsmen
    global Griffins
    global monks
    global knights
    global angels
    Peasants = {'name':'Крестьяне','hp': random.randint(2,5),'Attack' : random.randint(1,2) , 'Defense' : random.randint(1,2) , 'Damage': random.randint(1,2) }
    Archers = {'name':'Лучники','hp': random.randint(3,10),'Attack' : random.randint(3,5) , 'Defense' : random.randint(3,5) , 'Damage': random.randint(2,4) }
    swordsmen = {'name':'Меченосцы','hp': random.randint(5,15),'Attack' : random.randint(5,8) , 'Defense' : random.randint(5,8) , 'Damage': random.randint(4,6) }
    Griffins = {'name':'Грифоны','hp': random.randint(20,40),'Attack' : random.randint(10,14) , 'Defense' : random.randint(10,14) , 'Damage': random.randint(6,8) }
    monks = {'name':'Монахи','hp': random.randint(40,80),'Attack' : random.randint(15,20) , 'Defense' : random.randint(15,20) , 'Damage': random.randint(12,16) }
    knights = {'name':'Рыцари','hp': random.randint(80,120),'Attack' : random.randint(20,26) , 'Defense' : random.randint(20,26) , 'Damage': random.randint(16,20) }
    angels = {'name':'Ангелы','hp': random.randint(100,150),'Attack' : random.randint(25,32) , 'Defense' : random.randint(25,32) , 'Damage': random.randint(20,24) }
    global live_unit 
    live_unit = Peasants

def print_live():
    print("Армия Ордена Порядка. Подробные характеристики войска.")
    print (Peasants)
    print (Archers)
    print (swordsmen)
    print (Griffins)
    print (monks)
    print (knights)
    print (angels)

def Custom_Artifacts():
    User_set = set()
    Examination = set()
    Set = 0
    list_Artifacts_undead = frozenset({"Кольцо некроманта", "Посох преисподней","Амулет некроманта","Плащ смертоносной тени"})
    list_Artifacts_live = frozenset({"Доспехи Забытого Героя","Корона лидерства","Сандалии святых", "Ожерелье победы"})
    Name_Artifacts_undead = ["Кольцо некроманта", "Посох преисподней","Амулет некроманта","Плащ смертоносной тени"]
    Name_Artifacts_live = ["Доспехи Забытого Героя","Корона лидерства","Сандалии святых", "Ожерелье победы"]

    while Set < 4:
        print(" ")
        print("Набор Некроманта",Name_Artifacts_undead)
        print("---------------------------------------------------------------------------------------------------------------")
        print("Набор Святого воина",Name_Artifacts_live)
        print(" ")
        inputUser = int(input("Выберите строку артефактов. Введите 1 или 2:"))
        if inputUser == 1:
            print(Name_Artifacts_undead)
            inputUser = int(input("Выберите номер артефакта. Напишите его:"))
            if inputUser >= 0 and inputUser <= 4:
                Examination.add(Name_Artifacts_undead[inputUser - 1])
                if Examination.issubset(User_set):
                    print("///////////////////////////////////////////////////////////////////")
                    print("У вас уже есть этот предмет")
                    print("///////////////////////////////////////////////////////////////////")
                    zzz = input("Введите любой символ, что бы продолжить:")
                else:
                    User_set.add(Name_Artifacts_undead[inputUser - 1])
        elif inputUser == 2:
            print(Name_Artifacts_live)
            inputUser = int(input("Выберите номер артефакта. Напишите его:"))
            if inputUser >= 0 and inputUser <= 4:
                Examination.add(Name_Artifacts_live[inputUser - 1])
                if Examination.issubset(User_set):
                    print("///////////////////////////////////////////////////////////////////")
                    print("У вас уже есть этот предмет")
                    print("///////////////////////////////////////////////////////////////////")
                    zzz = input("Введите любой символ, что бы продолжить:")
                else:
                    User_set.add(Name_Artifacts_live[inputUser - 1])
        print("Ваш инвентарь:",User_set)
        Examination.clear()
        Set = len(User_set)
        print(Set)


def fight():
    MoveUndead = True
    MoveLive = True
    Move = random.randint(1,2)
    if Move == 1:
        print("Первый ход за нежитью")
    elif Move == 2:
        print("Первый ход за Житью")
    roundF = 0
    Battle = 1
    PlayFight = True
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    print(f"Битва {Battle}")
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
    while PlayFight == True:
        if MoveUndead == True and MoveLive == True:
            roundF += 1
            print("--------------------------------------------------------------------------------------------")
            print(roundF,"Раунд")
            print("--------------------------------------------------------------------------------------------")
            MoveLive = False
            MoveUndead = False
        Army()
        if Move == 1 and undead_unit['hp'] >= 0:
            if live_unit['Defense'] <= undead_unit['Attack']:
                Damage_unded = undead_unit['Damage']*(1+(undead_unit['Attack'] - live_unit['Defense'])*0.05)
            elif live_unit['Defense'] >= undead_unit['Attack']:
                Damage_unded = undead_unit['Damage']/(1+(live_unit['Defense'] - undead_unit['Attack'])*0.05)
            Damage_unded = round(Damage_unded, 0)
            live_unit['hp'] -= Damage_unded 
            print(undead_unit['name'], f"Наносит:{Damage_unded}урона")
            print(live_unit['name'],f"Здоровье:{live_unit['hp']}")
            print(" ")
            Move = 2
            MoveUndead = True
        elif Move == 2 and live_unit['hp'] >= 0:
            if undead_unit['Defense'] <= live_unit['Attack']:
                Damage_live = undead_unit['Damage']*(1+(undead_unit['Attack'] - live_unit['Defense'])*0.05)
            elif undead_unit['Defense'] >= live_unit['Attack']:
                Damage_live = undead_unit['Damage']/(1+(live_unit['Defense'] - undead_unit['Attack'])*0.05)
            Damage_live = round(Damage_live, 0)
            undead_unit['hp'] -= Damage_live
            print(live_unit['name'], f"Наносит:{Damage_live}урона")
            print(undead_unit['name'],f"Здоровье:{undead_unit['hp']}")
            print(" ")
            Move = 1
            MoveLive = True
        if undead_unit == Bone_Dragon and undead_unit['hp'] <= 0:
            PlayFight = False
            if team == 1:
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                print("Вы проиграли...")
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                break
            elif team == 2:
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|||||||||||||||||||||||||||||||///////////////")
                print(" XXXXXXXXXXXXXXXXXXX      Вы выиграли!!!           XXXXXXXXXXXXXX")
                print("////////////////////|||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                break
        if live_unit == angels and live_unit['hp'] <= 0:
            PlayFight = False
            if team == 2:
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                print("Вы проиграли...")
                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                break
            elif team == 1:
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|||||||||||||||||||||||||||||||///////////////")
                print(" XXXXXXXXXXXXXXXXXXX      Вы выиграли!!!           XXXXXXXXXXXXXX")
                print("////////////////////|||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
                print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                break
    
        if undead_unit['hp'] <= 0:
            print(undead_unit['name'], "Потерпел поражение")
            if team == 1:
                Battle += 1
                roundF = 0
                print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
                print(f"Битва {Battle}")
                print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
                 
        if live_unit['hp'] <= 0:
            print(live_unit['name'], "Потерпел поражение")
            if team == 2:
                Battle += 1
                roundF = 0
                print("///////////////////////////////////////////////////////////////////////////////////////////////////////")
                print(f"Битва {Battle}")
                print("///////////////////////////////////////////////////////////////////////////////////////////////////////")

            
def Army():
    global undead_unit
    global live_unit 
    undead_unit = Skeleton 
    live_unit = Peasants
    if undead_unit['hp'] <= 0:
        undead_unit = Zombie
        if undead_unit['hp'] <= 0:
            undead_unit = Ghosts
            if undead_unit['hp'] <= 0:
                undead_unit = Vampires
                if undead_unit['hp'] <= 0:
                    undead_unit = Lychee
                    if undead_unit['hp'] <= 0:
                        undead_unit = Banshee
                        if undead_unit['hp'] <= 0:
                            undead_unit = Bone_Dragon
    if live_unit['hp'] <= 0:
        live_unit = Archers
        if live_unit['hp'] <= 0:
            live_unit = swordsmen
            if live_unit['hp'] <= 0:
                live_unit = Griffins
                if live_unit['hp'] <= 0:
                    live_unit = monks
                    if live_unit['hp'] <= 0:
                        live_unit = knights
                        if live_unit['hp'] <= 0:
                            live_unit = angels

def Main():
    Custom_Artifacts()
    playEnd = True
    while playEnd == True:
        global team
        global roundF
        roundF = 0
        global Battle 
        Battle = 1
        army_unded()
        Live()
        team = team_selection()
        if team == 1:
            print_unded()
        elif team == 2:
            print_live()
        fight()
        endZone = True
        while endZone == True:
            play = str(input("Хотите повторить игру? Напишите Да/Нет:"))
            if play == "Нет" or play == "нет":
                playEnd = False
                endZone = False
            elif play == "Да" or play == "да":
                print("Игра запускается...")
                endZone = False
            else:
                print("Неверный ответ.")
Main()