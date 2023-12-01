import random
import math
import os

#Base stats
Alive = "Choose character"
GameState = 0
PlyXP = 0
PlyLevel = 1
PlyGuard = "None"
PlyGold = 15
PlyCharType = "None"
PlyDamageBuff = 0

#Non-specific buffs
PlyBuffType = "None"
PlyBuffTurns = 0
PlyBuffAccBonus = 0
PlyBuffDMGBonus = 0
PlyBuffDMGResBonus = 0
PlyBuffCritBonus = 0
PlyAddDamageBuff = 0

#Strictly spell-based buffs
PlySpellBuffType = "None"
PlySpellBuffTurns = 0
PlySpellDamageBuff = 0
PlySpellAccBuff = 0
PlySpellCritBuff = 0

#(Leper) Spell debuffs
PlyDebuffType = "None"
PlyDebuffTurns = 0
Afflicted = 0

#Potions
PotionUsed = "False"
PotionBuffType = "None"
PotionBuffTurns = 0
PlyAccPotions = 0
PlyDodgePotions = 0
PlyHPPotions = 0
PlyLuckPotions = 0
PlyResistancePotions = 0
PlyStrengthPotions = 0

#Potion Buffs
PotionAccBuff = 0
PotionCritBuff = 0
PotionDMGBuff = 0
PotionDMGResBuff = 0
PotionDodgeBuff = 0

#Knight Skills
ParryCritChance = 0
ParryNegationChance = 0

#Leper Affliction
Affliction = 0

#Rogue Spells
RogueBonus = 0
RogueCritBonus = 0
CaltropHits = 0

#Cleric Skills
ClericHPRegen = 0
ClericManaBonus = 0
ClericDMGRes = 0
ClericDMG = 0
ClericAcc = 0
ClericCrit = 0
ClericRevive = 0

#Plague Doctor Skills
PlagueAttacks = 0
PlagueBonusCrit = 0
PlagueMalusEnemyAcc = 0
PlagueBonusDodge = 0
PlagueBonusDMG = 0

#Enemy stats
CurEnemy = None
CurEnemyHP = 0
CurMaxEnemyHP = 0
TrueEnemyAccuracy = 0
CurEnemyBuffType = "None"
CurEnemyBuffTurns = 0
CurEnemyBonusDMG = 0
CurEnemyDebuffType = "None"
CurEnemyDebuffTurns = 0
CurEnemySpellDebuffType = "None"
CurEnemySpellDebuffTurns = 0
CurEnemyDoTType = "None"
CurEnemyDoTTurns = 0

#Poison
TruePoisonDMG = 2
PoisonDMGBuff = 0

#Encounters and Combat
EncounterChance = 0
Ambush = False
InCombat = False
WhoseTurn = None

#Menu-based stuff
Casting = 0
Potions = 0

#Travel
DistanceToTravel = 50
TurnsToTraverse = 3

HelpMenu = ""

#Character sheet = Health, Mana, Damage (min, max), Damage Res, Guard Reduction, Accuracy

while Alive == "Choose character":
    print("\nChoose a character:\n- The (K)night\n- The (L)eper\n- The (R)ogue\n- The (C)leric\n- The (P)lague Doctor")
    print("\nOr type 'help' for information on the various mechanics and stats.")
    CharChoice = input("\nChoose: ")
    if CharChoice.casefold() == "help":
        HelpMenu = "List"
        while HelpMenu == "List":
            print("(1) - Characters\n(2) - XP and Levels\n(3) - Mana\n(4) - Damage Resistance\n(5) - Guarding and Parrying\n(6) - Accuracy\n(7) - Critical Hits\n(8) - Dodge\n(9) - Resting\n(10) - Traveling\n(11) - Ambushes\n(12) - Locations\n(13) - Victory Condition")
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
                HelpMenu = "Dodge"
            elif HelpChoice == "10":
                HelpMenu = "Traveling"
            elif HelpChoice == "11":
                HelpMenu = "Ambush"
            elif HelpChoice == "12":
                HelpMenu = "Locations"
            elif HelpChoice == "13":
                HelpMenu = "Victory"
        while HelpMenu == "Characters":
            print("(1) - The Knight\n(2) - The Leper\n(3) - The Rogue\n(4) - The Cleric\n(5) - The Plague Doctor")
            print("\nList <- (B)ack - (N)ext Page -> Levels")
            Page1 = input("\nChoose: ")
            if Page1 == "1":
                HelpMenu = "Knight"
            elif Page1 == "2":
                HelpMenu = "Leper"
            elif Page1 == "3":
                HelpMenu = "Rogue"
            elif Page1 == "4":
                HelpMenu = "Cleric"
            elif Page1 == "%":
                HelpMenu = "Plague Doctor"
            elif Page1.casefold() == "b":
                HelpMenu = "List"
            elif Page1.casefold() == "n":
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
            print("\nThe Leper is a hard-hitting but inaccuracte character, better at dealing high damage-per-hit.\nThe Leper is not as tanky as the Knight, but has a much easier time dealing with high health enemies, so long as his hits land.\nThe Leper has a unique mechanic, where he will suffer 2 points of damage after a set amount of turns.\nThis mechanic is called Affliction, and can be stalled by resting.\nAffliction at the start triggers every 3 turns, but leveling up increases this delay.\nEvery time the Leper suffers from Affliction, they also gain a temporary buff.\nA Leper is someone who suffers from Leprosy, a term often used in medieval times.\nThe most renowned Leper of medieval times was Baldwin IV of Jerusalem, who ruled Jerusalem in spite of debilitating Leprosy.")
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
            print("\nThe Rogue <- (B)ack - (N)ext Page -> The Plague Doctor")
            Cleric = input("\nChoose: ")
            if Cleric.casefold() == "b":
                HelpMenu = "Rogue"
            elif Cleric.casefold() == "n":
                HelpMenu = "Plague Doctor"
        while HelpMenu == "Plague Doctor":
            print("\nThe Plague Doctor is a character focused on inflicting DoTs (Damage-over-Time) on his enemies.\nThe Plague Doctor's basic attacks inflict poison on all hits, with spells buffing the damage and duration of DoTs\nPlague Doctors are a well known figure from Medieval times, during the Bubonic Plague\nPlague Doctors would wear beaked masks, with flower petals and other pleasant smelling substances stuffed into the beak.\nThis was done to hide the stench of dead corpses.")
            print("\nThe Cleric <- (B)ack - (N)ext Page -> XP and Levels")
            PlagueDoctor = input("\nChoose: ")
            if PlagueDoctor.casefold() == "b":
                HelpMenu = "Cleric"
            elif PlagueDoctor.casefold() == "n":
                HelpMenu = "Levels"
        while HelpMenu == "Levels":
            print("\nXP and Levels are a basic mechanic of the game that improve the players stats as they level up.\nThe first level is earned by gaining 20 XP. Every subsequent level requires an additional 5 XP to level up\nEach level up increases Max HP by 2, Max Mana and Damage by 1.\nXP earned from enemies is based on their health, with higher health enemies dropping greater amounts of XP.\nThe maximum level a character can reach is 30.")
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
            print("\nCritical Hits <- (B)ack - (N)ext Page -> Dodge")
            Rest = input("\nChoose: ")
            if Rest.casefold() == "b":
                HelpMenu = "Crits"
            elif Rest.casefold() == "n":
                HelpMenu = "Dodge"
        while HelpMenu == "Dodge":
            print("\nDodge is a mechanic where enemy attacks have a chance to not deal damage.\nAny enemy attack that would hit the player rolls an additional chance for dodge.\nIf the roll succeeds, the player dodges the attack and takes no damage.")
            print("\nResting <- (B)ack - (N)ext Page -> Traveling")
            Rest = input("\nChoose: ")
            if Rest.casefold() == "b":
                HelpMenu = "Resting"
            elif Rest.casefold() == "n":
                HelpMenu = "Traveling"
        while HelpMenu == "Traveling":
            print("\nTraveling is how the player traverses the game and reaches new areas.\nEach time the player travels, they either come across a path or a crossroads\nWhen at a crossroads, the player is given the choice to pick one of two paths.\nEach path has its own set of enemies and chances of encounter.")
            print("\nDodge <- (B)ack - (N)ext Page -> Ambushes")
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
        print("\n- 20 Health\n- 3 Mana\n- Damage 3-6\n- Damage Resistance 2\n- Guard Damage Reduction 4\n- Parry Chance 25\n- Accuracy 60\n- Dodge 10\n- Critical Hit Chance 40")
        ChooseKnight = input("Choose Knight? Y/N ")
        if ChooseKnight.casefold() == "y":
            PlyCharType = "Knight"
            PlyStartHPCap = 18
            PlyStartManaCap = 2
            MinDMG = 2
            MaxDMG = 5
            PlyParry = 25
            TruePlyAccuracy = 60
            TruePlyCritChance = 25
            TruePlyDodge = 10
            TruePlyDMGRes = 2
            PlyGuardRes = 2
            PlyHPPotions = 2
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
                    TruePlyDMGRes = int(OpenSave.readline())
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
        print("\nThe Leper:\n- Stronger Attacks\n- Lower Accuracy\n- Afflicted")
        print("\n- 20 Health\n- 5 Mana\n- Damage 5-8\n- Damage Resistance 0\n- Guard Damage Reduction 2\n- Parry Chance 40\n- Accuracy 50\n- Dodge 15\n- Critical Hit Chance 45")
        ChooseLeper = input("Choose Leper? Y/N ")
        if ChooseLeper.casefold() == "y":
            PlyCharType = "Leper"
            PlyStartHPCap = 18
            PlyStartManaCap = 4
            MinDMG = 4
            MaxDMG = 7
            PlyParry = 40
            TruePlyAccuracy = 50
            TruePlyCritChance = 30
            TruePlyDodge = 15
            TruePlyDMGRes = 0
            PlyGuardRes = 2
            PlyResistancePotions = 1
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
                    TruePlyDMGRes = int(OpenSave.readline())
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
        print("\n- 15 Health\n- 5 Mana\n- Damage 3-6\n- Damage Resistance 0\n- Guard Damage Reduction 1\n- Parry Chance 65\n- Accuracy 75\n- Dodge 25\n- Critical hit Chance 60")
        ChooseRogue = input("Choose Rogue? Y/N ")
        if ChooseRogue.casefold() == "y":
            PlyCharType = "Rogue"
            PlyStartHPCap = 13
            PlyStartManaCap = 4
            MinDMG = 2
            MaxDMG = 5
            TruePlyDMGRes = 0
            PlyGuardRes = 1
            PlyParry = 65
            TruePlyAccuracy = 75
            TruePlyCritChance = 45
            TruePlyDodge = 25
            PlyDodgePotions = 1
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
                    TruePlyDMGRes = int(OpenSave.readline())
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
        print("\n- 25 Health\n- 8 Mana\n- Damage 2-4\n- Damage Resistance 0\n- Guard Damage Reduction 2\n- Parry Chance 25\n- Accuracy 60\n- Dodge 20\n- Critical Hit Chance 35")
        ChooseCleric = input("Choose Cleric? Y/N ")
        if ChooseCleric.casefold() == "y":
            PlyCharType = "Cleric"
            PlyStartHPCap = 23
            PlyStartManaCap = 7
            MinDMG = 1
            MaxDMG = 3
            TruePlyDMGRes = 0
            PlyGuardRes = 2
            PlyParry = 25
            TruePlyAccuracy = 60
            TruePlyCritChance = 35
            TruePlyDodge = 20
            PlyHPPotions = 2
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
                    TruePlyDMGRes = int(OpenSave.readline())
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
    elif CharChoice.casefold() == "plague" or CharChoice.casefold() == "the plague doctor" or CharChoice.casefold() == "p":
        print("\nThe Plague Doctor:\n- Attacks inflict Poison\n- Better DoT\n- Less Damage")
        print("\n- 20 Health\n- 5 Mana\n- Damage 1-3\n- Damage Resistance 0\n- Guard Damage Reduction 2\n- Parry Chance 20\n- Accuracy 60\n- Dodge 20\n- Critical Hit Chance 30")
        ChoosePlague = input("Choose Plague Doctor? Y/N ")
        if ChoosePlague.casefold() == "y":
            PlyCharType = "Plague Doctor"
            PlagueAttacks = 1
            PlyStartHPCap = 18
            PlyStartManaCap = 4
            MinDMG = 1
            MaxDMG = 3
            TruePlyDMGRes = 0
            PlyGuardRes = 2
            PlyParry = 20
            TruePlyAccuracy = 60
            TruePlyDodge = 20
            TruePlyCritChance = 20
            PlyHPPotions = 1
            if os.path.exists("plague doctor_save.txt"):
                Choice = input("Open old save? Y/N ")
                if Choice.casefold() == "y":
                    OpenSave = open("plague doctor_save.txt", "r")
                    PlyHP = int(OpenSave.readline())
                    PlyMana = int(OpenSave.readline())
                    PlyXP = int(OpenSave.readline())
                    PlyLevel = int(OpenSave.readline())
                    PlyGold = int(OpenSave.readline())
                    PlyPotions = int(OpenSave.readline())
                    PlyDamageBuff = int(OpenSave.readline())
                    TruePlyDMGRes = int(OpenSave.readline())
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

