from random import randint
import random
import math

def numCheck(string):
    """This function takes in astring and chek if it is an integer and if it is one it returns an int of the string. otherwise it will retunr false.
        Parameters:
        :param string: a list of characters that is checked for an int
    """
    if string == "":
        return False
    elif string[0] == "0" or string[0] == "1" or string[0] == "2" or string[0] == "3" or string[0] == "4" or string[0] == "5" or string[0] == "6" or string[0] == "7" or string[0] == "8" or string[0] == "9":
        return int(string)
    else:
        return False
def nopeCheck(player, playerList, card, deck):
    """This function  takes in a player whose turn it, the list of all other players, the card being played, and the deck. It then checks the hands of all of the other players to see if there are any nope cards. Then it will give those players the opprotunity to play a nope if they would like and cancel the players action.
        Parameters:
        :param: the player that is taking a turn
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
        :param card: the card that is being played
        :param deck: the deck of cards
    """
    nopes = [[]]
    result = False
    for i in range (1,len(playerList)):
        nopes.append(search("Nope", playerList[i].hand))
    for i in range(1,len(nopes)):
        if nopes[i] > -1:
            if playerList[i].name[:-2] != "Computer":
                print(playerList[player].name, " is trying to play", card)
                play =input("Would you like to nope it? please enter Yes or No ")
                while play != "Yes" and play != "No":
                    play =input("Would you like to nope it? please enter Yes or No ")
                discard = playerList[i].hand.pop(nopes[i])
                deck.discardPile.append(discard)
                if play == "Yes":
                    print(playerList[i].name, "noped", card)
                    result = True
                break
            else:    
                if card == "Future" and card == "Skip" and card == "Taco Cat" and card == 'Melon Cat' and card == 'Beard Cat' and card == 'Rainbow-ralphing Cat' or card == 'Skip' or card == 'Attack' or card == 'Favor':
                    print(playerList[i].name, "noped", card)
                    discard = playerList[i].hand.pop(nopes[i])
                    deck.discardPile.append(discard)
                    result = True        
                    break
    return result           
                
