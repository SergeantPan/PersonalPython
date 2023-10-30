import random
import math
import os

Alive = "Choose character"
GameState = 0
PlyXP = 0
PlyLevel = 1
PlyGuard = False
PlyGold = 15
PlyPotions = 1
PlyCharType = "None"
PlyDamageBuff = 0
PlyBuffType = "None"
PlyBuffTurns = 0
PlySpellDamageBuff = 0
PlyDebuffType = "None"
PlyDebuffTurns = 0

UnlockedSpell = "None"

RogueBonus = 0
CaltropHits = 0

ClericManaBonus = 0

CurEnemy = None
CurEnemyHP = 0
TrueEnemyAccuracy = 0
CurEnemyBuffType = "None"
CurEnemyBuffTurns = 0
CurEnemyDebuffType = "None"
CurEnemyDebuffTurns = 0
CurEnemyBonusDMG = 0

EncounterChance = 0
Ambush = False
InCombat = False
WhoseTurn = None

Casting = 0

DistanceToTravel = 50
TurnsToTraverse = 3

#Character sheet = Health, Mana, Damage (min, max), Damage Res, Guard Reduction, Accuracy
while Alive == False:
    if GameState == 0:
        print("\nYou have died!")
        Restart = input("\nRestart game? Y/N ")
        if Restart.casefold() == "y":
            Alive = "Choose Character"
        elif Restart.casefold() == "n":
            print("\nStopping game.")
            break
    elif GameState == 1:
        print("\nVictory! You have reached the castle!")
        Restart = input("\nRestart game? Y/N ")
        if Restart.casefold() == "y":
            Alive = True
            GameState = 0
            Alive = "Choose Character"
        elif Restart.casefold() == "n":
            print("\nStopping game.")
            break

HelpMenu = ""

