#Ratventure by Tan Jun Jie P09 IT01
import random
import ast
day = 1 #day counter
main_menu_list = ['New Game', 'Resume Game', 'Exit Game'] #list of main menu options that i print
town_menu_list = ['View Character', 'View Map', 'Move', 'Rest', 'Church', 'Shop', 'Save Game', 'Exit Game'] #list of town menu options that i print
outdoor_menu_list =['View Character', 'View Map', 'Move', 'Sense Orb','Exit Game'] #list of outdoor menu options that i print
combat_menu_list =['Attack', 'Run'] #list of combat menu options that i print
invalid_option_list = ['Invalid Option.', 'Please Try Again.'] #list of invalid options that i print
church_menu_list = ['Blessing', 'Heal', 'Purify', 'Leave Church']  #list for church menu list
blessing_list = ['Blessing of Strength', 'Blessing of Enhanced Vigor'] #list of blessings
shop_menu_list = ['Potion of Healing', 'Iron Sword', 'Chainmail Armour', 'Phoenix Down', 'Exit']  #list of shop menu


gmap= [['H/T',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ','T',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ','T',' ',' '],
       [' ','T',' ',' ',' ',' ',' ',' '],   #map of the game world
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ','T',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ','K']]

orb_map = [[' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' '],  #map of the orb
           [' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' '],
           [' ',' ',' ',' ',' ',' ',' ',' ']]
enemy_map = [[' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],   #map of the enemies
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ','T',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ','K']]

potion_of_healing = 0  #number of healing potions the hero has
phoenix_down = 0  #number of phoenix down the hero has
iron_sword = False
chainmail_armour = False
bless_num = 0 #what blessing the hero has
bless_count = 0 #counter for how long blessing should less
curse_num = 0 #what curse the player has
curse = False   #whether the player has been cursed
orb_check = False #this is to check if the character has the Orb of Power
hero_pos = [0,0]  #this is the character's position
orb_pos = [0, 0]  #this is the position of the Orb of Power
x = 0    #the X-coordinate for the hero
y = 0    #the Y-coordinate for the hero
money = 0  #money that the hero has


hero_stats = {'Name': 'The Hero', 'Min Damage': 2, 'Max Damage': 4, 'Defense': 1, 'HP': 20} #the stats for the hero
rat_king_stats = {'Name':'Rat King', 'Min Damage': 8, 'Max Damage': 12, 'Defense': 5, 'HP': 25} #the stats for the Rat King
rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}  #the stats for the rat

def ran_orb(): #this function is to randomize the orb of power
    global orb_pos
    global orb_map
    orb_x = random.randint(0, 7)
    orb_y = random.randint(0, 7)
    ran_orb_check(orb_x, orb_y)
    orb_pos[0] = orb_x
    orb_pos[1] = orb_y
    orb_map[orb_x][orb_y] = 'O'
    


def ran_orb_check(orb_x, orb_y): #this function is to check and make sure the orb doesnt spawn on a town or on the Rat King
    if gmap[orb_x][orb_y] == 'T':
        orb_x = random.randint(0, 7)
        orb_y = random.randint(0, 7)
        ran_orb_check(orb_x, orb_y)
    elif gmap[orb_x][orb_y] == 'H/T':
        orb_x = random.randint(0, 7)
        orb_y = random.randint(0, 7)
        ran_orb_check(orb_x, orb_y)
    elif gmap[orb_x][orb_y] == 'K':
        orb_x = random.randint(0, 7)
        orb_y = random.randint(0, 7)
        ran_orb_check(orb_x, orb_y)
        


def main_menu(main_menu_list): #main menu function
    print('Welcome to Ratventure!')
    print('--------------------------')
    for i in range(len(main_menu_list)):
        print('{}) {}'.format((i+1), main_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        new_game()
    elif choice == '2':
        resume_game()
        new_game()
    elif choice == '3':
         exit_game()
    elif choice == 'with great power comes great responsibility': #a cheat code I placed in
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        main_menu(main_menu_list)
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        main_menu(main_menu_list)
    else:
        print('Please enter a valid option.')
        main_menu(main_menu_list)


def new_game(): #this is the town menu (despite the new game name)
    print('Day {}: You are in Town.'.format(day))
    for i in range(len(town_menu_list)):
        print('{}) {}'.format((i+1), town_menu_list[i]))
    print()
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        view_character()
        new_game()
    elif choice == '2':
        view_map()
        new_game()
    elif choice == '3':
        move_around()
    elif choice == '4':
        rest()
        new_game()
    elif choice == '5':
        church()
    elif choice == '6':
        shop()
    elif choice == '7':
        save_game()
        new_game()
    elif choice == '8':
        exit_game()
    elif choice == 'with great power comes great responsibility': #cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        new_game()
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        new_game()
    else:
        print('Invalid Choice.')
        print('Please Try Again.')
        new_game()

def view_character(): #view character function
    global iron_sword
    global chainmail_armour
    global phoenix_down
    global curse
    global curse_num
    print(hero_stats['Name'])
    print('Damage: {}-{}'.format(hero_stats['Min Damage'], hero_stats['Max Damage']))
    print('Defence: {}'.format(hero_stats['Defense']))
    print('HP: {}'.format(hero_stats['HP']))
    print('You currently have {} Gold'.format(money))
    if hero_stats['HP'] >= 5 and hero_stats['HP'] < 11: #this is to have different messages depending on hero's health
        print('You have minor injuries')
        print('You should rest when you can.')
    elif hero_stats['HP'] >= 11 and hero_stats['HP'] < 16:
        print('You suffer some minor scratches.')
    elif hero_stats['HP'] >= 16:
        print('You are healthy.')
    else:
        print('You are severly injured.')
        print('You should find a place to rest.')
    if iron_sword == False:
        print('Weapon: Practice Sword')
    else:
        print('Weapon: Iron Sword')
    if chainmail_armour == False:
        print('Armour: Leather Armour')
    else:
        print('Armour: Chainmail Armour')
    print('{} Potion of Healings in Inventory'.format(potion_of_healing))
    if phoenix_down == True:
        print('1 Phoenix Down')
    if bless_count > 0:
        if bless_num == 1:
            print('Blessed by Ares')
            print('All Attack Increased by 2')
            print('Lasts for {} Day'.format(bless_count))
        elif bless_num == 2:
            print('Blessed by Soteria')
            print('Defense Increased by 2 and HP Increased by 5')
            print('Lasts for {} Day'.format(bless_count))
    else:
        print('No blessing currently')
    if curse == True:  #display what curse the hero has
        if curse_num == 1:
            print('Curse of Lowered Accuracy')
        elif curse_num == 1:
            print('Curse of Fragility')
        elif curse_num == 1:
            print('Curse with Enemy Longevitiy')
    else:
        print('No curses currently')
    if orb_check == True:
        print('You are holding the Orb of Power') #this is to display whether the hero has the Orb of Power
    else:
        print('You currently do not have the Orb of Power')
    print()

        
def resume_game(): #this is to resume game
    global hero_stats
    global gmap
    global orb_map
    global hero_pos
    global day
    global orb_pos
    save_file = open('Save file.txt', 'r')
    save_file_list = []
    load_file = save_file.readlines()
    for i in load_file:
        i = ast.literal_eval(i)
        save_file_list.append(i)
    save_file.close
    hero_stats = save_file_list[0]
    gmap = save_file_list[1]
    orb_map = save_file_list[2]
    hero_pos = save_file_list[3]
    day = save_file_list[4]
    orb_pos = save_file_list[5]

def exit_game(): #a simple exit game function
    print('Thanks for playing!')

    
def view_map(): #to print and view the map
    for i in range(8):
        print('+---+---+---+---+---+---+---+---+')
        for j in range(8):
            if gmap[i][j] == 'H/T':
                print('|{}'.format(gmap[i][j]), end='')
            else:
                print('| {}'.format(gmap[i][j]), end=' ')
        print('|')
    print('+---+---+---+---+---+---+---+---+')
    print()

    
def move_around(): #to move around
    global rat_stats
    global rat_king_stats
    global bless_num
    global bless_count
    global hero_pos
    global x
    global y
    global day
    view_map()
    print('W = up; A = left; S = down; D = right')
    move = input('Your move: ')
    print()
    if move == 'W':
        if x <= 0: #check to make sure the player does not move outside the map
            print('You can not move outside the map!')
            print('Please Try Again')
            print()
            move_around()
        else:
            if gmap[x][y] == 'H/T':  #to change the previous tile back to what it originally is
                gmap[x][y] = 'T'
            else:
                gmap[x][y] = ' '
            x -= 1
            hero_pos[0] = x
            day += 1
            if day >= 10 and day < 21:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
            elif day >= 20:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
            if bless_count > 0:
                bless_count -= 1
                if bless_count == 0:
                    if bless_num == 1:
                        hero_stats['Min Damage'] -= 2
                        hero_stats['Max Damage'] -= 2
                        bless_num = 0
                    elif bless_num == 2:
                        hero_stats['Defense'] -= 2
                        hero_stats['HP'] -= 5
                        bless_num = 0
            if gmap[x][y] == 'T':
                gmap[x][y] == 'H/T'
                print()
                new_game()
            elif gmap[x][y] == 'K':
                gmap[x][y] = 'H/K'
                print()
                rat_king_encounter()
            else:
                gmap[x][y] = 'H'
                print()
                rat_encounter()          
            
    elif move == 'A':
        if y < 1:  #check to make sure the player does not move outside the map
            print('You can not move outside the map!')
            print('Please Try Again')
            print()
            move_around()
        else:
            if gmap[x][y] == 'H/T':  #to change the previous tile back to what it originally is
                gmap[x][y] = 'T'
            else:
                gmap[x][y] = ' '
            y -= 1
            hero_pos[1] = y
            day += 1
            if day >= 10 and day < 21:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
            elif day >= 20:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
            if bless_count > 0:
                bless_count -= 1
                if bless_count == 0:
                    if bless_num == 1:
                        hero_stats['Min Damage'] -= 2
                        hero_stats['Max Damage'] -= 2
                        bless_num = 0
                    elif bless_num == 2:
                        hero_stats['Defense'] -= 2
                        hero_stats['HP'] -= 5
                        bless_num = 0
            if gmap [x][y] == 'T':
                gmap[x][y] = 'H/T'
                print()
                new_game()
            elif gmap[x][y] == 'K':
                gmap[x][y] = 'H/K'
                print()
                rat_king_encounter()
            else:
                gmap[x][y] = 'H'
                print()
                rat_encounter()

    elif move == 'S':
        if x > 6:  #check to make sure the player does not move outside the map
            print('You can not move outside the map!')
            print('Please Try Again')
            print()
            move_around()
        else:
            if gmap[x][y] == 'H/T':  #to change the previous tile back to what it originally is
                gmap[x][y] = 'T'
            else:
                gmap[x][y] = ' '
            x += 1
            hero_pos[0] = x
            day += 1
            if day >= 10 and day < 21:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
            elif day >= 20:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
            if bless_count > 0:
                bless_count -= 1
                if bless_count == 0:
                    if bless_num == 1:
                        hero_stats['Min Damage'] -= 2
                        hero_stats['Max Damage'] -= 2
                        bless_num = 0
                    elif bless_num == 2:
                        hero_stats['Defense'] -= 2
                        hero_stats['HP'] -= 5
                        bless_num = 0
            if gmap [x][y] == 'T':
                gmap[x][y] = 'H/T'
                print()
                new_game()
            elif gmap[x][y] == 'K':
                gmap[x][y] = 'H/K'
                print()
                rat_king_encounter()
            else:
                gmap[x][y] = 'H'
                print()
                rat_encounter()

    elif move == 'D':
        if y > 6:  #check to make sure the player does not move outside the map
            print('You can not move outside the map!')
            print('Please Try Again')
            print()
            move_around()
        else:
            if gmap[x][y] == 'H/T':  #to change the previous tile back to what it originally is
                gmap[x][y] = 'T'
            else:
                gmap[x][y] = ' '
            y += 1
            hero_pos[1] = y
            day += 1
            if day >= 10 and day < 21:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
            elif day >= 20:
                rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
                rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
            if bless_count > 0:
                bless_count -= 1
                if bless_count == 0:
                    if bless_num == 1:
                        hero_stats['Min Damage'] -= 2
                        hero_stats['Max Damage'] -= 2
                        bless_num = 0
                    elif bless_num == 2:
                        hero_stats['Defense'] -= 2
                        hero_stats['HP'] -= 5
                        bless_num = 0
            if gmap [x][y] == 'T':
                gmap[x][y] = 'H/T'
                
                print()
                new_game()
            elif gmap[x][y] == 'K':
                gmap[x][y] = 'H/K'
                print()
                rat_king_encounter()
            else:
                gmap[x][y] = 'H'
                print()
                rat_encounter()
                
    elif move == 'teleport': #cheat code for moving around
        player_input_x = input('Enter X coordinate (0-7): ')
        player_input_y = input('Enter Y-Coordinate (0-7): ')
        if (
            player_input_x == '0' or player_input_x == '1' or player_input_x == '2' or
            player_input_x == '3' or player_input_x == '4' or player_input_x == '5' or
            player_input_x == '6' or player_input_x == '7'):   #to make sure the entered value is within the map
            if (
                player_input_y == '0' or player_input_y == '1' or player_input_y == '2' or
                player_input_y == '3' or player_input_y == '4' or player_input_y == '5' or
                player_input_y == '6' or player_input_y == '7'):  #to make sure the entered value is within the map
            
                if gmap[x][y] == 'H/T':  #to change the previous tile back to what it originally is
                    gmap[x][y] = 'T'
                else:
                    gmap[x][y] = ' '
                x = int(player_input_x)
                y = int(player_input_y)
                day += 1
                if day >= 10 and day < 21:
                    rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
                    rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
                elif day >= 20:
                    rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
                    rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
                if bless_count > 0:
                    bless_count -= 1
                    if bless_num == 1:
                        hero_stats['Min Damage'] -= 2
                        hero_stats['Max Damage'] -= 2
                        bless_num = 0
                    elif bless_num == 2:
                        hero_stats['Defense'] -= 2
                        hero_stats['HP'] -= 5
                        bless_num = 0
                if gmap[x][y] == 'T':
                    gmap[x][y] = 'H/T'
                    print()
                    new_game()
                elif gmap[x][y] == 'K':
                    gmap[x][y] = 'H/K'
                    print()
                    rat_king_encounter()
                else:
                    gmap[x][y] = 'H'
                    print()
                    rat_encounter()
            else:
                print()
                print('Invalid Choice.')
                print('Please Try Again.')
                move_around()
        else:
            print()
            print('Invalid Choice.')
            print('Please Try Again.')
            move_around()
            
    elif move == 'with great power comes great responsibility': #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        move_around()
    elif move == 'where is the Orb of Power':  #cheat code for finding orb location
        print('The orb is located at X-Coordinate of {} and Y-Coordinate of {}'.format(orb_pos[0], orb_pos[1]))
        print()
        move_around()
    elif move =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        move_around()
    else:
        print()
        print('Invalid Choice.')
        print('Please Try Again.')
        move_around()
    
def rest(): #rest function
    global rat_stats
    global rat_king_stats
    global bless_num
    global bless_count
    hero_stats['HP'] = 20
    print('You are fully healed.')
    global day
    day += 1
    if day >= 10 and day < 21:
        rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
        rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
    elif day >= 20:
        rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
        rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
    if bless_count > 0:
        bless_count -= 1
        if bless_num == 1:
            hero_stats['Min Damage'] -= 2
            hero_stats['Max Damage'] -= 2
            bless_num = 0
        elif bless_num == 2:
            hero_stats['Defense'] -= 2
            hero_stats['HP'] -= 5
            bless_num = 0
    print()
        
def save_game(): #this is to save the game
    global hero_stats
    global gmap
    global orb_map
    global hero_pos
    global day
    global orb_pos
    save_file = open('Save file.txt', 'w')
    save_file.write(str(hero_stats) + '\n')
    save_file.write(str(gmap) + '\n')
    save_file.write(str(orb_map) + '\n')
    save_file.write(str(hero_pos) + '\n')
    save_file.write(str(day) + '\n')
    save_file.write(str(orb_pos) + '\n')
    print('Game Saved.')
    print()

def rat_king_encounter(): #function when the hero encounters the rat king
    print('Day {}: You see the Rat King!'.format(day))
    print('Encounter! - {}'.format(rat_king_stats['Name']))
    print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
    print('Defense: {}'.format(rat_king_stats['Defense']))
    print('HP: {}'.format(rat_king_stats['HP']))
    rk_combat_menu(combat_menu_list)

def rat_encounter(): #function when the hero encounters the rat
    print('Day {}: You are out in the open.'.format(day))
    print('Encounter! - {}'.format(rat_stats['Name']))
    print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
    print('Defense: {}'.format(rat_stats['Defense']))
    print('HP: {}'.format(rat_stats['HP']))
    combat_menu(combat_menu_list)

def rk_combat_menu(combat_menu_list):  #function for combat menu when the hero encounters the rat king
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_king_attack() 
    elif choice == '2':
        run_from_rat_king()
    elif choice == 'with great power comes great responsibility': #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        rk_combat_menu(combat_menu_list)
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        rk_combat_menu(combat_menu_list)
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        rk_combat_menu(combat_menu_list)
    
def combat_menu(combat_menu_list): #function for combat menu when the hero encounters the rat
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_attack() 
    elif choice == '2':
        run_from_rat()
    elif choice == 'with great power comes great responsibility':  #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        combat_menu(combat_menu_list)
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        combat_menu(combat_menu_list)
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        combat_menu(combat_menu_list)
    
def rat_king_attack(): #function to calculate the attack sequence for rat King
    global hero_stats
    global day
    global rat_king_stats
    global curse
    global curse_num
    global potion_of_healing
    if orb_check == False:  #to check if hero has Orb of Power and can deal damage
        damage_dealt_by_hero = 0
        damage_dealt_by_rat_king = (random.randint(rat_king_stats['Min Damage'],rat_king_stats['Max Damage'])) - hero_stats['Defense']
        print('You do not have the Orb of Power - the {} is immune!'.format(rat_king_stats['Name']))
    else:
        damage_dealt_by_hero = (random.randint(hero_stats['Min Damage'],hero_stats['Max Damage'])) - rat_king_stats['Defense']   #randomize the damage between min and max damage
        damage_dealt_by_rat_king = (random.randint(rat_king_stats['Min Damage'],rat_king_stats['Max Damage'])) - hero_stats['Defense']
        print('You have dealt {} damage to the {}'.format(damage_dealt_by_hero, rat_king_stats['Name']))
    if curse == True:
        if curse_num == 1:
            accuracy = random.randint(1,2)
            if attack == 1:
                damage_dealt_by_hero = 0
    else:
        damage_dealt_by_hero = (random.randint(hero_stats['Min Damage'],hero_stats['Max Damage'])) - rat_stats['Defense']
    rat_king_stats['HP'] = rat_king_stats['HP'] - damage_dealt_by_hero
    if damage_dealt_by_hero < 0:  #to ensure attack doesnt go into the negatives and heal the enemy/hero
        damage_dealt_by_hero = 0
    if damage_dealt_by_rat_king < 0:
        damage_dealt_by_rat_king = 0
    rat_king_stats['HP'] = rat_king_stats['HP'] - damage_dealt_by_hero
    if rat_king_stats['HP'] < 1:
        if rat_stats['HP'] <= -1:    #this to make it that there is a different dialogue if you overkill the enemy
            print('You brutally mutilated the {} in cold blood'.format(rat_king_stats['Name']))
            print('The {} is dead! You are victorious!'.format(rat_king_stats['Name']))
            if hero_stats['HP'] >= 5 and hero_stats['HP'] < 11:  #to have different dialogue depending on hero's health after the fight
                print('You survived minor wounds from the fight')
            elif hero_stats['HP'] >= 11 and hero_stats['HP'] <16:
                print('You suffered a couple scratches from the fight.')
            elif hero_stats['HP'] >= 16:
                print('You easily defeated the {}'.format(rat_king_stats['Name']))
                print('You barely won the fight.')
            else:
                print('You barely won the fight.')
            print('The World is saved! You Win!')
        else:
            print('You dealt a fatal wound to the {}'.format(rat_king_stats['Name'])) #this to make it that there is a different dialogue if you overkill the enemy
            print('The {} is dead! You are victorious!'.format(rat_king_stats['Name']))
            if hero_stats['HP'] >= 5 and hero_stats['HP'] < 11:   #to have different dialogue depending on hero's health after the fight
                print('You survived minor wounds from the fight')
            elif hero_stats['HP'] >= 11 and hero_stats['HP'] <16:
                print('You suffered a couple scratches from the fight.')
            elif hero_stats['HP'] >= 16:
                print('You easily defeated the {}'.format(rat_king_stats['Name']))
                print('You barely won the fight.')
            else:
                print('You barely won the fight.')
            print('The World is saved! You Win!')
    else:
        print('Ouch! The {} hit you for {} damage!'.format(rat_king_stats['Name'], damage_dealt_by_rat_king))
        hero_stats['HP'] = hero_stats['HP'] - damage_dealt_by_rat_king
        if hero_stats['HP'] < 1: #for if the hero dies
            print('You have 0 HP left.')
            rat_king_stats = {'Name':'Rat King', 'Min Damage': 8, 'Max Damage': 12, 'Defense': 5, 'HP': 25} #reset hero stats
            game_over()
        else:
            print('You have {} HP left.'.format(hero_stats['HP']))
            print('Encounter! - {}'.format(rat_king_stats['Name']))
            print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
            print('Defense: {}'.format(rat_king_stats['Defense']))
            print('HP: {}'.format(rat_king_stats['HP']))
            for i in range(len(combat_menu_list)):
                print('{}) {}'.format((i+1), combat_menu_list[i]))
            print('3) Use Potion of Healing')
            choice = input('Enter Choice: ')
            print()
            if choice == '1':
                rat_king_attack()
            elif choice == '2':
                run_from_rat_king()
            elif choice == 'with great power comes great responsibility':  #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                rat_king_attack_error()
            elif choice == '3':  #for healing potion
                if potion_of_healing < 1:
                    print('Currently Do not have any Potion of Healing Left')
                    rat_king_attack_error()
                else:
                    choice = input('Use Potion of Healing?(Y/N): ')
                    if choice == 'Y':
                        hero_stats['HP'] += 5
                        potion_of_healing -= 1
                        print('You have healed for 5 HP')
                        print()
                        rat_king_attack_error()
                    elif choice == 'N':
                        print()
                        rat_king_attack_error()
                    elif choice =='Greed is Good':
                        print('Money Cheat Activated!')
                        money_cheat()
                        print()
                        rat_king_attack_error()
                    elif choice == 'with great power comes great responsibility':  #stats cheat code
                        print('Stats Cheat Activated!')
                        print()
                        stats_cheat()
                        rat_king_attack_error()
                    else:
                        for i in range(len(invalid_option_list)):
                            print('{}'.format(invalid_option_list[i]))
                        print()
                        rat_king_attack_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                rat_king_attack_error()
            else:
                for i in range(len(invalid_option_list)):
                    print('{}'.format(invalid_option_list[i]))
                print()
                rat_king_attack_error()

def rat_king_attack_error(): #when the user enters an invalid option during the attack sequence for the Rat King
    global potion_of_healing
    print('The {} have {} HP left.'.format(rat_king_stats['Name'], rat_king_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_king_stats['Name']))
    print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
    print('Defense: {}'.format(rat_king_stats['Defense']))
    print('HP: {}'.format(rat_king_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    print('3) Use Potion of Healing')
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_king_attack()
    elif choice == '2':
        run_from_rat_king()
    elif choice == '3':  #for healing potion
        if potion_of_healing < 1:
            print('Currently Do not have any Potion of Healing Left')
            rat_attack_error()
        else:
            choice = input('Use Potion of Healing?(Y/N): ')
            if choice == 'Y':
                hero_stats['HP'] += 5
                potion_of_healing -= 1
                print('You have healed for 5 HP')
                print()
                rat_attack_error()
            elif choice == 'N':
                print()
                rat_attack_error()
            elif choice == 'with great power comes great responsibility':   #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                rat_attack_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                rat_attack_error()
            else:
                for i in range(len(invalid_option_list)):
                    print('{}'.format(invalid_option_list[i]))
                print()
                rat_attack_error()
    elif choice == 'with great power comes great responsibility':  #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        rat_king_attack_error()
    elif choice =='Greed is Good':   #money cheat code
        print('Money Cheat Activated!')
        money_cheat()
        print()
        rat_king_attack_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        print()
        rat_king_attack_error()
                
  
def rat_attack():  #attack sequence for Rat
    global money
    global curse
    global curse_num
    global hero_stats
    global day
    global rat_stats
    global potion_of_healing
    if curse == True:
        if curse_num == 1:
            accuracy = random.randint(1,2)
            if attack == 1:
                damage_dealt_by_hero = 0
    else:
        damage_dealt_by_hero = (random.randint(hero_stats['Min Damage'],hero_stats['Max Damage'])) - rat_stats['Defense']
    damage_dealt_by_rat = (random.randint(rat_stats['Min Damage'],rat_stats['Max Damage'])) - hero_stats['Defense']
    if damage_dealt_by_hero < 0: #to ensure attack doesnt go into the negatives and heal the enemy/hero
        damage_dealt_by_hero = 0
    if damage_dealt_by_rat < 0:
        damage_dealt_by_rat = 0
    print('You have dealt {} damage to the rat'.format(damage_dealt_by_hero))
    rat_stats['HP'] = rat_stats['HP'] - damage_dealt_by_hero
    if rat_stats['HP'] < 1:
        if rat_stats['HP'] <= -4:    #this to make it that there is a different dialogue if you overkill the enemy
            print('You brutally mutilated the {} in cold blood'.format(rat_stats['Name']))
            print('The {} is dead! You are victorious!'.format(rat_stats['Name']))
            if hero_stats['HP'] >= 5 and hero_stats['HP'] < 11:   #to have different dialogue depending on hero's health after the fight
                print('You are quite wounded.')
                print('Maybe you should find a town to rest at.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            elif hero_stats['HP'] >= 11 and hero_stats['HP'] <16:
                print('You are slightly wounded.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            elif hero_stats['HP'] >= 16:
                print('You easily won the fight.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            else:
                print('You are severely wounded.')
                print('You should find a town to rest at.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
        else:
            print('You dealt a fatal wound to the {}'.format(rat_stats['Name']))
            print('The {} is dead! You are victorious!'.format(rat_stats['Name']))
            if hero_stats['HP'] >= 5 and hero_stats['HP'] < 11:  #to have different dialogue depending on hero's health after the fight
                print('You are quite wounded.')
                print('Maybe you should find a town to rest at.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            elif hero_stats['HP'] >= 11 and hero_stats['HP'] <16:
                print('You are slightly wounded.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            elif hero_stats['HP'] >= 16:
                print('You easily won the fight.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
            else:
                print('You are severely wounded.')
                print('You should find a town to rest at.')
                rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                print()
                money += random.randint(5, 10)
                outdoor_menu()
    else:
        print('Ouch! The {} hit you for {} damage!'.format(rat_stats['Name'], damage_dealt_by_rat))
        hero_stats['HP'] = hero_stats['HP'] - damage_dealt_by_rat
        if hero_stats['HP'] < 1:
            print('You have 0 HP left.')
            rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
            game_over()
        else:
            print('You have {} HP left.'.format(hero_stats['HP']))
            print('Encounter! - {}'.format(rat_stats['Name']))
            print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
            print('Defense: {}'.format(rat_stats['Defense']))
            print('HP: {}'.format(rat_stats['HP']))
            for i in range(len(combat_menu_list)):
                print('{}) {}'.format((i+1), combat_menu_list[i]))
            print('3) Use Potion of Healing')
            choice = input('Enter Choice: ')
            print()
            if choice == '1':
                rat_attack()
            elif choice == '2':
                run_from_rat()
            elif choice == '3':  #for healing potion
                if potion_of_healing < 1:
                    print('Currently Do not have any Potion of Healing Left')
                    rat_attack_error()
                else:
                    choice = input('Use Potion of Healing?(Y/N): ')
                    if choice == 'Y':
                        hero_stats['HP'] += 5
                        potion_of_healing -= 1
                        print('You have healed for 5 HP')
                        print()
                        rat_attack_error()
                    elif choice == 'N':
                        print()
                        rat_attack_error()
                    elif choice == 'with great power comes great responsibility':   #stats cheat code
                        print('Stats Cheat Activated!')
                        print()
                        stats_cheat()
                        rat_attack_error()
                    elif choice =='Greed is Good':
                        print('Money Cheat Activated!')
                        money_cheat()
                        print()
                        rat_attack_error()
                    else:
                        for i in range(len(invalid_option_list)):
                            print('{}'.format(invalid_option_list[i]))
                        print()
                        rat_attack_error()
            elif choice == 'with great power comes great responsibility':    #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                rat_attack_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                rat_attack_error()
            else:
                for i in range(len(invalid_option_list)):
                    print('{}'.format(invalid_option_list[i]))
                print()
                rat_attack_error()
                
def rat_attack_error():  #when player input invalid option during attack sequence for rat
    global potion_of_healing
    print('The {} have {} HP left.'.format(rat_stats['Name'], rat_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_stats['Name']))
    print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
    print('Defense: {}'.format(rat_stats['Defense']))
    print('HP: {}'.format(rat_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    print('3) Use Potion of Healing')
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_attack()
    elif choice == '2':
        run_from_rat()
    elif choice == '3':  #for healing potion
        if potion_of_healing < 1:
            print('Currently Do not have any Potion of Healing Left')
            rat_attack_error()
        else:
            choice = input('Use Potion of Healing?(Y/N): ')
            if choice == 'Y':
                hero_stats['HP'] += 5
                potion_of_healing -= 1
                print('You have healed for 5 HP')
                print()
                rat_attack_error()
            elif choice == 'N':
                print()
                rat_attack_error()
            elif choice == 'with great power comes great responsibility':   #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                rat_attack_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                rat_attack_error()
            else:
                for i in range(len(invalid_option_list)):
                     print('{}'.format(invalid_option_list[i]))
                print()
                rat_attack_error()
    elif choice == 'with great power comes great responsibility':  #stat cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        rat_attack_error()
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        rat_attack_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        print()
        rat_attack_error()
        
def run_from_rat(): #function for when player runs from rat
    global rat_stats
    global hero_stats
    run_chance = random.randint(1, 2) #to make running away a 50/50 chance
    if run_chance == 2:
        print('You run and hide.')  #when player succeed in running away
        for i in range(len(outdoor_menu_list)):
            print('{}) {}'.format((i+1), outdoor_menu_list[i]))
        choice = input('Enter Choice: ')
        print()
        if choice == '1':   #so that every option other than move would trigger the attack sequence again
            view_character()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_encounter()
        elif choice == '2':
            view_map()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_encounter()
        elif choice == '3':
            move_around()
        elif choice == '4':
            sense_orb()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_encounter()
        elif choice == '5':
            exit_game()
        elif choice == 'with great power comes great responsibility':  #stats cheat code
            print('Stats Cheat Activated!')
            print()
            stats_cheat()
            run_from_rat_error()
        elif choice =='Greed is Good':
            print('Money Cheat Activated!')
            money_cheat()
            print()
            run_from_rat_error()
        else:
            for i in range(len(invalid_option_list)):
                print('{}'.format(invalid_option_list[i]))
            print()
            run_from_rat_error()
    else:
        print('You have failed to run away.')   #when players fails to run away
        damage_dealt_by_rat = (random.randint(rat_stats['Min Damage'],rat_stats['Max Damage'])) - hero_stats['Defense']
        if damage_dealt_by_rat < 0:
            damage_dealt_by_rat = 0
        print('Ouch! The {} hit you for {} damage!'.format(rat_stats['Name'], damage_dealt_by_rat)) #rat would hit first
        hero_stats['HP'] = hero_stats['HP'] - damage_dealt_by_rat
        if hero_stats['HP'] < 1:    
            print('You have 0 HP left.')
            rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
            game_over()
        else:
            print('You have {} HP left.'.format(hero_stats['HP']))
            print('Encounter! - {}'.format(rat_stats['Name']))
            print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
            print('Defense: {}'.format(rat_stats['Defense']))
            print('HP: {}'.format(rat_stats['HP']))
            for i in range(len(combat_menu_list)):
                print('{}) {}'.format((i+1), combat_menu_list[i]))
            print('3) Use Potion of Healing')
            choice = input('Enter Choice: ')
            print()
            if choice == '1':
                rat_attack()
            elif choice == '2':
                run_from_rat()
            elif choice == '3':  #for healing potion
                if potion_of_healing < 1:
                    print('Currently Do not have any Potion of Healing Left')
                    run_from_rat_fail_error()
                else:
                    choice = input('Use Potion of Healing?(Y/N): ')
                    if choice == 'Y':
                        hero_stats['HP'] += 5
                        potion_of_healing -= 1
                        print('You have healed for 5 HP')
                        print()
                        run_from_rat_fail_error()
                    elif choice == 'N':
                        print()
                        run_from_rat_fail_error()
                    elif choice == 'with great power comes great responsibility':   #stats cheat code
                        print('Stats Cheat Activated!')
                        print()
                        stats_cheat()
                        run_from_rat_fail_error()
            elif choice == 'with great power comes great responsibility':
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                run_from_rat_fail_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                run_from_rat_fail_error()
            else:
                for i in range(len(invalid_option_list)):
                    print('{}'.format(invalid_option_list[i]))
                print()
                run_from_rat_fail_error()

def run_from_rat_fail_error(): #this is for when player input an invalid option when he fails to run away from the rat
    print('You have failed to run away.')
    print('The {} have {} HP left.'.format(rat_stats['Name'], rat_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_stats['Name']))
    print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
    print('Defense: {}'.format(rat_stats['Defense']))
    print('HP: {}'.format(rat_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    print('3) Use Potion of Healing')
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_attack()
    elif choice == '2':
        run_from_rat()
    elif choice == '3':  #for healing potion
        if potion_of_healing < 1:
            print('Currently Do not have any Potion of Healing Left')
            rat_attack_error()
        else:
            choice = input('Use Potion of Healing?(Y/N): ')
            if choice == 'Y':
                hero_stats['HP'] += 5
                potion_of_healing -= 1
                print('You have healed for 5 HP')
                print()
                run_from_rat_fail_error()
            elif choice == 'N':
                print()
                run_from_rat_fail_error()
            elif choice == 'with great power comes great responsibility':   #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                rrun_from_rat_fail_error()
            elif choice =='Greed is Good':
                print('Money Cheat Activated!')
                money_cheat()
                print()
                run_from_rat_fail_error()
            else:
                for i in range(len(invalid_option_list)):
                     print('{}'.format(invalid_option_list[i]))
                print()
                run_from_rat_fail_error()
    elif choice == 'with great power comes great responsibility':  #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        run_from_rat_fail_error()
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        run_from_rat_fail_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        print()
        run_from_rat_fail_error()

def run_from_rat_error(): #this is for when player input invalid option when successfully ran away from rat
    print('You run and hide.')
    print('The {} have {} HP left.'.format(rat_stats['Name'], rat_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_stats['Name']))
    print('Damage: {}-{}'.format(rat_stats['Min Damage'], rat_stats['Max Damage']))
    print('Defense: {}'.format(rat_stats['Defense']))
    print('HP: {}'.format(rat_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        view_character()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_encounter()
    elif choice == '2':
        view_map()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_encounter()
    elif choice == '3':
        move_around()
    elif choice == '4':
        sense_orb()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_encounter()
    elif choice == '5':
        exit_game()
    elif choice == 'with great power comes great responsibility':  #stat cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        run_from_rat_error()
    elif choice =='Greed is Good':    #money cheat code
        print('Money Cheat Activated!')
        money_cheat()
        print()
        run_from_rat_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        print()
        run_from_rat_error()

def run_from_rat_king():  #function for when player runs from rat
    global potion_of_healing
    global rat_king_stats
    global hero_stats
    run_chance = random.randint(1, 10)  #to make running away from the rat king a 1/10 chance
    if run_chance == 7:
        print('You run and hide.')  #when player succeeds at running
        for i in range(len(outdoor_menu_list)):
            print('{}) {}'.format((i+1), outdoor_menu_list[i]))
        choice = input('Enter Choice: ')
        print()
        if choice == '1':
            view_character()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_king_encounter()
        elif choice == '2':
            view_map()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_king_encounter()
        elif choice == '3':
            move_around()
        elif choice == '4':
            sense_orb()
            print('You have been found by the {}'.format(rat_stats['Name']))
            rat_king_encounter()
        elif choice == '5':
            exit_game()
        elif choice == 'with great power comes great responsibility':
            print('Stats Cheat Activated!')
            print()
            stats_cheat()
            run_from_rat_king_error()
        elif choice =='Greed is Good':    #money cheat code
            print('Money Cheat Activated!')
            money_cheat()
            print()
            run_from_rat_king_error()
        else:
            for i in range(len(invalid_option_list)):
                print('{}'.format(invalid_option_list[i]))
            print()
            run_from_rat_king_error()
    else:
        print('You have failed to run away.') #when player fails at running
        damage_dealt_by_rat_king = (random.randint(rat_king_stats['Min Damage'],rat_king_stats['Max Damage'])) - hero_stats['Defense']
        if damage_dealt_by_rat_king < 0:
            damage_dealt_by_rat_king = 0
        print('Ouch! The {} hit you for {} damage!'.format(rat_king_stats['Name'], damage_dealt_by_rat_king))
        hero_stats['HP'] = hero_stats['HP'] - damage_dealt_by_rat_king
        if hero_stats['HP'] < 1:
            print('You have 0 HP left.')
            rat_king_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
            game_over()
        else:
            print('You have {} HP left.'.format(hero_stats['HP']))
            print('Encounter! - {}'.format(rat_king_stats['Name']))
            print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
            print('Defense: {}'.format(rat_king_stats['Defense']))
            print('HP: {}'.format(rat_king_stats['HP']))
            for i in range(len(combat_menu_list)):
                print('{}) {}'.format((i+1), combat_menu_list[i]))
            print('3) Use Potion of Healing')
            choice = input('Enter Choice: ')
            print()
            if choice == '1':
                rat_king_attack()
            elif choice == '2':
                run_from_rat_king()
            elif choice == 'with great power comes great responsibility':  #stats cheat code
                print('Stats Cheat Activated!')
                print()
                stats_cheat()
                run_from_rat_king_fail_error()
            elif choice == '3':  #for healing potion
                if potion_of_healing < 1:
                    print('Currently Do not have any Potion of Healing Left')
                    run_from_rat_king_fail_error()
                else:
                    choice = input('Use Potion of Healing?(Y/N): ')
                    if choice == 'Y':
                        hero_stats['HP'] += 5
                        potion_of_healing -= 1
                        print('You have healed for 5 HP')
                        print()
                        run_from_rat_king_fail_error()
                    elif choice == 'N':
                        print()
                        run_from_rat_king_fail_error()
            elif choice =='Greed is Good':   #money cheat code
                print('Money Cheat Activated!')
                money_cheat()
                print()
                run_from_rat_king_fail_error()
            else:
                for i in range(len(invalid_option_list)):
                    print('{}'.format(invalid_option_list[i]))
                print()
                run_from_rat_king_fail_error()

def run_from_rat_king_fail_error():  #this is for when player input an invalid option when he fails to run away from the rat
    print('You have failed to run away.')
    print('The {} have {} HP left.'.format(rat_king_stats['Name'], rat_king_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_king_stats['Name']))
    print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
    print('Defense: {}'.format(rat_king_stats['Defense']))
    print('HP: {}'.format(rat_king_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    print('3) Use Potion of Healing')
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        rat_king_attack()
    elif choice == '2':
        run_from_rat_king()
    elif choice == 'with great power comes great responsibility': #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        run_from_rat_king_fail_error()
    elif choice == '3':  #for healing potion
        if potion_of_healing < 1:
            print('Currently Do not have any Potion of Healing Left')
            run_from_rat_king_fail_error()
        else:
            choice = input('Use Potion of Healing?(Y/N): ')
            if choice == 'Y':
                hero_stats['HP'] += 5
                potion_of_healing -= 1
                print('You have healed for 5 HP')
                print()
                run_from_rat_king_fail_error()
            elif choice == 'N':
                print()
                run_from_rat_king_fail_error()
    elif choice =='Greed is Good':   #money cheat code
        print('Money Cheat Activated!')
        money_cheat()
        print()
        run_from_rat_king_fail_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        run_from_rat_king_fail_error()

def run_from_rat_king_error(): #this is for when player input invalid option when successfully ran away from rat king
    print('You run and hide.')
    print('The {} have {} HP left.'.format(rat_king_stats['Name'], rat_king_stats['HP']))
    print('You have {} HP left.'.format(hero_stats['HP']))
    print('Encounter! - {}'.format(rat_king_stats['Name']))
    print('Damage: {}-{}'.format(rat_king_stats['Min Damage'], rat_king_stats['Max Damage']))
    print('Defense: {}'.format(rat_king_stats['Defense']))
    print('HP: {}'.format(rat_king_stats['HP']))
    for i in range(len(combat_menu_list)):
        print('{}) {}'.format((i+1), combat_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        view_character()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_king_encounter()
    elif choice == '2':
        view_map()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_king_encounter()
    elif choice == '3':
        move_around()
    elif choice == '4':
        sense_orb()
        print('You have been found by the {}'.format(rat_stats['Name']))
        rat_king_encounter()
    elif choice == '5':
        exit_game()
    elif choice == 'with great power comes great responsibility':  #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        run_from_rat_king_error()
    elif choice =='Greed is Good':    #money cheat code
        print('Money Cheat Activated!')
        money_cheat()
        print()
        run_from_rat_king_error()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        print()
        run_from_rat_king_error()
        
def outdoor_menu():  #function for outdoor menu
    global rat_king_stats
    global rat_stats
    global day
    global bless_count
    global bless_num
    print('Day {}: You are out in the open.'.format(day))
    for i in range(len(outdoor_menu_list)):
        print('{}) {}'.format((i+1), outdoor_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        view_character()
        outdoor_menu()
    elif choice == '2':
        view_map()
        outdoor_menu()
    elif choice == '3':
        move_around()
    elif choice == '4':
        sense_orb()
        day += 1
        if day >= 10 and day < 21:
            rat_king_stats = {'Name':'Rat King', 'Min Damage': 10, 'Max Damage': 14, 'Defense': 6, 'HP': 30} #stat increase as day goes on
            rat_stats = {'Name': 'Rat', 'Min Damage': 3, 'Max Damage': 5, 'Defense': 2, 'HP': 15}  #stat increase as day goes on
        elif day >= 20:
            rat_king_stats = {'Name':'Rat King', 'Min Damage': 12, 'Max Damage': 16, 'Defense': 7, 'HP': 35} #stat increase as day goes on
            rat_stats = {'Name': 'Rat', 'Min Damage': 5, 'Max Damage': 7, 'Defense': 3, 'HP': 20}  #stat increase as day goes on
        if bless_count > 0:
            bless_count -= 1
            if bless_num == 1:
                hero_stats['Min Damage'] -= 2
                hero_stats['Max Damage'] -= 2
                bless_num = 0
            elif bless_num == 2:
                hero_stats['Defense'] -= 2
                hero_stats['HP'] -= 5
                bless_num = 0
        outdoor_menu()
    elif choice == '5':
        exit_game()
    elif choice == 'with great power comes with great responsiblity':  #stats cheat code
        print('Stats Cheat Activated!')
        print()
        stats_cheat()
        outdoor_menu()
    elif choice =='Greed is Good':
        print('Money Cheat Activated!')
        money_cheat()
        print()
        outdoor_menu()
    else:
        for i in range(len(invalid_option_list)):
            print('{}'.format(invalid_option_list[i]))
        outdoor_menu()
    
        
def sense_orb(): #code for the sense/pick up orb of power
    global curse
    global orb_check
    global hero_stats
    if orb_map[x][y] != 'O':   #code for when the player is not on the Orb of power
        if orb_pos[0] > hero_pos[0] :
            if orb_pos[1] > hero_pos[1]:
                print('You sense that the Orb of Power is to the southeast')
                outdoor_menu()
            elif orb_pos[1] < hero_pos[1]:
                print('You sense that the Orb of Power is to the southwest')
            elif orb_pos[1] == hero_pos[1]:
                print('You sense that the Orb of Power is to the south')
        elif orb_pos[0] < hero_pos[0]:
            if orb_pos[1] > hero_pos[1]:
                print('You sense that the Orb of Power is to the northeast')
                outdoor_menu()
            elif orb_pos[1] < hero_pos[1]:
                print('You sense that the Orb of Power is to the northwest')
            elif orb_pos[1] == hero_pos[1]:
                print('You sense that the Orb of Power is to the north')
        elif orb_pos[0] == hero_pos[0]:
            if orb_pos[1] > hero_pos[1]:
                print('You sense that the Orb of Power is to the east')
            elif orb_pos[1] < hero_pos[1]:
                print('You sense that the Orb of Power is to the west')
    else:
        print('You have found the Orb of Power!')  #when player is on the Orb of power
        while (hero_stats['Min Damage'] == 2 and hero_stats['Max Damage'] == 4 and hero_stats['Defense'] == 1):
            choice = input('Do you want to pick it up? (Y/N): ')  #whether the player wants to pick up the orb
            if choice == 'Y':
                hero_stats['Min Damage'] += 5
                hero_stats['Max Damage'] += 5
                hero_stats['Defense'] += 5
                print('You picked up the Orb of Power!')
                print('Your Attack increased by 5!')
                print('Your Defense increased b 5!')
                orb_check = True
                outdoor_menu()
                break
            elif choice == 'N':
                choice = input('Are you sure? (Y/N): ')  #to confirm his choice of decline
                if choice == 'Y':
                    choice = input('Are you really sure? (Y/N): ') #to confirm confirm his choice of decline
                    if choice == 'Y':
                        choice = input('Are you really reallly sure? (Y/N): ')  #to confirm confirm confirm his choice of decline
                        if choice == 'Y':
                            print('Fine. Have it your way.')  #removes the orb after the player declines
                            print('May you succeed in your endeavours')
                            print()
                            orb_map[x][y] = ' '
                            outdoor_menu()
                            break
                        elif choice == 'N':
                            continue
                        elif choice == 'SCREW YOU ORB': #easter egg when player types this in
                            print('You are now cursed by the Orb of Power')  #gets various curses
                            curse = True
                            orb_curse()
                            print()
                            outdoor_menu()
                        else:
                            print('Invalid Choice.')  #when player inputs an invalid option
                            print('Please Try Again.')
                            print()
                            continue
                    elif choice == 'N':
                        continue
                    elif choice == 'SCREW YOU ORB':
                        print('You are now cursed by the Orb of Power')
                        curse = True
                        orb_curse()
                        print()
                        outdoor_menu()
                    else:
                        print('Invalid Choice.')
                        print('Please Try Again.')
                        print()
                        continue
                elif choice == 'N':
                    continue
                elif choice == 'SCREW YOU ORB':
                    print('You are now cursed by the Orb of Power')
                    curse = True
                    orb_curse()
                    print()
                    outdoor_menu()
                else:
                    print('Invalid Choice.')
                    print('Please Try Again.')
                    print()
                    continue
            elif choice == 'SCREW YOU ORB':
                print('You are now cursed by the Orb of Power')
                curse = True
                orb_curse()
                print()
                outdoor_menu()
            else:
                print('Invalid Choice.')
                print('Please Try Again.')
                print()
                continue            

def game_over():  #game over function
    global day
    global hero_stats
    global hero_pos
    global gmap
    print('GAME OVER')
    if phoenix_down == True:
        print('You have 1 Phoenix Down currently')   #revive hero if there is phoenix down in inventory
        print('Do you want to use it?(Y/N): ')
        choice = input('Do you want to try again? (Y/N): ')
        print()
        if choice == 'Y':
            print('You have been revived!')
            if gmap[x][y] == 'K' or 'H/K':   #if player dies and revives on the Rat king
                rat_king_encounter()
            else:
                outdoor_menu()
        elif choice == 'N':
            day = 1   #reset day counter
            hero_stats = {'Name': 'The Hero', 'Min Damage': 2, 'Max Damage': 4, 'Defense': 1, 'HP': 20}  #reset hero stats
            hero_pos = [0, 0]   #reset hero position
            gmap= [['H/T',' ',' ',' ',' ',' ',' ',' '],   #reset game map
                   [' ',' ',' ','T',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ','T',' ',' '],
                   [' ','T',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ','T',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ','K']]
            exit_game()
        elif choice == 'Giving up is what kills people':  #cheat code to self revive
            print('You have been revived!')
            if gmap[x][y] == 'K' or 'H/K':   #if player dies and revives on the Rat king
                rat_king_encounter()
            else:
                outdoor_menu() #otherwise revive and access the outdoor menu
        else:
            print('Invalid Choice.')    #when the player inputs an invalid option
            print('Please Try Again.')
            game_over() 
    else:
        choice = input('Do you want to try again? (Y/N): ')
        print()
        if choice == 'Y':
            day = 1  #reset day counter
            hero_pos = [0, 0] #reset hero position
            hero_stats = {'Name': 'The Hero', 'Min Damage': 2, 'Max Damage': 4, 'Defense': 1, 'HP': 20}  #reset hero stats
            gmap= [['H/T',' ',' ',' ',' ',' ',' ',' '],    #reset game map
                   [' ',' ',' ','T',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ','T',' ',' '],
                   [' ','T',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ','T',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ','K']]
            main_menu(main_menu_list)
        elif choice == 'N':
            day = 1   #reset day counter
            hero_stats = {'Name': 'The Hero', 'Min Damage': 2, 'Max Damage': 4, 'Defense': 1, 'HP': 20}  #reset hero stats
            hero_pos = [0, 0]   #reset hero position
            gmap= [['H/T',' ',' ',' ',' ',' ',' ',' '],   #reset game map
                   [' ',' ',' ','T',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ','T',' ',' '],
                   [' ','T',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ','T',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ','K']]
            exit_game()
        elif choice == 'Giving up is what kills people':  #cheat code to self revive
            print('You have been revived!')
            if gmap[x][y] == 'K' or 'H/K':   #if player dies and revives on the Rat king
                rat_king_encounter()
            else:
                outdoor_menu() #otherwise revive and access the outdoor menu
        else:
            print('Invalid Choice.')    #when the player inputs an invalid option
            print('Please Try Again.')
            game_over()

def orb_curse():  #curse that the player would recieve if he yells at the orb
    global rat_stats
    global rat_king_stats
    global hero_stats
    global curse_num
    global curse
    curse = True
    curse_selection = random.randint(1, 3)
    if curse_selection == 1:
        print('You have been cursed with low accuracy')
        curse_num = 1
    elif curse_selection == 2:
        print('You have been cursed with high fragility')
        hero_stats['Defense'] = 0
        curse_num = 2
    elif curse_selection == 3:
        print('You have been cursed with Enemy Longevitiy')
        rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 25}
        rat_king_stats = {'Name':'Rat King', 'Min Damage': 8, 'Max Damage': 12, 'Defense': 5, 'HP': 70}
        curse_num = 3

def church():   #function for church
    global rat_stats
    global rat_king_stats
    global orb_check
    global money
    global hero_stats
    global curse
    global curse_num
    global bless_count
    global bless_num
    print('Welcome to the Church! - Priestess')
    print('What can I do for you? - Priestess')
    for i in range(len(church_menu_list)):
        print('{}) {}'.format((i+1), church_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':
        print('Which Blessing would you want? - Priestess')   #blessing
        for i in range(len(blessing_list)):
            print('{}) {}'.format((i+1), blessing_list[i]))
        choice = input('Enter Choice: ')
        print()
        if choice == '1':
            print('That will costs 20 Gold. - Priestess')
            pay = input('Pay up?(Y/N): ')
            if pay == 'Y':
                if money < 20:   #check if user has enough gold
                    print('Sorry you do not have the required amount of Gold. - Priestess')
                    church()
                else:
                    money -= 20
                    print('You are now Blessed by the God of War,  Ares')    #first blessing
                    print('You feel stronger')
                    print('You lost 20 Gold')
                    global bless_count
                    global bless_num
                    bless_count = 3
                    bless_num = 1
                    hero_stats['Min Damage'] += 2
                    hero_stats['Max Damage'] += 2
                    church()
            elif pay == 'N':
                print('Alright, I hope our other services meet your needs :) - Priestess')
                church()
            else:
                print('Invalid Choice.')    #for invalid options
                print('Please Try Again.')
                church_repeat
        elif choice == '2': #second blessing
            print('That will costs 30 Gold. - Priestess')
            pay = input('Pay up?(Y/N): ')
            if pay == 'Y':
                if money < 30:
                    print('Sorry you do not have the required amount of Gold. - Priestess') #if player does not have enough money
                    church()
                else:
                    money -= 30
                    print('You are now Blessed by the Goddess of Safety and Salvation,  Soteria')  #get blessing
                    print('You feel tougher')
                    print('You lost 20 Gold')
                    bless_count = 3   #for how long blessing lasts
                    bless_num = 2     #for what type of blessing
                    hero_stats['Defense'] += 2
                    hero_stats['HP'] += 5
                    church()
            elif pay == 'N':
                print('Alright, I hope our other services meet your needs :) - Priestess')
                church_repeat()
            else:
                print('Invalid Choice.')   #for invalid options
                print('Please Try Again.')
                church()
        else:
            print('Invalid Choice.')   #for invalid options
            print('Please Try Again.')
            church()
            
    elif choice == '2':    #for healing
        print('That will costs 15 Gold. - Priestess')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 15:   #check for required amount of gold in hero's inventory
                print('Sorry you do not have the required amount of Gold. - Priestess')  
                church()
            else:
                money -= 15
                print('You are now Healed by the God of Healing, Apollo')
                print('You feel healthier.')
                print('You lost 15 Gold')
                hero_stats['HP'] = 20
                church()
        elif pay == 'N':
            print('Alright, I hope our other services meet your needs :) - Priestess')
            church()
        

    elif choice == '3':     #to purify any curse on the hero
        print('That will costs 30 Gold. - Priestess')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 30:
                print('Sorry you do not have the required amount of Gold. - Priestess')   #check for required gold
                church()
            else:
                if curse == True:
                    money -= 30
                    print('You have been purified by a Holy Light')
                    print('You feel your soul being cleansed.')
                    print('You lost 15 Gold')
                    if curse_num == 2:
                        if orb_check == True:
                            if bless_num > 0:
                                hero_stats['Defense'] = 8
                                print('Your Curse of Fragility has been removed.')
                                print()
                            else:
                                hero_stats['Defense'] = 6
                                print('Your Curse of Fragility has been removed.')
                                print()
                        else:
                            if bless_num > 0:
                                hero_stats['Defense'] = 3
                                print('Your Curse of Fragility has been removed.')
                                print()
                            else:
                                hero_stats['Defense'] = 1
                                print('Your Curse of Fragility has been removed.')
                                print()
                    elif curse_num == 3:
                        rat_stats = {'Name': 'Rat', 'Min Damage': 1, 'Max Damage': 3, 'Defense': 1, 'HP': 10}
                        rat_king_stats = {'Name':'Rat King', 'Min Damage': 8, 'Max Damage': 12, 'Defense': 5, 'HP': 25}
                        print('Your Curse of Enemy Longevitiy has been removed.')
                    curse_num = 0
                    curse = False
                    church()
                    
                else:
                    print('You do not have any curses on you at the moment. - Priestess')  #if hero has no curse
                    church()
        elif pay == 'N':
            print('Alright, I hope our other services meet your needs :) - Priestess')
            church()

        else:
            print('Invalid Choice')  #for invalid options
            print('Please Try Again')
            church_repeat
    elif choice == '4':
        print()
        new_game()
    elif choice == 'with great power comes great responsibility':   #stats cheat code
        print('Stats Cheat Code Activated!')
        stats_cheat()
        print()
        church()
    elif choice =='Greed is Good':   #money cheat code
        print('Money Cheat Activated!')
        money_cheat()
        print()
        church()
    else:
        print('Invalid Choice.')   #for invalid options
        print('Please Try Again.')  
        church()

def shop():   #shop function
    global phoenix_down
    global potion_of_healing
    global iron_sword
    global chainmail_armour
    global hero_stats
    global shop_menu_list
    global money
    print('Welcome to my store. - Merchant')
    print('Look around and buy anything that catches your eye. - Merchant')
    for i in range(len(shop_menu_list)):
        print('{}) {}'.format((i+1), shop_menu_list[i]))
    choice = input('Enter Choice: ')
    print()
    if choice == '1':   #buy potion of healing
        print('Potion of Healing')
        print('Heals 5 HP Upon Use')
        print('Costs 5 Gold')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 5:
                print('Sorry you currently do not have the adequate amount of funds to afford this') #check funds
                print()
                shop()
            else:
                money -= 5
                print('You now have Potion of Healing')
                potion_of_healing += 1
                print()
                shop()
        elif pay == 'N':
            print('I hope my other wares catches your eye. - Merchant')
            shop()
        elif pay == 'Greed is Good': #money cheat code
            print('Money Cheat Activated!')
            print()
            money_cheat()
            shop()
        else:
            print('Invalid Choice.')  #for invalid options
            print('Please Try Again.')
            print()
            shop()
    elif choice == '2':
        print('Iron Sword')  #buy weapon
        print('Increase Current Damage by 2')
        print('Costs 25 Gold')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 25:
                print('Sorry you currently do not have the adequate amount of funds to afford this')  #check funds
                print()
                shop()
            else:
                money -= 25
                print('You now have Iron Sword')
                hero_stats['Min Damage'] += 2
                hero_stats['Max Damage'] += 2
                shop_menu_list[1] = 'Out of Stock'
                iron_sword = True
                print()
                shop()
        elif pay == 'N':
            print('I hope my other wares catches your eye. - Merchant')
            shop()
        elif pay == 'Greed is Good':  #money cheat code
            print('Money Cheat Activated!')
            print()
            money_cheat()
            shop()
        else:
            print('Invalid Choice.')  #for invalid options
            print('Please Try Again.')
            print()
            shop()
    elif choice == '3':
        print('Chainmail Armour')   #buy armour
        print('Increase Current Defense by 2')
        print('Costs 40 Gold')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 40:
                print('Sorry you currently do not have the adequate amount of funds to afford this')  #check funds
                print()
                shop()
            else:
                money -= 40
                print('You now have Chainmail Armour')
                hero_stats['Defense'] += 2
                shop_menu_list[2] = 'Out of Stock'
                chainmail_armour = True
                print()
                shop()
        elif pay == 'N':
            print('I hope my other wares catches your eye. - Merchant')
            shop()
        elif pay == 'Greed is Good':  #money cheat code
            print('Money Cheat Activated!')
            print()
            money_cheat()
            shop()
        else:
            print('Invalid Choice.')
            print('Please Try Again.')   #for invalid options
            print()
            shop()
        
    elif choice == '4':   #for revive item
        print('Phoenix Down')
        print('Legend has it that it was made with the feathers of a phoenix.')
        print('Rumored to give the holder a second life.')
        print('Costs 60 Gold')
        pay = input('Pay up?(Y/N): ')
        if pay == 'Y':
            if money < 60:  #check funds
                print('Sorry you currently do not have the adequate amount of funds to afford this')
                print()
                shop()
            else:
                money -= 60
                print('You now have Phoenix Down')
                shop_menu_list[3] = 'Out of Stock'
                phoenix_down = True
                print()
                shop()
        elif pay == 'N':
            print('I hope my other wares catches your eye. - Merchant')
            shop()
        elif pay == 'Greed is Good':   #money cheat code
            print('Money Cheat Activated!')
            print()
            money_cheat()
            shop()
        else:
            print('Invalid Choice.')  #for invalid options
            print('Please Try Again.')
            print()
            shop()
    elif choice == '5':
        print('Please come again next time! - Merchant')
        new_game()
    elif choice == 'Greed is Good':  #money cheat code
        print('Money Cheat Activated!')
        print()
        money_cheat()
        shop()
    elif choice == 'with great power comes great responsibility':   #stats cheat code
        print('Stats Cheat Code Activated!')
        stats_cheat()
        print()
        church()
    else:
        print('Invalid Choice.')
        print('Please Try Again.')
        print()
        shop()        
        
def money_cheat(): #cheat code for lots of cash
    global money
    money = 99999
    
def stats_cheat(): #a cheat code that gives me max stats
    global orb_checkk
    global hero_stats
    orb_check = True    #make it so the player has an Orb 
    hero_stats['HP'] = 999
    hero_stats['Defense'] = 999
    hero_stats['Min Damage'] = 999
    hero_stats['Max Damage'] = 999

ran_orb()   #randomize orb of power location
main_menu(main_menu_list)   #to being the entire code