def SkillsNSpells():
    if PlyCharType == "Knight":
        print("\nSpells:")
        print("Holy Strike - Perform a special attack that deals +50% DMG vs Unholy Enemy - 2 Mana")
        if PlyLevel >= 3:
            print("Fiat Lux - Cast a blinding flash of light that reduces Enemy Accuracy by -25 for 3 turns. - 2 Mana")
        if PlyLevel >= 7 and PlyLevel < 19:
            print("Bolster Shield - Raise your shield and parry the next enemy attack. - 3 Mana - Upgrades at level 19")
        elif PlyLevel >= 19:
            print("Bolster Shield - Raise your shield and parry the next enemy attack. Parry attack has +15 Critical Hit Chance - 3 Mana")
        if PlyLevel >= 11 and PlyLevel < 23:
            print("Crusade Banner - Raise your banner and restore 5 HP. Gain +25 Accuracy and +3 DMG for 3 turns. - 4 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Crusade Banner - Raise your banner and restore 5 HP. Gain +25 Accuracy and +3 DMG for 3 turns. Does not end turn. - 4 Mana")
        if PlyLevel >= 15 and PlyLevel < 27:
            print("Shoulder Charge - Charge the enemy dealing massive DMG. - 5 Mana - Upgrades at Level 27")
        elif PlyLevel >= 27:
            print("Shoulder Charge - Charge the enemy dealing massive DMG and stunning them for 1 turn. - 5 Mana")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Knights Guard - Parry attacks have a 15% chance to crit.")
            print("Apothecarys Boon - Potions are 25% stronger.")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Knights Guard 1 - Parry attacks have a 15% chance to crit. Guard has a 5% chance to negate all damage.")
            print("Apothecarys Boon - Potions are 25% stronger.")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Knights Guard 1 - Parry attacks have a 15% chance to crit. Guard has a 5% chance to negate all damage.")
            print("Apothecarys Boon 1 - Potions are 50% stronger.")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Knights Guard 2 - Parry attacks have a 20% chance to crit. Guard has a 5% chance to negate all damage.")
            print("Apothecarys Boon 1 - Potions are 50% stronger.")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Knights Guard 2 - Parry attacks have a 20% chance to crit. Guard has a 5% chance to negate all damage.")
            print("Apothecarys Boon 2 - Potions are 50% stronger. 20% chance to use a potion for free.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Knights Guard 3 - Parry attacks have a 20% chance to crit. Guard has a 7% chance to negate all damage.")
            print("Apothecarys Boon 2 - Potions are 50% stronger. 20% chance to use a potion for free.")
        elif PlyLevel >= 25:
            print("Knights Guard 3 - Parry attacks have a 20% chance to crit. Guard has a 7% chance to negate all damage.")
            print("Apothecarys Boon 3 - Potions are 50% stronger. 20% chance to use a potion for free. Using a potion grants a random buff (Only one at a time)")
        if PlyLevel == 30:
            print("Mastery: Automatically enter guard at the end of your turn, unless bolstered.")
    elif PlyCharType == "Leper":
        print("\nSpells:")
        if PlyLevel < 19:
            print("Ready to Strike - Your next attack has +25 Accuracy and +3 DMG. - 2 Mana - Upgrades at Level 19")
        elif PlyLevel >= 19:
            print("Ready to Strike - Your next attack has +25 Accuracy and +3 DMG. Does not end your turn. - 2 Mana")
        if PlyLevel >= 3 and PlyLevel < 23:
            print("Do Your Worst! - The enemy gains +25 accuracy for their attack. You gain 50% DMG resistance and retaliate with a normal attack that deals 25% less DMG. - 3 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Do Your Worst! - The enemy gains +25 accuracy for their attack. You gain 50% DMG resistance and retaliate with a normal attack. - 3 Mana")
        if PlyLevel >= 7 and PlyLevel < 27:
            print("Short Respite - Recover", PlyHPCap * 0.2, "HP. - 3 Mana - Upgrades at 27")
        elif PlyLevel >= 27:
            print("Short Respite - Recover", PlyHPCap * 0.4, "HP. - 3 Mana")
        if PlyLevel >= 11:
            print("Infected Blood - Perform a regular attack that inflicts Poison DoT against the enemy. - 4 Mana")
        if PlyLevel >= 15:
            print("Overwhelming Blow - Perform a high DMG attack, but suffer +25% DMG Vulnerability on the enemy turn. - 5 Mana")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Crippling Affliction - Every 3 turns of combat or travel, you take 2 points of DMG.")
            print("Dedication To Survive - Every time Crippling Affliction damages you, gain +25% DMG for 1 turn.")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Crippling Affliction 1 - Every 4 turns of combat or travel, you take 2 points of DMG.")
            print("Dedication To Survive - Every time Crippling Affliction damages you, gain +25% DMG for 1 turn.")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Crippling Affliction 1 - Every 4 turns of combat or travel, you take 2 points of DMG.")
            print("Dedication To Survive 1 - Every time Crippling Affliction damages you, gain +25% DMG and +20% DMG Res for 1 turn.")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Crippling Affliction 2 - Every 4 turns of combat or travel, you take 2 points of DMG. Can be triggered manually.")
            print("Dedication To Survive 1 - Every time Crippling Affliction damages you, gain +25% DMG and +20% DMG Res for 1 turn.")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Crippling Affliction 2 - Every 4 turns of combat or travel, you take 2 points of DMG. Can be triggered manually.")
            print("Dedication To Survive 2 - Every time Crippling Affliction damages you, gain +25% DMG, +20% DMG Res and +10 Accuracy for 1 turn.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Crippling Affliction 3 - Every 5 turns of combat or travel, you take 2 points of DMG. Can be triggered manually.")
            print("Dedication To Survive 2 - Every time Crippling Affliction damages you, gain +25% DMG, +20% DMG Res and +10 Accuracy for 1 turn.")
        elif PlyLevel >= 25:
            print("Crippling Affliction 3 - Every 5 turns of combat or travel, you take 2 points of DMG. Can be triggered manually.")
            print("Dedication To Survive 3 - Every time Crippling Affliction damages you, gain +25% DMG, +20% DMG Res and +10 Accuracy for 3 turns.")
        if PlyLevel == 30:
            print("Mastery: Crippling Affliction is paused during travel.")
    elif PlyCharType == "Rogue":
        print("\nSpells:")
        if PlyLevel < 19:
            print("Vanish - Reduce Enemy Accuracy by -25 and increase your Critical Hit Chance by +15 for 3 turns. - 2 Mana - Upgrades at Level 19")
        elif PlyLevel >= 19:
            print("Vanish - Reduce Enemy Accuracy by -25 and increase your Critical Hit Chance by +15 for 3 turns. Does not end turn. - 2 Mana")
        if PlyLevel >= 3 and PlyLevel < 23:
            print("Caltrops - The enemy takes 3 DMG every time they hit you. Can trigger 3 times. Does not end the turn. - 3 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Caltrops - The enemy takes 3 DMG every time they attack you. Can trigger 5 times. Does not end the turn. - 3 Mana")
        if PlyLevel >= 7:
            print("Poisoned Blades - Attacks that hit cause the enemy to suffer Poison DoT. Lasts 3 turns, does not end your turn. - 4 Mana")
        if PlyLevel >= 11 and PlyLevel < 27:
            print("Backstab - Perform an attack that has +15 Critical Hit Chance and +3 DMG, but -25 Accuracy. - 5 Mana - Upgrades at Level 27")
        elif PlyLevel > 27:
            print("Backstab - Perform an attack that has +15 Critical Hit Chance and +3 DMG. - 5 Mana")
        if PlyLevel >= 15:
            print("Smoke Bomb - Escape the encounter and continue traveling. You will not gain any XP or Gold by doing this. - 6 Mana")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Assassins Precision - Naturally high Critical Hit and Parry chance.")
            print("Lethal Wounds - Critical Hits have a 25% chance to inflict Bleeding for 3 turns.")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Assassins Precision 1 - Naturally high Critical Hit and Parry chance, +5%")
            print("Lethal Wounds - Critical Hits have a 25% chance to inflict Bleeding for 3 turns.")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Assassins Precision 1 - Naturally high Critical Hit and Parry chance, +5%")
            print("Lethal Wounds 1 - Critical Hits have a 40% chance to inflict Bleeding for 3 turns.")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Assassins Precision 2 - Naturally high Critical Hit and Parry chance, +5%. Parries can crit at 25% of your base Critical Hit Chance.")
            print("Lethal Wounds 1 - Critical Hits have a 40% chance to inflict Bleeding for 3 turns.")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Assassins Precision 2 - Naturally high Critical Hit and Parry chance, +5%. Parries can crit at 25% of your base Critical Hit Chance.")
            print("Lethal Wounds 2 - Critical Hits have a 50% chance to inflict Bleeding for 3 turns. +3 DMG vs Bleeding enemies.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Assassins Precision 3 - Naturally high Critical Hit and Parry chance, +5%. Parries can crit at 50% of your base Critical Hit Chance.")
            print("Lethal Wounds 2 - Critical Hits have a 50% chance to inflict Bleeding for 3 turns. +3 DMG vs Bleeding enemies.")
        elif PlyLevel >= 25:
            print("Assassins Precision 3 - Naturally high Critical Hit and Parry chance, +5%. Parries can crit at 50% of your base Critical Hit Chance.")
            print("Lethal Wounds 3 - Critical Hits have a 50% chance to inflict permanent Bleeding. +3 DMG vs Bleeding enemies.")
        if PlyLevel == 30:
            print("Mastery: Critical Hits that deal >50% of the enemy HP in one attack instantly kill.")
    elif PlyCharType == "Cleric":
        print("\nSpells:")
        if PlyLevel < 19:
            print("Confuse - Reduce Enemy Accuracy by -25. Does not end your turn. - 2 Mana - Upgrades at Level 19")
        elif PlyLevel >= 19:
            print("Confuse - Reduce Enemy Accuracy by -25 and DMG by -3. Does not end your turn. - 2 Mana")
        if PlyLevel >= 3:
            print("Purged By Light - Smite your enemy with holy light, dealing bonus damage. +50% DMG vs Unholy Enemies. - 3 Mana")
        if PlyLevel >= 7 and PlyLevel < 23:
            print("Self Heal - Recover", PlyHPCap * 0.2, "HP. - 4 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Self Heal - Recover", PlyHPCap * 0.4, "HP. - 4 Mana")
        if PlyLevel >= 11:
            print("Armaments of Light - Gain +3(5) DMG, +25(33) Accuracy and +3(5) DMG Res for 3 turns (vs Unholy enemies) - 5 Mana")
        if PlyLevel >= 15 and PlyLevel < 27:
            print("Bathed in Light - Fully heal and deal massive DMG vs the enemy. +25% DMG vs Unholy enemies - 6 Mana - Upgrades at Level 27")
        elif PlyLevel >= 27:
            print("Bathed in Light - Fully heal, gain +3 DMG Res for 5 turns and deal massive DMG vs the enemy. +25% DMG vs Unholy enemies - 6 Mana")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Guarded By The Light - +2 DMG Res vs Unholy.")
            print("Natural Regeneration - 1HP/Turn.")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Guarded By The Light 1 - +2 DMG Res, DMG vs Unholy.")
            print("Natural Regeneration - 1HP/Turn.")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Guarded By The Light 1 - +2 DMG Res, DMG vs Unholy.")
            print("Natural Regeneration 1 - 2HP/Turn.")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Guarded By The Light 2 - +2 DMG Res, DMG and +15 Accuracy vs Unholy.")
            print("Natural Regeneration 1 - 2HP/Turn.")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Guarded By The Light 2 - +2 DMG Res, DMG and +15 Accuracy vs Unholy.")
            print("Natural Regeneration 2 - 2 Mana + HP/Turn.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Guarded By The Light 3 - +2 DMG Res, DMG, +15 Accuracy and +20 Critical Hit Chance vs Unholy.")
            print("Natural Regeneration 2 - 2 Mana + HP/Turn.")
        elif PlyLevel >= 25:
            print("Guarded By The Light 3 - +2 DMG Res, DMG, +15 Accuracy and +20 Critical Hit Chance vs Unholy.")
            print("Natural Regeneration 3 - 3 Mana + HP/Turn.")
        if PlyLevel == 30:
            print("Mastery: Gain the Revive ability. When killed during combat, recover to full HP and Mana. 20 turn cooldown.")
    elif PlyCharType == "Plague Doctor":
        print("\nSpells:")
        print("Diseased Victim - Perform an attack that deals +50%(+75%) DMG vs Poisoned Enemy. (Viral Overload) - 2 Mana")
        if PlyLevel >= 3:
            print("Stronger Dose - Your next attack inflicts Poison that deals +2(+3) DMG and lasts 3(4) turns longer. Does not end your turn. (Viral Overload) - 3 Mana")
        if PlyLevel >= 7 and PlyLevel < 19:
            print("Crude Bandages - Heal yourself for", PlyHPCap * 0.2, "HP. - 4 Mana - Upgrades at Level 19")
        elif PlyLevel >= 19:
            print("Crude Bandages - Heal yourself for", PlyHPCap * 0.4, "HP. - 4 Mana")
        if PlyLevel >= 11 and PlyLevel < 23:
            print("Blood Letting - Attack 3 times in a row with a -15 Accuracy penalty. Each attack rolls for hit chance. Each hit stacks Poison DMG and Duration. - 5 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Blood Letting - Attack 3 times in a row. Each attack rolls for hit chance. Each hit stacks Poison DMG and Duration. - 5 Mana")
        if PlyLevel >= 15 and PlyLevel < 27:
            print("Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. - 6 Mana - Upgrades at Level 27")
        elif PlyLevel >= 27:
            print("Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. Does not end your turn. - 6 Mana")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Poisoned Blades - Attacks inflict 1 turn of poison that deals 2 damage.")
            print("Poison Affinity - Gain +5 Accuracy and +10 Crit Chance vs Poisoned enemies.")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Poisoned Blades 1 - Attacks inflict 2 turns of poison that deals 2 damage.")
            print("Poison Affinity - Gain +5 Accuracy and +10 Crit Chance vs Poisoned enemies.")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Poisoned Blades 1 - Attacks inflict 2 turns of poison that deals 2 damage.")
            print("Poison Affinity 1 - Gain +5 Accuracy, +10 Dodge and +10 Crit Chance vs Poisoned enemies.")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Poisoned Blades 2 - Attacks inflict 3 turns of poison that deals 2 damage.")
            print("Poison Affinity 1 - Gain +5 Accuracy, +10 Dodge and +10 Crit Chance vs Poisoned enemies.")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Poisoned Blades 2 - Attacks inflict 3 turns of poison that deals 2 damage.")
            print("Poison Affinity 2 - Gain +5 Accuracy, +10 Dodge and +10 Crit Chance vs Poisoned enemies. Poisoned enemies suffer a -20 Accuracy debuff.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Poisoned Blades 3 - Attacks inflict 3 turns of poison that deals 3 damage.")
            print("Poison Affinity 2 - Gain +5 Accuracy, +10 Dodge and +10 Crit Chance vs Poisoned enemies. Poisoned enemies suffer a -20 Accuracy debuff.")
        elif PlyLevel >= 25:
            print("Poisoned Blades 3 - Attacks inflict 3 turns of poison that deals 3 damage.")
            print("Poison Affinity 3 - Gain +2 DMG, +5 Accuracy, +10 Dodge and +10 Crit Chance vs Poisoned enemies. Poisoned enemies suffer a -20 Accuracy debuff.")
        if PlyLevel == 30:
            print("Mastery: Poison ignores enemy immunity.")
    elif PlyCharType == "Scavenger":
        print("\nSpells:")
        if PlyLevel < 19:
            print("Scrapper - Throw sharp pieces of metal at the enemy, causing them to suffer bleeding. Does not end turn. - 2 Mana - Upgrades at Level 19")
        elif PlyLevel >= 19:
            print("Scrapper - Throw sharp knives fashioned from metal at the enemy, causing them to suffer bleeding. +20 Accuracy. Does not end turn. - 2 Mana")
        if PlyLevel >= 3 and PlyLevel < 23:
            print("Improvised Weaponry - Perform a regular attack that deals -50% DMG but inflicts Bleeding and Poison. - 3 Mana - Upgrades at Level 23")
        elif PlyLevel >= 23:
            print("Improvised Weaponry - Perform a regular attack that deals -25% DMG but inflicts Bleeding and Poison. - 3 Mana")
        if PlyLevel >= 7:
            print("Scrap Shield - Increase Parry Chance +20 and gain +2 Guard DMG Res for 3 Guarded hits. - 4 Mana")
        if PlyLevel >= 11 and PlyLevel < 27:
            print("Scrap Metal Armor - Improvised armor that grants +2 DMG reduction for 3 hits - 5 Mana - Upgrades at Level 27")
        elif PlyLevel >= 27:
            print("Scrap Metal Armor - Improvised armor that grants +3 DMG reduction for 5 hits - 5 Mana")
        if PlyLevel >= 15:
            print("Handmade Bomb - Throw a bomb, inflicting massive DMG and Bleeding.")
        print("\nSkills:")
        if PlyLevel < 5:
            print("Scavenging - Chance to loot 1-3 materials is 20%")
            print("Looting - Gold earned from fights is +15%")
        elif PlyLevel >= 5 and PlyLevel < 9:
            print("Scavenging 1 - Chance to loot 1-3 materials is 25%")
            print("Looting - Gold earned from fights is +15%")
        elif PlyLevel >= 9 and PlyLevel < 13:
            print("Scavenging 1 - Chance to loot 1-3 materials is 25%")
            print("Looting 1 - Gold earned from fights is +20%")
        elif PlyLevel >= 13 and PlyLevel < 17:
            print("Scavenging 2 - Chance to loot 1-3 materials is 25%. 20% chance to loot additional materials.")
            print("Looting 1 - Gold earned from fights is +20%")
        elif PlyLevel >= 17 and PlyLevel < 21:
            print("Scavenging 2 - Chance to loot 1-3 materials is 25%. 20% chance to loot additional materials.")
            print("Looting 2 - Gold earned from fights is +25%. Merchants are 10% cheaper.")
        elif PlyLevel >= 21 and PlyLevel < 25:
            print("Scavenging 3 - Chance to loot 3-6 materials is 25%. 20% chance to loot additional materials. Items require 15% less materials to craft.")
            print("Looting 2 - Gold earned from fights is +25%. Merchants are 10% cheaper.")
        elif PlyLevel >= 25:
            print("Scavenging 3 - Chance to loot 3-6 materials is 25%. 20% chance to loot additional materials. Items require 15% less materials to craft.")
            print("Looting 2 - Gold earned from fights is +25%. Merchants are 20% cheaper. 10% chance to receive potions from enemies.")
        if PlyLevel == 30:
            print("Mastery: 5% chance to receive a free item from killed enemies.")
    input("\nPress ENTER to continue")

QuietForestEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bandit", "Dire Wolf", "Boar", "Fungus", "Bear"]
EvilForestEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bandit", "Corrupted Wolf", "Corrupt Boar", "Evil Fairy", "Corrupted Fungus", "Vampire"]
OpenFieldEnemy = ["Bandit", "Dire Wolf", "Boar", "Dark Knight"]
GraveyardEnemy = ["Zombie", "Skeleton", "Ghost", "Cultist"]
SmallHillEnemy = ["Angry Goat", "Angry Eagle", "Vicious Hawk", "Snake"]
VillageEnemy = ["Raving Madman", "Infected Villager", "Corrupt Priest", "Angry Farmer", "Rotting Cow", "Vicious Hound"]
OpenPathEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Bear", "Bandit", "Boar", "Raving Madman", "Dark Knight"]

WeakEnemy = ["Green Slime", "Blue Slime", "Red Slime", "Corrupt Boar", "Evil Fairy", "Zombie", "Snake", "Boar", "Rotting Cow"]
NormalEnemy = ["Bandit", "Bear", "Dire Wolf", "Fungus", "Corrupted Fungus", "Corrupted Wolf", "Skeleton", "Ghost", "Cultist", "Angry Goat", "Angry Eagle", "Vicious Hawk", "Raving Madman", "Infected Villager", "Corrupt Priest", "Angry Farmer", "Vicious Hound", "Mimic"]
StrongEnemy = ["Vampire", "Dark Knight"]