while Alive == "Choose character":
    print("\nChoose a character:\n- The (K)night\n- The (L)eper\n- The (R)ogue\n- The (C)leric")
    print("\nOr type 'help' for information on the various mechanics and stats.")
    CharChoice = input("\nChoose: ")
    if CharChoice.casefold() == "help":
        HelpMenu = "List"
        while HelpMenu == "List":
            print("(1) - Characters\n(2) - XP and Levels\n(3) - Mana\n(4) - Damage Resistance\n(5) - Guarding and Parrying\n(6) - Accuracy\n(7) - Critical Hits\n(8) - Resting\n(9) - Traveling\n(10) - Ambushes\n(11) - Locations\n(12) - Victory Condition")
            HelpChoice = input("\nChoose: ")
            if HelpChoice == "1":
                HelpMenu = "Characters"
            elif HelpChoice == "2":
                HelpMenu = "Levels"
            elif HelpChoice == "3":
                HelpMenu = "Mana"
            elif HelpChoice == "4":
                HelpMenu = "Damage Resistance"
            elif HelpChoice == "5":
                HelpMenu = "Guard"
            elif HelpChoice == "6":
                HelpMenu = "Accuracy"
            elif HelpChoice == "7":
                HelpMenu = "Crits"
            elif HelpChoice == "8":
                HelpMenu = "Resting"
            elif HelpChoice == "9":
                HelpMenu = "Traveling"
            elif HelpChoice == "10":
                HelpMenu = "Ambush"
            elif HelpChoice == "11":
                HelpMenu = "Locations"
            elif HelpChoice == "12":
                HelpMenu = "Victory"
        while HelpMenu == "Characters":
            print("(1) - The Knight\n(2) - The Leper\n(3) - The Rogue\n(4) - The Cleric")
            print("\nList <- (B)ack - (N)ext Page -> Levels")
            Page1 = input("\nChoose: ")
            if Page1 == "1":
                HelpMenu = "Knight"
            if Page1 == "2":
                HelpMenu = "Leper"
            if Page1 == "3":
                HelpMenu = "Rogue"
            if Page1 == "4":
                HelpMenu = "Cleric"
            if Page1.casefold() == "b":
                HelpMenu = "List"
            if Page1.casefold() == "n":
                HelpMenu = "Levels"
        while HelpMenu == "Knight":
            print("\nThe Knight is a basic character, with passive damage reduction and a strong guard.\nThe Knight is good at taking hits, despite his low chance to parry enemy attacks.\nHis low starting mana means he is less adept at casting spells.\nA good starter character for learning the game.")
            print("\nCharacters <- (B)ack - (N)ext Page -> The Leper")
            Knight = input("\nChoose: ")
            if Knight.casefold() == "b":
                HelpMenu = "Characters"
            elif Knight.casefold() == "n":
                HelpMenu = "Leper"
        while HelpMenu == "Leper":
            print("\nThe Leper is a hard-hitting but inaccuracte character, better at dealing high damage-per-hit.\nThe Leper is not as tanky as the Knight, but has a much easier time dealing with high health enemies, so long as his hits land.\nA Leper is someone who suffers from Leprosy, a term often used in medieval times.\nThe most renowned Leper of medieval times was Baldwin IV of Jerusalem, who ruled Jerusalem in spite of debilitating Leprosy.")
            print("\nThe Knight <- (B)ack - (N)ext Page -> The Rogue")
            Leper = input("\nChoose: ")
            if Leper.casefold() == "b":
                HelpMenu = "Knight"
            elif Leper.casefold() == "n":
                HelpMenu = "Rogue"
        while HelpMenu == "Rogue":
            print("\nThe Rogue is low health but high accuracy character, for a more challenging experience overall.\nThe Rogue has the highest critical hit and parry chance of all characters, and deals additional damage on crits.")
            print("\nThe Leper <- (B)ack - (N)ext Page -> The Cleric")
            Rogue = input("\nChoose: ")
            if Rogue.casefold() == "b":
                HelpMenu = "Leper"
            elif Rogue.casefold() == "n":
                HelpMenu = "Cleric"
        while HelpMenu == "Cleric":
            print("\nThe Cleric is a high HP high Mana character, with a focus on magic and healing.\nThe Cleric has naturally high health and mana, but with reduced damage on regular attacks.")
            print("\nThe Rogue <- (B)ack - (N)ext Page -> XP and Levels")
            Cleric = input("\nChoose: ")
            if Cleric.casefold() == "b":
                HelpMenu = "Rogue"
            elif Cleric.casefold() == "n":
                HelpMenu = "Levels"
        while HelpMenu == "Levels":
            print("\nXP and Levels are a basic mechanic of the game that improve the players stats as they level up.\nThe first level is earned by gaining 20 XP. Every subsequent level requires an additional 5 XP to level up\nEach level up increases Max HP by 2, Max Mana and Damage by 1.\nXP earned from enemies is based on their health, with higher health enemies dropping greater amounts of XP.")
            print("\nThe Cleric <- (B)ack - (N)ext Page -> Mana")
            Levels = input("\nChoose: ")
            if Levels.casefold() == "b":
                HelpMenu = "Cleric"
            elif Levels.casefold() == "n":
                HelpMenu = "Mana"
        while HelpMenu == "Mana":
            print("\nMana is used to cast spells of various kinds.\nAt the start of every turn, one point of mana is recovered, until the player has maximum mana.\nMana will also passively recover while traveling.")
            print("\nXP and Levels <- (B)ack - (N)ext Page -> Damage Resistance")
            Mana = input("\nChoose: ")
            if Mana.casefold() == "b":
                HelpMenu = "Levels"
            elif Mana.casefold() == "n":
                HelpMenu = "Damage Resistance"
        while HelpMenu == "Damage Resistance":
            print("\nDamage Resistance reduces the amount of damage the player takes from each enemy attack.\nDamage Resistance can only be acquired through spells or by acquiring Armor from Chests or the Merchant.")
            print("\nMana <- (B)ack - (N)ext Page -> Guarding and Parrying")
            DamageRes = input("\nChoose: ")
            if DamageRes.casefold() == "b":
                HelpMenu = "Mana"
            elif DamageRes.casefold() == "n":
                HelpMenu = "Guard"
        while HelpMenu == "Guard":
            print("\nGuarding is an ability that allows the player to protect themselves against the next enemy attack.\nWhen the player Guards against an enemy attack that hits, the damage dealt by the enemy is reduced equal to the characters Guard Reduction\nWhile Guarding, the player has a chance to Parry the enemy attack and deal extra damage.\nEach character has their own Parry Chance, with The Rogues being the highest, and The Knights being the lowest.\nParrying an attack means the enemy attack is negated, and the player attacks the enemy instead. This attack deals 1.25x the players damage.")
            print("\nDamage Resistance <- (B)ack - (N)ext Page -> Accuracy")
            Guard = input("\nChoose: ")
            if Guard.casefold() == "b":
                HelpMenu = "Damage Resistance"
            elif Guard.casefold() == "n":
                HelpMenu = "Accuracy"
        while HelpMenu == "Accuracy":
            print("\nAccuracy determines the chances of the player or the enemy hitting their target.\nEvery attack rolls for accuracy, and will either hit or miss depending on the chance.\nEnemies have three different categories of accuracy, with weaker enemies having lower accuracy and vice versa.\nThe player can also use various spells to increase their own accuracy, or reduce the enemys accuracy.")
            print("\nGuarding and Parrying <- (B)ack - (N)ext Page -> Critical Hits")
            Accuracy = input("\nChoose: ")
            if Accuracy.casefold() == "b":
                HelpMenu = "Guard"
            elif Accuracy.casefold() == "n":
                HelpMenu = "Crits"
        while HelpMenu == "Crits":
            print("\nCritical hits trigger randomly when attacking the enemy.\nEach character has their own critical hit chance, which determines the chances of performing a critical hit.\nAny attack that is a critical hit automatically deals double damage, with The Rogue gaining a +2 damage bonus to crits.\nEnemies cannot perform critical hits.")
            print("\nAccuracy <- (B)ack - (N)ext Page -> Resting")
            Crits = input("\nChoose: ")
            if Crits.casefold() == "b":
                HelpMenu = "Accuracy"
            elif Crits.casefold() == "n":
                HelpMenu = "Resting"
        while HelpMenu == "Resting":
            print("\nResting is a mechanic that can be used outside of combat.\nWhen the player rests, they recover 5 HP and 2 Mana.\nThis method of healing is good for characters like the Knight and Rogue, who have very little in the way of healing beyond potions.\nHowever, when Resting there is also a possibility of being ambushed by an enemy.")
            print("\nCritical Hits <- (B)ack - (N)ext Page -> Traveling")
            Rest = input("\nChoose: ")
            if Rest.casefold() == "b":
                HelpMenu = "Crits"
            elif Rest.casefold() == "n":
                HelpMenu = "Traveling"
        while HelpMenu == "Traveling":
            print("\nTraveling is how the player traverses the game and reaches new areas.\nEach time the player travels, they either come across a path or a crossroads\nWhen at a crossroads, the player is given the choice to pick one of two paths.\nEach path has its own set of enemies and chances of encounter.")
            print("\nResting <- (B)ack - (N)ext Page -> Ambushes")
            Traveling = input("\nChoose: ")
            if Traveling.casefold() == "b":
                HelpMenu = "Resting"
            elif Traveling.casefold() == "n":
                HelpMenu = "Ambush"
        while HelpMenu == "Ambush":
            print("\nAmbushes are random enemy attacks that can occur whenever the player rests, or while traveling.\nWhen ambushed, the enemy will automatically attack the player. ")
            print("\nTraveling <- (B)ack - (N)ext Page -> Locations")
            Ambushes = input("\nChoose: ")
            if Ambushes.casefold() == "b":
                HelpMenu = "Traveling"
            elif Ambushes.casefold() == "n":
                HelpMenu = "Locations"
        while HelpMenu == "Locations":
            print("\nThere are multiple locations in the game, each with their own monsters and encounters.\nSome are far more dangerous than others, while some are far more relaxed and simpler.\nUnique encounters include the Merchant Shop and the Village.\nAt the Merchant Shop, the player is given the opportunity to buy equipment that boosts their stats.\nMeanwhile, visiting a Village fully restores the players HP and Mana.\nHowever, neither of these paths count towards the total distance traveled.")
            print("\nAmbushes <- (B)ack - (N)ext Page -> Victory Conditions")
            Location = input("\nChoose: ")
            if Location.casefold() == "b":
                HelpMenu = "Ambush"
            elif Location.casefold() == "n":
                HelpMenu = "Victory"
        while HelpMenu == "Victory":
            print("\nThe basic premise of the game is to reach the Castle, which is 50 paths away. Once the player reaches the Castle, the game is won.")
            print("\nLocations <- (B)ack - (N)ext Page -> Character Selection")
            Victory = input("\nChoose: ")
            if Victory.casefold() == "b":
                HelpMenu = "Locations"
            elif Victory.casefold() == "n":
                break

    if CharChoice.casefold() == "knight" or CharChoice.casefold() == "the knight" or CharChoice.casefold() == "k":
        print("\nThe Knight:\n- Better Protection\n- Stronger Guard\n- Weaker Magic\n- Lower Parry Chance")
        print("\n- 20 Health\n- 3 Mana\n- Damage 3-6\n- Damage Resistance 2\n- Guard Damage Reduction 4\n- Parry Chance 25\n- Accuracy 75\n- Critical Hit Chance 40")
        ChooseKnight = input("Choose Knight? Y/N ")
        if ChooseKnight.casefold() == "y":
            PlyCharType = "Knight"
            PlyStartHPCap = 18
            PlyStartManaCap = 2
            MinDMG = 2
            MaxDMG = 5
            TruePlyAccuracy = 75
            PlyParry = 25
            TruePlyCritChance = 40
            PlyDMGRes = 2
            PlyGuardRes = 2
            PlyPotions = 2
            if os.path.exists("knight_save.txt"):
                Choice = input("Open old save? Y/N ")
                if Choice.casefold() == "y":
                    OpenSave = open("knight_save.txt", "r")
                    PlyHP = int(OpenSave.readline())
                    PlyMana = int(OpenSave.readline())
                    PlyXP = int(OpenSave.readline())
                    PlyLevel = int(OpenSave.readline())
                    PlyGold = int(OpenSave.readline())
                    PlyPotions = int(OpenSave.readline())
                    PlyDamageBuff = int(OpenSave.readline())
                    PlyDMGRes = int(OpenSave.readline())
                    PlyGuardRes = int(OpenSave.readline())
                    DistanceToTravel = int(OpenSave.readline())
                    OpenSave.close()
                    Alive = True
                elif Choice.casefold() == "n":
                    PlyHP = 20
                    PlyMana = 3
                    Alive = True
            else:
                PlyHP = 20
                PlyMana = 3
                Alive = True

    elif CharChoice.casefold() == "leper" or CharChoice.casefold() == "the leper" or CharChoice.casefold() == "l":
        print("\nThe Leper:\n- Stronger Attacks\n- Lower Accuracy")
        print("\n- 20 Health\n- 5 Mana\n- Damage 5-8\n- Damage Resistance 0\n- Guard Damage Reduction 2\n- Parry Chance 40\n- Accuracy 60\n- Critical Hit Chance 45")
        ChooseLeper = input("Choose Leper? Y/N ")
        if ChooseLeper.casefold() == "y":
            PlyCharType = "Leper"
            PlyStartHPCap = 18
            PlyStartManaCap = 4
            MinDMG = 4
            MaxDMG = 7
            PlyParry = 40
            TruePlyAccuracy = 60
            TruePlyCritChance = 45
            PlyDMGRes = 0
            PlyGuardRes = 2
            if os.path.exists("leper_save.txt"):
                Choice = input("Open old save? Y/N ")
                if Choice.casefold() == "y":
                    OpenSave = open("leper_save.txt", "r")
                    PlyHP = int(OpenSave.readline())
                    PlyMana = int(OpenSave.readline())
                    PlyXP = int(OpenSave.readline())
                    PlyLevel = int(OpenSave.readline())
                    PlyGold = int(OpenSave.readline())
                    PlyPotions = int(OpenSave.readline())
                    PlyDamageBuff = int(OpenSave.readline())
                    PlyDMGRes = int(OpenSave.readline())
                    PlyGuardRes = int(OpenSave.readline())
                    DistanceToTravel = int(OpenSave.readline())
                    OpenSave.close()
                    Alive = True
                elif Choice.casefold() == "n":
                    PlyHP = 20
                    PlyMana = 5
                    Alive = True
            else:
                PlyHP = 20
                PlyMana = 5
                Alive = True

    elif CharChoice.casefold() == "rogue" or CharChoice.casefold() == "the rogue" or CharChoice.casefold() == "r":
        print("\nThe Rogue:\n- Stronger Critical Hits\n- Higher Accuracy\n- Extra Parry Chance\n- Less Health\n- Weaker Guard")
        print("\n- 15 Health\n- 5 Mana\n- Damage 3-6\n- Damage Resistance 0\n- Guard Damage Reduction 1\n- Parry Chance 65\n- Accuracy 85\n- Critical hit Chance 60")
        ChooseRogue = input("Choose Rogue? Y/N ")
        if ChooseRogue.casefold() == "y":
            PlyCharType = "Rogue"
            PlyStartHPCap = 13
            PlyStartManaCap = 4
            MinDMG = 2
            MaxDMG = 5
            PlyDMGRes = 0
            PlyGuardRes = 1
            PlyParry = 65
            TruePlyAccuracy = 85
            TruePlyCritChance = 65
            RogueBonus = 1
            if os.path.exists("rogue_save.txt"):
                Choice = input("Open old save? Y/N ")
                if Choice.casefold() == "y":
                    OpenSave = open("rogue_save.txt", "r")
                    PlyHP = int(OpenSave.readline())
                    PlyMana = int(OpenSave.readline())
                    PlyXP = int(OpenSave.readline())
                    PlyLevel = int(OpenSave.readline())
                    PlyGold = int(OpenSave.readline())
                    PlyPotions = int(OpenSave.readline())
                    PlyDamageBuff = int(OpenSave.readline())
                    PlyDMGRes = int(OpenSave.readline())
                    PlyGuardRes = int(OpenSave.readline())
                    DistanceToTravel = int(OpenSave.readline())
                    OpenSave.close()
                    Alive = True
                elif Choice.casefold() == "n":
                    PlyHP = 15
                    PlyMana = 5
                    Alive = True
            else:
                PlyHP = 15
                PlyMana = 5
                Alive = True
    elif CharChoice.casefold() == "cleric" or CharChoice.casefold() == "the cleric" or CharChoice.casefold() == "c":
        print("\nThe Cleric:\n- More Mana\n- More HP\n- Less Damage")
        print("\n- 25 Health\n- 8 Mana\n- Damage 2-4\n- Damage Resistance 0\n- Guard Damage Reduction 2\n- Parry Chance 25\n- Accuracy 70\n- Critical Hit Chance 35")
        ChooseCleric = input("Choose Cleric? Y/N ")
        if ChooseCleric.casefold() == "y":
            PlyCharType = "Cleric"
            PlyStartHPCap = 23
            PlyStartManaCap = 7
            MinDMG = 1
            MaxDMG = 3
            PlyDMGRes = 0
            PlyGuardRes = 2
            PlyParry = 25
            TruePlyAccuracy = 70
            TruePlyCritChance = 35
            PlyPotions = 1
            if os.path.exists("cleric_save.txt"):
                Choice = input("Open old save? Y/N ")
                if Choice.casefold() == "y":
                    OpenSave = open("cleric_save.txt", "r")
                    PlyHP = int(OpenSave.readline())
                    PlyMana = int(OpenSave.readline())
                    PlyXP = int(OpenSave.readline())
                    PlyLevel = int(OpenSave.readline())
                    PlyGold = int(OpenSave.readline())
                    PlyPotions = int(OpenSave.readline())
                    PlyDamageBuff = int(OpenSave.readline())
                    PlyDMGRes = int(OpenSave.readline())
                    PlyGuardRes = int(OpenSave.readline())
                    DistanceToTravel = int(OpenSave.readline())
                    OpenSave.close()
                    Alive = True
                elif Choice.casefold() == "n":
                    PlyHP = 25
                    PlyMana = 8
                    Alive = True
            else:
                PlyHP = 25
                PlyMana = 8
                Alive = True

