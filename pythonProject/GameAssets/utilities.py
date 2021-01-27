from .characters import Player, Beast, MoveTo
from .items import Item, ItemType
from .inGameAssets import beasts_list
import random

def help():
    print("Welcome to Game! ")
    print("T U T O R I A L")
    print("-- Chosing a menu item -- ")
    print("1: Create new game --> Create a new game")
    print("2: Load Game --> Load saved game")
    print("3: About --> Print this message")
    print("4: Exit --> Exit Game")
    print(" A Bad choice results in exiting the game")

def get_player_stats(P: Player):
    print("[S T A T S]")
    stats = str.format("Name: {0} \nLVL: {1} \nHP: {2} \nATK: {3} \nDEF: {4} \nEXP:{5} \nPostion: \n    North: {6} \n    South: {7} \n    East: {8} \n    West: {9} ",
               P.name, P.get_level(),P.HP,
               P.ATK, P.DEF, P.EXP,
               P.position["North"],P.position["South"],P.position["East"],P.position["West"],
               )

    print(stats)

def get_beast_stats(P: Beast):
    stats = str.format("Name: {0} \nLVL: {1} \nHP: {2} \nATK: {3} \nDEF: {4}",
               P.name,P.LVL, P.HP,
               P.ATK, P.DEF
               )

    print(stats)

def prompt_to_move(p: Player):
    print("You may enter: n | North, s | South, w | West or e | East to navigate onto the map")
    i = str(input("Move(n-e-w-s) -> ")).lower()
    if i == "n" or i == "north":
        p.Move(MoveTo.North)
        print("You moved further more into the North")
    elif i == "e" or i == "east":
        p.Move(MoveTo.East)
        print("... your warrior instinct seeking for beasts to defeat, uou then moved into East")
    elif i == "w" or i == "west":
        p.Move(MoveTo.West)
        print("Moved toward West; may be the good way")
    elif i == "s" or i == "south":
        p.Move(MoveTo.South)
        print("Moving to South")
    else:
        direction = random.choice([MoveTo.South, MoveTo.West, MoveTo.East, MoveTo.North])
        p.Move(direction=direction)

    return p.position["North"] + p.position["South"] + p.position["East"] + p.position["West"]

def get_possible_beast(p: Player):
    PB = []
    for i in range(len(beasts_list)):
        if p.LVL < beasts_list[i]["level"] < (10 * p.LVL) + 1:
            B = Beast(name=beasts_list[i]["name"], HP=beasts_list[i]["level"]*15, LVL=beasts_list[i]["level"], ATK=(p.ATK+25), DEF=int(p.DEF/1.3))

            PB.append(B)
    return PB

def prompt_to_attack(p: Player, B: Beast):
    i = str(input("([Attaquer] = 1 ou [Utiliser Item] = 2 ) -> "))
    if i.lower() == "1":
        p.attack(B)
    elif i.lower() == "2":
        if len(p.Inventory) == 0:
            print("You have no Item yet")
        else:
            print('**[Choisissez un Item]**')
            switch = 1
            Li = []
            for item in p.Inventory:
                print(str.format("{0}: nom: {1} \nboost: +{2}% {3} \n",switch, item.name, item.boost_points, item.Type.name.split('_')[0]))
                Li.append(switch)
                switch += 1
            entree = str(input("votre choix(1-{0})> ".format(switch-1)))
            for inp in Li:
                if str(inp) == entree:
                    It = p.Inventory[int(inp)-1]
                    p.useItem(It)
                    break
    else:
        p.attack(B)