UnholyEnemy = ["Zombie", "Skeleton", "Infected Villager", "Corrupt Priest", "Rotting Cow", "Vicious Hound", "Cultist", "Vampire"]
PoisonImmune = ["Green Slime", "Blue Slime", "Red SLime", "Skeleton", "Ghost"]
CaltropImmune = ["Evil Fairy", "Ghost", "Angry Eagle", "Vicious Hawk", "Dark Knight"]

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
    if PlyHP <= 0 and Alive == True:
        if PlyCharType == "Cleric" and PlyLevel == 30 and ClericRevive == 0:
            print("You are revived from death!")
            PlyHP = PlyHPCap
            PlyMana = PlyManaCap
            ClericRevive = 20
        else:
            Alive = False

    PlyHPCap = PlyStartHPCap + (2 * PlyLevel)
    PlyManaCap = PlyStartManaCap + (1 * PlyLevel)
    PlyDamage = random.randrange(int(MinDMG), int(MaxDMG)) + PlyDamageBuff + PlySpellDamageBuff + PlyAddDamageBuff + PlyLevel
    if PlyLevel < 30:
        XPRequired = 15 + (5 * PlyLevel)
    elif PlyLevel == 30:
        XPRequired = "Disabled"
    if PlyCharType == "Cleric":
        if PlyLevel >= 17 and PlyLevel < 25:
            ClericManaBonus = 1
        elif PlyLevel >= 25:
            ClericManaBonus = 2
    if PlyLevel >= 5 and PlyCharType == "Rogue":
        RogueCritBonus = 1
    if PlyLevel == 30 and PlyCharType == "Plague Doctor" and PoisonImmune.count() != 0:
        PoisonImmune.clear()
    if PlyXP >= XPRequired:
        PlyXP = PlyXP - XPRequired
        PlyLevel = PlyLevel + 1
        print("\nYou have leveled up!\n\nYou are now level", str(PlyLevel) + "!")
        if PlyLevel == 3:
            if PlyCharType == "Knight":
                print("\nYou have unlocked the spell Fiat Lux!")
            elif PlyCharType == "Leper":
                print("\nYou have unlocked the spell Do Your Worst!")
            elif PlyCharType == "Rogue":
                print("\nYou have unlocked the spell Caltrops")
            elif PlyCharType == "Cleric":
                print("\nYou have unlocked the spell Purged By Light")
            elif PlyCharType == "Plague Doctor":
                print("\nYou have unlocked the spell Stronger Dose")
            elif PlyCharType == "Scavenger":
                print("\nYou have unlocked the spell Improvised Weaponry")
        elif PlyLevel == 5:
            if PlyCharType == "Knight":
                print("Skill Improved: Knights Guard 1 - Guard has a 5% chance to negate all damage")
            elif PlyCharType == "Leper":
                print("Skill Improved: Crippling Affliction 1 - Damage triggers every 4 turns")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Assassins Precision 1 - Crit and Parry chance are increased by another +5%")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Guarded By The Light 1 - +2 DMG vs Unholy")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poisoned Blades 1 - Poison lasts 2 turns")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Scavenging 1 - Increase chance of materials by +5%")
        elif PlyLevel == 7:
            if PlyCharType == "Knight":
                print("\nYou have unlocked the spell Bolster Shield")
            elif PlyCharType == "Leper":
                print("\nYou have unlocked the spell Short Respite")
            elif PlyCharType == "Rogue":
                print("\nYou have unlocked the spell Poisoned Blades")
            elif PlyCharType == "Cleric":
                print("\nYou have unlocked the spell Self Heal")
            elif PlyCharType == "Plague Doctor":
                print("\nYou have unlocked the spell Crude Bandages")
            elif PlyCharType == "Scavenger":
                print("\nYou have unlocked the spell Scrap Shield")
        elif PlyLevel == 9:
            if PlyCharType == "Knight":
                print("Skill Improved: Apothecarys Boon 1 - Potions are 25% stronger")
            elif PlyCharType == "Leper":
                print("Skill Improved: Dedication To Survive 1 - Every time Crippling Affliction damages you, gain 20% DMG reduction as well")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Lethal Wounds 1 - Critical Hits have a 40% chance to inflict Bleeding")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Natural Regeneration 1 - 2HP/Turn")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poison Affinity 1 - Gain +10 Dodge vs Poisoned enemies")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Increase gold earned to 20%")
        elif PlyLevel == 11:
            if PlyCharType == "Knight":
                print("\nYou have unlocked the spell Crusade Banner")
            elif PlyCharType == "Leper":
                print("\nYou have unlocked the spell Infected Blood")
            elif PlyCharType == "Rogue":
                print("\nYou have unlocked the spell Backstab")
            elif PlyCharType == "Cleric":
                print("\nYou have unlocked the spell Regeneration")
            elif PlyCharType == "Plague Doctor":
                print("\nYou have unlocked the spell Blood Letting")
            elif PlyCharType == "Scavenger":
                print("\nYou have unlocked the spell Scrap Metal Armor")
        elif PlyLevel == 13:
            if PlyCharType == "Knight":
                print("Skill Improved: Knights Guard 2 - Increase chance of parry crits by +5%")
            elif PlyCharType == "Leper":
                print("Skill Improved: Crippling Affliction 2 - Crippling Affliction can be triggered at any time.\nThis will reset the timer and trigger buffs from Dedication to Survive")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Assassins Precision 2 - Parries can now Crit at 25% of base Crit Chance")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Guarded By The Light 2 - +15 Accuracy vs Unholy")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poisoned Blades 2 - Poison lasts 3 turns")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Scavenging 2 - 20% Chance to loot extra materials")
        elif PlyLevel == 15:
            if PlyCharType == "Knight":
                print("\nYou have unlocked the spell Shoulder Charge")
            elif PlyCharType == "Leper":
                print("\nYou have unlocked the spell Overwhelming Blow")
            elif PlyCharType == "Rogue":
                print("\nYou have unlocked the spell Smoke Bomb")
            elif PlyCharType == "Cleric":
                print("\nYou have unlocked the spell Mana Regeneration")
            elif PlyCharType == "Plague Doctor":
                print("\nYou have unlocked the spell Viral Overload")
            elif PlyCharType == "Scavenger":
                print("\nYou have unlocked the spell Handmade Bomb")
        elif PlyLevel == 17:
            if PlyCharType == "Knight":
                print("Skill Improved: Apothecarys Boon 2 - Gain a 20% chance to not lose a potion when used")
            elif PlyCharType == "Leper":
                print("Skill Improved: Dedication To Survive 2 - Every time Crippling Affliction damages you, gain +10 Accuracy")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Lethal Wounds 2 - Critical Hits have a 50% chance to inflict Bleeding. +3 DMG vs Bleeding enemies")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Natural Regeneration 2 - 2 Mana/Turn")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poison Affinity 2 - Poisoned enemies suffer a -20 Accuracy debuff")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Increase gold earned to 25%, Merchant is 10% cheaper")
        elif PlyLevel == 19:
            if PlyCharType == "Knight":
                print("Spell Upgraded: Bolster Shield has a +15 Chance to Crit when Parrying")
            elif PlyCharType == "Leper":
                print("Spell Upgraded: Ready To Strike no longer ends your turn")
            elif PlyCharType == "Rogue":
                print("Spell Upgraded: Vanish no longer ends your turn")
            elif PlyCharType == "Cleric":
                print("Spell Upgraded: Confuse now reduces enemy DMG by -25%")
            elif PlyCharType == "Plague Doctor":
                print("Spell Upgraded: Crude Bandages now heals for 40% of your HP")
            elif PlyCharType == "Scavenger":
                print("Spell Upgraded: Scrapper gains +20 Accuracy")
        elif PlyLevel == 21:
            if PlyCharType == "Knight":
                print("Skill Improved: Knights Guard 3 - Guard has a 7% chance to negate all damage. Guard DMG Res is increased by +2")
            elif PlyCharType == "Leper":
                print("Skill Improved: Crippling Affliction 3 - Damage triggers every 5 turns")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Assassins Precision 3 - Parries can now Crit at 50% of base chance")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Guarded By The Light 3 - +20 Crit Chance vs Unholy")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poisoned Blades 3 - Poison deals 3 damage")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Scavenging 3 - Items require 15% less material to craft. Loot 3x more materials.")
        elif PlyLevel == 23:
            if PlyCharType == "Knight":
                print("Spell Upgraded: Crusade Banner no longer ends turn and lasts 5 turns")
            elif PlyCharType == "Leper":
                print("Spell Upgraded: Do Your Worst! retaliation deals full DMG")
            elif PlyCharType == "Rogue":
                print("Spell Upgraded: Caltrops now trigger every time the enemy attacks and last 5 attacks")
            elif PlyCharType == "Cleric":
                print("Spell Upgraded: Self Heal now heals for 40% of Max HP")
            elif PlyCharType == "Plague Doctor":
                print("Spell Upgraded: Blood Letting now only has a -10 Accuracy Penalty")
            elif PlyCharType == "Scavenger":
                print("Spell Upgraded: Improvised Weaponry DMG Reduction is now only -25%")
        elif PlyLevel == 25:
            if PlyCharType == "Knight":
                print("Skill Improved: Apothecarys Boon 3 - Potions grant a random bonus buff when used.\n Only one buff can be active at once")
            elif PlyCharType == "Leper":
                print("Skill Improved: Dedication To Survive 3 - Crippling Affliction is no longer triggered by enemy damage")
            elif PlyCharType == "Rogue":
                print("Skill Improved: Lethal Wounds 3 - Critical Hits now cause permanent Bleeding on enemies. Bleeding deals +1 DMG")
            elif PlyCharType == "Cleric":
                print("Skill Improved: Natural Regeneration 3 - 3HP + Mana/Turn")
            elif PlyCharType == "Plague Doctor":
                print("Skill Improved: Poison Affinity 3 - Gain +2 DMG vs Poisoned enemies")
            elif PlyCharType == "Scavenger":
                print("Skill Improved: Looting 3 - Chance to loot potions from enemies. Merchant is 20% cheaper")
        elif PlyLevel == 27:
            if PlyCharType == "Knight":
                print("Spell Upgraded: Shoulder Charge now stuns the enemy for 1 turn")
            elif PlyCharType == "Leper":
                print("Spell Upgraded: Short Respite now heals for 30% HP")
            elif PlyCharType == "Rogue":
                print("Spell Upgraded: Backstab no longer has an accuracy penalty")
            elif PlyCharType == "Cleric":
                print("Spell Upgraded: Bathed In Light grants +3 DMG Res for 5 turns")
            elif PlyCharType == "Plague Doctor":
                print("Spell Upgraded: Viral Overload no longer ends your turn")
            elif PlyCharType == "Scavenger":
                print("Spell Upgraded: Scrap Metal Armor now provides +3 DMG Res for 5 hits")
        elif PlyLevel == 30:
            if PlyCharType == "Knight":
                print("Mastery Unlocked: Automatically Guard at the end of your turn (Unless bolstered)")
            elif PlyCharType == "Leper":
                print("Mastery Unlocked: Crippling Affliction is paused during travel")
            elif PlyCharType == "Rogue":
                print("Mastery Unlocked: Critical Hits that deal >50% of the enemy HP in one attack instantly kill.")
            elif PlyCharType == "Cleric":
                print("Mastery Unlocked: Gain the ability to Revive. Revive restores the Player to full HP and Mana. 20 turn cooldown")
            elif PlyCharType == "Plague Doctor":
                print("Mastery Unlocked: Poison can now affect ANY enemy")
            elif PlyCharType == "Scavenger":
                print("Mastery Unlocked: 5% Chance to receive a free item from killed enemies")
        PlyHPCap = PlyStartHPCap + (2 * PlyLevel)
        PlyManaCap = PlyStartManaCap + (1 * PlyLevel)
        PlyHP = PlyHP + 2
        PlyMana = PlyMana + 1
    if PlyHP > PlyHPCap:
        PlyHP = PlyHPCap
    if PlyMana > PlyManaCap:
        PlyMana = PlyManaCap

    if Afflicted == 1:
        print("\nYou are damaged by your affliction, taking 2 damage.")
        Affliction = 0
        PlyHP = PlyHP - 2
        if PlyHP <= 0 and Alive == True:
                Alive = False
        if InCombat == True:
            if PlyLevel < 9:
                print("You gain +3 DMG for this turn.")
                PlyBuffType = "DMG"
                PlyBuffTurns = 1
            elif PlyLevel >= 9 and PlyLevel < 17:
                print("You gain +3 DMG and +3 DMG Res for this turn.")
                PlyBuffType = "DMG DMG Res"
                PlyBuffTurns = 1
            elif PlyLevel >= 17 and PlyLevel < 25:
                print("You gain +3 DMG, +3 DMG Res and +10 Acc for this turn.")
                PlyBuffType = "Acc-10 DMG DMG Res"
                PlyBuffTurns = 1
            elif PlyLevel >= 25:
                print("You gain +3 DMG and +3 DMG Res and +10 Acc for this turn.")
                PlyBuffType = "Acc-10 DMG DMG Res"
                PlyBuffTurns = 3
        Afflicted = 0

    while Potions == 1:
        if PotionUsed == True:
            print("You cannot use a second potion this turn.")
            Potions = 0
        print("\nYou have:")
        if PlyAccPotions > 0:
            print("(1)", PlyAccPotions, "Accuracy potions")
        if PlyDodgePotions > 0:
            print("(2)", PlyDodgePotions, "Dodge potions")
        if PlyHPPotions > 0:
            print("(3)", PlyHPPotions, "Health potions")
        if PlyLuckPotions > 0:
            print("(4)", PlyLuckPotions, "Luck potions")
        if PlyResistancePotions > 0:
            print("(5)", PlyResistancePotions, "Resistance potions")
        if PlyStrengthPotions > 0:
            print("(6)", PlyStrengthPotions, "Strength potions")
        Choice = input("\nPotion: ")
        if Choice == 1 and PlyAccPotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyAccPotions = PlyAccPotions - 1
            else:
                    PlyAccPotions = PlyAccPotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Accuracy. You gain +25 Accuracy for 4 turns.")
                    PotionBuffType = "Acc+"
                    PotionBuffTurns = 4
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Accuracy. You gain +30 Accuracy for 5 turns.")
                    PotionBuffType = "Acc++"
                    PotionBuffTurns = 5
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Accuracy. You gain +30 Accuracy for 5 turns.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Dodge for 5 turns.")
                        PotionBuffType = "Acc++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain", PlyHPCap * 0.6, "HP.")
                        PlyHP = PlyHP + (PlyHPCap * 0.6)
                        if PlyHP > PlyHPCap:
                            PlyHP = PlyHPCap
                            print("You now have", PlyHP, "health.")
                        PotionBuffType = "Acc++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Critical Hit Chance for 5 turns.")
                        PotionBuffType = "Acc++ Crit++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +5 Damage Resistance for 5 turns.")
                        PotionBuffType = "Acc++ DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage for 5 turns.")
                        PotionBuffType = "Acc++ DMG++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Accuracy. You gain +20 Accuracy for 3 turns.")
                PotionBuffType = "Acc"
                PotionBuffTurns = 3
                PotionUsed = "True"
        elif Choice == 2 and PlyDodgePotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyDodgePotions = PlyDodgePotions - 1
            else:
                    PlyDodgePotions = PlyDodgePotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Dodge. You gain +25 Dodge for 4 turns.")
                    PotionBuffType = "Dodge+"
                    PotionBuffTurns = 4
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Dodge. You gain +30 Dodge for 5 turns.")
                    PotionBuffType = "Dodge++"
                    PotionBuffTurns = 5
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Dodge. You gain +30 Dodge for 5 turns.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Accuracy for 5 turns.")
                        PotionBuffType = "Acc++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain", PlyHPCap * 0.6, "HP.")
                        PlyHP = PlyHP + (PlyHPCap * 0.6)
                        if PlyHP > PlyHPCap:
                            PlyHP = PlyHPCap
                            print("You now have", PlyHP, "health.")
                        PotionBuffType = "Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Critical Hit Chance for 5 turns.")
                        PotionBuffType = "Crit++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +5 Damage Resistance for 5 turns.")
                        PotionBuffType = "DMG Res++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage for 5 turns.")
                        PotionBuffType = "DMG++ Dodge++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Dodge. You gain +20 Dodge for 3 turns.")
                PotionBuffType = "Dodge"
                PotionBuffTurns = 3
                PotionUsed = "True"
        elif Choice == 3 and PlyHPPotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyHPPotions = PlyHPPotions - 1
            else:
                    PlyHPPotions = PlyHPPotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Health. You gain", PlyHPCap * 0.5, "HP.")
                    PlyHP = PlyHP + (PlyHPCap * 0.5)
                    if PlyHP > PlyHPCap:
                        PlyHP = PlyHPCap
                    print("You now have", PlyHP, "health.")
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Health. You gain", PlyHPCap * 0.6, "HP.")
                    PlyHP = PlyHP + (PlyHPCap * 0.6)
                    if PlyHP > PlyHPCap:
                        PlyHP = PlyHPCap
                    print("You now have", PlyHP, "health.")
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Health. You gain", PlyHPCap * 0.6, "HP.")
                    PlyHP = PlyHP + (PlyHPCap * 0.6)
                    if PlyHP > PlyHPCap:
                        PlyHP = PlyHPCap
                    print("You now have", PlyHP, "health.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Accuracy for 5 turns.")
                        PotionBuffType = "Acc++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain +30 Dodge for 5 turns.")
                        PotionBuffType = "Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Critical Hit Chance for 5 turns.")
                        PotionBuffType = "Crit++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +5 Damage Resistance for 5 turns.")
                        PotionBuffType = "DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage for 5 turns.")
                        PotionBuffType = "DMG++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Health. You gain", PlyHPCap * 0.4, "HP.")
                PlyHP = PlyHP + (PlyHPCap * 0.4)
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                PotionUsed = "True"
        elif Choice == 4 and PlyLuckPotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyLuckPotions = PlyLuckPotions - 1
            else:
                    PlyLuckPotions = PlyLuckPotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Luck. You gain +25 Critical Hit Chance for 4 turns.")
                    PotionBuffType = "Crit+"
                    PotionBuffTurns = 4
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Luck. You gain +30 Critical Hit Chance for 5 turns.")
                    PotionBuffType = "Crit++"
                    PotionBuffTurns = 5
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Luck. You gain +30 Critical Hit Chance for 5 turns.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Accuracy for 5 turns.")
                        PotionBuffType = "Acc++ Crit++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain", PlyHPCap * 0.6, "HP.")
                        PlyHP = PlyHP + (PlyHPCap * 0.6)
                        if PlyHP > PlyHPCap:
                            PlyHP = PlyHPCap
                            print("You now have", PlyHP, "health.")
                        PotionBuffType = "Crit++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Dodge for 5 turns.")
                        PotionBuffType = "Crit++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +5 Damage Resistance for 5 turns.")
                        PotionBuffType = "Crit++ DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage for 5 turns.")
                        PotionBuffType = "Crit++ DMG++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Luck. You gain +20 Critical Hit Chance for 3 turns.")
                PotionBuffType = "Crit"
                PotionBuffTurns = 3
                PotionUsed = "True"
        elif Choice == 5 and PlyResistancePotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyResistancePotions = PlyResistancePotions - 1
            else:
                    PlyResistancePotions = PlyResistancePotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Resistance. You gain +4 DMG Res for 4 turns.")
                    PotionBuffType = "DMG Res+"
                    PotionBuffTurns = 4
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Resistance. You gain +5 DMG Res for 5 turns.")
                    PotionBuffType = "DMG Res++"
                    PotionBuffTurns = 5
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Resistance. You gain +5 DMG Res for 5 turns.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Accuracy for 5 turns.")
                        PotionBuffType = "Acc++ DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain", PlyHPCap * 0.6, "HP.")
                        PlyHP = PlyHP + (PlyHPCap * 0.6)
                        if PlyHP > PlyHPCap:
                            PlyHP = PlyHPCap
                            print("You now have", PlyHP, "health.")
                        PotionBuffType = "DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Dodge for 5 turns.")
                        PotionBuffType = "DMG Res++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +30 Critical Hit Chance for 5 turns.")
                        PotionBuffType = "Crit++ DMG Res++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage for 5 turns.")
                        PotionBuffType = "DMG++ DMG Res++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Resistance. You gain +3 DMG Res for 3 turns.")
                PotionBuffType = "DMG Res"
                PotionBuffTurns = 3
                PotionUsed = "True"
        elif Choice == 6 and PlyStrengthPotions > 0:
            if PlyCharType == "Knight" and PlyLevel >= 17:
                NoPotion = random.randint(1,100)
                if NoPotion <= 20:
                    print("Apothecarys Boon! The potion is not used.")
                else:
                    PlyStrengthPotions = PlyStrengthPotions - 1
            else:
                    PlyStrengthPotions = PlyStrengthPotions - 1
            if PlyCharType == "Knight":
                if PlyLevel < 9:
                    print("\nYou use the Potion of Strength. You gain +4 DMG for 4 turns.")
                    PotionBuffType = "DMG+"
                    PotionBuffTurns = 4
                elif PlyLevel >= 9 and PlyLevel < 25:
                    print("\nYou use the Potion of Strength. You gain +5 DMG for 5 turns.")
                    PotionBuffType = "DMG++"
                    PotionBuffTurns = 5
                elif PlyLevel >= 25:
                    print("\nYou use the Potion of Strength. You gain +5 DMG for 5 turns.")
                    PotionRand = random.randint(1,5)
                    if PotionRand == 1:
                        print("Apothecarys Boon! You also gain +30 Accuracy for 5 turns.")
                        PotionBuffType = "Acc++ DMG++"
                        PotionBuffTurns = 5
                    elif PotionRand == 2:
                        print("Apothecarys Boon! You also gain", PlyHPCap * 0.6, "HP.")
                        PlyHP = PlyHP + (PlyHPCap * 0.6)
                        if PlyHP > PlyHPCap:
                            PlyHP = PlyHPCap
                            print("You now have", PlyHP, "health.")
                        PotionBuffType = "DMG++"
                        PotionBuffTurns = 5
                    elif PotionRand == 3:
                        print("Apothecarys Boon! You also gain +30 Dodge for 5 turns.")
                        PotionBuffType = "DMG++ Dodge++"
                        PotionBuffTurns = 5
                    elif PotionRand == 4:
                        print("Apothecarys Boon! You also gain +30 Critical Hit Chance for 5 turns.")
                        PotionBuffType = "Crit++ DMG++"
                        PotionBuffTurns = 5
                    elif PotionRand == 5:
                        print("Apothecarys Boon! You also gain +5 Damage Resistance for 5 turns.")
                        PotionBuffType = "DMG++ DMG Res++"
                        PotionBuffTurns = 5
                    PotionUsed = "True"
            else:
                print("\nYou use the Potion of Strength. You gain +3 DMG for 3 turns.")
                PotionBuffType = "DMG"
                PotionBuffTurns = 3
                PotionUsed = "True"

    while Casting == 1:
        if PotionBuffTurns > 0:
            if PotionBuffType == "Acc" or PotionBuffType == "Acc+" or PotionBuffType == "Acc++":
                if PotionBuffType == "Acc":
                    PotionAccBuff = 20
                elif PotionBuffType == "Acc+":
                    PotionAccBuff = 25
                elif PotionBuffType == "Acc++" or PotionBuffType == "Acc++ Crit++" or PotionBuffType == "Acc++ DMG++" or PotionBuffType == "Acc++ DMG Res++" or PotionBuffType == "Acc++ Dodge++":
                    PotionAccBuff = 30
                else:
                    PotionAccBuff = 0
            if PotionBuffType == "Crit" or PotionBuffType == "Crit+" or PotionBuffType == "Crit++":
                if PotionBuffType == "Crit":
                    PotionCritBuff = 20
                elif PotionBuffType == "Crit+":
                    PotionCritBuff = 25
                elif PotionBuffType == "Crit++" or PotionBuffType == "Acc++ Crit++" or PotionBuffType == "Crit++ DMG++" or PotionBuffType == "Crit++ DMG Res++" or PotionBuffType == "Crit++ Dodge++":
                    PotionCritBuff = 30
                else:
                    PotionCritBuff = 0
            if PotionBuffType == "DMG" or PotionBuffType == "DMG+" or PotionBuffType == "DMG++":
                if PotionBuffType == "DMG":
                    PotionDMGBuff = 3
                elif PotionBuffType == "DMG+":
                    PotionDMGBuff = 4
                elif PotionBuffType == "DMG++" or PotionBuffType == "Acc++ DMG++" or PotionBuffType == "Crit++ DMG++" or PotionBuffType == "DMG++ DMG Res++" or PotionBuffType == "DMG++ Dodge++":
                    PotionDMGBuff = 5
                else:
                    PotionDMGBuff = 0
            if PotionBuffType == "DMG Res" or PotionBuffType == "DMG Res+" or PotionBuffType == "DMG Res++":
                if PotionBuffType == "DMG Res":
                    PotionDMGResBuff = 3
                elif PotionBuffType == "DMG Res+":
                    PotionDMGResBuff = 4
                elif PotionBuffType == "DMG Res++" or PotionBuffType == "Acc++ DMG Res++" or PotionBuffType == "Crit++ DMG Res++" or PotionBuffType == "DMG++ DMG Res++" or PotionBuffType == "DMG Res++ Dodge++":
                    PotionDMGResBuff = 5
                else:
                    PotionDMGResBuff = 0
        if PlySpellBuffTurns > 0:
            if PlySpellBuffType == "Acc" or PlySpellBuffType == "Acc + DMG":
                PlySpellAccBuff = 25
            else:
                PlySpellAccBuff = 0
            if PlySpellBuffType == "DMG" or PlySpellBuffType == "Acc + DMG":
                PlySpellDamageBuff = 3
            else:
                PlySpellDamageBuff = 0
            if PlySpellBuffType == "Crit Chance":
                PlySpellCritBuff = 15
            else:
                PlySpellCritBuff = 0
        if PlyBuffTurns > 0:
            if PlyBuffType == "Acc-10 DMG DMG Res":
                PlyBuffAccBonus = 10
                PlyBuffDMGBonus = 3
                PlyBuffDMGResBonus = 3
            else:
                PlyBuffAccBonus = 0
                PlyBuffDMGBonus = 0
                PlyBuffDMGResBonus = 0
            if PlyBuffType == "Acc":
                PlyBuffAccBonus = 25
            else:
                PlyBuffAccBonus = 0
            if PlyBuffType == "DMG" or PlyBuffType == "DMG DMG Res":
                PlyBuffDMGBonus = 3
            else:
                PlyBuffDMGBonus = 0
            if PlyBuffType == "DMG Res" or PlyBuffType == "DMG DMG Res":
                PlyBuffDMGResBonus = 3
            else:
                PlyBuffDMGResBonus = 0
            if PlyBuffType == "Crit Chance":
                PlyBuffCritBonus = 15
            else:
                PlyBuffCritBonus = 0
        PlyDamage = random.randrange(int(MinDMG), int(MaxDMG)) + PlyBuffDMGBonus + PlyDamageBuff + PlySpellDamageBuff + PlyAddDamageBuff + PlyLevel
        if PlyCharType == "Knight":
            print("\nChoose spell:")
            print("(0) Cancel")
            if CurEnemy in UnholyEnemy:
                print("(1) Holy Strike - Perform a special attack that deals bonus DMG. +50% DMG vs Unholy Enemy. - 2 Mana")
            else:
                print("(1) Holy Strike - Perform a special attack that deals bonus DMG. - 2 Mana")
            if PlyLevel >= 3:
                print("(2) Fiat Lux - Cast a blinding flash of light that reduces Enemy Accuracy by -25 for 3 turns. - 2 Mana")
            if PlyLevel >= 7 and PlyLevel < 19:
                print("(3) Bolster Shield - Raise your shield and parry the next enemy attack. - 3 Mana")
            elif PlyLevel > 19:
                print("(3) Bolster Shield - Raise your shield and parry the next enemy attack. +15 chance to crit on parry. - 3 Mana")
            if PlyLevel >= 11 and PlyLevel < 23:
                print("(4) Crusade Banner - Raise your banner and restore 5 HP. Gain +25 Accuracy and +3 DMG for 3 turns. - 4 Mana")
            elif PlyLevel >= 23:
                print("(4) Crusade Banner - Raise your banner and restore 5 HP. Gain +25 Accuracy and +3 DMG for 5 turns. Does not end your turn. - 4 Mana")
            if PlyLevel >= 15 and PlyLevel < 27:
                print("(5) Shoulder Charge - Charge the enemy dealing massive DMG. - 5 Mana")
            elif PlyLevel >= 27:
                print("(5) Shoulder Charge - Charge the enemy dealing massive DMG and Stunning them for 1 turn. - 5 Mana")
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
                CurEnemySpellDebuffType = "Acc"
                CurEnemySpellDebuffTurns = 3
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 7 and PlyMana >= 3:
                print("\nYou bolster your shield against the enemy attack.")
                PlyMana = PlyMana - 3
                PlyGuard = "Bolstered"
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 11 and PlyMana >= 4:
                print("\nYou raise your banner with holy fervor. You gain +25 Accuracy and +3 Damage for 3 turns.")
                print("You regain 5 HP.")
                PlyMana = PlyMana - 4
                PlyHP = PlyHP + 5
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "HP.")
                PlySpellBuffType = "Acc + DMG"
                if PlyLevel < 23:
                    WhoseTurn = 2
                    PlyBuffTurns = 3
                else:
                    PlyBuffTurns = 5
                Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 15 and PlyMana >= 5:
                print("You charge down the enemy, dealing massive damage.")
                print("You deal", math.ceil(PlyDamage * 1.5), "points of damage.")
                PlyMana = PlyMana - 5
                CurEnemyHP = CurEnemyHP - (math.ceil(PlyDamage * 1.5))
                if PlyLevel < 27:
                    WhoseTurn = 2
                else:
                    print("The enemy is stunned, giving you a free turn!")
                Casting = 0
        if PlyCharType == "Leper":
            print("Choose spell:")
            print("(0) Cancel")
            if PlyLevel < 19:
                print("(1) Ready to Strike - Your next attack has +25 Accuracy and +3 DMG. - 2 Mana")
            elif PlyLevel >= 19:
                print("(1) Ready to Strike - Your next attack has +25 Accuracy and +3 DMG. Does not end your turn. - 2 Mana")
            if PlyLevel >= 3 and PlyLevel < 23:
                print("(2) Do Your Worst! - The enemy gains +25 accuracy for their attack. You gain 50% DMG resistance and retaliate with a normal attack that deals 25% less DMG. - 3 Mana")
            elif PlyLevel >= 23:
                print("(2) Do Your Worst! - The enemy gains +25 accuracy for their attack. You gain 50% DMG resistance and retaliate with a normal attack. - 3 Mana")
            if PlyLevel >= 7 and PlyLevel < 27:
                print("(3) Short Respite - Recover", PlyHPCap * 0.2, "HP. - 3 Mana")
            elif PlyLevel >= 27:
                print("(3) Short Respite - Recover", PlyHPCap * 0.4, "HP. - 3 Mana")
            if PlyLevel >= 11:
                if CurEnemy in PoisonImmune:
                    print("(4) Infected Blood - Perform a regular attack that inflicts Poison DoT against the enemy. This enemy is immune to poison! - 4 Mana")
                else:
                    print("(4) Infected Blood - Perform a regular attack that inflicts Poison DoT against the enemy. - 4 Mana")
            if PlyLevel >= 15:
                print("(5) Overwhelming Blow - Perform a high DMG attack, but suffer +25% DMG Vulnerability on the enemy turn. - 5 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or ((SpellChoice == 2 or SpellChoice == 3) and PlyMana < 3) or (SpellChoice == 4 and PlyMana < 4) or (SpellChoice == 5 and PlyMana < 5):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou ready your blade for your next attack.")
                PlyMana = PlyMana - 2
                PlySpellBuffType = "Acc + DMG"
                PlySpellBuffTurns = 1
                if PlyLevel < 19:
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
            elif SpellChoice == 3 and PlyLevel >= 7 and PlyMana >= 3:
                if PlyHP == PlyHPCap:
                    print("\nYou are already at full health")
                    Casting = 0
                PlyMana = PlyMana - 3
                if PlyLevel < 27:
                    print("\nYou rest for a moment, recovering", PlyHPCap * 0.2, "HP.")
                    PlyHP = PlyHP + PlyHPCap * 0.2
                elif PlyLevel >= 27:
                    print("\nYou rest for a moment, recovering", PlyHPCap * 0.4, "HP.")
                    PlyHP = PlyHP + PlyHPCap * 0.4
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                WhoseTurn = 2
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 11 and PlyMana >= 4:
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
                        CurEnemyDoTType = "Poisoned"
                        CurEnemyDoTTurns = 3
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 15 and PlyMana >= 5:
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
            if PlyLevel < 19:
                print("(1) Vanish - Reduce Enemy Accuracy by -25 and increase your Critical Hit Chance by +15 for 3 turns. - 2 Mana")
            elif PlyLevel <= 19:
                print("(1) Vanish - Reduce Enemy Accuracy by -25 and increase your Critical Hit Chance by +15 for 3 turns. Does not end your turn. - 2 Mana")
            if PlyLevel >= 3 and PlyLevel < 23:
                if CurEnemy in CaltropImmune:
                    print("(2) Caltrops - The enemy takes 3 DMG every time they hit you. Can trigger 3 times. Does not end the turn. This enemy is immune to Caltrops. - 3 Mana")
                else:
                    print("(2) Caltrops - The enemy takes 3 DMG every time they hit you. Can trigger 3 times. Does not end the turn. - 3 Mana")
            elif PlyLevel >= 23:
                if CurEnemy in CaltropImmune:
                    print("(2) Caltrops - The enemy takes 3 DMG every time they attack you. Can trigger 5 times. Does not end the turn. This enemy is immune to Caltrops. - 3 Mana")
                else:
                    print("(2) Caltrops - The enemy takes 3 DMG every time they attack you. Can trigger 5 times. Does not end the turn. - 3 Mana")
            if PlyLevel >= 7:
                if CurEnemy in PoisonImmune:
                    print("(3) Poisoned Blades - Attacks that hit cause the enemy to suffer Poison DoT. Lasts 3 turns, does not end your turn. This enemy is immune to Poison - 4 Mana")
                else:
                    print("(3) Poisoned Blades - Attacks that hit cause the enemy to suffer Poison DoT. Lasts 3 turns, does not end your turn. - 4 Mana")
            if PlyLevel >= 11 and PlyLevel < 27:
                print("(4) Backstab - Perform an attack that has +15 Critical Hit Chance and +3 DMG, but -25 Accuracy. - 5 Mana")
            elif PlyLevel >= 27:
                print("(4) Backstab - Perform an attack that has +15 Critical Hit Chance and +3 DMG. - 5 Mana")
            if PlyLevel >= 15:
                print("(5) Smoke Bomb - Escape the encounter and continue traveling. You will not gain any XP or Gold by doing this. - 6 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or (SpellChoice == 2 and PlyMana < 3) or (SpellChoice == 3 and PlyMana < 4) or (SpellChoice == 4 and PlyMana < 5) or (SpellChoice == 5 and PlyMana < 6):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                if PlyBuffTurns == 3 and CurEnemyDebuffTurns == 3:
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    print("\nYou vanish into the shadows, ready to strike.")
                    PlyMana = PlyMana - 2
                    if PlySpellBuffType == "None":
                        PlySpellBuffType = "Crit Chance"
                    PlySpellBuffTurns = 3
                    CurEnemyDebuffType = "Acc"
                    CurEnemyDebuffTurns = 3
                    if PlyLevel < 19:
                        WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                if (CaltropHits == 3 and PlyLevel < 23) or (CaltropHits == 5 and PlyLevel >= 23):
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    print("\nYou drop Caltrops to disrupt the enemy.")
                    PlyMana = PlyMana - 3
                    if PlyLevel < 23:
                        CaltropHits = 3
                    elif PlyLevel >= 23:
                        CaltropHits = 5
                    Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 7 and PlyMana >= 4:
                if PlyBuffTurns == 3:
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    print("\nYou coat your blades in poison, increasing their lethality.")
                    PlyMana = PlyMana - 4
                    if PlyBuffType == "None":
                        PlyBuffType = "Poison"
                    PlyBuffTurns = 3
                    Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 11 and PlyMana >= 5:
                print("\nYou attempt to backstab the enemy.")
                Accuracy = random.randrange(1, 100)
                PlyMana = PlyMana - 5
                if PlyLevel < 27:
                    BackstabAccuracy = PlyAccuracy - 25
                elif PlyLevel >= 27:
                    BackstabAccuracy = PlyAccuracy
                if Accuracy <= BackstabAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance + 10:
                        print("Critical Hit!")
                        PlyDamage = (PlyDamage + 2) * 2
                    print("You deal", math.ceil(PlyDamage * 1.33), "points of damage.")
                    CurEnemyHP = CurEnemyHP - (math.ceil(PlyDamage * 1.33))
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > BackstabAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 5 and PlyLevel >= 15 and PlyMana >= 6:
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
            if PlyLevel < 19:
                print("(1) Confuse - Reduce Enemy Accuracy by -25. Does not end your turn. - 2 Mana")
            elif PlyLevel >= 19:
                print("(1) Confuse - Reduce Enemy Accuracy by -25 and DMG by -3. Does not end your turn. - 2 Mana")
            if PlyLevel >= 3:
                if CurEnemy in UnholyEnemy:
                    print("(2) Purged By Light - Smite your enemy with holy light, dealing bonus damage. +50% DMG vs Unholy Enemy. - 3 Mana")
                else:
                    print("(2) Purged By Light - Smite your enemy with holy light, dealing bonus damage. - 3 Mana")
            if PlyLevel >= 7 and PlyLevel < 23:
                print("(3) Self Heal - Recover", PlyHPCap * 0.2, "HP. - 4 Mana")
            elif PlyLevel >= 23:
                print("(3) Self Heal - Recover", PlyHPCap * 0.4, "HP. - 4 Mana")
            if PlyLevel >= 11:
                if CurEnemy in UnholyEnemy:
                    print("(4) Armaments of Light - Gain +5 DMG, +33 Accuracy and +5 DMG Res for 3 turns - 5 Mana")
                else:
                    print("(4) Armaments of Light - Gain +3 DMG, +25 Accuracy and +3 DMG Res for 3 turns - 5 Mana")
            if PlyLevel >= 15 and PlyLevel < 27:
                if CurEnemy in UnholyEnemy:
                    print("(5) Bathed in Light - Fully heal and deal massive DMG vs the enemy. +25% DMG vs Unholy - 6 Mana")
                else:
                    print("(5) Bathed in Light - Fully heal and deal massive DMG vs the enemy - 6 Mana")
            elif PlyLevel >= 27:
                if CurEnemy in UnholyEnemy:
                    print("(5) Bathed in Light - Fully heal, gain +3 DMG Res for 5 turns and deal massive DMG vs the enemy. +25% DMG vs Unholy - 6 Mana")
                else:
                    print("(5) Bathed in Light - Fully heal, gain +3 DMG Res for 5 turns and deal massive DMG vs the enemy - 6 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or (SpellChoice == 2 and PlyMana < 3) or (SpellChoice == 3 and PlyMana < 4) or (SpellChoice == 4 and PlyMana < 5) or (SpellChoice == 5 and PlyMana < 6):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou cast a ray of light to confuse the enemy.")
                if CurEnemySpellDebuffTurns == 3:
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    PlyMana = PlyMana - 2
                    if PlyLevel < 19:
                        CurEnemySpellDebuffType = "Acc"
                    elif PlyLevel >= 19:
                        CurEnemySpellDebuffType = "Acc + DMG"
                    CurEnemySpellDebuffTurns = 3
                    Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                print("\nYou purge the enemy with holy light.")
                PlyMana = PlyMana - 3
                Accuracy = random.randrange(1, 100)
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
            elif SpellChoice == 3 and PlyLevel >= 7 and PlyMana >= 4:
                if PlyHP == PlyHPCap:
                    print("\nYou are already at full health")
                    Casting = 0
                PlyMana = PlyMana -4
                if PlyLevel < 23:
                    print("\nYou heal yourself for", PlyHPCap * 0.2, "HP.")
                    PlyHP = PlyHP + PlyHPCap * 0.2
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 11 and PlyMana >= 5:
                if (PlySpellBuffType == "AOL" or PlySpellBuffType == "Acc + DMG + DMG Res") and PlySpellBuffTurns == 3:
                    print("\nYou have already cast this spell!")
                    Casting = 0
                PlyMana = PlyMana - 5
                print("\nYou are blessed by Holy Light, making them stronger")
                if CurEnemy in UnholyEnemy:
                    PlySpellBuffType = "AOL"
                    PlySpellBuffTurns = 3
                else:
                    PlySpellBuffType = "Acc + DMG + DMG Res"
                    PlySpellBuffTurns = 3
            elif SpellChoice == 5 and PlyLevel >= 15 and PlyMana >= 6:
                PlyMana = PlyMana - 6
                PlyHP = PlyHPCap
                print("\nYou bathe the area in holy light.")
                print("You now have full health.")
                if PlyLevel >= 27:
                    if PlySpellBuffType != "AOL" or PlySpellBuffType != "Acc + DMG + DMG Res":
                        PlySpellBuffType = "DMG Res"
                        PlySpellBuffTurns = 5
                if CurEnemy in UnholyEnemy:
                    PlyDamage = math.ceil((PlyDamage * 1.5) * 1.25)
                else:
                    PlyDamage = math.ceil(PlyDamage * 1.5)
                print("You deal", PlyDamage, "points of damage.")
                CurEnemyHP = CurEnemyHP - PlyDamage
                Casting = 0
        if PlyCharType == "Plague Doctor":
            print("Choose spell:")
            print("(0) Cancel")
            if CurEnemyDebuffType == "Poisoned":
                print("(1) Diseased Victim - Perform an attack that deals +50% DMG vs Poisoned Enemy. - 2 Mana")
            elif CurEnemyDebuffType == "Viral Overload":
                print("(1) Diseased Victim - Perform an attack that deals +75% DMG vs Poisoned Enemy. - 2 Mana")
            elif CurEnemy in PoisonImmune:
                print("(1) Diseased Victim - Perform an attack that deals +50% DMG vs Poisoned Enemy. Enemy is immune to Poison. - 2 Mana")
            else:
                print("(1) Diseased Victim - Perform an attack that deals +50% DMG vs Poisoned Enemy. Enemy is not Poisoned. - 2 Mana")
            if PlyLevel >= 3:
                if CurEnemyDebuffType == "Viral Overload":
                    print("(2) Stronger Dose - Your next attack inflicts Poison that deals +3 DMG and lasts 4 turns longer. Does not end your turn. - 3 Mana")
                elif CurEnemy in PoisonImmune:
                    print("(2) Stronger Dose - Your next attack inflicts Poison that deals +2 DMG and lasts 3 turns longer. Does not end your turn. Enemy is immune to Poison. - 3 Mana")
                else:
                    print("(2) Stronger Dose - Your next attack inflicts Poison that deals +2 DMG and lasts 3 turns longer. Does not end your turn. - 3 Mana")
            if PlyLevel >= 7 and PlyLevel < 19:
                print("(3) Crude Bandages - Heal yourself for", PlyHPCap * 0.2, "HP. - 4 Mana")
            elif PlyLevel >= 19:
                print("(3) Crude Bandages - Heal yourself for", PlyHPCap * 0.4, "HP. - 4 Mana")
            if PlyLevel >= 11 and PlyLevel < 23:
                if CurEnemy in PoisonImmune:
                    print("(4) Blood Letting - Attack 3 times in a row with a -15 Accuracy penalty. Each attack rolls for hit chance. Enemy is immune to Poison. - 5 Mana")
                else:
                    print("(4) Blood Letting - Attack 3 times in a row with a -15 Accuracy penalty. Each attack rolls for hit chance. Each hit stacks Poison DMG and Duration. - 5 Mana")
            elif PlyLevel >= 23:
                if CurEnemy in PoisonImmune:
                    print("(4) Blood Letting - Attack 3 times in a row. Each attack rolls for hit chance. Enemy is immune to Poison. - 5 Mana")
                else:
                    print("(4) Blood Letting - Attack 3 times in a row. Each attack rolls for hit chance. Each hit stacks Poison DMG and Duration. - 5 Mana")
            if PlyLevel >= 15 and PlyLevel < 27:
                if CurEnemy in PoisonImmune:
                    print("(5) Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. Enemy is immune to Poison. - 6 Mana")
                else:
                    print("(5) Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. - 6 Mana")
            if PlyLevel >= 27:
                if CurEnemy in PoisonImmune:
                    print("(5) Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. Does not end your turn. Enemy is immune to Poison. - 6 Mana")
                else:
                    print("(5) Viral Overload - Permanently afflict the enemy with Poison. Diseased Victim and Stronger Dose are improved. Does not end your turn. - 6 Mana")
            SpellChoice = int(input("\nSpell: "))
            if (SpellChoice == 1 and PlyMana < 2) or (SpellChoice == 2 and PlyMana < 3) or (SpellChoice == 3 and PlyMana < 4) or (SpellChoice == 4 and PlyMana < 5) or (SpellChoice == 5 and PlyMana < 6):
                print("Not enough Mana!")
            if SpellChoice == 0:
                Casting = 0
            elif SpellChoice == 1 and PlyMana >= 2:
                print("\nYou attack the enemy.")
                PlyMana = PlyMana - 2
                Accuracy = random.randrange(1, 100)
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = (PlyDamage * 2)
                    else:
                        PlyDamage = PlyDamage
                    if CurEnemyDoTType == "Poisoned" or CurEnemyDoTType == "Strong Poisoned":
                        PlyDamage = math.ceil(PlyDamage * 1.5)
                    elif CurEnemyDoTType == "Viral Overload" or CurEnemyDoTType == "Viral Overload +":
                        PlyDamage = math.ceil(PlyDamage * 1.75)
                    else:
                        PlyDamage = PlyDamage
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    WhoseTurn = 2
                    Casting = 0
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    WhoseTurn = 2
                    Casting = 0
            elif SpellChoice == 2 and PlyLevel >= 3 and PlyMana >= 3:
                if PlagueAttacks == 2 or PlagueAttacks == 4:
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    print("\nYou replace your poison with a stronger kind.")
                    PlyMana = PlyMana - 3
                    PoisonDMGBuff = PoisonDMGBuff + 2
                    if PlagueAttacks == 1 or PlagueAttacks == 3:
                        PlagueAttacks = PlagueAttacks + 1
                    Casting = 0
            elif SpellChoice == 3 and PlyLevel >= 7 and PlyMana >= 4:
                print("\nYou heal yourself for 3 HP.")
                PlyMana = PlyMana -4
                PlyHP = PlyHP + 3
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                print("You now have", PlyHP, "health.")
                Casting = 0
            elif SpellChoice == 4 and PlyLevel >= 11 and PlyMana >= 5:
                print("\nYou swing rapidly, attacking the enemy three times.")
                BloodLet = 0
                PlyMana = PlyMana - 5
                while BloodLet < 3:
                    Accuracy = random.randrange(1, 100)
                    if Accuracy <= PlyAccuracy:
                        Crit = random.randrange(1, 100)
                        if Crit <= PlyCritChance:
                            print("Critical Hit!")
                            PlyDamage = (PlyDamage * 2)
                        else:
                            PlyDamage = PlyDamage
                        if CurEnemyDoTType == "Poisoned" or CurEnemyDoTType == "Strong Poisoned":
                            PlyDamage = math.ceil(PlyDamage * 1.5)
                        elif CurEnemyDoTType == "Viral Overload" or CurEnemyDoTType == "Viral Overload +":
                            PlyDamage = math.ceil(PlyDamage * 1.75)
                        else:
                            PlyDamage = PlyDamage
                        print("You deal", PlyDamage, "points of damage.")
                        if CurEnemy not in PoisonImmune:
                            CurEnemyHP = CurEnemyHP - PlyDamage
                            CurEnemyDoTType = "Poisoned"
                            if CurEnemyDoTTurns < 2:
                                CurEnemyDoTTurns = 2
                            else:
                                CurEnemyDoTTurns = CurEnemyDoTTurns + 1
                        PoisonDMGBuff = PoisonDMGBuff + 1
                        BloodLet = BloodLet + 1
                    elif Accuracy > PlyAccuracy:
                        print("Miss! You deal no damage.")
                        BloodLet = BloodLet + 1
                    if BloodLet == 3:
                        break
                Casting = 0
                WhoseTurn = 2
                BloodLet = 0
            elif SpellChoice == 5 and PlyLevel >= 15 and PlyMana >= 6:
                if CurEnemyDoTType == "Viral Overload" or CurEnemyDoTType == "Viral Overload +":
                    print("\nYou have already cast this spell!")
                    Casting = 0
                else:
                    PlyMana = PlyMana - 6
                    if CurEnemy in PoisonImmune:
                        print("\nYou attempt to poison the enemy, but they are immune.")
                    else:
                        print("\nYou overwhelm the opponents immune system, permanently poisoning them.")
                        CurEnemyDoTType = "Viral Overload"
                    PoisonDMGBuff = PoisonDMGBuff + 1
                    WhoseTurn = 2
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
                    RandomPotion = random.randint(1,6)
                    if RandomPotion == 1:
                        PotionType = "Acc"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Accuracy (+25 Accuracy) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Accuracy (+30 Accuracy) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Accuracy (+20 Accuracy) - 30 Gold"
                    elif RandomPotion == 2:
                        PotionType = "Crit"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Luck (+25 Critical Hit Chance) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Luck (+30 Critical Hit Chance) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Luck (+20 Critical Hit Chance) - 30 Gold"
                    elif RandomPotion == 3:
                        PotionType = "DMG"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Strength (+4 Damage) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Strength (+5 Damage) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Strength (+3 Damage) - 30 Gold"
                    elif RandomPotion == 4:
                        PotionType = "DMG Res"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Resistance (+4 Damage Resistance) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Resistance (+5 Damage Resistance) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Resistance (+3 Damage Resistance) - 30 Gold"
                    elif RandomPotion == 5:
                        PotionType = "HP"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Health (+50% Health) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Health (+60% Health) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Health (+40% Health) - 30 Gold"
                    elif RandomPotion == 6:
                        PotionType = "Dodge"
                        if PlyCharType == "Knight":
                            if PlyLevel < 9:
                                PotionLine = "\n - A Potion of Dodge (+25 Dodge) - 30 Gold"
                            elif PlyLevel >= 9:
                                PotionLine = "\n - A Potion of Dodge (+30 Dodge) - 30 Gold"
                        else:
                            PotionLine = "\n - A Potion of Dodge (+20 Dodge) - 30 Gold"
                else:
                    PotionLine = ""
                print("\nThe merchant is selling:", ArmorLine, SwordLine, ShieldLine, PotionLine)
                print("\nYou have", PlyGold, "gold")
                Purchase = input("\n(A)rmor - (W)eapon - (S)hield - (P)otion - (L)eave ")
                if (Purchase.casefold() == "armor" or Purchase.casefold() == "a") and ArmorBought != True:
                    if PlyGold >= 60:
                        print("\nYou purchase the armor")
                        TruePlyDMGRes = TruePlyDMGRes + 1
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
                        print("Your guard now protects against", PlyGuardRes, " points of damage.")
                        PlyGold = PlyGold - 40
                        print("Gold:", PlyGold)
                        ShieldBought = True
                    elif ShieldBought == True:
                        print('\nThe merchant says: "Sorry traveler, I got no more shields to sell ya"')
                    elif PlyGold < 40:
                        print('\nThe merchant chuckles and says: "Sorry, but you dont have enough gold for that"')
                elif (Purchase.casefold() == "p"or Purchase.casefold() == "potion") and PotionBought != True:
                    if PlyGold >= 30:
                        if PotionType == "Acc":
                            print("\nYou purchase the Potion of Accuracy")
                            PlyAccPotions = PlyAccPotions + 1
                            print("You now have", PlyAccPotions, "Potions.")
                        elif PotionType == "Crit":
                            print("\nYou purchase the Potion of Luck")
                            PlyLuckPotions = PlyLuckPotions + 1
                            print("You now have", PlyLuckPotions, "Potions.")
                        elif PotionType == "DMG":
                            print("\nYou purchase the Potion of Strength")
                            PlyStrengthPotions = PlyStrengthPotions + 1
                            print("You now have", PlyStrengthPotions, "Potions.")
                        elif PotionType == "DMG Res":
                            print("\nYou purchase the Potion of Resistance")
                            PlyResistancePotions = PlyResistancePotions + 1
                            print("You now have", PlyResistancePotions, "Potions.")
                        elif PotionType == "HP":
                            print("\nYou purchase the Potion of Health")
                            PlyHPPotions = PlyHPPotions + 1
                            print("You now have", PlyHPPotions, "Potions.")
                        elif PotionType == "Dodge":
                            print("\nYou purchase the Potion of Dodge")
                            PlyDodgePotions = PlyDodgePotions + 1
                            print("You now have", PlyDodgePotions, "Potions.")
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
        if PlyHP <= 0 and Alive == True:
            Alive = False
        print("\nHealth:", str(PlyHP) + "/" + str(PlyHPCap), "Mana:", str(PlyMana) + "/" + str(PlyManaCap), "Gold:", PlyGold)
        print("Level", PlyLevel, PlyCharType, "Experience:", str(PlyXP) + "/" + str(XPRequired))
        if CurPath != None and TurnsToTraverse > 0:
            print("\nThis path requires", TurnsToTraverse, "more turns to traverse through.")
            print("You must still travel", DistanceToTravel, "tiles to reach the castle.")
        else:
            print("\nYou must still travel", DistanceToTravel, "tiles to reach the castle.")
        if PlyCharType == "Leper" and PlyLevel < 30:
            if PlyLevel < 5:
                print("\nAffliction will trigger in", (3 - Affliction), "turn(s).")
            elif PlyLevel >= 5 and PlyLevel < 21:
                print("\nAffliction will trigger in", (4 - Affliction), "turn(s).")
            elif PlyLevel >= 21:
                print("\nAffliction will trigger in", (5 - Affliction), "turn(s).")
        Movement = input("\n(T)ravel - (R)est - (Sk)ills and Spells - (Sa)ve Game ")
        if Movement.casefold() == "save" or Movement.casefold() == "save game" or Movement.casefold() == "sa":
            print("Saving Game...")
            SaveGame()
        elif Movement.casefold() == "skills" or Movement.casefold() == "spells" or Movement.casefold() == "sk" or Movement.casefold() == "skills and spells":
            SkillsNSpells()
        elif Movement.casefold() == "travel" or Movement.casefold() == "t":
            print("\nYou continue traveling.")
            if ClericRevive > 0:
                ClericRevive = ClericRevive - 1
            if PlyCharType == "Leper" and PlyLevel < 30:
                Affliction = Affliction + 1
            if PlyCharType == "Leper":
                if PlyLevel < 5 and Affliction == 3:
                    Afflicted = 1
                elif PlyLevel >=5 and PlyLevel < 21 and Affliction == 4:
                    Afflicted = 1
                elif PlyLevel >= 21 and Affliction == 5:
                    Afflicted = 1
            if CurPath == None:
                Travel = random.randrange(1,15)
                if Travel == 1:
                    print("\nYou were ambushed during your travel!")
                    if CurPath == None:
                        CurPathEnemy = OpenPathEnemy
                    Ambush = True
                    InCombat = True
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
                        Chest = input("Open the chest Y/N ")
                        if Chest.casefold() == "y":
                            ChestEvent = random.randrange(1, 15)
                            if ChestEvent < 4:
                                print("\nThe chest contains nothing of interest")
                            elif ChestEvent >= 4 and ChestEvent <= 8:
                                print("\nYou find some gold inside the chest!")
                                PlyGold = PlyGold + random.randrange(10, 50)
                                print("You now have", PlyGold, "gold")
                            elif ChestEvent == 9:
                                print("\nYou find a new sword inside the chest!")
                                PlyDamageBuff = PlyDamageBuff + 1
                                print("You now deal", PlyDamageBuff, "additional points of damage")
                            elif ChestEvent == 10:
                                print("\nYou find new armor inside the chest!")
                                TruePlyDMGRes = TruePlyDMGRes + 1
                                print("You now have", TruePlyDMGRes, "points of damage resistance")
                            elif ChestEvent == 11:
                                print("\nYou find a new shield inside the chest!")
                                PlyGuardRes = PlyGuardRes + 1
                                print("Your guard now protects against", PlyGuardRes, "points of damage")
                            elif ChestEvent == 12:
                                RandomPotion = random.randint(1,6)
                                if RandomPotion == "Acc":
                                    print("\nYou find a Potion of Accuracy")
                                    PlyAccPotions = PlyAccPotions + 1
                                    print("You now have", PlyAccPotions, "Potions.")
                                elif RandomPotion == "Crit":
                                    print("\nYou find a Potion of Luck")
                                    PlyLuckPotions = PlyLuckPotions + 1
                                    print("You now have", PlyLuckPotions, "Potions.")
                                elif RandomPotion == "DMG":
                                    print("\nYou find a Potion of Strength")
                                    PlyStrengthPotions = PlyStrengthPotions + 1
                                    print("You now have", PlyStrengthPotions, "Potions.")
                                elif RandomPotion == "DMG Res":
                                    print("\nYou find a Potion of Resistance")
                                    PlyResistancePotions = PlyResistancePotions + 1
                                    print("You now have", PlyResistancePotions, "Potions.")
                                elif RandomPotion == "HP":
                                    print("\nYou find a Potion of Health")
                                    PlyHPPotions = PlyHPPotions + 1
                                    print("You now have", PlyHPPotions, "Potions.")
                                elif RandomPotion == "Dodge":
                                    print("\nYou find a Potion of Dodge")
                                    PlyDodgePotions = PlyDodgePotions + 1
                                    print("You now have", PlyDodgePotions, "Potions.")
                            elif ChestEvent >= 13:
                                print("\nThe chest is a mimic!")
                                CurEnemy = "Mimic"
                                Ambush = True
                                InCombat = True
                        elif Chest.casefold() == "n":
                            print("\nYou leave the chest alone")
                    else:
                        if PlyMana < PlyManaCap:
                            PlyMana = PlyMana + 1
                        print("You encounter no enemies")
                if TurnsToTraverse == 0:
                    CurPath = None
                    DistanceToTravel = DistanceToTravel - 1
                    TurnsToTraverse = 3
                    if DistanceToTravel == 0:
                        GameState = 1
                        Alive = False
        elif Movement.casefold() == "rest" or Movement.casefold() == "r":
            Ambush = random.randrange(1, 12)
            if Ambush == 1:
                if CurPath == None:
                    CurPathEnemy = OpenPathEnemy
                print("\nYou were ambushed during your sleep!")
                Ambush = True
                InCombat = True
            else:
                print("\nYou rest for a moment, recovering 5 HP and 2 Mana.")
                if ClericRevive > 0:
                    ClericRevive = ClericRevive - 1
                if PlyCharType == "Leper" and PlyLevel < 30:
                    print("Crippling Affliction is reset.")
                    Affliction = 0
                PlyHP = PlyHP + 5
                if PlyHP > PlyHPCap:
                    PlyHP = PlyHPCap
                PlyMana = PlyMana + 2
                if PlyMana > PlyManaCap:
                    PlyMana = PlyManaCap
                print("You now have", PlyHP, "HP and", PlyMana, "mana.")
        
    if InCombat == True and (CurEnemy == None or Ambush == True):
        if CurEnemy == None:
            CurEnemy = random.choice(CurPathEnemy)
        if PlyLevel < 3:
            CurEnemyLevel = PlyLevel + random.randrange(0, 2)
        else:
            CurEnemyLevel = PlyLevel + random.randrange(-2, 2)

        if CurEnemy in WeakEnemy:
            CurEnemyHP = random.randrange(1, 6) + (2 * CurEnemyLevel)
            CurMaxEnemyHP = CurEnemyHP
            TrueEnemyAccuracy = random.randrange(30, 50)
            EnemyDMG = "Weak"
        elif CurEnemy in NormalEnemy:
            CurEnemyHP = random.randrange(4, 12) + (2 * CurEnemyLevel)
            CurMaxEnemyHP = CurEnemyHP
            TrueEnemyAccuracy = random.randrange(45, 70)
            EnemyDMG = "Normal"
        elif CurEnemy in StrongEnemy:
            CurEnemyHP = random.randrange(6, 15) + (2 * CurEnemyLevel)
            CurMaxEnemyHP = CurEnemyHP
            TrueEnemyAccuracy = random.randrange(50, 85)
            EnemyDMG = "Strong"
        else:
            CurEnemyHP = random.randrange(4, 12) + (2 * CurEnemyLevel)
            CurMaxEnemyHP = CurEnemyHP
            TrueEnemyAccuracy = random.randrange(45, 70)
            EnemyDMG = "Normal"

        CurEnemyXP = CurEnemyHP - 4
        if CurEnemyXP <= 0:
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
        
        if Ambush == True:
            PlyDodge = TruePlyDodge + PotionDodgeBuff + PlagueBonusDodge
            PlyDMGRes = TruePlyDMGRes + PotionDMGResBuff + PlyBuffDMGResBonus + ClericDMGRes
            Ambush = False
            WhoseTurn = 2

    if InCombat == True and CurEnemy != None and CurEnemyHP > 0:
        if WhoseTurn == None:
            WhoseTurn = 1
        if PlyHP <= 0 and Alive == True:
            Alive = False
        while PlyHP > 0 and Casting == 0 and WhoseTurn == 1:
            if PlyCharType == "Plague Doctor" and (CurEnemyDoTType == "Poisoned" or CurEnemyDoTType == "Strong Poisoned" or CurEnemyDoTType == "Viral Overload" or CurEnemyDoTType == "Viral Overload+"):
                if PlyLevel < 5:
                    PlagueBonusAcc = 5
                    PlagueBonusCrit = 10
                elif PlyLevel >= 5 and PlyLevel < 25:
                    PlagueBonusAcc = 5
                    PlagueBonusCrit = 10
                    PlagueBonusDodge = 10
                elif PlyLevel >= 25:
                    PlagueBonusAcc = 5
                    PlagueBonusCrit = 10
                    PlagueBonusDodge = 10
                    PlagueBonusDMG = 2
            elif PlyCharType != "Plague Doctor" or (CurEnemyDoTType != "Poisoned" and CurEnemyDoTType != "Strong Poisoned" and CurEnemyDoTType != "Viral Overload" and CurEnemyDoTType != "Viral Overload+"):
                    PlagueBonusAcc = 0
                    PlagueBonusCrit = 0
                    PlagueBonusDodge = 0
                    PlagueBonusDMG = 0

            PlyDodge = TruePlyDodge + PotionDodgeBuff + PlagueBonusDodge
            PlyDMGRes = TruePlyDMGRes + PotionDMGResBuff + PlyBuffDMGResBonus + ClericDMGRes
            PlyAccuracy = TruePlyAccuracy + PotionAccBuff + PlyBuffAccBonus + PlySpellAccBuff + PlagueBonusAcc + ClericAcc
            PlyCritChance = TruePlyCritChance + PotionCritBuff + PlyBuffCritBonus + PlySpellCritBuff + (5 * RogueCritBonus) + PlagueBonusCrit + ClericCrit

            if PlyCharType == "Cleric":
                if PlyHP < PlyHPCap:
                    if PlyLevel < 9:
                        PlyHP = PlyHP + 1
                    elif PlyLevel >= 9 and PlyLevel < 25:
                        PlyHP = PlyHP + 2
                    elif PlyLevel >= 25:
                        PlyHP = PlyHP + 3
                    if PlyHP > PlyHPCap:
                        PlyHP = PlyHPCap
                if CurEnemy in UnholyEnemy:
                    ClericDMGRes = 2
                    if PlyLevel >= 9 and PlyLevel < 13:
                        ClericDMG = 2
                    elif PlyLevel >= 13 and PlyLevel < 21:
                        ClericDMG = 2
                        ClericAcc = 15
                    elif PlyLevel >= 21:
                        ClericDMG = 2
                        ClericAcc = 15
                        ClericCrit = 20
                else:
                    ClericDMGRes = 0
                    ClericDMG = 0
                    ClericAcc = 0
                    ClericCrit = 0

            if PlyDebuffTurns == 0 and PlyDebuffType != "None":
                PlyDebuffType = "None"
                CurEnemyBonusDMG = 0
            if PotionBuffTurns > 0:
                if PotionBuffType == "Acc" or PotionBuffType == "Acc+" or PotionBuffType == "Acc++":
                    if PotionBuffType == "Acc":
                        PotionAccBuff = 20
                    elif PotionBuffType == "Acc+":
                        PotionAccBuff = 25
                    elif PotionBuffType == "Acc++" or PotionBuffType == "Acc++ Crit++" or PotionBuffType == "Acc++ DMG++" or PotionBuffType == "Acc++ DMG Res++" or PotionBuffType == "Acc++ Dodge++":
                        PotionAccBuff = 30
                    else:
                        PotionAccBuff = 0
                if PotionBuffType == "Crit" or PotionBuffType == "Crit+" or PotionBuffType == "Crit++":
                    if PotionBuffType == "Crit":
                        PotionCritBuff = 20
                    elif PotionBuffType == "Crit+":
                        PotionCritBuff = 25
                    elif PotionBuffType == "Crit++" or PotionBuffType == "Acc++ Crit++" or PotionBuffType == "Crit++ DMG++" or PotionBuffType == "Crit++ DMG Res++" or PotionBuffType == "Crit++ Dodge++":
                        PotionCritBuff = 30
                    else:
                        PotionCritBuff = 0
                if PotionBuffType == "DMG" or PotionBuffType == "DMG+" or PotionBuffType == "DMG++":
                    if PotionBuffType == "DMG":
                        PotionDMGBuff = 3
                    elif PotionBuffType == "DMG+":
                        PotionDMGBuff = 4
                    elif PotionBuffType == "DMG++" or PotionBuffType == "Acc++ DMG++" or PotionBuffType == "Crit++ DMG++" or PotionBuffType == "DMG++ DMG Res++" or PotionBuffType == "DMG++ Dodge++":
                        PotionDMGBuff = 5
                    else:
                        PotionDMGBuff = 0
                if PotionBuffType == "DMG Res" or PotionBuffType == "DMG Res+" or PotionBuffType == "DMG Res++":
                    if PotionBuffType == "DMG Res":
                        PotionDMGResBuff = 3
                    elif PotionBuffType == "DMG Res+":
                        PotionDMGResBuff = 4
                    elif PotionBuffType == "DMG Res++" or PotionBuffType == "Acc++ DMG Res++" or PotionBuffType == "Crit++ DMG Res++" or PotionBuffType == "DMG++ DMG Res++" or PotionBuffType == "DMG Res++ Dodge++":
                        PotionDMGResBuff = 5
                    else:
                        PotionDMGResBuff = 0
                if PlySpellBuffTurns > 0:
                    if PlySpellBuffType == "Acc" or PlySpellBuffType == "Acc + DMG":
                        PlySpellAccBuff = 25
                    else:
                        PlySpellAccBuff = 0
                    if PlySpellBuffType == "DMG" or PlySpellBuffType == "Acc + DMG":
                        PlySpellDamageBuff = 3
                    else:
                        PlySpellDamageBuff = 0
                    if PlySpellBuffType == "Crit Chance":
                        PlySpellCritBuff = 15
                    else:
                        PlySpellCritBuff = 0
                if PlyBuffTurns > 0:
                    if PlyBuffType == "Acc-10 DMG DMG Res":
                        PlyBuffAccBonus = 10
                        PlyBuffDMGBonus = 3
                        PlyBuffDMGResBonus = 3
                    else:
                        PlyBuffAccBonus = 0
                        PlyBuffDMGBonus = 0
                        PlyBuffDMGResBonus = 0
                    if PlyBuffType == "Acc":
                        PlyBuffAccBonus = 25
                    else:
                        PlyBuffAccBonus = 0
                    if PlyBuffType == "DMG" or PlyBuffType == "DMG DMG Res":
                        PlyBuffDMGBonus = 3
                    else:
                        PlyBuffDMGBonus = 0
                    if PlyBuffType == "DMG Res" or PlyBuffType == "DMG DMG Res":
                        PlyBuffDMGResBonus = 3
                    else:
                        PlyBuffDMGResBonus = 0
                    if PlyBuffType == "Crit Chance":
                        PlyBuffCritBonus = 15
                    else:
                        PlyBuffCritBonus = 0

            print("\nEnemy", CurEnemy, "HP:", CurEnemyHP)
            print("\nHealth:", PlyHP, "Mana:", PlyMana)

            if PlyCharType == "Leper":
                Affliction = Affliction + 1
            if PlyCharType == "Leper":
                if PlyLevel < 5 and Affliction == 3:
                    Afflicted = 1
                elif PlyLevel >= 5 and PlyLevel < 21 and Affliction == 4:
                    Afflicted = 1
                elif PlyLevel >= 21 and Affliction == 5:
                    Afflicted = 1
            if PlyCharType == "Leper" and PlyLevel >= 13:
                Choices = "\n(A)ttack - (G)uard - (M)agic - (P)otion - (C)rippling Affliction "
            else:
                Choices = "\n(A)ttack - (G)uard - (M)agic - (P)otion "
            Combat = input(Choices)
            if Combat.casefold() == "attack" or Combat.casefold() == "a":
                Accuracy = random.randrange(1, 100)
                print("\nYou attack the", CurEnemy + ".")
                if Accuracy <= PlyAccuracy:
                    Crit = random.randrange(1, 100)
                    if Crit <= PlyCritChance:
                        print("Critical Hit!")
                        PlyDamage = (PlyDamage * 2) + (RogueBonus * 2)
                        if PlyCharType == "Rogue":
                            BleedChance = random.randrange(1, 100)
                            if PlyLevel >= 5 and PlyLevel < 9:
                                if BleedChance <= 25:
                                    print("The enemy is afflicted by bleeding.")
                                    if CurEnemyDoTType == "Poisoned":
                                        CurEnemyDoTType == "Poisoned Bleed"
                                    else:
                                        CurEnemyDoTType == "Bleed"
                                    CurEnemyDoTTurns = 3
                            elif PlyLevel >= 9 and PlyLevel < 13:
                                if BleedChance <= 40:
                                    print("The enemy is afflicted by bleeding.")
                                    if CurEnemyDoTType == "Poisoned":
                                        CurEnemyDoTType == "Poisoned Bleed"
                                    else:
                                        CurEnemyDoTType == "Bleed"
                                    CurEnemyDoTTurns = 3
                            elif PlyLevel >= 17 and PlyLevel < 25:
                                if BleedChance <= 50:
                                    print("The enemy is afflicted by bleeding.")
                                    if CurEnemyDoTType == "Poisoned":
                                        CurEnemyDoTType == "Poisoned Bleed"
                                    else:
                                        CurEnemyDoTType == "Bleed"
                                    CurEnemyDoTTurns = 3
                            elif PlyLevel >= 25:
                                if BleedChance <= 50:
                                    print("The enemy is afflicted by bleeding.")
                                    if CurEnemyDoTType == "Poisoned":
                                        CurEnemyDoTType == "Poisoned PermaBleed"
                                    else:
                                        CurEnemyDoTType == "PermaBleed"
                    else:
                        PlyDamage = PlyDamage
                    if PlyCharType == "Rogue" and PlyLevel >= 17 and (CurEnemyDoTType == "Bleed" or CurEnemyDoTType == "Poisoned Bleed" or CurEnemyDoTType == "PermaBleed" or CurEnemyDoTType == "Poisoned PermaBleed"):
                        PlyDamage = PlyDamage + 3
                    print("You deal", PlyDamage, "points of damage.")
                    CurEnemyHP = CurEnemyHP - PlyDamage
                    if PlyCharType == "Rogue" and PlyLevel == 30 and PlyDamage > (CurMaxEnemyHP * 0.5):
                        print("Executed! The enemy is killed instantly.")
                        CurEnemyHP = 0
                    if PlySpellBuffTurns > 0:
                        PlySpellBuffTurns = PlySpellBuffTurns - 1
                    if PlyBuffTurns > 0:
                        PlyBuffTurns = PlyBuffTurns - 1
                    if CurEnemy not in PoisonImmune:
                        if (PlyBuffType == "Poison" or PlagueAttacks == 1):
                            print("You afflict the enemy with poison.")
                            if CurEnemyDoTType == "None" and CurEnemyDoTType != "Viral Overload":
                                CurEnemyDoTType = "Poisoned"
                            elif CurEnemyDoTType == "Bleed":
                                CurEnemyDoTType = "Poisoned Bleed"
                            elif CurEnemyDoTType == "PermaBleed":
                                CurEnemyDoTType = "Poisoned PermaBleed"
                            if CurEnemyDoTTurns < 2 and CurEnemyDoTType != "Viral Overload":
                                CurEnemyDoTTurns = 2
                        elif PlagueAttacks == 2:
                            print("You afflict the enemy with strong poison.")
                            if (CurEnemyDoTType == "None" or CurEnemyDoTType == "Poisoned") and CurEnemyDoTType != "Viral Overload":
                                CurEnemyDoTType = "Strong Poisoned"
                            if CurEnemyDoTTurns < 3 and CurEnemyDoTType != "Viral Overload":
                                CurEnemyDoTTurns = 3
                            PlagueAttacks = 1
                        elif PlagueAttacks == 3:
                            CurEnemyDoTType = "Viral Overload"
                        elif PlagueAttacks == 4:
                            if CurEnemyDoTType == "Viral Overload +":
                                CurEnemyDoTTurns = 3
                            PlagueAttacks = 3
                elif Accuracy > PlyAccuracy:
                    print("Miss! You deal no damage.")
                    if PlySpellBuffTurns > 0:
                        PlySpellBuffTurns = PlySpellBuffTurns - 1
                    if PlyBuffTurns > 0:
                        PlyBuffTurns = PlyBuffTurns - 1
                WhoseTurn = 2
            elif Combat.casefold() == "guard" or Combat.casefold() == "g":
                print("\nYou guard yourself against the enemy.")
                PlyGuard = "True"
                if PlySpellBuffTurns > 0:
                        PlySpellBuffTurns = PlySpellBuffTurns - 1
                if PlyBuffTurns > 0:
                    PlyBuffTurns = PlyBuffTurns - 1
                WhoseTurn = 2
            elif Combat.casefold() == "magic" or Combat.casefold() == "m":
                Casting = 1
            elif Combat.casefold() == "potions" or Combat.casefold() == "p":
                Potions = 1
            elif (Combat.casefold() == "crippling affliction" or Combat.casefold() == "c") and PlyCharType == "Leper" and PlyLevel >= 13:
                Afflicted = 1
        if WhoseTurn == 2 and CurEnemyHP > 0:
            PotionUsed = "False"
            if PlyCharType == "Knight" and PlyLevel == 30 and PlyGuard != "Bolstered":
                PlyGuard == "True"
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
            if ((CurEnemyDoTType == "Poisoned" or CurEnemyDoTType == "Poisoned Bleed" or CurEnemyDoTType == "Poisoned PermaBleed" or CurEnemyDoTType == "Viral Overload +") and CurEnemyDoTTurns > 0) or CurEnemyDoTType == "Viral Overload":
                PoisonDMG = TruePoisonDMG + PoisonDMGBuff
                print("\nThe enemy is damaged by the poison, taking", PoisonDMG, "damage.")
                CurEnemyHP = CurEnemyHP - PoisonDMG
            if CurEnemyDoTType == "Bleed" or CurEnemyDoTType == "Poisoned Bleed" or CurEnemyDoTType == "Poisoned PermaBleed":
                print("\nThe enemy is bleeding heavily, taking 3 points of damage.")
                CurEnemyHP = CurEnemyHP - 3
            print("\nThe enemy", CurEnemy, "attacks you.")
            EnemyAccuracy = random.randrange(1, 100)
            if CurEnemyBuffTurns == 0 and CurEnemyBuffType != "None":
                CurEnemyBuffType = "None"
            if CurEnemyDoTTurns == 0:
                if CurEnemyDoTType != "None" and CurEnemyDoTType != "Viral Overload +" and CurEnemyDoTType != "Viral Overload":
                    CurEnemyDoTType == "None"
                elif CurEnemyDoTType == "Viral Overload +":
                    CurEnemyDoTType = "Viral Overload"
            if (CurEnemySpellDebuffType == "Acc" or CurEnemySpellDebuffType == "Acc + DMG") and CurEnemyDebuffTurns > 0:
                CurEnemyAccuracy = TrueEnemyAccuracy - 25
            else:
                CurEnemyAccuracy = TrueEnemyAccuracy
            if (CurEnemySpellDebuffType == "DMG" or CurEnemySpellDebuffType == "Acc + DMG") and CurEnemyDebuffTurns > 0:
                CurEnemyBonusDMG = -3
            else:
                CurEnemyBonusDMG = 0
            if PlyCharType == "Plague Doctor" and PlyLevel >= 17 and (CurEnemyDoTType == "Poisoned" or CurEnemyDoTType == "Strong Poisoned" or CurEnemyDoTType == "Viral Overload" or CurEnemyDoTType == "Viral Overload+"):
                CurEnemyAccuracy = TrueEnemyAccuracy - 20
            elif PlyCharType == "Plague Doctor" and PlyLevel < 17 or (CurEnemyDoTType != "Poisoned" and CurEnemyDoTType != "Strong Poisoned" and CurEnemyDoTType != "Viral Overload" and CurEnemyDoTType != "Viral Overload+"):
                CurEnemyAccuracy = TrueEnemyAccuracy
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
                Dodge = random.randrange(1, 100)
                ParryDMG = math.ceil(PlyDamage * 1.25)
                if PlyGuard == "None":
                    if Dodge <= PlyDodge:
                        print("You dodge the attack. You take no damage.")
                    else:
                        if EnemyAttack - PlyDMGRes <= 0:
                            EnemyAttack = 0
                            print("You take no damage.")
                        else:
                            print("You take", (EnemyAttack - PlyDMGRes), "points of damage.")
                            PlyHP = PlyHP - (EnemyAttack - PlyDMGRes)
                    WhoseTurn = 1
                elif PlyGuard == "Bolstered":
                    print("You deflect the enemy attack!")
                    if PlyCharType == "Knight":
                        RandomCrit = random.randrange(1,100)
                        if PlyLevel < 13:
                            ParryCritChance = 15
                        elif PlyLevel >= 13 and PlyLevel < 19:
                            ParryCritChance = 20
                        elif PlyLevel >= 19:
                            ParryCritChance = 35
                        if RandomCrit <= ParryCritChance:
                            print("Critical Hit!")
                            ParryDMG = ParryDMG * 2
                    print("The enemy takes", ParryDMG, "damage.")
                    CurEnemyHP = CurEnemyHP - ParryDMG
                    PlyGuard = "None"
                    WhoseTurn = 1
                elif PlyGuard == "Taunt":
                    print("You brace for the enemy attack")
                    print("You take", (EnemyAttack - PlyDMGRes) * 0.5, "points of damage.")
                    PlyHP = PlyHP - ((EnemyAttack - PlyDMGRes) * 0.5)
                    if PlyLevel < 23:
                        print("You retaliate, dealing", PlyDamage * 0.75, "points of damage.")
                        CurEnemyHP = CurEnemyHP - (PlyDamage * 0.75)
                    elif PlyLevel >= 23:
                        print("You retaliate, dealing", PlyDamage, "points of damage.")
                        CurEnemyHP = CurEnemyHP - PlyDamage
                    PlyGuard = "None"
                    WhoseTurn = 1
                elif PlyGuard == "True" and ParryChance > PlyParry:
                    ParryNegation = random.randint(1,100)
                    if PlyCharType == "Knight":
                        if PlyLevel < 21:
                            ParryNegationChance = 5
                        elif PlyLevel >= 21:
                            ParryNegationChance = 7
                    if EnemyAttack - PlyDMGRes - PlyGuardRes <= 0 or ParryNegation <= ParryNegationChance:
                        EnemyAttack = 0
                        print("You take no damage.")
                        PlyGuard = "None"
                    else:
                        PlyHP = PlyHP - (EnemyAttack - PlyDMGRes - PlyGuardRes)
                        print("You take", (EnemyAttack - PlyDMGRes - PlyGuardRes), "points of damage.")
                        PlyGuard = "None"
                    WhoseTurn = 1
                elif PlyGuard == "True" and ParryChance <= PlyParry:
                    if PlyCharType == "Knight":
                        if PlyLevel >= 13:
                            ParryCritChance = 20
                        else:
                            ParryCritChance = 15
                        RandomCrit = random.randrange(1,100)
                        if RandomCrit <= ParryCritChance:
                            print("Critical Hit!")
                            ParryDMG = ParryDMG * 2
                    if PlyCharType == "Rogue":
                        if PlyLevel >= 13 and PlyLevel < 17:
                            ParryCritChance = math.ceil(PlyCritChance * 0.25)
                        elif PlyLevel >= 21:
                            ParryCritChance = math.ceil(PlyCritChance * 0.5)
                        RandomCrit = random.randrange(1,100)
                        if RandomCrit <= ParryCritChance:
                            print("Critical Hit!")
                            ParryDMG = ParryDMG * 2
                    print("Parry! The enemy takes", ParryDMG, "damage.")
                    CurEnemyHP = CurEnemyHP - ParryDMG
                    PlyGuard = "None"
                    WhoseTurn = 1
                if CaltropHits > 0 and CurEnemy not in CaltropImmune:
                    print("The", CurEnemy, "takes 3 damage from the caltrops.")
                    CurEnemyHP = CurEnemyHP - 3
                    CaltropHits = CaltropHits - 1
                if CurEnemySpellDebuffTurns > 0:
                    CurEnemySpellDebuffTurns = CurEnemySpellDebuffTurns - 1
                if CurEnemyDebuffTurns > 0:
                    CurEnemyDebuffTurns = CurEnemyDebuffTurns - 1
                if ClericRevive > 0:
                    ClericRevive = ClericRevive - 1
            elif EnemyAccuracy > CurEnemyAccuracy:
                if CurEnemyDebuffTurns > 0:
                    CurEnemyDebuffTurns = CurEnemyDebuffTurns - 1
                if CurEnemySpellDebuffTurns > 0:
                    CurEnemySpellDebuffTurns = CurEnemySpellDebuffTurns - 1
                print("Miss! You take no damage.")
                PlyGuard = "None"
                WhoseTurn = 1
            if PlyLevel >= 23 and CaltropHits > 0 and CurEnemy not in CaltropImmune:
                print("The", CurEnemy, "takes 3 damage from the caltrops.")
                CurEnemyHP = CurEnemyHP - 3
                CaltropHits = CaltropHits - 1
            if ClericRevive > 0:
                ClericRevive = ClericRevive - 1

    if InCombat == True and CurEnemyHP <= 0 and Ambush == False:
        print("\nThe enemy", CurEnemy, "is defeated!")
        if PlyLevel < 30:
            print("You earned", CurEnemyXP, "XP")
            PlyXP = PlyXP + CurEnemyXP
        Gold = random.randrange(0, 8) + (2 * CurEnemyLevel)
        print("You find", Gold, "pieces of gold on the enemy.")
        PlyGold = PlyGold + Gold
        CurEnemy = None
        CurEnemyLevel = 0
        CurEnemyHP = 0
        CurMaxEnemyHP = 0
        CurEnemyXP = 0
        CurEnemyAccuracy = 0
        CurEnemyBuffType = "None"
        CurEnemyBuffTurns = 0
        CurEnemyDebuffType = "None"
        CurEnemyDebuffTurns = 0
        CurEnemySpellDebuffType = "None"
        CurEnemySpellDebuffTurns = 0
        CurEnemyDoTType = "None"
        CurEnemyDoTTurns = 0
        PlyBuffType = "None"
        PlyBuffTurns = 0
        PlySpellBuffType = "None"
        PlySpellBuffTurns = 0
        PlyDebuffType = "None"
        PlyDebuffTurns = 0
        InCombat = False
        WhoseTurn = None

if Alive == False:
    if GameState == 0:
        print("\nYou have died!")
    elif GameState == 1:
        print("\nVictory! You have reached the castle!")
    print("Stopping game.\n")