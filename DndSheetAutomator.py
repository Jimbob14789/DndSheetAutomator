import random
#each of the die types is set as a list for use with the random module
d4 = [1,2,3,4]
d6 = [1,2,3,4,5,6]
d8 = [1,2,3,4,5,6,7,8]
d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#placing the deathsave variables up here is an attempted fix to not being healed above 0 during death saves loop
deathsavesucess = 0
deathsavefailure = 0
totaldamage = 0
#the xp requirements are included with their corresponding level are put in a list
#for easy reference later
levelxp = [0,1,300,2,900,3,2700,4,6500,5,14000,6,23000,7,34000,8,48000,9,64000,10,85000,11,100000,12,120000,13,140000,14,165000,15,195000,16,225000,17,265000,18,305000,19,355000,20]

#the file directory for the character sheet is put here
sheet = open('C:\\Users\\jimdo\\Downloads\\sheet.txt')
#each line of the sheet is read in order
for x in sheet:
    #this is used to find and separate the current level
    if 'Monk' in x:
        levelline = x
        levelsplit = x.split(' ') 
        level = int(levelsplit[1])
    #xp is found and separated
    if 'XP' in x:
        xsplit = x.split(" ")
        xp = int(xsplit[0])
    #hp is found and separated, since hp is written x/y the two components are separated
    if 'hp' in x:
        hpsplit = x.split(" ")
        hp = hpsplit[1]
        hpmaxsplit = hp.split("/")
        hpmax = int(hpmaxsplit[1])
        currenthp = int(hpmaxsplit[0])
    #the hit die is found and separated
    if 'HD' in x:
        hitdiesplit = x.split('d')
        hitdie = int(hitdiesplit[1])
    #con modifier is found and separated
    if 'Con[' in x:
        consplit = x.split(',')
        con = int(consplit[1])
    #dex modifier is found and separated
    if 'Dex[' in x:
        dexsplit = x.split(',')
        dex = int(dexsplit[1])
#when skill checks are implemented the other stats will be added here

#the main loop for each funtion, when the user types done the loop is exited
while True:
    #had a try, realized i didnt need it, and now am too lazy to unindent everything
    if True:
        menu = input("MENU Type 'damage' to access the damage calc. Type 'attack' for attack roll. Type 'done' to end  the session and enter xp calc\n")
            #section for damage calculation the try is added in order to prevent a callback on a non number input
        if menu == 'damage':
            while True:
                try:
                    damagetaken = input("enter the damage taken and type 'done' to return to menu. If being healed type a negative number\n")
                    if damagetaken == 'done':
                        break
                    currenthp = currenthp-int(damagetaken)
                    if currenthp <= 0:
                        print('your current hp is',currenthp)
                        print('damn son you dead')
                        #section for death saves if hp is 0 or below exited by typing done
                        while True:
                            try:
                                deathsave = input("Type 'roll' to roll death save. 'healed' to exit\n")
                                if deathsave == 'healed':
                                    try:
                                        healed = input('type amount healed')
                                        currenthp = currenthp+healed
                                        deathsavefailure = 0
                                        deathsavesucess = 0
                                        break
                                    except:
                                        print('type a valid amount')
                                if deathsave == 'roll':
                                    deathsaveroll = random.choice(d20)
                                    if deathsaveroll == 20:
                                        currenthp = 1
                                        deathsavefailure = 0
                                        deathsavesucess = 0
                                        print('nice! natural 20 you now have 1hp and dont have to roll!')
                                        break
                                    elif deathsaveroll == 1:
                                        deathsavefailure = deathsavefailure + 2
                                        print('you rolled a natural one you now have',deathsavesucess,'sucesses and',deathsavefailure,'failures')
                                    elif deathsaveroll < 10:
                                        deathsavefailure = deathsavefailure + 1
                                        print('you rolled a',deathsaveroll,'meaning you now have',deathsavesucess,'sucesses and',deathsavefailure,'failures')
                                    elif deathsaveroll >=10:
                                        deathsavesucess = deathsavesucess + 1
                                        print('you rolled a',deathsaveroll,'meaning you now have',deathsavesucess,'sucesses and',deathsavefailure,'failures')
                                    if deathsavesucess == 3:
                                        print('you made 3 death saves and no longer have to roll')
                                        currenthp = 1
                                        deathsavesucess = 0
                                        deathsavefailure = 0
                                        break
                                    elif deathsavefailure >= 3:
                                        print('damn you actually died')
                                        break
                                elif deathsave == 'done':
                                    break
                            except:
                                print('enter a valid word')
                    elif currenthp > hpmax:
                        currenthp = hpmax
                        print('your hp is now',currenthp)
                    else:
                        print('Your hp is '+str(currenthp)+'/'+str(hpmax))   
                except:
                    print('enter a valid number')
        if menu == 'attack':
            #attack menu, each attack the character can do is split into a different section plus a total damage counter and a way to reset that counter
            while True:
                attack = input("Type 'staff' for staff attack. Type 'fist' for fist. Type 'luz' for javelin. Type 'done' to return to menu. Type 'reset' to reset total damge. Type 'total' to see total damage\n")
                if attack == 'total':
                    print('The total damage is',totaldamage)
                if attack == 'reset':
                    totaldamage = 0
                if attack == 'luz':
                    attackroll = random.choice(d20)+9
                    if attackroll - 9 == 1:
                        print('Natural 1!')
                        break
                    hit = input('you rolled '+str(attackroll)+' did that hit y/n \n')
                    if hit == 'y':
                        if attackroll - 10 == 20:
                            damageroll = random.choice(d6)+random.choice(d6)+random.choice(d6)+5*2
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'with a nat 20')
                        else:
                            damageroll = random.choice(d6)+random.choice(d6)+random.choice(d6)+5
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'damage')
                    elif hit == 'n':
                        break
                if attack == 'staff':
                    attackroll = random.choice(d20)+10
                    if attackroll - 10 == 1:
                        print('Natural 1!')
                        break
                    hit1 = input('you rolled '+str(attackroll)+' did that hit y/n \n')
                    if hit1 == 'y':
                        if attackroll - 10 == 20:
                            damageroll = random.choice(d8)+6*2
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'with a nat 20')
                        else:
                            damageroll = random.choice(d8)+6
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'damage')
                    elif hit1 == 'n':
                        break
                if attack == 'fist':
                    attackroll = random.choice(d20)+9
                    if attackroll - 9 == 1:
                        print('Natural 1!')
                        break
                    hit2 = input('you rolled '+str(attackroll)+' did that hit y/n\n')
                    if hit2 =='y':
                        if attackroll - 9 == 20:
                            damageroll = random.choice(d8)+5*2
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'damage')
                        else:
                            damageroll = random.choice(d8)+5
                            totaldamage = damageroll+totaldamage
                            print('you did',damageroll,'damage')
                    elif hit2 == 'n':
                        break
                if attack == 'done':
                    break
        if menu == 'done':
            break
while True:
    newxp = input("Enter the xp gained this session\n",)
    try:
        finalxp = int(newxp) + int(xp)
        print('Your new xp is',finalxp)
        xptonext = finalxp - levelxp[level*2]
        if xptonext >= 0:
            level = level+1
            print('You leveled up! Your new level is',level)
            currenthp = str(currenthp+con+hitdie/2)
            hpmax = str(hpmax+con+hitdie/2)
            print('Your new hp is '+currenthp+'/'+hpmax)
            if level == 12|19:
                print('You have ability score improvements(not implemented yet)')
        else:
            print('You did not level up, you still have',abs(xptonext),'more xp to go')
        break
    except:
        print("enter a valid number numbnuts")

