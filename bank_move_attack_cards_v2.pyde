import random

player_names = {1: 'player ONE', 2: 'player TWO', 3: 'player THREE', 4: 'player FOUR'}
bank = {'player ONE': 0, 'player TWO': 0, 'player THREE': 0, 'player FOUR': 0}
turnOfPlayer = 0

Player_one_movement_card = []
Player_one_attack_card = []
Player_two_movement_card = []
Player_two_attack_card = []
Player_three_movement_card = []
Player_three_attack_card = []
Player_four_movement_card = []
Player_four_attack_card = []
neutral_movement_cards = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l',
                          'l', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', ]
powerUpDownCard_stack = ['mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.I', 'mk.II', 'mk.II', 'mk.II', 'mk.II', 'mk.II',
                         'shield', 'shield', 'shield', 'shield', 'shield', 'shield', 'nuke', 'blockade', 'blockade',
                         'blockade', 'blockade', 'blockade', 'blockade']
powerUpDownCard_price = {'mk.I': 10, 'mk.II': 15, 'shield': 15, 'blockade': 7, 'nuke': 35, 'used': 0}


# adds money(blobs) to the bank account of the player
def add_money(x, y, w, h, r, t, f):
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 100)
            rect((width* x), (height* y), (width* w), (height* h), r)
        else:
            rect((width* x), (height* y), (width* w), (height* h), r)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                global turnOfPlayer
                if turnOfPlayer == 0:
                    pass
                else:
                    player = player_names[t]
                    r = random.randint(1, 6)
                    bank[player] = bank[player] + r
                    turnOfPlayer = 0






# shuffles the cards stack and deals 5 movement card per player
def shuffle():
    if len(neutral_movement_cards) == 30:
        random.shuffle(neutral_movement_cards)
        for a in range(5):
            Player_one_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_two_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_three_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]
            Player_four_movement_card.append(neutral_movement_cards[a])
            del neutral_movement_cards[a]


# moves the chosen card to the neutral movement cardstack and the first movement card of the neutral stack is added to the player movement cardstack.
# movement_cards(card number,player movement card stack)
def movement_cards(k, p):
    neutral_movement_cards.append(p[k])
    del p[k]

#git is working, for real now!!. second change 




def hand_out_movement_card(x, y, w, h, r, t, f):
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 100)
            rect((width* x), (height* y), (width* w), (height* h), r)
        else:
            rect((width* x), (height* y), (width* w), (height* h), r)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                global turnOfPlayer
                if turnOfPlayer == 0:
                    pass
                if turnOfPlayer == 1:
                    if len(Player_one_movement_card)==5:
                        pass
                    else:
                        Player_one_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]
                        turnOfPlayer = 0
                        
                if turnOfPlayer == 2:
                    if len(Player_two_movement_card)==5:
                        pass
                    else:
                        Player_two_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]    
                        turnOfPlayer = 0        
                if turnOfPlayer == 3:
                    if len(Player_three_movement_card)==5:
                        pass
                    else:
                        Player_three_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]   
                        turnOfPlayer = 0               
                if turnOfPlayer == 4:
                    if len(Player_four_movement_card)==5:
                        pass
                    else:
                        Player_four_movement_card.append(neutral_movement_cards[0])
                        del neutral_movement_cards[0]
                        turnOfPlayer = 0






# rectangle with (x, y, width, height, radius) in percentages
def rect_h(x, y, w, h, r):
    rect((width / 100) * x, (height / 100) * y, (width / 100) * w, (height / 100) * h, r)

    
    
    
    
    
    
    
    
# button to change player turn value
# turn_button(x,y,width,height,radius,turn number, if elif):
def turn_button(x, y, w, h, r, t, f):
    global turnOfPlayer
    if f == 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
            fill(100, 100, 100, 100)
            rect((width*x), (height*y), (width * w), (height*h), r)
        else:
            rect((width*x), (height*y), (width * w), (height*h), r)
    elif f == 'play':
        if mouseButton == LEFT:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * w)) and mouseY < ((height*y) + (height*h)))):
                turnOfPlayer = t