FirstMerchant = False
ArmorBought = False
SwordBought = False
ShieldBought = False
PotionBought = False

def SaveGame():
    NewSave = open(str(PlyCharType) + "_save.txt", "w")
    NewSave.write(str(PlyHP)+ "\n" + str(PlyMana) + "\n" + str(PlyXP)+ "\n" + str(PlyLevel)+ "\n" + str(PlyGold)+ "\n" + str(PlyPotions)+ "\n" + str(PlyDamageBuff)+ "\n" + str(PlyDMGRes) + "\n" + str(PlyGuardRes)+ "\n" + str(DistanceToTravel))
    NewSave.close
    print("Game Saved!")

QuietForestEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bandit", "Dire Wolf", "Boar", "Fungus", "Bear"]
EvilForestEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bandit", "Corrupted Wolf", "Corrupt Boar", "Evil Fairy", "Corrupted Fungus", "Vampire"]
OpenFieldEnemy = ["Bandit", "Dire Wolf", "Boar", "Dark Knight"]
GraveyardEnemy = ["Zombie", "Skeleton", "Ghost", "Cultist"]
SmallHillEnemy = ["Angry Goat", "Angry Eagle", "Vicious Hawk", "Snake"]
VillageEnemy = ["Raving Madman", "Infected Villager", "Corrupt Priest", "Angry Farmer", "Rotting Cow", "Vicious Hound"]
OpenPathEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bear", "Bandit", "Boar", "Raving Madman", "Dark Knight"]

WeakEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Corrupt Boar", "Evil Fairy", "Zombie", "Snake", "Boar", "Rotting Cow"]
NormalEnemy = ["Bandit", "Dire Wolf", "Fungus", "Corrupted Fungus", "Skeleton", "Ghost", "Cultist", "Angry Goat", "Angry Eagle", "Vicious Hawk", "Raving Madman", "Infected Villager", "Corrupt Priest", "Angry Farmer", "Vicious Hound", "Mimic"]
StrongEnemy = ["Vampire", "Dark Knight"]

UnholyEnemy = ["Zombie", "Skeleton", "Infected Villager", "Corrupt Priest", "Rotting Cow", "Vicious Hound", "Cultist", "Vampire"]
PoisonImmune = ["Green Slime", "Blue Slime", "Red SLime", "Skeleton", "Ghost"]

EnemyQuotes = ["The Slime flutters and croaks at you.", "The Slime emits a rough groaning sound.", "The Slime lurches at you aggressively.", "The Slime attempts to bash you with its gelatinous body",
               '"Hand over the gold and nobody gets hurt!"', '"Its survival of the toughest out here, and I aint about to die!"', '"You picked the wrong path to travel, stranger"', '"I aint scared of no random wanderer like you!"',
               "The wolf growls at you aggressively", "The wolf lunges at you, attempting to bite you", "The wolf flashes its teeth, preparing to attack", "The wolf growls and barks at you",
               "The boar screams and charges at you", "The boar attempts to attack you with its tusks, narrowly missing", "The boar attacks you unprovoked, forcing you to defend yourself", "The boar stands in your path, refusing to move",
               '"The forest is our home! Youre not welcome here!"', "The evil fairy is angered by your presence", "The evil fairy attempts to thwart you with its spells", '"Leave this place human, the forest is ours!"',
               "The large mushroom creature charges you", "The fungus creature attempts to poison you with its spores", "The large mass of fungus blocks your path", "The fungus creature stands tall as it prepares to fight you",
               '"Halt, traveler! You trespass upon the Kings sacred land!"', "The Dark Knight blocks your path, preparing its sword to strike you", "You are unnerved by the Dark Knights piercing gaze", '"You face a soldier of the Nevarian Kingdom! Prepare yourself for battle!"',
               "The zombie groans as it lurches towards you", '"Braaaiiinnsss"', "The zombie shambles and shakes as it rises off of the ground", "The rotting corpse is barely holding itself together",
               "The bones creak and groan as the skeleton assembles itself together", "The restless skeleton draws a sword as it attempts to strike you down", "The undead skeleton emits a shrill cry as it charges towards you", "The skeleton flails aimlessly as it attempts to attack you",
               "A chill runs down your spine as the ghost makes its presence known", "You feel a creeping dread in your soul as you face down the ghost", "The spirit of the dead seeks to attack you", "You are briefly overtaken by shock, as the ghostly apparition appears out of nowhere",
               '"YOU will make a fine sacrifice for the Old Gods!"', '"Who dares disturb the ritual?!"', "The cultist draws a sharp dagger and points their hand at you", "The cultist lets out a maddening scream as they charge towards you",
               'The goat lets out an angry "Baaa!", before charging towards you', "The goat refuses to let you pass, instead preparing its horns to ram you", '"Baaa!"', "The goat has a mad look in its eyes, as it readies itself to attack you",
               "The bird lets out a shriek as it dives down to attack you", "The bird claws at you with its powerful talons in an attempt to wound you", "The bird dives at you several times in an attmept to peck you", "The fierce bird shrieks at you several times",
               "As you step through the grass, you hear a hissing noise", "The snake lunges at you from the grass in an attempt to attack you", "You narrowly avoid the venomous fangs of the deadly snake", "The slithering snake hisses at you, ready to strike",
               '"Get out of our village you freak!"', '"We dont take kindly to strangers around here"', "The mad villager spits in your direction, before preparing their pitchfork to attack you", "The villager screams at you incoherently, swinging at you with wild fervor",
               '"Ahahah, hahahaha, HAHAHAHA!"', "The lunatic screams at you at the top of his lungs", '"THE SPOTS! THE BLOOD! THE VOICES! OH GOD, THE VOICES!"', "The madmans eyes dart around furiously, unable to focus on any one thing",
               "Black fluid flows from various holes on the hounds body", "The hound growls and barks at you aggressively", "The hound is missing various patches of fur, covered in blood and black fluid", "The hound snarls at you, as it attempts to bite you several times",
               '"Begone, you vile demon!"', '"You desecrate concecrated land with your presence, creature!"', '"In the name of God, the Son and the Holy Spirit, I smie thee!"', "The Corrupt Priest throws a small glass container of water at you",
               "The rotting carcass of a cow emits various disturbing noises", "Blood and gore spill out of the open cavities on the rotting cow", '"MooOOO!"', "The cow barely keeps itself upright, as it blocks your way",
               "The vampire bears its fangs at you, ready to strike", "A fluttering bat quickly transforms into a vampire, who hisses at you", "The vampire turns around, dropping the dried out corpse of its most recent victim onto the ground", "A cloaked figure appears before you, but before you can react they are already on the attack",
               "The large bear stands on its hind feet, growling at you", "The large bear aggressively swipes at you with its claws", "The bear charges at you on all fours, as you brace for the attack", "The sound of angry growling catches your attention, as a large bear charges at you",
               "The fake chest opens its maw and attempts to bite your hand off", "The Mimic springs into life, nearly knocking you over", "The Mimic snaps its jaws at you, its sharp teeth gnashing at you", "You are caught off guard by the Mimic, as it takes the opportunity to attack"]
