import random, enum
from .items import Item, ItemType

critical_boost = [3, 12, 5, 8, 3, 5, 8, 3, 3, 5]                   # Percentage of boost provided by a [critical] Attack

hit_miss_critical = [0, 1, 2, 0, 0]

"""
0: Normal attack                                       # 60% of chance to deal a normal hit
1: Attack missed                                       # 20% of chance to miss attack
2: [critical] attack                                     # 20% of chance to deal a [critical] dmg
"""

LEVELS_BOARD = [100, 150, 250, 350, 500, 650, 800, 1000, 2500, 4500, 9999]


class MoveTo(enum.Enum):
    North = "North"
    East = "East"
    West = "West"
    South = "South"


class Character(object):
    def __init__(self, name, HP, ATK, DEF, LVL=1):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.LVL = LVL
        self.EXP = 0
        self.position = {
            "North": 0,
            "East": 0,
            "West": 0,
            "South": 0
        }

    def attack(self, Target):
        pass

    def isAlive(self) -> bool:
        return (self.HP > 0)


class Player(Character):
    def __init__(self, name, HP, ATK, DEF, LVL=1):
        super(Player, self).__init__(name="Bob", HP=HP, ATK=ATK, DEF=DEF, LVL=1)
        self.Inventory = []
        self.EXP = 0

    def attack(self, Target: Character):

        if(random.choice(hit_miss_critical) == 2):
            a = Target.HP
            Target.HP = Target.HP - ((1 + (random.choice(critical_boost))/100 )* self.ATK)
            print("You dealed a {0} points [critical] damage to {1}".format(int(a-Target.HP), Target.name))
        elif(random.choice(hit_miss_critical) == 1):
            print("This beast seems malicious, your attack missed!")
            pass
        elif(random.choice(hit_miss_critical) == 0):
            a = Target.HP
            Target.HP = Target.HP - self.ATK + Target.DEF/100
            print("You dealed a {0} points damage to {1}".format(int(a-Target.HP), Target.name))

    def boosted_attack(self, Target: Character, boost_points):
        """A normal attack, but actually deals additional damages due to Item"""
        if(random.choice(hit_miss_critical) == 2):
            Target.HP = Target.HP - ((1 + (random.choice(critical_boost))/100 )* self.ATK) - boost_points
        elif(random.choice(hit_miss_critical) == 1):
            # Attack Missed
            pass
        elif(random.choice(hit_miss_critical) == 0):
            Target.HP = Target.HP - self.ATK + Target.DEF - boost_points

    def Move(self, direction: MoveTo):
        if direction.value == "North":
            self.position["North"] += 1

        elif direction.value == "South":
            self.position["South"] += 1

        elif direction.value == "East":
            self.position["East"] += 1

        elif direction.value == "West":
            self.position["West"] += 1

    def add2Inventory(self, item: Item):
        self.Inventory.append(item)

    def useItem(self, item: Item, Target: Character =None):
        # Apply Item effects
        if item.Type == ItemType.attack_boost:
            self.boosted_attack(Target, item.boost_points)
            print("You used {} that provides you +{} ATK boost points".format(item.name, item.boost_points))
        elif item.Type == ItemType.defense_boost:
            self.DEF += item.boost_points  # Define an in-Combat Context , do not apply boost to self
            print("You used {} that provides you +{} DEF boost points".format(item.name, item.boost_points))
        elif item.Type == ItemType.healing_potion:
            self.HP += item.boost_points
            print("You used {} that provides you +{} HP points".format(item.name, item.boost_points))

        # then remove from inventory
        self.Inventory.remove(item)

    def raise_EXP(self, B: Character):
        """il doit tuer 10 bêtes de lvl équiv. avant de level up
           il faut appeler cette méthode à chaque fois qu'il Tue la beast
        """
        self.EXP += B.LVL

        if 0 < self.EXP < LEVELS_BOARD[0]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.39
            self.ATK = self.ATK*1.45
        elif LEVELS_BOARD[0] <= self.EXP < LEVELS_BOARD[1]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.4
            self.ATK = self.ATK*1.53
        elif LEVELS_BOARD[1] <= self.EXP < LEVELS_BOARD[2]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.53
            self.ATK = self.ATK*1.535
        elif LEVELS_BOARD[2] <= self.EXP < LEVELS_BOARD[3]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.4
            self.ATK = self.ATK*1.45
        elif LEVELS_BOARD[3] <= self.EXP < LEVELS_BOARD[4]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.539
            self.ATK = self.ATK*1.53
        elif LEVELS_BOARD[4] <= self.EXP < LEVELS_BOARD[5]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.4
            self.ATK = self.ATK*1.59
        elif LEVELS_BOARD[5] <= self.EXP < LEVELS_BOARD[6]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.4
            self.ATK = self.ATK*1.59
        elif LEVELS_BOARD[6] <= self.EXP < LEVELS_BOARD[7]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.6
            self.ATK = self.ATK*1.76
        elif LEVELS_BOARD[7] <= self.EXP < LEVELS_BOARD[8]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.6
            self.ATK = self.ATK*1.6
        elif LEVELS_BOARD[8] <= self.EXP < LEVELS_BOARD[9]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.4
            self.ATK = self.ATK*1.26
        elif LEVELS_BOARD[9] <= self.EXP <= LEVELS_BOARD[10]:
            self.HP = self.HP *1.5
            self.DEF = self.DEF * 1.63
            self.ATK = self.ATK*1.45
        elif self.EXP > LEVELS_BOARD[10] + 1:
            self.LVL = "WarLock"
            self.HP = self.HP *1.84
            self.DEF = self.DEF * 1.56
            self.ATK = self.ATK*1.89


    def level_watcher(self):
        if 0 < self.EXP < LEVELS_BOARD[0]:
            self.LVL = 1
        elif LEVELS_BOARD[0] <= self.EXP < LEVELS_BOARD[1]:
            self.LVL = 2
        elif LEVELS_BOARD[1] <= self.EXP < LEVELS_BOARD[2]:
            self.LVL = 3
        elif LEVELS_BOARD[2] <= self.EXP < LEVELS_BOARD[3]:
            self.LVL = 4
        elif LEVELS_BOARD[3] <= self.EXP < LEVELS_BOARD[4]:
            self.LVL = 5
        elif LEVELS_BOARD[4] <= self.EXP < LEVELS_BOARD[5]:
            self.LVL = 6
        elif LEVELS_BOARD[5] <= self.EXP < LEVELS_BOARD[6]:
            self.LVL = 7
        elif LEVELS_BOARD[6] <= self.EXP < LEVELS_BOARD[7]:
            self.LVL = 8
        elif LEVELS_BOARD[7] <= self.EXP < LEVELS_BOARD[8]:
            self.LVL = 9
        elif LEVELS_BOARD[8] <= self.EXP < LEVELS_BOARD[9]:
            self.LVL = 10
        elif LEVELS_BOARD[9] <= self.EXP <= LEVELS_BOARD[10]:
            self.LVL = 11
        elif self.EXP > LEVELS_BOARD[10] + 1:
            self.LVL = "WarLock"

        return self.LVL

    def get_level(self):
        return self.level_watcher()

class Beast(Character):
    def __init__(self, name, HP, ATK, DEF, LVL=1):
        super(Beast, self).__init__(name=name,HP=HP, ATK=ATK, DEF=DEF, LVL=LVL)

    def attack(self, Target: Player):  # Beast Target is a player
        if(random.choice(hit_miss_critical) == 2):
            a = Target.HP
            Target.HP = Target.HP - ((1 + (random.choice(critical_boost))/100 )* self.ATK)
            print("{0} dealed a {1} points [critical] damage to you".format(self.name, int(a-Target.HP)))
        elif(random.choice(hit_miss_critical) == 1):
            print("Your senses were keen, {0} missed it attack".format(self.name))
        elif(random.choice(hit_miss_critical) == 0):
            a = Target.HP
            Target.HP = Target.HP - self.ATK + Target.DEF/100
            print("{0} dealed a {1} points damage to you".format(self.name, int(a-Target.HP)))