# display test on the screen
def text_display():
    fill(0, 0, 0)
    p1 = 'player one: \n' + str(bank['player ONE']) + ' blobs'
    p2 = 'player two: \n' + str(bank['player TWO']) + ' blobs'
    p3 = 'player three: \n' + str(bank['player THREE']) + ' blobs'
    p4 = 'player four: \n' + str(bank['player FOUR']) + ' blobs'
    
    dice = 'Dice'
    cards = 'Cards'
    textSize(width * 0.01)
    text(p1, width * 0.02, height* 0.19)
    text(p2, width * 0.91, height * 0.19)
    text(p3, width  * 0.02, height* 0.955)
    text(p4, width * 0.91, height * 0.955)
    
    textSize(width  * 0.02)
    text(dice, width * 0.48, height * 0.125)
    text(cards, width  * 0.475, height * 0.18)
    
    textSize(width * 0.01)
    if turnOfPlayer == 0:
        turn = 'Please choose the player turn by clicking \n on the player spaceship'
        text(turn, width * 0.402, height  * 0.047)
    else:
        turn = 'player ' + str(turnOfPlayer) + ' turn'
        text(turn, width * 0.465, height * 0.06)

    # attack cards prise text
    attack_cards_price = ' CARDS PRICE \n Mk.I:       10 Blobs \n Mk.II:      15 Blobs \n Shield:    15 Blobs \n Nuke:      35 Blobs \n Blockade: 7 blobs '
    fill(250, 250,250)
    textSize(width * 1)
    text(attack_cards_price, width  * 0.89, height * 0.46)








# displays movement cards on the screen by checking the player stack list
# movement_card_play(x,y,player stack list name,list item number)
def movement_card(x, y, p, k, f):
    if f == 'play':
        if mousePressed:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + (height* 0.13)))):
                    movement_cards(k, p)
    elif 'display':
        if (mouseX > (width*x) and mouseY > (height*y) and (mouseX < ((width*x) + (width * 0.05)) and mouseY < ((height*y) + height* 0.13))):
            if p == Player_three_movement_card or p == Player_four_movement_card:
                if p[k] == 'f':
                    image(move_forward, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
    
                elif p[k] == 'r':
                    image(move_right, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'l':
                    image(move_left, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
            else:
                
                if p[k] == 'f':
                    image(move_forward, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'r':
                    image(move_right, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        
                elif p[k] == 'l':
                    image(move_left, (width*x), (height* (y+0.02)), (width *0.05), (height* 0.13))
        else:
            if p[k] == 'f':
                image(move_forward, (width*x), (height*y), (width *0.05), (height* 0.13))
    
            elif p[k] == 'r':
                image(move_right, (width*x), (height*y), (width *0.05), (height* 0.13))
    
            elif p[k] == 'l':
                image(move_left, (width*x), (height*y), (width *0.05), (height* 0.13))
            








# checks the bank account and if there is enough money then then the player can buy the attack and defence cards that are still available
# displays the attack and defence cards that are still available on the screen
# attack_card(x,y,card name, if and elif ):
def attack_card(x, y, k, f):
    global turnOfPlayer
    p = powerUpDownCard_stack[k]
    if f == 'buy':
        if mousePressed:
            if (mouseX > (width / 100) * x and mouseY > (height / 100) * y) and (
                    mouseX < ((width / 100) * x) + ((width / 100) * 5) and mouseY < ((height / 100) * y) + (
                    (height / 100) * 13)):
                if turnOfPlayer == 0:
                    pass
                else:
                    player = player_names[turnOfPlayer]
                    price = -powerUpDownCard_price[p]
                    if bank[player] + price < 0:
                        turnOfPlayer = 0
                    else:
                        if powerUpDownCard_stack[k]=='used':
                            turnOfPlayer = 0
                        else:
                            bank[player] = bank[player] + price
                            if turnOfPlayer == 1:
                                Player_one_attack_card.append(powerUpDownCard_stack[k])
                                turnOfPlayer = 0
                                powerUpDownCard_stack[k] = 'used'
                            elif turnOfPlayer == 2:
                                Player_two_attack_card.append(powerUpDownCard_stack[k])
                                turnOfPlayer = 0
                                powerUpDownCard_stack[k] = 'used'
                            elif turnOfPlayer == 3:
                                Player_three_attack_card.append(powerUpDownCard_stack[k])
                                turnOfPlayer = 0
                                powerUpDownCard_stack[k] = 'used'
                            elif turnOfPlayer == 4:
                                Player_four_attack_card.append(powerUpDownCard_stack[k])
                                turnOfPlayer = 0
                                powerUpDownCard_stack[k] = 'used'
    elif f == 'display':            
        if powerUpDownCard_stack[k] == 'mk.I':
            image(mk_I_laser, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13)
    
        elif powerUpDownCard_stack[k] == 'mk.II':
            image(mk_II_laser, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13)
    
        elif powerUpDownCard_stack[k] == 'shield':
            image(shield, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13)
    
        elif powerUpDownCard_stack[k] == 'blockade':
            image(blockade, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13)
    
        elif powerUpDownCard_stack[k] == 'nuke':
            image(nuke, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13)
    
        elif powerUpDownCard_stack[k] == 'used':
            image(sold, (width / 100) * x, (height / 100) * y, (width / 100) * 5, (height / 100) * 13) 
        
        
        if (mouseX > (width / 100) * x and mouseY > (height / 100) * y) and (mouseX < ((width / 100) * x) + ((width / 100) * 5) and mouseY < ((height / 100) * y) + ((height / 100) * 13)):
        
            if powerUpDownCard_stack[k] == 'mk.I':
                image(mk_I_laser, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) *(5+0.5), (height / 100) * (13+0.5))
        
            elif powerUpDownCard_stack[k] == 'mk.II':
                image(mk_II_laser, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) * (5+0.5), (height / 100) * (13+0.5))
        
            elif powerUpDownCard_stack[k] == 'shield':
                image(shield, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) * (5+0.5), (height / 100) * (13+0.5))
        
            elif powerUpDownCard_stack[k] == 'blockade':
                image(blockade, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) * (5+0.5), (height / 100) * (13+0.5))
        
            elif powerUpDownCard_stack[k] == 'nuke':
                image(nuke, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) * (5+0.5), (height / 100) * (13+0.5))
        
            elif powerUpDownCard_stack[k] == 'used':
                image(sold, (width / 100) * (x-0.25), (height / 100) * (y-0.25), (width / 100) * (5+0.5), (height / 100) * (13+0.5))        