def SKIP(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to play a skip card and end their turn without drawing a card
        :param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """
    nope = nopeCheck(player, playerList, "Skip", deck)
    if nope == False:
        print(playerList[player].name, "played a skip card and skipped their turn.")
        return "End"
    else:
        return 
def counter(player, playerList):
    """This function  takes in a player and the list of all other players. It returns a list of counts with the numbers of each individual cobmo cards and the number of different combo cards a player has.
        :param player: the player who is taking a turn and hand it is searching for the combo cards
        :param playerList: all of the players plaing the game
    """
    tacoCat = 0
    hairyPotatoCat = 0
    melonCat = 0
    beardCat = 0
    rainbowRalphingCat = 0
    total = 0
    for i in range(len(playerList[player].hand)):
        if playerList[player].hand[i].name == "Taco Cat":
            tacoCat += 1
        elif playerList[player].hand[i].name  == "Hairy Potato Cat":
            hairyPotatoCat += 1
        elif playerList[player].hand[i].name  == 'Melon Cat':
            melonCat += 1
        elif playerList[player].hand[i].name  == 'Beard Cat':
            beardCat += 1
        elif playerList[player].hand[i].name  == 'Rainbow-ralphing Cat':
            rainbowRalphingCat +=1
    counts = [tacoCat, hairyPotatoCat, melonCat, beardCat, rainbowRalphingCat]
    for num in counts:
        if num > 0:
            total+=1
    counts = [tacoCat, hairyPotatoCat, melonCat, beardCat, rainbowRalphingCat, total]
    return counts 


def FUTURE(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to play a future card and see the top three cards of the deck
        :param player: the player who is playing the future card
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """
    nope = nopeCheck(player, playerList, "Future", deck)
    if nope == False:     
        if playerList[player].name[:-2] != "Computer" :
            if len(deck.cards) > 2:
                print("The top cards are", deck.cards[0],",", deck.cards[1],"," ,deck.cards[2])
            elif len(deck.cards) == 2:
                print("The top cards are",deck.cards[0], deck.cards[1])
            elif len(deck.cards) == 1:
                 print("The top cards are",deck.cards[0])
            return True
        else:
            if len(deck.cards) > 2:
                CARDS = [deck.cards[0].name, deck.cards[1].name, deck.cards[2].name]
                return CARDS
            elif len(deck.cards) == 2:
                CARDS = [deck.cards[0].name, deck.cards[1].name]
                return CARDS
            elif len(deck.cards) == 1:
                CARDS = [deck.cards[0].name]
                return CARDS
        print(playerList[player].name,"looked into the future and saw the top 3 cards of the deck" )
    else:
        nothing = ["", "", ""]
        return nothing
    
def FAVOR(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to play a favor card and steal a card of opponents choice from their hand.
        ;param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """    
    nope = nopeCheck(player, playerList,"Favor", deck)
    if nope == False:
        if playerList[player].name[:-2] == "Computer":
            steal = randint(1, len(playerList)-1)
            while playerList[player].name == playerList[steal].name:
                steal = randint(1, len(playerList)-1)
            if playerList[steal].name[:-2] != "Computer":
                cardSteal = str(input("You have been target with a favor. What card would you like to give up? "))
                cardSteal = search(cardSteal, playerList[steal].hand)
                while cardSteal == -1:
                    if cardSteal == "":
                        cardSteal = randint(0, len(playerList[steal].hand)-1)
                        break
                    cardSteal = str(input("Please the card that you would like to give up? "))
                    cardSteal = search(cardSteal, playerList[steal].hand)
                    while cardSteal == -1:
                        cardSteal = str(input("Please the card that you would like to give up? "))
                        cardSteal = search(cardSteal, playerList[steal].hand)
                playerList[player].hand.append(playerList[steal].hand.pop(search(cardSteal, playerList[steal].hand)))
            else:
                cardSteal = randint(1, len(playerList[steal].hand))
                playerList[player].hand.append(playerList[steal].hand.pop(cardSteal))
        else:
            steal = input("What player do you want to steal from?")
            steal = numCheck(steal)
            while steal == False and steal >= len(playerList):
                steal = input("Please input a number. What player do you want to steal from?")
                steal = int(steal)
            stolenCard = playerList[steal].hand.pop(randint(0, len(playerList[steal].hand)-1))
            playerList[player].hand.append(stolenCard)
            print("You stole a ", stolenCard, " card from ", playerList[steal].name )
        print(playerList[player].name, 'played a favor card targeting', playerList[steal])
    else:
        return
def ATTACK(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to play an attack card which makes the next player take turns in a row.
        ;param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """     
    nope = nopeCheck(player, playerList, "Attack", deck)
    if nope == False:
        if playerList[player].name == playerList[1].name:
            playerList[player].pop(playerList[1])

        extraTurn = playerList[player + 1]
        playerList.insert(2, extraTurn)
        print(playerList[player].name,"attacked", playerList[player + 1])
        return "End"
    else:
        return
        
def SHUFFLE(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to play a shuffle card which shuffles the deck.
        ;param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """     
    nope = nopeCheck(player, playerList, "Shuffle", deck)
    if nope == False:    
        random.shuffle(deck.cards)
        print(playerList[player].name," shuffled the deck")

def COMBO(card, player, playerList, deck, counts, diffComboCardTotal):
    """This function  takes in a player, the list of all other players, the deck, the counts of their combo cards, and the number of different combo cards they have. It allows the player to combo off. Picking pairs will let them steal a random card from an opponent. Triple will let them see their opponents hand and pick the card the steal. Five different will allow them to take a card from the discard pile and put it in their hand.
        ;param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
        :param counts: list of the number of each combo card the player is holding
        :param iffComboCardTotal: is the number of different combo cards a player is holding
    """     
    possible = False
    if playerList[player].name[:-2] != "Computer":
        while possible == False:
            comboType = str(input("What kind of combo would you like to play? Pair, Triple, or Five different? "))
            while comboType != "Pair" and comboType != "Triple" and comboType != "Five different":
                comboType = str(input("What kind of combo would you like to play? Pair, Triple, or Five different? "))
            if comboType == "Pair":
                possible = True
                steal = input(" please do not input zero because that is you or 1 if that it is your first attack turn. Which player would you like to steal from?")
                steal = numCheck(steal)
                while steal >= len(playerList) and steal == playerList[player].name and steal == False:
                    steal = input("That player doesnt exist or is yourself. please enter a number less than,", len(playerList,"Which player would you like to steal from?"))
                    steal = numCheck(steal)
                for i in range(2):
                    discard = playerList[player].hand.pop(search(card, playerList[player].hand))
                    deck.discardPile.append(discard)
                nope = nopeCheck(player, playerList, card, deck)
                if nope == False: 
                    pos = randint(0, len(playerList[steal].hand)-1)
                    print("You stole",playerList[steal].hand[pos], "from", playerList[steal])
                    playerList[player].hand.append(playerList[steal].hand[pos])
            elif comboType == "Triple" and counts[card]>=3:
                possible = True
                steal = input(" please do not input zero because that is you or 1 if that it is your first attack turn. Which player would you like to steal from?")
                steal = numCheck(steal)
                while steal >= len(playerList) and steal == playerList[player].name and steal == False:
                    steal = input("That player doesnt exist or is yourself. please enter a number less than,", len(playerList,"Which player would you like to steal from?"))
                    steal = numCheck(steal)
                for i in range(3):
                    discard = playerlist[player].hand.pop(search(card, playerList[player].hand))
                    deck.discardPile.append(discard)
                nope = nopeCheck(player, playerList, card, deck)
                if nope == False: 
                    cardStolen = input(steal, "is holding", playerList[steal].hand, " what card would you like to steal? ")
                    pos = search(cardStolen, playerList[steal]. hand)
                    while pos == False:
                        cardStolen = input("That player is not holding that card", steal, "is holding", playerList[steal].hand, " what card would you like to steal? ")
                        pos = search(cardStolen, playerList[steal]. hand)          
                        print("You stole",playerList[steal].hand[pos], "from", playerList[steal])
                        playerList[player].hand.pop(playerList[steal].hand[pos])
                                
            elif comboType == "Five different" and diffComboCardTotal >= 5:
                possible = True
                tacoCat = playerList[player].hand.pop(search("Taco Cat", playerList[player].hand))
                melonCat = playerList[player].hand.pop(search("Melon Cat", playerList[player].hand))
                hairyPotatoCat = playerList[player].hand.pop(search("Hairy Potato Cat", playerList[player].hand))
                beardCat = playerList[player].hand.pop(search("Beard Cat", playerList[player].hand))
                rainbowRalphingCat =  playerList[player].hand.pop(search("Rainbow-ralphing Cat", playerList[player].hand))
                deck.discardPile.append(tacoCat)
                deck.discardPile.append(melonCa)
                deck.discardPile.append(hairyPotatoCat)
                deck.discardPile.append(beardCat)
                deck.discardPile.append(rainbowRalphingCat)
                nope = nopeCheck(player, playerList, card, deck)
                if nope == False: 
                    intoHand = str(input("What card would you like to take from the graveyard and put into your hand? "))
                    pos = search(intoHand, deck.discardPile)
                    while pos == False:
                        intoHand = str(input("That card is not in the discard. What card would you like to take from the graveyard and put into your hand? "))
                        pos = search(intoHand, deck.discardPile)
                    playerList[player].hand.append(deck.discardPile[pos])
                    print(playerList[player], "took",intoHand, " from the discard and added it back to their hand in exhange for 5 unique combo card")

    else:
        steal = randint(1, len(playerList)-1)
        while playerList[steal].name == playerList[player].name:
             steal = randint(1, len(playerList)-1)
        if diffComboCardTotal >= 5:
            tacoCat = playerList[player].hand.pop(search("Taco Cat", playerList[player].hand))
            melonCat = playerList[player].hand.pop(search("Melon Cat", playerList[player].hand))
            hairyPotatoCat = playerList[player].hand.pop(search("Hairy Potato Cat", playerList[player].hand))
            beardCat = playerList[player].hand.pop(search("Beard Cat", playerList[player].hand))
            rainbowRalphingCat =  playerList[player].hand.pop(search("Rainbow-ralphing Cat", playerList[player].hand))
            futureCheck = search("Future", playerList[steal].hand)
            attackCheck = search("Attack", playerList[steal].hand)
            shuffleCheck = search("Shuffle",playerList[steal].hand)
            skipCheck = search("Skip", playerList[steal].hand)
            favorCheck = search("Favor", playerList[steal].hand)
            defuseCheck = search("Defuse", playerList[steal].hand)
            deck.discardPile.append(tacoCat)
            deck.discardPile.append(melonCat)
            deck.discardPile.append(hairyPotatoCat)
            deck.discardPile.append(beardCat)
            deck.discardPile.append(rainbowRalphingCat)
            nope = nopeCheck(player, playerList, card, deck)
            if nope == False: 
                if defuseCheck != -1:
                    intoHand = playerList[steal].hand.pop(defuseCheck)
                    playerList[player].hand.append(intoHand)
                elif attackCheck != -1:
                    intoHand = playerList[steal].hand.pop(attackCheck)
                    playerList[player].hand.append(intoHand)
                elif futureCheck != -1: 
                    intoHand = playerList[steal].hand.pop(futureCheck)
                    playerList[player].hand.append(intoHand)
                elif skipCheck != -1: 
                    intoHand =playerList[steal].hand.pop(skipCheck)
                    playerList[player].hand.append(intoHand)
                elif favorCheck != -1:
                    intoHand=playerList[steal].hand.pop(favorCheck)
                    playerList[player].hand.append(intHand)
                elif shuffleCheck != -1:
                    intoHand=playerList[steal].hand.pop(shuffleCheck)
                    playerList[player].hand.append(intoHand)
                else:
                    intoHand = playerList[steal].hand.pop(randint(0,len(playerList[steal].hand)-1))
                    playerList[player].hand.append(intoHand)
                print(playerList[player], "took",intoHand, " from the discard and added it back to their hand in exhange for 5 unique combo cards")
        elif counts[card] >= 3:
            for i in range(3):
                discard = playerList[player].hand.pop(search(card, playerList[player].hand))
                deck.discardPile.append(discard)
            futureCheck = search("Future", playerList[steal].hand)
            attackCheck = search("Attack", playerList[steal].hand)
            shuffleCheck = search("Shuffle",playerList[steal].hand)
            skipCheck = search("Skip", playerList[steal].hand)
            favorCheck = search("Favor", playerList[steal].hand)
            defuseCheck = search("Defuse", playerList[steal].hand)
            nope = nopeCheck(player, playerList, card, deck)
            if nope == False: 
                if defuseCheck != -1:
                    intoHand = playerList[steal].hand.pop(defuseCheck)
                    playerList[player].hand.append(intoHand)
                elif attackCheck != -1:
                    intoHand = playerList[steal].hand.pop(attackCheck)
                    playerList[player].hand.append(intoHand)
                elif futureCheck != -1: 
                    intoHand = playerList[steal].hand.pop(futureCheck)
                    playerList[player].hand.append(intoHand)
                elif skipCheck != -1: 
                    intoHand = playerList[steal].hand.pop(skipCheck)
                    playerList[player].hand.append(intoHand)
                elif favorCheck != -1: 
                    intoHand = playerList[steal].hand.pop(favorCheck)
                    playerList[player].hand.append(intoHand)
                elif shuffleCheck != -1:
                    intoHand = playerList[steal].hand.pop(shuffleCheck)
                    playerList[player].hand.append(intoHand)
                else:
                    intoHand = playerList[steal].hand.pop(randint(0, len(playerList[steal].hand)-1))
                    playerList[player].hand.append(intoHand)
                print(playerList[player],"stole a card from ", playerList[steal])   
        elif counts[card] >= 2:
            steal = randint(0, len(playerList)-1)
            for i in range(2):
                discard = playerList[player].hand.pop(search(card, playerList[player].hand))
                deck.discardPile.append(discard)
            nope = nopeCheck(player, playerList, card, deck)
            if nope == False: 
                pos = randint(0, len(playerList[steal].hand)-1)
                print(playerList[steal].name)
                print(playerList)
                print(playerList[player].name, "comboed off and stole from " + playerList[steal].name)
                playerList[player].hand.append(playerList[steal].hand.pop(pos))



def search(card, listOfCards):
    """This function  takes in a card and list of cards. It searches the list for that card returns its position and if not their it returns false.
        :param card: the card it is searching for
        :param listOfCards: the list of cards that it is searching through
    """  
    if card == "":
        return card
    inHand = -1
    for a in range(0,len(listOfCards)):
        if listOfCards[a].name == card:  
            return a
    if inHand == -1:
        return inHand

class deck:
    ''' This class creates a deck object which is used to play a game of exploding kittens.
    '''
    def __init__(self, cards, discardPile):
        ''' This constructer method takes in lists to represent the cards in the deck and the discard pile
        :param cards: list of cards in the deck
        :param discardPile: list of cards in the discard pile
        '''
        self.cards = cards
        self.discardPile = discardPile
        
    def buildAndDeal(self, playerList):
        """This function sets up a game of exploding kittens. It shuffles the deck and deals out five cards to each player, then adds in the remaing defuses and the appropriate amount of defuses, and then shuffles again.
        :param playerList: all of the players plaing the game
        """ 
        self.cards = []
        for i in range(4):
            attack = card('Attack', "Makes the next player take 2 turns instead of 1", ATTACK)
            skip = card('Skip',"Immediately end your turn without drawing a card. If you play a Skip card as a defense to an Attack card, it only ends 1 of the 2 turns. 2 Skipcards would end both turns.", SKIP)
            shuffle = card('Shuffle', 'Shuffle the Draw Pile thoroughly and randomly without viewing the cards.', SHUFFLE )
            favor = card('Favor',"Force any other player to give you 1 card from their hand. They choose which card to give you.", FAVOR)
            tacoCat = card('Taco Cat', "These cards are powerless on their own, but can be played in Pairs or Special Combos.", COMBO)
            melonCat = card('Melon Cat', "These cards are powerless on their own, but can be played in Pairs or Special Combos.", COMBO)
            hairyPotatoCat = card('Hairy Potato Cat', "These cards are powerless on their own, but can be played in Pairs or Special Combos.", COMBO)
            beardCat = card('Beard Cat', "These cards are powerless on their own, but can be played in Pairs or Special Combos.", COMBO)
            rainbowRalphingCat = card('Rainbow-ralphing Cat',"These cards are powerless on their own, but can be played in Pairs or Special Combos.", COMBO)
            self.cards.append(attack)
            self.cards.append(skip)
            self.cards.append(shuffle)
            self.cards.append(favor)
            self.cards.append(tacoCat)
            self.cards.append(melonCat)
            self.cards.append(hairyPotatoCat)
            self.cards.append(beardCat)
            self.cards.append(rainbowRalphingCat)
        for i in range(5):
            seeTheFuture = card('Future', "Peek at the top 3 cards from the Draw Pile and put them back in the same order. Don’t show the cards to the other players. ", FUTURE)
            nope = card('Nope', "Stop any action except for an Exploding Kitten or a Defuse card ", "nope()")
            self.cards.append(seeTheFuture)
            self.cards.append(nope)
        random.shuffle(self.cards) 
        for i in range(len(playerList)):
            for j in range (4):
                playerList[i].hand.append(self.cards.pop(0))
            defuse = card('Defuse',"Defuses an exploding cat and saves your life", "This is automatic")
            playerList[i].hand.append(defuse)
        for i in range(len(playerList)-1):
            explodingKitten = card('Exploding Kitten',"You must show this card immediately. Unless you have a Defuse card, you’re dead. Discard all of your cards, including the Exploding Kitten.", "explode()")
            self.cards.append(explodingKitten)
        for i in range(6-len(playerList)):
            defuse = card('Defuse',"Defuses an exploding cat and saves your life", "This is automatic")
            self.cards.append(defuse)
        random.shuffle(self.cards) 
        return playerList
    
class card:
    '''This class represents the cards used to play the game.
    '''
    def __init__(self, name, description, play):
        '''This is a constructer method and it takes in the name of the card, the cards description, and a function that takes place when the card is played
        :param name: name of the card
        :param description: a description of what the card does
        :param  play: what the card does when played 
        '''
        self.description = description
        self.play = play
        self.name = name
    def __repr__(self):
        return '%s' % (self.name)
    
    def play(self):
        self.playn = play()
    
    
class player: 
    '''This class represents the player that plays the game
    '''
    def __init__(self, name, hand, status):
        '''This is the constructer and it takes in the players name, their hand, and their status
        :param name: name of the player.
        :param hand: the cards that the play is holding
        :param status: whever the player is alive or they have exploded
        '''
        self.hand = []
        self.status = status
        self.name = name
    def __repr__(self):
        return '%s' % (self.name)
    def explode(self):
        '''when they draw an exploding kitten and are unable to defuse it they explode
        '''
        self. status = "dead"

    
def draw(player, playerList, deck):
    """This function  takes in a player, the list of all other players, and the deck. It allows the player to draw a card at the end of their turn
        :param player: the player whose turn it is
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
    """     
    Defuse = False
    print(playerList[player].name, 'ended their turn and drew a card')
    drawn = deck.cards.pop(0)
    if drawn.name == 'Exploding Kitten':  
        print(playerList[player].name , "drew an exploding kitten")
        for a in range(len(playerList[player].hand)):
            if playerList[player].hand[a].name == "Defuse":
                print(playerList[player].name , "defused an exploding kitten")
                discard =  playerList[player].hand.pop(a)
                deck.discardPile.append(discard)
                if playerList[0].name[:-2] != "Computer":
                    pos = input("Where in the deck would you like to reinsert the exploding kitten?")
                    pos = numCheck(pos)
                    while pos <= -1 and pos > len(deck.cards) and pos == False:
                        if pos == "":
                            pos = randint(0, len(deck.cards)-1)
                            break
                        pos = input("The deck does not have that many cards remaining. Because there are only" + len(deck.cards)+ "cards left in the deck. Where in the deck would you like to reinsert the exploding kitten?")
                        pos = numCheck(pos)
                    pos = int(pos)
                else:
                    pos = randint(0, len(deck.cards))
                    if len(deck.cards) == 0:
                        pos =0
                deck.cards.insert(pos, drawn)
                Defuse = True 
                break 
        if Defuse == False:        
            print(playerList[player].name, "exploded")
            playerList[player].explode()
            if playerList[player].name == playerList[player+1].name:
                playerList.pop(player)
                playerList.pop(player)
            else:
                playerList.pop(player)
    else: 
        playerList[player].hand.append(drawn)
    return drawn

    
def playerTakeTurn(deck, player, playerList, numOfPlayers):
    """This function simulates a turn in a game of Exploding Kittens.
        Parameters:
        :param player: the player taking the turn
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
        :param numOfPlayers: the orginal number of players and decides which strategy the ai will use
    """
    comboCards = ["Taco Cat","Hairy Potato Cat","Melon Cat", "Beard Cat", "Rainbow-ralphing Cat"]
    if playerList[player].name[:-2] == "Computer":
        endTurn = ""
        if numOfPlayers >= 4:
            while endTurn != "End":
                futureCheck = search("Future", playerList[player].hand)
                attackCheck = search("Attack", playerList[player].hand)
                shuffleCheck = search("Shuffle",playerList[player].hand)
                skipCheck = search("Skip", playerList[player].hand)
                favorCheck = search("Favor", playerList[player].hand)
                if favorCheck != -1:
                    playerList[player].hand[favorCheck].play(player, playerList, deck)
                    deck.discardPile.append(playerList[player].hand.pop(favorCheck))
                if len(deck.cards) >= 30:
                    draw(player, playerList, deck)
                    endTurn = "End" 
                elif len(deck.cards) >=15:        
                    counts = counter(player, playerList)
                    diffComboCardTotal = counts.pop(5)
                    countsDict = {}
                    for i in range(len(comboCards)):
                        countsDict[comboCards[i]] = counts[i]
                    while diffComboCardTotal >= 5:
                        pos = search("Melon Cat", playerList[player].hand)
                        playerList[player].hand[pos].play('Melon Cat', player, playerList, deck, countsDict, diffComboCardTotal)
                        counts = counter(player, playerList)
                        diffComboCardTotal = counts.pop(5)
                        countsDict = {}
                        for i in range(len(comboCards)):
                            countsDict[comboCards[i]] = counts[i]
                    for i in range(len(counts)):
                        if counts[i] >= 2:
                            pos = search(comboCards[i], playerList[player].hand)
                            playerList[player].hand[pos].play(comboCards[i], player, playerList, deck, countsDict, diffComboCardTotal)
                    endTurn = "End"            
                    draw(player, playerList, deck)

                else:           
                    if futureCheck != -1:
                        topCards = playerList[player].hand[futureCheck].play(player, playerList, deck)
                        if len(topCards) >= 2:
                            if attackCheck != -1 and topCards[1] == "Exploding Kitten" and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(attackCheck))  
                                endTurn = "End"
                            elif attackCheck == -1 and topCards[1] == "Exploding Kitten":
                                draw(player, playerList, deck)
                                endTurn = "End"
                            elif skipCheck != -1 and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[skipCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End"
                            elif shuffleCheck != -1 and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[shuffleCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(shuffleCheck))
                                draw(player, playerList, deck)
                                endTurn = "End"
                            elif skipCheck != -1 and topCards[0] == "Exploding Kittens":
                                endTurn = playerList[player].hand[skipCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End"
                                return
                            else:
                                draw(player, playerList, deck)
                                endTurn = "End"
                        else:
                            if attackCheck != -1:
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(attackCheck))
                                endTurn = "End" 
                            elif skipCheck != -1:
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End" 
                    elif attackCheck != -1:
                        playerList[player].hand[attackCheck].play(player, playerList, deck)
                        deck.discardPile.append(playerList[player].hand.pop(attackCheck))
                        endTurn = "End" 
                    elif playerList[player].name == playerList[player+1].name and skipCheck != -1:
                        playerList[player].hand[skipCheck].play(player, playerList, deck)
                        deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                        endTurn = "End" 
                    else:
                        draw(player, playerList, deck)
                        endTurn = "End" 
                
                
        else:
            while endTurn != "End":
                futureCheck = search("Future", playerList[player].hand)
                attackCheck = search("Attack", playerList[player].hand)
                shuffleCheck = search("Shuffle",playerList[player].hand)
                skipCheck = search("Skip", playerList[player].hand)
                favorCheck = search("Favor", playerList[player].hand)
                if favorCheck != -1:
                    playerList[player].hand[favorCheck].play(player, playerList, deck)
                    deck.discardPile.append(playerList[player].hand.pop(favorCheck))
                if len(deck.cards) > 15:
                    draw(player, playerList, deck)
                    endTurn = "End"        
                if len(deck.cards) <=15:        
                    counts = counter(player, playerList)
                    diffComboCardTotal = counts.pop(5)
                    countsDict = {}
                    for i in range(len(comboCards)):
                        countsDict[comboCards[i]] = counts[i]
                    while diffComboCardTotal >= 5:
                        pos = search("Melon Cat", playerList[player].hand)
                        playerList[player].hand[pos].play('Melon Cat', player, playerList, deck, countsDict, diffComboCardTotal)
                        counts = counter(player, playerList)
                        diffComboCardTotal = counts.pop(5)
                        countsDict = {}
                        for i in range(len(comboCards)):
                            countsDict[comboCards[i]] = counts[i]
                    for i in range(len(counts)):
                        if counts[i] >= 2:
                            pos = search(comboCards[i], playerList[player].hand)
                            playerList[player].hand[pos].play(comboCards[i], player, playerList, deck, countsDict, diffComboCardTotal)         
                    if futureCheck != -1:
                        topCards = playerList[player].hand[futureCheck].play(player, playerList, deck)
                        if len(topCards) >= 2:
                            if attackCheck != -1 and topCards[1] == "Exploding Kitten" and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(attackCheck))  
                                endTurn = "End"
                            elif attackCheck == -1 and topCards[1] == "Exploding Kitten":
                                draw(player, playerList, deck)
                                endTurn = "End"
                            elif skipCheck != -1 and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[skipCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End"
                            elif shuffleCheck != -1 and topCards[0] == "Exploding Kitten":
                                playerList[player].hand[shuffleCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(shuffleCheck))
                                draw(player, playerList, deck)
                                endTurn = "End"
                            elif skipCheck != -1 and topCards[0] == "Exploding Kittens":
                                endTurn = playerList[player].hand[skipCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End"
                                return
                            else:
                                draw(player, playerList, deck)
                                endTurn = "End"
                        else:
                            if attackCheck != -1:
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(attackCheck))
                                endTurn = "End" 
                            elif skipCheck != -1:
                                playerList[player].hand[attackCheck].play(player, playerList, deck)
                                deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                                endTurn = "End" 
                    elif attackCheck != -1:
                        playerList[player].hand[attackCheck].play(player, playerList, deck)
                        deck.discardPile.append(playerList[player].hand.pop(attackCheck))
                        endTurn = "End" 
                    elif playerList[player].name == playerList[player+1].name and skipCheck != -1:
                        playerList[player].hand[skipCheck].play(player, playerList, deck)
                        deck.discardPile.append(playerList[player].hand.pop(skipCheck))
                        endTurn = "End" 
                    else:
                        draw(player, playerList, deck)
                        endTurn = "End" 
    else:
        print("You have ", playerList[player].hand, " in your hand. There are", len(deck.cards)," cards remaining in the deck and there are", len(deck.discardPile)," cards in the discard pile." )
        cardPlayed = str(input("If you hit the enter key you will end your turn and draw a card. What card would you like to play? "))
        while cardPlayed != '' and cardPlayed != "Attack" and cardPlayed != "Skip":
            pos = search(cardPlayed, playerList[player].hand)
            while pos == -1 or cardPlayed == "Defuse":
                cardPlayed = str(input("That card is either not in your hand, you do not have a pair, or a defuse which will be played automatically when needed. If you hit enter and input nothing it will end your turn. What card would you like to play? "))
                pos = search(cardPlayed, playerList[player].hand)
            if cardPlayed == "Taco Cat" or cardPlayed == 'Melon Cat' or cardPlayed == "Hairy Potato Cat" or cardPlayed == 'Beard Cat'  or cardPlayed == 'Rainbow-ralphing Cat':
                counts = counter(player, playerList)
                diffComboCardTotal = counts.pop(5)
                countsDict = {}
                for i in range(len(comboCards)):
                    countsDict[comboCards[i]] = counts[i]
                if countsDict[cardPlayed] >= 2 or diffComboCardTotal >= 5:
                    playerList[player].hand[pos].play(cardPlayed, player, playerList, deck, counts, diffComboCardTotal)
                else:
                    pos = -1
            if cardPlayed == "Favor" or cardPlayed == "Shuffle" or cardPlayed == 'Future':
                playerList[player].hand[pos].play(player, playerList, deck)
                playerList[player].hand.pop(pos)
                deck.discardPile.append(card)
                print(playerList[player].hand)
            cardPlayed = str(input("If you would like to play a second card please enter it to play. Else hit enter to end your turn and draw a card."))
        if cardPlayed == "Skip":
            pos = search(cardPlayed, playerList[player].hand)
            playerList[player].hand[pos].play(player, playerList, deck)
            discard = playerList[player].hand.pop(pos)
            deck.discardPile.append(discard)
        elif cardPlayed == "Attack":
            pos = search(cardPlayed, playerList[player].hand)
            playerList[player].hand[pos].play(player, playerList, deck)
            discard = playerList[player].hand.pop(pos)
            deck.discardPile.append(discard)
        if cardPlayed != "Attack" and cardPlayed != "Skip":
            drawn = draw(player, playerList, deck)
            print("You drew a", drawn.name, "card.")
        
    if len(playerList) > 1:
        if playerList[player].name == playerList[1].name:
            playerList.pop(player)
        else:
            player = playerList.pop(player)
            playerList.append(player)
    return

def playGame(playerList, deck, numOfPlayers):
    """This function runs a game of Exploding Kittens.
        Parameters:
        :param playerList: all of the players plaing the game
        :param deck: the deck that the game will be played with
        :param numOfPlayers: the orginal number of players and decides which strategy the ai will use
    """
    while len(playerList) > 1:
        playerTakeTurn(deck, 0, playerList, numOfPlayers)
    if playerList[0].status == "alive" and playerList[0].name[:-2] != "Computer":
        print("Congratulations! You survived a minefield of explosive kittens")
    else:
        print("Looks like one of the kittens got ya. Better luck next time")
        print(playerList[0].name, " was the winner.")
    
def test():
    """This function just runs an test game so i can test out many of my functions
    """
    Andrew = player("andrew", [], "alive")
    Computer = player("Computer 0", [], "alive")
    playerList = [Andrew, Computer]
    gameDeck = deck([], [])
    playerList = gameDeck.buildAndDeal(playerList)
    playGame(playerList, gameDeck)

def main():
    playerList = []
    numberOfPlayers = input("You can play with 2-5 players. How many players would you like to play with?")
    numberOfPlayers = numCheck(numberOfPlayers)
    while numberOfPlayers<2 and numberOfPlayers<5 or numberOfPlayers == False:
        numberOfPlayers = input("You can play with 2-5 players. How many players would you like to play with?")
        numberOfPlayers = numCheck(numberOfPlayers)
    name = str(input("What is your name?"))
    playerOfGame = player(name, [], "alive")
    playerList.append(playerOfGame)
    for i in range(1,numberOfPlayers):
        name = "Computer " + str(i)
        playerOfGame = player(name, [], "alive")
        playerList.append(playerOfGame)
    numOfPlayers = len(playerList)
    gameDeck = deck ( [], [])
    gameDeck.buildAndDeal(playerList)
    playGame(playerList, gameDeck, numOfPlayers)
        
        
if __name__ == "__main__":
    main()
    