# 1-4 Slime
# 5-8 Bandit
# 9-12 Wolf
# 13-16 Boar
# 17-20 Evil Fairy
# 21-24 Fungus
# 25-28 Dark Knight
# 29-32 Zombie
# 33-36 Skeleton
# 37-40 Ghost
# 41-44 Cultist
# 45-48 Goat
# 49-52 Eagle + Hawk
# 53-56 Snake
# 57-60 Villagers
# 61-64 Raving Lunatic
# 65-68 Hound
# 69-72 Corrupt Priest
# 73-76 Rotting Cow
# 77-80 Vampire
# 81-84 Bear
# 85-88 Mimic

RandPath = ["Quiet Forest", "Evil Forest", "Open Field", "Graveyard", "Small Hill", "Corrupted Village", "Village", "Travelling Merchant", "Open Path"]
CurPath = None
UniqueLocation = None

while Alive == True:
    PlyHPCap = PlyStartHPCap + (2 * PlyLevel)
    PlyManaCap = PlyStartManaCap + (1 * PlyLevel)
    PlyDamage = random.randrange(int(MinDMG), int(MaxDMG)) + PlyDamageBuff + PlySpellDamageBuff + PlyLevel
    XPRequired = 15 + (5 * PlyLevel)
    if PlyHP <= 0:
        Alive = False
    if PlyXP >= XPRequired:
        PlyXP = PlyXP - XPRequired
        PlyLevel = PlyLevel + 1
        print("\nYou have leveled up!\n\nYou are now level", str(PlyLevel) + "!")
        if PlyLevel == 3:
            if PlyCharType == "Knight":
                UnlockedSpell = "Fiat Lux"
            elif PlyCharType == "Leper":
                UnlockedSpell = "Do Your Worst"
            elif PlyCharType == "Rogue":
                UnlockedSpell = "Caltrops"
            elif PlyCharType == "Cleric":
                UnlockedSpell = "Purged By Light"
            print("You have unlocked the spell", UnlockedSpell + "!")
        elif PlyLevel == 5:
            if PlyCharType == "Knight":
                UnlockedSpell = "Bolster Shield"
            elif PlyCharType == "Leper":
                UnlockedSpell = "Short Respite"
            elif PlyCharType == "Rogue":
                UnlockedSpell = "Poisoned Blades"
            elif PlyCharType == "Cleric":
                UnlockedSpell = "Self Heal"
            print("\nYou have unlocked the spell", UnlockedSpell + "!")
        elif PlyLevel == 7:
            if PlyCharType == "Knight":
                UnlockedSpell = "Crusade Banner"
            elif PlyCharType == "Leper":
                UnlockedSpell = "Infected Blood"
            elif PlyCharType == "Rogue":
                UnlockedSpell = "Backstab"
            elif PlyCharType == "Cleric":
                UnlockedSpell = "Regeneration"
            print("\nYou have unlocked the spell", UnlockedSpell + "!")
        elif PlyLevel == 9:
            if PlyCharType == "Knight":
                UnlockedSpell = "Shoulder Charge"
            elif PlyCharType == "Leper":
                UnlockedSpell = "Overwhelming Blow"
            elif PlyCharType == "Rogue":
                UnlockedSpell = "Smoke Bomb"
            elif PlyCharType == "Cleric":
                UnlockedSpell = "Mana Regeneration"
            print("\nYou have unlocked the spell", UnlockedSpell + "!")
        PlyHPCap = PlyStartHPCap + (2 * PlyLevel)
        PlyManaCap = PlyStartManaCap + (1 * PlyLevel)
        PlyHP = PlyHP + 2
        PlyMana = PlyMana + 1
    if PlyHP > PlyHPCap:
        PlyHP = PlyHPCap
    if PlyMana > PlyManaCap:
        PlyMana = PlyManaCap

    while Casting == 1:
        PlyDamage = random.randrange(int(MinDMG), int(MaxDMG)) + PlyDamageBuff + PlySpellDamageBuff + PlyLevel
        if PlyBuffTurns > 0:
            if PlyBuffType == "Acc" or PlyBuffType == "Acc + DMG":
                PlyAccuracy = TruePlyAccuracy + 25
            else:
                PlyAccuracy = TruePlyAccuracy
            if PlyBuffType == "Crit Chance":
                PlyCritChance = TruePlyCritChance + 15
            else:
                PlyCritChance = TruePlyCritChance
        if PlyCharType == "Knight":
            print("\nChoose spell:")
            print("(0) Cancel")
            if CurEnemy in UnholyEnemy:
                print("(1) Holy Strike - Perform a special attack that deals bonus damage. +50% DMG vs Unholy Enemy - 2 Mana")
            else:
                print("(1) Holy Strike - Perform a special attack that deals bonus damage - 2 Mana")
            if PlyLevel >= 3:
                print("(2) Fiat Lux - Cast a blinding flash of light that reduces enemy accuracy by 25 for 3 turns - 2 Mana")
            if PlyLevel >= 5:
                print("(3) Bolster Shield - Raise your shield and parry the next enemy attack - 3 Mana")
            if PlyLevel >= 7:
                print("(4) Crusade Banner - Raise your banner and restore 5 HP, 25 Accuracy and +3 Damage for your next attack - 4 Mana")
            if PlyLevel >= 9:
                print("(5) Shoulder Charge - Charge the enemy dealing massive damage - 5 Mana")
            SpellChoice = int(input("\nSpell: "))
            if ((SpellChoice == 1 or SpellChoice == 2) and PlyMana < 2) or (SpellChoice == 3 and PlyMana < 3) or (SpellChoice == 4 and PlyMana < 4) or (SpellChoice == 5 and PlyMana < 5):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                Accuracy = random.randrange(1, 100)
                print("\nYou perform a Holy Strike against the", CurEnemy + ".")
                PlyMana = PlyMana - 2
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = ((PlyDamage + 2) * 2)
                    else:
                        PlyDamage = PlyDamage + 2
                    if CurEnemy in UnholyEnemy:
                        PlyDamage = math.ceil(PlyDamage * 1.5)
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 2:
                print("\nYou cast Fiat Lux against the", CurEnemy + ".")
                PlyMana = PlyMana - 2
                CurEnemyDebuffType = "Acc"
                CurEnemyDebuffTurns = 3
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 5 and PlyMana >= 3:
                print("\nYou bolster your shield against the enemy attack.")
                PlyMana = PlyMana - 3
                PlyGuard == "Bolstered"
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 7 and PlyMana >= 4:
                print("\nYou raise your banner with holy fervor. Your next attack has +25 Accuracy and +3 Damage.")
                print("You regain 5 HP.")
                PlyMana = PlyMana - 4
                PlyHP = PlyHP + 5
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "HP.")
                PlyBuffType = "Acc + DMG"
                PlySpellDamageBuff = 3
                PlyBuffTurns = 1
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 9 and PlyMana >= 5:
                print("You charge down the enemy, dealing massive damage.")
                print("You deal", math.ceil(PlyDamage * 1.5), "points of damage.")
                PlyMana = PlyMana - 5
                CurEnemyHP = CurEnemyHP - (math.ceil(PlyDamage * 1.5))
                WhoseTurn = 2
                Casting = 0
        if PlyCharType == "Leper":
            print("Choose spell:")
            print("(0) Cancel")
            print("(1) Ready to Strike - Your next attack has increased accuracy and damage. - 2 Mana")
            if PlyLevel >= 3:
                print("(2) Do Your Worst! - The enemy gains +25 accuracy for their attack. You gain 50% damage resistance and retaliate with a normal attack that deals 25% less damage. - 3 Mana")
            if PlyLevel >= 5:
                print("(3) Short Respite - Recover 4 HP. Does not end your turn. - 3 Mana")
            if PlyLevel >= 7:
                if CurEnemy in PoisonImmune:
                    print("(4) Infected Blood - Perform a regular attack that inflicts poison DoT against the enemy. This enemy is immune to poison! - 4 Mana")
                else:
                    print("(4) Infected Blood - Perform a regular attack that inflicts poison DoT against the enemy. - 4 Mana")
            if PlyLevel >= 9:
                print("(5) Crushing Blow - Perform a high damage attack, but suffer 25% damage vulnerability on the enemy turn. - 5 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or ((SpellChoice == 2 or SpellChoice == 3) and PlyMana < 3) or (SpellChoice == 4 and PlyMana < 4) or (SpellChoice == 5 and PlyMana < 5):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou ready your blade for your next attack.")
                PlyMana = PlyMana - 2
                PlyBuffType = "Acc + DMG"
                PlyBuffTurns = 1
                PlySpellDamageBuff = 3
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                print("\nYou taunt the enemy and prepare to counterattack.")
                PlyMana = PlyMana - 3
                CurEnemyBuffType = "Acc"
                CurEnemyBuffTurns = 1
                PlyGuard == "Taunt"
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 5 and PlyMana >= 3:
                print("\nYou rest for a moment, recovering 4 HP.")
                PlyMana = PlyMana - 3
                PlyHP = PlyHP + 4
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 7 and PlyMana >= 4:
                print("\nYou coat your blade in infected blood and strike the enemy.")
                Accuracy = random.randrange(1, 100)
                PlyMana = PlyMana - 4
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = PlyDamage * 2
                    if CurEnemy in PoisonImmune:
                        print("\nThe enemy is immune to the effects of the blood!")
                    else:
                        print("\nThe enemy is poisoned by the blood.")
                        CurEnemyDebuffType = "Poisoned"
                        CurEnemyDebuffTurns = 3
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 9 and PlyMana >= 5:
                print("You heave your blade at the enemy, dealing massive damage.")
                print("You deal", math.ceil(PlyDamage * 1.5), "points of damage.")
                CurEnemyHP = CurEnemyHP - (math.ceil(PlyDamage * 1.5))
                PlyMana = PlyMana - 5
                PlyDebuffType = "DMG Vuln"
                PlyDebuffTurns = 0
                WhoseTurn = 2
                Casting = 0
        if PlyCharType == "Rogue":
            print("Choose spell:")
            print("(0) Cancel")
            print("(1) Vanish - Reduce enemy accuracy by 25 and increase your Critical Hit Chance by +15 for 3 turns - 2 Mana")
            if PlyLevel >= 3:
                print("(2) Caltrops - The enemy takes 3 damage every time they attack. Can trigger 3 times. Does not end the turn - 3 Mana")
            if PlyLevel >= 5:
                if CurEnemy in PoisonImmune:
                    print("(3) Poisoned Blades - Attacks that hit cause the enemy to suffer Poison DoT. Lasts 3 turns, does not end your turn. This enemy is immune to Poison - 4 Mana")
                else:
                    print("(3) Poisoned Blades - Attacks that hit cause the enemy to suffer Poison DoT. Lasts 3 turns, does not end your turn. - 4 Mana")
            if PlyLevel >= 7:
                print("(4) Backstab - Perform an attack that has increased Critical Hit Chance and Damage, but reduced accuracy - 5 Mana")
            if PlyLevel >= 9:
                print("(5) Smoke Bomb - Escape the encounter and continue traveling. You will not gain any XP or Gold by doing this. - 6 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or (SpellChoice == 2 and PlyMana < 3) or (SpellChoice == 3 and PlyMana < 4) or (SpellChoice == 4 and PlyMana < 5) or (SpellChoice == 5 and PlyMana < 6):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou vanish into the shadows, ready to strike.")
                PlyMana = PlyMana - 2
                if PlyBuffType == "None":
                    PlyBuffType = "Crit Chance"
                elif PlyBuffType == "Poison":
                    PlyBuffType = "Crit Chance + Poison"
                PlyBuffTurns = 3
                CurEnemyDebuffType = "Acc"
                CurEnemyDebuffTurns = 3
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                print("\nYou drop Caltrops to disrupt the enemy.")
                PlyMana = PlyMana - 3
                CaltropHits = 3
                Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 5 and PlyMana >= 4:
                print("\nYou coat your blades in poison, increasing their lethality.")
                PlyMana = PlyMana - 4
                if PlyBuffType == "None":
                    PlyBuffType = "Poison"
                elif PlyBuffType == "Crit Chance":
                    PlyBuffType = "Crit Chance + Poison"
                PlyBuffTurns = 3
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 7 and PlyMana >= 5:
                print("\nYou attempt to backstab the enemy.")
                Accuracy = random.randrange(1, 100)
                PlyMana = PlyMana - 5
                if Accuracy <= PlyAccuracy - 25:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance + 10:
                        print("Critical Hit!")
                        PlyDamage = PlyDamage * 2
                    print("You deal", math.ceil(PlyDamage * 1.33), "points of damage.")
                    CurEnemyHP = CurEnemyHP - (math.ceil(PlyDamage * 1.33))
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy - 25:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 9 and PlyMana >= 6:
                print("You cast a smoke bomb and escape the encounter.")
                WhoseTurn = 0
                InCombat = False
                CurEnemy = None
                CurEnemyLevel = 0
                CurEnemyHP = 0
                CurEnemyXP = 0
                CurEnemyAccuracy = 0
                CurEnemyBuffType = "None"
                CurEnemyBuffTurns = 0
                CurEnemyDebuffType = "None"
                CurEnemyDebuffTurns = 0
                PlyBuffType = "None"
                PlyBuffTurns = 0
                PlyDebuffType = "None"
                PlyDebuffTurns = 0
                Casting = 0
        if PlyCharType == "Cleric":
            print("Choose spell:")
            print("(0) Cancel")
            print("(1) Confuse - Reduce enemy accuracy by -25. Does not end your turn. - 2 Mana")
            if PlyLevel >= 3:
                if CurEnemy in UnholyEnemy:
                    print("(2) Purged By Light - Smite your enemy with holy light, dealing bonus damage. +50% DMG vs Unholy Enemy. - 3 Mana")
                else:
                    print("(2) Purged By Light - Smite your enemy with holy light, dealing bonus damage. - 3 Mana")
            if PlyLevel >= 5:
                print("(3) Self Heal - Recover 5 HP. Does not end your turn. - 4 Mana")
            if PlyLevel >= 7:
                print("(4) Regenerate - Regenerate 3 HP/turn. Lasts 3 turns. Does not end your turn. - 5 Mana")
            if PlyLevel >= 9:
                print("(5) Mana Regeneration - Increase your Mana Regeneration to 3 Mana/turn. Lasts for the rest of the encounter. Does not end your turn. - 6 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or (SpellChoice == 2 and PlyMana < 3) or (SpellChoice == 3 and PlyMana < 4) or (SpellChoice == 4 and PlyMana < 5) or (SpellChoice == 5 and PlyMana < 6):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou cast a ray of light to confuse the enemy.")
                PlyMana = PlyMana - 2
                CurEnemyDebuffType = "Acc"
                CurEnemyDebuffTurns = 3
                Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                print("\nYou purge the enemy with holy light.")
                PlyMana = PlyMana - 3
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = ((PlyDamage + 2) * 2)
                    else:
                        PlyDamage = PlyDamage + 2
                    if CurEnemy in UnholyEnemy:
                        PlyDamage = math.ceil(PlyDamage * 1.5)
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 5 and PlyMana >= 4:
                print("\nYou heal yourself for 5 HP.")
                PlyMana = PlyMana -4
                PlyHP = PlyHP + 5
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 7 and PlyMana >= 5:
                print("\nYou cast Regeneration on yourself.")
                PlyMana = PlyMana - 5
                PlyBUffType = "Regeneration"
                PlyBuffTurns = 3
                Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 9 and PlyMana >= 6:
                print("\nYou cast Mana Regeneration on yourself, increasing your mana recovery to 3.")
                PlyMana = PlyMana - 6
                ClericManaBonus = 2
                Casting = 0

    if InCombat == False and UniqueLocation != None:
            if UniqueLocation == "Merchant":
                TurnsToTraverse = 0
                if FirstMerchant == False:
                    print('\nHe says: "Greetings traveler, care to browse my wares?"')
                    FirstMerchant = True
                if ArmorBought == False:
                    ArmorLine = "\n - Stronger armor (+1 Damage Reduction) - 60 Gold"
                else:
                    ArmorLine = ""
                if SwordBought == False:
                    SwordLine = "\n - A better weapon (+1 Damage) - 50 Gold"
                else:
                    SwordLine = ""
                if ShieldBought == False:
                    ShieldLine = "\n - A stronger shield (+1 Guard Protection) - 40 Gold"
                else:
                    ShieldLine = ""
                if PotionBought == False:
                    PotionLine = "\n - A healing potion (+1 Potion) - 30 Gold"
                else:
                    PotionLine = ""
                print("\nThe merchant is selling:", ArmorLine, SwordLine, ShieldLine, PotionLine)
                print("\nYou have", PlyGold, "gold")
                Purchase = input("\n(A)rmor - (W)eapon - (S)hield - (P)otion - (L)eave ")
                if (Purchase.casefold() == "armor" or Purchase.casefold() == "a") and ArmorBought != True:
                    if PlyGold >= 60:
                        print("\nYou purchase the armor")
                        PlyDMGRes = PlyDMGRes + 1
                        print("You now have", PlyDMGRes, "points of damage resistance.")
                        PlyGold = PlyGold - 50
                        print("Gold:", PlyGold)
                        ArmorBought = True
                    elif ArmorBought == True:
                        print('\nThe merchant says: "Sorry traveler, I got no more armor to sell ya"')
                    elif PlyGold < 60:
                        print('\nThe merchant chuckles and says: "Sorry, but you dont have enough gold for that"')
                elif (Purchase.casefold() == "weapon" or Purchase.casefold() == "w") and SwordBought != True:
                    if PlyGold >= 50:
                        print("\nYou purchase the weapon")
                        PlyDamageBuff = PlyDamageBuff + 1
                        print("You now deal", PlyDamageBuff, "additional points of damage.")
                        PlyGold = PlyGold - 50
                        print("Gold:", PlyGold)
                        SwordBought = True
                    elif SwordBought == True:
                        print('\nThe merchant says: "Sorry traveler, I got no more weapons to sell ya"')
                    elif PlyGold < 50:
                        print('\nThe merchant chuckles and says: "Sorry, but you dont have enough gold for that"')
                elif (Purchase.casefold() == "shield" or Purchase.casefold() == "s") and ShieldBought != True:
                    if PlyGold >= 40:
                        print("\nYou purchase the shield")
                        PlyGuardRes = PlyGuardRes + 1
                        print("Your guard now protects against", PlyDMGRes, " points of damage.")
                        PlyGold = PlyGold - 40
                        print("Gold:", PlyGold)
                        ShieldBought = True
                    elif ShieldBought == True:
                        print('\nThe merchant says: "Sorry traveler, I got no more shields to sell ya"')
                    elif PlyGold < 40:
                        print('\nThe merchant chuckles and says: "Sorry, but you dont have enough gold for that"')
                elif (Purchase.casefold() == "p"or Purchase.casefold() == "potion") and PotionBought != True:
                    if PlyGold >= 30:
                        print("\nYou purchase the healing potion")
                        PlyPotions = PlyPotions + 1
                        print("You now have", PlyPotions, "potions.")
                        PlyGold = PlyGold - 30
                        print("Gold:", PlyGold)
                        PotionBought = True
                    elif PotionBought == True:
                        print('\nThe merchant says: "Sorry traveler, I got no more potions to sell ya"')
                    elif PlyGold < 30:
                        print('\nThe merchant chuckles and says: "Sorry, but you dont have enough gold for that"')
                elif Purchase.casefold() == "leave" or Purchase.casefold() == "l":
                    print('\nYou leave the merchants shop.\n"Until next time, traveler!" he calls out.')
                    UniqueLocation = None
                    CurPath = None
                    FirstMerchant = False
                    ArmorBought = False
                    SwordBought = False
                    ShieldBought = False
                    PotionBought = False
            elif UniqueLocation == "Village":
                TurnsToTraverse = 0
                print("\nYou come across a quiet village.")
                print("You take a brief rest at the village")
                print("You are fully healed and all your mana is restored")
                PlyMana = PlyManaCap
                PlyHP = PlyHPCap
                UniqueLocation = None
                CurPath = None
    elif InCombat == False and UniqueLocation == None:
        print("\nHealth:", str(PlyHP) + "/" + str(PlyHPCap), "Mana:", str(PlyMana) + "/" + str(PlyManaCap), "Gold:", PlyGold)
        print("Level", PlyLevel, PlyCharType, "Experience:", str(PlyXP) + "/" + str(XPRequired))
        if CurPath != None and TurnsToTraverse > 0:
            print("\nThis path requires", TurnsToTraverse, "more turns to traverse through.")
            print("You must still travel", DistanceToTravel, "tiles to reach the castle.")
        else:
            print("\nYou must still travel", DistanceToTravel, "tiles to reach the castle.")
        Movement = input("\n(T)ravel - (R)est - (S)ave Game ")
        if Movement.casefold() == "save" or Movement.casefold() == "save game" or Movement.casefold() == "s":
            print("Saving Game...")
            SaveGame()
        elif Movement.casefold() == "travel" or Movement.casefold() == "t":
            print("\nYou continue traveling.")
            if CurPath == None:
                Travel = random.randrange(1,15)
                if Travel == 1:
                    print("\nYou were ambushed during your travel!")
                    if CurPath == None:
                        CurPathEnemy = OpenPathEnemy
                    WhoseTurn = 2
                    InCombat = True
                    Ambush = True
                elif Travel >= 2 and Travel <= 8:
                    TurnsToTraverse = 3
                    Path1 = random.choice(RandPath)
                    Path2 = random.choice(RandPath)
                    if Path2 == Path1:
                        Path2 = random.choice(RandPath)
                    ChoosePath = True
                    print("\nYou come across a crossroads\nThe first path leads to a", Path1, "and the second one to a", Path2)
                    print("\nChoose:\n- Path (1):", Path1, "\n- Path (2):", Path2)
                    while ChoosePath == True:
                        Choice = input("\nPath: ")
                        if Choice.casefold() == "path 1" or Choice.casefold() == "1":
                            CurPath = Path1
                            ChoosePath = False
                            if CurPath == "Quiet Forest":
                                EncounterChance = 20
                                CurPathEnemy = QuietForestEnemy
                            elif CurPath == "Evil Forest":
                                EncounterChance = 60
                                CurPathEnemy = EvilForestEnemy
                            elif CurPath == "Open Field":
                                EncounterChance = 45
                                CurPathEnemy = OpenFieldEnemy
                            elif CurPath == "Graveyard":
                                EncounterChance = 60
                                CurPathEnemy = GraveyardEnemy
                            elif CurPath == "Small Hill":
                                EncounterChance = 20
                                CurPathEnemy = SmallHillEnemy
                            elif CurPath == "Village":
                                EncounterChance = 0
                                UniqueLocation = "Village"
                            elif CurPath == "Corrupted Village":
                                EncounterChance = 60
                                CurPathEnemy = VillageEnemy
                            elif CurPath == "Travelling Merchant":
                                EncounterChance = 0
                                UniqueLocation = "Merchant"
                            elif CurPath == "Open Path":
                                EncounterChance = 45
                                CurPathEnemy = OpenPathEnemy
                        elif Choice.casefold() == "path 2" or Choice.casefold() == "2":
                            CurPath = Path2
                            ChoosePath = False
                            if CurPath == "Quiet Forest":
                                EncounterChance = 20
                                CurPathEnemy = QuietForestEnemy
                            elif CurPath == "Evil Forest":
                                EncounterChance = 60
                                CurPathEnemy = EvilForestEnemy
                            elif CurPath == "Open Field":
                                EncounterChance = 45
                                CurPathEnemy = OpenFieldEnemy
                            elif CurPath == "Graveyard":
                                EncounterChance = 60
                                CurPathEnemy = GraveyardEnemy
                            elif CurPath == "Small Hill":
                                EncounterChance = 20
                                CurPathEnemy = SmallHillEnemy
                            elif CurPath == "Village":
                                EncounterChance = 0
                                UniqueLocation = "Village"
                            elif CurPath == "Corrupted Village":
                                EncounterChance = 60
                                CurPathEnemy = VillageEnemy
                            elif CurPath == "Travelling Merchant":
                                EncounterChance = 0
                                UniqueLocation = "Merchant"
                            elif CurPath == "Open Path":
                                EncounterChance = 45
                                CurPathEnemy = OpenPathEnemy
                elif CurPath == None and Travel > 8:
                    TurnsToTraverse = 3
                    Path = random.choice(RandPath)
                    print("\nYou come across a", Path)
                    CurPath = Path
                    if CurPath == "Quiet Forest":
                        EncounterChance = 20
                        CurPathEnemy = QuietForestEnemy
                    elif CurPath == "Evil Forest":
                        EncounterChance = 60
                        CurPathEnemy = EvilForestEnemy
                    elif CurPath == "Open Field":
                        EncounterChance = 45
                        CurPathEnemy = OpenFieldEnemy
                    elif CurPath == "Graveyard":
                        EncounterChance = 60
                        CurPathEnemy = GraveyardEnemy
                    elif CurPath == "Small Hill":
                        EncounterChance = 20
                        CurPathEnemy = SmallHillEnemy
                    elif CurPath == "Village":
                        EncounterChance = 0
                        UniqueLocation = "Village"
                    elif CurPath == "Corrupted Village":
                        EncounterChance = 60
                        CurPathEnemy = VillageEnemy
                    elif CurPath == "Travelling Merchant":
                        EncounterChance = 0
                        UniqueLocation = "Merchant"
                    elif CurPath == "Open Path":
                        EncounterChance = 45
                        CurPathEnemy = OpenPathEnemy
            elif UniqueLocation == None and CurPath != None:
                if TurnsToTraverse > 0:
                    TurnsToTraverse = TurnsToTraverse - 1
                    Encounter = random.randrange(1, 100)
                    if Encounter < EncounterChance:
                        InCombat = True
                    elif Encounter >= 95:
                        print("\nYou come across a mysterious chest")
                        ChestActive = True
                        while ChestActive == True:
                            Chest = input("Open the chest Y/N ")
                            if Chest.casefold() == "y":
                                ChestEvent = random.randrange(1, 15)
                                if ChestEvent < 4:
                                    print("\nThe chest contains nothing of interest")
                                    ChestActive = False
                                elif ChestEvent >= 4 and ChestEvent <= 8:
                                    print("\nYou find some gold inside the chest!")
                                    PlyGold = PlyGold + random.randrange(10, 50)
                                    print("You now have", PlyGold, "gold")
                                    ChestActive = False
                                elif ChestEvent == 9:
                                    print("\nYou find a new sword inside the chest!")
                                    PlyDamageBuff = PlyDamageBuff + 1
                                    print("You now deal", PlyDamageBuff, "additional points of damage")
                                    ChestActive = False
                                elif ChestEvent == 10:
                                    print("\nYou find new armor inside the chest!")
                                    PlyDMGRes = PlyDMGRes + 1
                                    print("You now have", PlyDMGRes, "points of damage resistance")
                                    ChestActive = False
                                elif ChestEvent == 11:
                                    print("\nYou find a new shield inside the chest!")
                                    PlyGuardRes = PlyGuardRes + 1
                                    print("Your guard now protects against", PlyGuardRes, "points of damage")
                                    ChestActive = False
                                elif ChestEvent == 12:
                                    print("\nYou find a health potion inside the chest!")
                                    PlyPotions = PlyPotions + 1
                                    print("You now have", PlyPotions, "healing potions")
                                    ChestActive = False
                                elif ChestEvent >= 13:
                                    print("\nThe chest is a mimic!")
                                    CurEnemy = "Mimic"
                                    InCombat = True
                                    WhoseTurn = 2
                                    Ambush = True
                                    ChestActive = False
                            elif Chest.casefold() == "n":
                                print("\nYou leave the chest alone")
                                ChestActive = False
                    else:
                        if PlyMana < PlyManaCap:
                            PlyMana = PlyMana + 1
                        print("You encounter no enemies")
                if TurnsToTraverse == 0:
                    CurPath = None
                    DistanceToTravel = DistanceToTravel - 1
                    TurnsToTraverse = 3
                    if DistanceToTravel == 0:
                        Alive = False
                        GameState = 1
        elif Movement.casefold() == "rest" or Movement.casefold() == "r":
            Ambush = random.randrange(1, 12)
            if Ambush == 1:
                if CurPath == None:
                    CurPathEnemy = OpenPathEnemy
                InCombat = True
                print("\nYou were ambushed during your sleep!")
                WhoseTurn = 2
                Ambush = True
            else:
                print("\nYou rest for a moment, recovering 5 HP and 2 Mana.")
                PlyHP = PlyHP + 5
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                PlyMana = PlyMana + 2
                if PlyMana > PlyManaCap:
                    PlyMana = PlyManaCap
                print("You now have", PlyHP, "HP and", PlyMana, "mana")
        
    if InCombat == True and (CurEnemy == None or Ambush == True):
        if CurEnemy == None:
            CurEnemy = random.choice(CurPathEnemy)

        if PlyLevel < 3:
            CurEnemyLevel = PlyLevel + random.randrange(0, 2)
        else:
            CurEnemyLevel = PlyLevel + random.randrange(-2, 2)

        if CurEnemy in WeakEnemy:
            CurEnemyHP = random.randrange(1, 6) + (2 * CurEnemyLevel)
            TrueEnemyAccuracy = random.randrange(30, 50)
            EnemyDMG = "Weak"
        elif CurEnemy in NormalEnemy:
            CurEnemyHP = random.randrange(4, 12) + (2 * CurEnemyLevel)
            TrueEnemyAccuracy = random.randrange(45, 70)
            EnemyDMG = "Normal"
        elif CurEnemy in StrongEnemy:
            CurEnemyHP = random.randrange(6, 15) + (2 * CurEnemyLevel)
            TrueEnemyAccuracy = random.randrange(50, 85)
            EnemyDMG = "Strong"

        CurEnemyXP = CurEnemyHP - 4
        if CurEnemyXP <= 1:
            CurEnemyXP = 1
        EnemyQuote = 0
        print("\nYou encounter a Level", CurEnemyLevel, CurEnemy + "!")
        if CurEnemy == "Green Slime" or CurEnemy == "Blue Slime" or CurEnemy == "Red Slime":
            EnemyQuote = random.randrange(1, 4)
        elif CurEnemy == "Bandit":
            EnemyQuote = random.randrange(5, 8)
        elif CurEnemy == "Dire Wolf" or CurEnemy == "Corrupted Wolf":
            EnemyQuote = random.randrange(9, 12)
        elif CurEnemy == "Boar" or CurEnemy == "Corrupt Boar":
            EnemyQuote = random.randrange(13, 16)
        elif CurEnemy == "Evil Fairy":
            EnemyQuote = random.randrange(17, 20)
        elif CurEnemy == "Fungus" or CurEnemy == "Corrupted Fungus":
            EnemyQuote = random.randrange(21, 24)
        elif CurEnemy == "Dark Knight":
            EnemyQuote = random.randrange(25, 28)
        elif CurEnemy == "Zombie":
            EnemyQuote = random.randrange(29, 32)
        elif CurEnemy == "Skeleton":
            EnemyQuote = random.randrange(33, 36)
        elif CurEnemy == "Ghost":
            EnemyQuote = random.randrange(37, 40)
        elif CurEnemy == "Cultist":
            EnemyQuote = random.randrange(41, 44)
        elif CurEnemy == "Angry Goat":
            EnemyQuote = random.randrange(45, 48)
        elif CurEnemy == "Angry Eagle" or CurEnemy == "Vicious Hawk":
            EnemyQuote = random.randrange(49, 52)
        elif CurEnemy == "Snake":
            EnemyQuote = random.randrange(53, 56)
        elif CurEnemy == "Infected Villager" or CurEnemy == "Angry Farmer":
            EnemyQuote = random.randrange(57, 60)
        elif CurEnemy == "Raving Madman":
            EnemyQuote = random.randrange(61, 64)
        elif CurEnemy == "Vicious Hound":
            EnemyQuote = random.randrange(65, 68)
        elif CurEnemy == "Corrupt Priest":
            EnemyQuote = random.randrange(69, 72)
        elif CurEnemy == "Rotting Cow":
            EnemyQuote = random.randrange(73, 76)
        elif CurEnemy == "Vampire":
            EnemyQuote = random.randrange(77, 80)
        elif CurEnemy == "Bear":
            EnemyQuote = random.randrange(81, 84)
        elif CurEnemy == "Mimic":
            EnemyQuote = random.randrange(85, 88)

        print(EnemyQuotes[EnemyQuote])
        EnemyQuote = 0
        Ambush = False

    if InCombat == True and CurEnemy != None and CurEnemyHP > 0:
        if WhoseTurn == None:
            WhoseTurn = 1
        while WhoseTurn == 1 and Casting == 0:
            PlyAccuracy = TruePlyAccuracy
            PlyCritChance = TruePlyCritChance
            if PlyDebuffTurns == 0 and PlyDebuffType != "None":
                PlyDebuffType = "None"
                CurEnemyBonusDMG = 0
            if PlyDebuffType == "DMG Vuln":
                CurEnemyBonusDMG = 2
            if PlyBuffTurns == 0 and PlyBuffType != "None":
                PlyAccuracy = TruePlyAccuracy
                PlyBuffType = "None"
                PlySpellDamageBuff = 0
            if PlyBuffTurns > 0:
                if PlyBuffType == "Acc" or PlyBuffType == "Acc + DMG":
                    PlyAccuracy = TruePlyAccuracy + 25
                else:
                    PlyAccuracy = TruePlyAccuracy
                if PlyBuffType == "Crit Chance" or PlyBuffType == "Crit Chance + Poison":
                    PlyCritChance = TruePlyCritChance + 15
                else:
                    PlyCritChance = TruePlyCritChance

            print("\nEnemy", CurEnemy, "HP:", CurEnemyHP)
            print("\nHealth:", PlyHP, "Mana:", PlyMana)
            Combat = input("\n(A)ttack - (G)uard - (M)agic - (P)otion ")
            if Combat.casefold() == "attack" or Combat.casefold() == "a":
                Accuracy = random.randrange(1, 100)
                print("\nYou attack the", CurEnemy + ".")
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = (PlyDamage * 2) + (RogueBonus * 2)
                    else:
                        PlyDamage = PlyDamage
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    if PlyBuffTurns > 0:
                        PlyBuffTurns = PlyBuffTurns - 1
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    if PlyBuffTurns > 0:
                        PlyBuffTurns = PlyBuffTurns - 1
            elif Combat.casefold() == "guard" or Combat.casefold() == "g":
                print("\nYou guard yourself against the enemy.")
                PlyGuard = True
                WhoseTurn = 2
                if PlyBuffTurns > 0:
                    PlyBuffTurns = PlyBuffTurns - 1
            elif Combat.casefold() == "magic" or Combat.casefold() == "m":
                Casting = 1
            elif Combat.casefold() == "potion" or Combat.casefold() == "p":
                if PlyPotions > 0:
                    print("\nYou used a potion of healing.")
                    PlyHP = PlyHP + 7
                    if PlyHP > PlyHPCap:
                        PlyHP = PlyHPCap
                    print("You now have", PlyHP, "health.")
                else:
                    print("\nYou have no potions left.")
        if WhoseTurn == 2 and CurEnemyHP > 0:
            if PlyMana < PlyManaCap:
                PlyMana = PlyMana + (1 + ClericManaBonus)
            if PlyMana > PlyManaCap:
                PlyMana = PlyManaCap
            if EnemyDMG == "Weak":
                EnemyAttack = random.randrange(0, 3) + CurEnemyLevel + CurEnemyBonusDMG
            elif EnemyDMG == "Normal":
                EnemyAttack = random.randrange(1, 4) + CurEnemyLevel + CurEnemyBonusDMG
            elif EnemyDMG == "Strong":
                EnemyAttack = random.randrange(2, 5) + CurEnemyLevel + CurEnemyBonusDMG
            if CurEnemyDebuffType == "Poisoned" and CurEnemyDebuffTurns > 0:
                print("The enemy is damaged by the poison, taking 3 damage.")
                CurEnemyHP = CurEnemyHP - 3
            print("\nThe enemy", CurEnemy, "attacks you.")
            EnemyAccuracy = random.randrange(1, 100)
            if CurEnemyBuffTurns == 0 and CurEnemyBuffType != "None":
                CurEnemyBuffType = "None"
            if CurEnemyDebuffTurns == 0 and CurEnemyDebuffType != "None":
                CurEnemyDebuffType == "None"
            if CurEnemyDebuffType == "Acc" and CurEnemyDebuffTurns > 0:
                CurEnemyAccuracy = TrueEnemyAccuracy - 25
            else:
                CurEnemyAccuracy = TrueEnemyAccuracy
            if CurEnemyBuffType == "Acc":
                CurEnemyAccuracy = TrueEnemyAccuracy + 25
            else:
                CurEnemyAccuracy = TrueEnemyAccuracy
            if EnemyAccuracy <= CurEnemyAccuracy:
                ParryChance = random.randrange(1, 100)
                ParryDMG = math.ceil(PlyDamage * 1.25)
                if PlyGuard == False:
                    if EnemyAttack - PlyDMGRes <= 0:
                        EnemyAttack = 0
                        print("You take no damage.")
                    else:
                        PlyHP = PlyHP - (EnemyAttack - PlyDMGRes)
                        print("You take", (EnemyAttack - PlyDMGRes), "points of damage.")
                elif PlyGuard == True and ParryChance > PlyParry:
                    if EnemyAttack - PlyDMGRes - PlyGuardRes <= 0:
                        EnemyAttack = 0
                        print("You take no damage.")
                        PlyGuard = False
                    else:
                        PlyHP = PlyHP - (EnemyAttack - PlyDMGRes)
                        print("You take", (EnemyAttack - PlyDMGRes), "points of damage.")
                        PlyGuard = False
                elif PlyGuard == True and ParryChance <= PlyParry:
                    print("Parry! The enemy takes", ParryDMG, "damage.")
                    CurEnemyHP = CurEnemyHP - ParryDMG
                    PlyGuard = False
                elif PlyGuard == "Bolstered":
                    print("You deflect the enemy attack!")
                    print("The enemy takes", ParryDMG, "damage.")
                    CurEnemyHP = CurEnemyHP - ParryDMG
                    PlyGuard = False
                elif PlyGuard == "Taunt":
                    print("You brace for the enemy attack")
                    print("You take", (EnemyAttack - PlyDMGRes) * 0.5, "points of damage.")
                    PlyHP = PlyHP - ((EnemyAttack - PlyDMGRes) * 0.5)
                    print("You retaliate, dealing", PlyDamage * 0.75, "points of damage.")
                    CUrEnemyHP = CurEnemyHP - (PlyDamage * 0.75)
                    PlyGuard = False
                if CaltropHits > 0:
                    print("The", CurEnemy, "takes 3 damage from the caltrops.")
                    CurEnemyHP = CurEnemyHP - 3
                    CaltropHits = CaltropHits - 1
                if PlyHP <= 0:
                    Alive = False
                if CurEnemyDebuffTurns > 0:
                    CurEnemyDebuffTurns = CurEnemyDebuffTurns - 1
                WhoseTurn = 1
            elif EnemyAccuracy > CurEnemyAccuracy:
                if CurEnemyDebuffTurns > 0:
                    CurEnemyDebuffTurns = CurEnemyDebuffTurns - 1
                print("Miss! You take no damage.")
                WhoseTurn = 1
                PlyGuard = False
    if InCombat == True and CurEnemyHP <= 0 and Ambush == False:
        print("\nThe enemy", CurEnemy, "is defeated!")
        print("You earned", CurEnemyXP, "XP")
        PlyXP = PlyXP + CurEnemyXP
        Gold = random.randrange(0, 8) + (2 * CurEnemyLevel)
        print("You find", Gold, "pieces of gold on the enemy.")
        PlyGold = PlyGold + Gold
        CurEnemy = None
        CurEnemyLevel = 0
        CurEnemyHP = 0
        CurEnemyXP = 0
        CurEnemyAccuracy = 0
        CurEnemyBuffType = "None"
        CurEnemyBuffTurns = 0
        CurEnemyDebuffType = "None"
        CurEnemyDebuffTurns = 0
        PlyBuffType = "None"
        PlyBuffTurns = 0
        PlyDebuffType = "None"
        PlyDebuffTurns = 0
        ClericManaBonus = 0
        InCombat = False
        WhoseTurn = None