# displays the attack and defence cards owned by the player on the screen next to the player spaceship
# removes attack and defence cards that player want to use by clicking on it
#   power_card(x,y,card number,if and elif,player power card stack)
def player_attack_card(x, y, k, f, p):
    if f == 'use':
        if mousePressed:
            if (mouseX > (width*x) and mouseY > (height*y) and (mouseX <  ((width*x) + width*0.035) and mouseY < ((height*y) + height*0.08))):
                del p[k - 1]

    elif f == 'display':
        if len(p) == 0:
            pass
        else:
            if p[k - 1] == 'mk.I':
                image(mk_I_laser, (width*x),  (height*y), width*0.035,height*0.08)

            elif p[k - 1] == 'mk.II':
                image(mk_II_laser,  (width*x),  (height*y), width*0.035, height*0.08)

            elif p[k - 1] == 'shield':
                image(shield, (width*x),  (height*y), width*0.035, height*0.08)

            elif p[k - 1] == 'blockade':
                image(blockade, (width*x), (height*y),width*0.035, height*0.08)

            elif p[k - 1] == 'nuke':
                image(nuke,  (width*x), (height*y),width* 0.035, height*0.08)

            elif p[k - 1] == 'used':
                image(sold, (width*x), (height*y), width*0.035, height*0.08)









def setup():
    frameRate(60)
    #size(1500,900)
    fullScreen()
    shuffle()
    
    global move_left, move_right, move_forward, Background, mk_I_laser, mk_II_laser, shield, blockade, nuke, sold
    
    move_left= loadImage("move_left.PNG")
    move_right= loadImage("move_right.PNG")
    move_forward= loadImage("move_forward.PNG")
    
    Background = loadImage("Background-1.jpg")
    
    mk_I_laser = loadImage("mk_I_laser.png")
    mk_II_laser = loadImage("mk_II_laser.png")
    shield = loadImage("shield.png")
    blockade = loadImage("blockade.png")
    nuke = loadImage("nuke.png")
    sold = loadImage("sold.png")
    
def draw():
    # Background
    
    image(Background, 0, 0, width, height)
    


    # player one background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    turn_button(0.005, 0.005, 0.10, 0.23, 20, 1, 'display')
    # player two background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    turn_button(0.895, 0.005, 0.10, 0.23, 20, 2, 'display')
    # player four background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    turn_button(0.895, 0.765, 0.10, 0.23, 20, 4, 'display')
    # player three background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    turn_button(0.005, 0.765, 0.10, 0.23, 20, 3, 'display')

    # player turn display background rectangle
    # rect(x, y, width, height, round)
    if turnOfPlayer == 0:
        fill(250, 250, 250, 100)
        rect(width*0.39, height*0.025, width*0.22,height*0.06, 20)
    else:
        fill(250, 250, 250, 100)
        rect(width*0.45, height*0.03, width*0.10,height*0.05, 20)


    # dice background rectangle
    # rect(x, y, width, height, round)
    fill(250, 250, 250, 100)
    add_money(0.45, 0.09, 0.10, 0.05, 20, turnOfPlayer, 'display')
    
    
    # display button to hand out movement card 
    fill(250, 250, 250, 100)
    hand_out_movement_card(0.45, 0.145,0.10, 0.05, 20, turnOfPlayer, 'display')
    
    
    
    # display player (blobs) amount and turn/dice test on the screen
    text_display()

    # display ships on the screen
    Ship1 = loadImage("BlueShip.png")
    image(Ship1, (width * 0.0155), (height* 0.015), (width * 0.075), (height * 0.15))
    Ship2 = loadImage("GreenShip.png")
    image(Ship2, (width * 0.907), (height* 0.015), (width * 0.075), (height * 0.15))
    Ship3 = loadImage("GreyShip.png")
    image(Ship3, (width * 0.0155), (height* 0.78), (width * 0.075), (height  * 0.15))
    Ship4 = loadImage("RedShip.png")
    image(Ship4, (width * 0.882), (height* 0.78), (width * 0.13), (height  * 0.14))

    # displays movement cards on the screen by checking the player stack list
    # movement_card_play(x,y,player stack list name,list item number,fuctionName)
    # player one
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_one_movement_card) >= 1:movement_card(0.12, 0.015, Player_one_movement_card, 0, 'display')
    if len(Player_one_movement_card) >= 2:movement_card(0.17, 0.015, Player_one_movement_card, 1, 'display')
    if len(Player_one_movement_card) >= 3:movement_card(0.22, 0.015, Player_one_movement_card, 2, 'display')
    if len(Player_one_movement_card) >= 4:movement_card(0.27, 0.015, Player_one_movement_card, 3, 'display')
    if len(Player_one_movement_card) >= 5:movement_card(0.32, 0.015, Player_one_movement_card, 4, 'display')
    # player two
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_two_movement_card) >= 1:movement_card(0.83, 0.015, Player_two_movement_card, 0, 'display')
    if len(Player_two_movement_card) >= 2:movement_card(0.78, 0.015, Player_two_movement_card, 1, 'display')
    if len(Player_two_movement_card) >= 3:movement_card(0.73, 0.015, Player_two_movement_card, 2, 'display')
    if len(Player_two_movement_card) >= 4:movement_card(0.68, 0.015, Player_two_movement_card, 3, 'display')
    if len(Player_two_movement_card) >= 5:movement_card(0.63, 0.015, Player_two_movement_card, 4, 'display')
    # player three
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_three_movement_card) >= 1:movement_card(0.12, 0.85, Player_three_movement_card, 0, 'display')
    if len(Player_three_movement_card) >= 2:movement_card(0.17, 0.85, Player_three_movement_card, 1, 'display')
    if len(Player_three_movement_card) >= 3:movement_card(0.22, 0.85, Player_three_movement_card, 2, 'display')
    if len(Player_three_movement_card) >= 4:movement_card(0.27, 0.85, Player_three_movement_card, 3, 'display')
    if len(Player_three_movement_card) >= 5:movement_card(0.32, 0.85, Player_three_movement_card, 4, 'display')
    # player four
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_four_movement_card) >= 1:movement_card(0.83, 0.85, Player_four_movement_card, 0, 'display')
    if len(Player_four_movement_card) >= 2:movement_card(0.78, 0.85, Player_four_movement_card, 1, 'display')
    if len(Player_four_movement_card) >= 3:movement_card(0.73, 0.85, Player_four_movement_card, 2, 'display')
    if len(Player_four_movement_card) >= 4:movement_card(0.68, 0.85, Player_four_movement_card, 3, 'display')
    if len(Player_four_movement_card) >= 5:movement_card(0.63, 0.85, Player_four_movement_card, 4, 'display')

    # displays the attack and defence cards that are still available on the screen
    # attack_card(x,y,card name, if and elif ):

    attack_card(57.5, 23.5, 0, 'display')
    attack_card(62.6, 23.5, 1, 'display')
    attack_card(67.7, 23.5, 2, 'display')
    attack_card(72.8, 23.5, 3, 'display')
    attack_card(77.9, 23.5, 4, 'display')
    attack_card(83, 23.5, 5, 'display')

    attack_card(57.5, 36.7, 6, 'display')
    attack_card(62.6, 36.7, 7, 'display')
    attack_card(67.7, 36.7, 8, 'display')
    attack_card(72.8, 36.7, 9, 'display')
    attack_card(77.9, 36.7, 10, 'display')
    attack_card(83, 36.7, 11, 'display')

    attack_card(57.5, 49.9, 12, 'display')
    attack_card(62.6, 49.9, 13, 'display')
    attack_card(67.7, 49.9, 14, 'display')
    attack_card(72.8, 49.9, 15, 'display')
    attack_card(77.9, 49.9, 16, 'display')
    attack_card(83, 49.9, 17, 'display')

    attack_card(57.5, 63.1, 18, 'display')
    attack_card(62.6, 63.1, 19, 'display')
    attack_card(67.7, 63.1, 20, 'display')
    attack_card(72.8, 63.1, 21, 'display')
    attack_card(77.9, 63.1, 22, 'display')
    attack_card(83, 63.1, 23, 'display')

    # displays the attack and defence cards owned by the player on the screen next to the player spaceship
    #   power_card(x,y,card number,if and elif,player power card stack)
    if len(Player_one_attack_card) >= 1: player_attack_card(0.12, 0.15, 1, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 2: player_attack_card(0.156, 0.15, 2, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 3: player_attack_card(0.192, 0.15, 3, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 4: player_attack_card(0.228, 0.15, 4, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 5: player_attack_card(0.264, 0.15, 5, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 6: player_attack_card(0.3, 0.15, 6, 'display', Player_one_attack_card)
    if len(Player_one_attack_card) >= 7: player_attack_card(0.336, 0.15, 7, 'display', Player_one_attack_card)

    if len(Player_two_attack_card) >= 1: player_attack_card(0.845, 0.15, 1, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 2: player_attack_card(0.809, 0.15, 2, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 3: player_attack_card(0.773, 0.15, 3, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 4: player_attack_card(0.737, 0.15, 4, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 5: player_attack_card(0.701, 0.15, 5, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 6: player_attack_card(0.669, 0.15, 6, 'display', Player_two_attack_card)
    if len(Player_two_attack_card) >= 7: player_attack_card(0.629, 0.15, 7, 'display', Player_two_attack_card)

    if len(Player_three_attack_card) >= 1: player_attack_card(0.12, 0.765, 1, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 2: player_attack_card(0.156, 0.765, 2, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 3: player_attack_card(0.192, 0.765, 3, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 4: player_attack_card(0.228, 0.765, 4, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 5: player_attack_card(0.264, 0.765, 5, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 6: player_attack_card(0.30, 0.765, 6, 'display', Player_three_attack_card)
    if len(Player_three_attack_card) >= 7: player_attack_card(0.336, 0.765, 7, 'display', Player_three_attack_card)

    if len(Player_four_attack_card) >= 1: player_attack_card(0.845, 0.765, 1, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 2: player_attack_card(0.809, 0.765, 2, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 3: player_attack_card(0.773, 0.765, 3, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 4: player_attack_card(0.737, 0.765, 4, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 5: player_attack_card(0.701, 0.765, 5, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 6: player_attack_card(0.665, 0.765, 6, 'display', Player_four_attack_card)
    if len(Player_four_attack_card) >= 7: player_attack_card(0.629, 0.765, 7, 'display', Player_four_attack_card)
    

def mousePressed():
    fill(250, 250, 250, 0)

    # dice background rectangle button
    # rect(x, y, width, height, round,functionName)
    add_money(0.45, 0.09, 0.10, 0.05, 20, turnOfPlayer, 'play')
    
    
    # button to hand out movement card 
    hand_out_movement_card(0.45, 0.145,0.10, 0.05, 20, turnOfPlayer, 'play')
    


    
    fill(250, 250, 250, 0)
    # makes the player background rectangle into a button
    # player one
    # rect(x, y, width, height, round)
    turn_button(0.005, 0.005, 0.10, 0.23, 20, 1, 'play')
    # player two
    # rect(x, y, width, height, round)
    turn_button(0.895, 0.005, 0.10, 0.23, 20, 2, 'play')
    # player four
    # rect(x, y, width, height, round)
    turn_button(0.895, 0.765, 0.10, 0.23, 20, 4, 'play')
    # player three
    # rect(x, y, width, height, round)
    turn_button(0.005, 0.765, 0.10, 0.23, 20, 3, 'play')

    # movement card will be removed by clicking on it and one new movement card from the neutral stack will be added to player stack
    # player one
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_one_movement_card) >= 1:movement_card(0.12, 0.015, Player_one_movement_card, 0, 'play')
    if len(Player_one_movement_card) >= 2:movement_card(0.17, 0.015, Player_one_movement_card, 1, 'play')
    if len(Player_one_movement_card) >= 3:movement_card(0.22, 0.015, Player_one_movement_card, 2, 'play')
    if len(Player_one_movement_card) >= 4:movement_card(0.27, 0.015, Player_one_movement_card, 3, 'play')
    if len(Player_one_movement_card) >= 5:movement_card(0.32, 0.015, Player_one_movement_card, 4, 'play')
    # player two
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_two_movement_card) >= 1:movement_card(0.83, 0.015, Player_two_movement_card, 0, 'play')
    if len(Player_two_movement_card) >= 2:movement_card(0.78, 0.015, Player_two_movement_card, 1, 'play')
    if len(Player_two_movement_card) >= 3:movement_card(0.73, 0.015, Player_two_movement_card, 2, 'play')
    if len(Player_two_movement_card) >= 4:movement_card(0.68, 0.015, Player_two_movement_card, 3, 'play')
    if len(Player_two_movement_card) >= 5:movement_card(0.63, 0.015, Player_two_movement_card, 4, 'play')
    # player three
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_three_movement_card) >= 1:movement_card(0.12, 0.85, Player_three_movement_card, 0, 'play')
    if len(Player_three_movement_card) >= 2:movement_card(0.17, 0.85, Player_three_movement_card, 1, 'play')
    if len(Player_three_movement_card) >= 3:movement_card(0.22, 0.85, Player_three_movement_card, 2, 'play')
    if len(Player_three_movement_card) >= 4:movement_card(0.27, 0.85, Player_three_movement_card, 3, 'play')
    if len(Player_three_movement_card) >= 5:movement_card(0.32, 0.85, Player_three_movement_card, 4, 'play')
    # player four
    # movement_card_play(x,y,player stack list name,list item number,if and alif)
    if len(Player_four_movement_card) >= 1:movement_card(0.83, 0.85, Player_four_movement_card, 0, 'play')
    if len(Player_four_movement_card) >= 2:movement_card(0.78, 0.85, Player_four_movement_card, 1, 'play')
    if len(Player_four_movement_card) >= 3:movement_card(0.73, 0.85, Player_four_movement_card, 2, 'play')
    if len(Player_four_movement_card) >= 4:movement_card(0.68, 0.85, Player_four_movement_card, 3, 'play')
    if len(Player_four_movement_card) >= 5:movement_card(0.63, 0.85, Player_four_movement_card, 4, 'play')

    # checks the bank account and if there is enough money then then player buy the attack and defence cards that are still available
    # attack_card(x,y,card name, if and elif ):
    attack_card(57.5, 23.5, 0, 'buy')
    attack_card(62.6, 23.5, 1, 'buy')
    attack_card(67.7, 23.5, 2, 'buy')
    attack_card(72.8, 23.5, 3, 'buy')
    attack_card(77.9, 23.5, 4, 'buy')
    attack_card(83, 23.5, 5, 'buy')
    
    attack_card(57.5, 36.7, 6, 'buy')
    attack_card(62.6, 36.7, 7, 'buy')
    attack_card(67.7, 36.7, 8, 'buy')
    attack_card(72.8, 36.7, 9, 'buy')
    attack_card(77.9, 36.7, 10, 'buy')
    attack_card(83, 36.7, 11, 'buy')


    attack_card(57.5, 49.9, 12, 'buy')
    attack_card(62.6, 49.9, 13, 'buy')
    attack_card(67.7, 49.9, 14, 'buy')
    attack_card(72.8, 49.9, 15, 'buy')
    attack_card(77.9, 49.9, 16, 'buy')
    attack_card(83, 49.9, 17, 'buy')

    attack_card(57.5, 63.1, 18, 'buy')
    attack_card(62.6, 63.1, 19, 'buy')
    attack_card(67.7, 63.1, 20, 'buy')
    attack_card(72.8, 63.1, 21, 'buy')
    attack_card(77.9, 63.1, 22, 'buy')
    attack_card(83, 63.1, 23, 'buy')

    # removes attack and defence cards that player want to use by clicking on it
    #   power_card(x,y,card number,if and elif,player power card stack)
    if len(Player_one_attack_card) >= 1: player_attack_card(0.12, 0.15, 1, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 2: player_attack_card(0.156, 0.15, 2, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 3: player_attack_card(0.192, 0.15, 3, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 4: player_attack_card(0.228, 0.15, 4, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 5: player_attack_card(0.264, 0.15, 5, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 6: player_attack_card(0.3, 0.15, 6, 'use', Player_one_attack_card)
    if len(Player_one_attack_card) >= 7: player_attack_card(0.336, 0.15, 7, 'use', Player_one_attack_card)

    if len(Player_two_attack_card) >= 1: player_attack_card(0.845, 0.15, 1, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 2: player_attack_card(0.809, 0.15, 2, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 3: player_attack_card(0.773, 0.15, 3, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 4: player_attack_card(0.737, 0.15, 4, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 5: player_attack_card(0.701, 0.15, 5, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 6: player_attack_card(0.669, 0.15, 6, 'use', Player_two_attack_card)
    if len(Player_two_attack_card) >= 7: player_attack_card(0.629, 0.15, 7, 'use', Player_two_attack_card)

    if len(Player_three_attack_card) >= 1: player_attack_card(0.12, 0.765, 1, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 2: player_attack_card(0.156, 0.765, 2, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 3: player_attack_card(0.192, 0.765, 3, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 4: player_attack_card(0.228, 0.765, 4, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 5: player_attack_card(0.264, 0.765, 5, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 6: player_attack_card(0.30, 0.765, 6, 'use', Player_three_attack_card)
    if len(Player_three_attack_card) >= 7: player_attack_card(0.336, 0.765, 7, 'use', Player_three_attack_card)

    if len(Player_four_attack_card) >= 1: player_attack_card(0.845, 0.765, 1, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 2: player_attack_card(0.809, 0.765, 2, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 3: player_attack_card(0.773, 0.765, 3, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 4: player_attack_card(0.737, 0.765, 4, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 5: player_attack_card(0.701, 0.765, 5, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 6: player_attack_card(0.665, 0.765, 6, 'use', Player_four_attack_card)
    if len(Player_four_attack_card) >= 7: player_attack_card(0.629, 0.765, 7, 'use', Player_four_attack_card)
    




    
