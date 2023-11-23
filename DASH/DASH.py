#created by BRADLEY BAKER 13263

#imports pygame for all the pygame features such as key presses and sound
#import sys so that the whole program closes when the user wants to leave the game
#import random to spwan object on a random poison on the window
import pygame, sys, random
#imports Vector2 from pygame to set the motion of the mouse
from pygame.math import Vector2
#imports mixer from pygame to play sounds and music
from pygame import mixer

#Class created for only menus
class Game:
    #initilizes pygame
    pygame.init()
    #sets the size of the menus
    WIDTH: int = 800
    HEIGHT: int = 800
    #initilizes the window display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
    #function cretaed so that when the user enters the game 
    #this is the first thing to display until certain keys are pressed
    def start_menu():
        #displays the start menu background from the postion of 0, 0 in the window
        screen.blit(start_menu, (0, 0))
        #creates a postion for the image to be displayed
        Game.dash(" ")
    
        #Loop so that the when certain keys are pressed it does a task
        #from another section of the code
        running = True
        while running:
            #places the menu in a queue and wait for for the queue to be exicuted
            event = pygame.event.wait()
            #leaves the game when the quit feature is selected
            if event.type == pygame.QUIT:
                #makes running false so the loop doesnt carry on looping
                running = False
            #retrives all the keys that could be pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(1)
                #If the key is pressed the music plays and the game begins
                if event.key == pygame.K_SPACE:
                    #plays the music
                    mixer.music.play()
                    #refernces to the code so that the user can play the game
                    playing.mouseLoop()
                #if the user presses this key the music pauses
                #and they are taken to rules menu
                if event.key == pygame.K_r:
                    #pauses the music
                    mixer.music.pause()
                    #refernces the rules menu code
                    Game.game_rules()
        #leaves the program without errors
        pygame.quit()

    #text creattion for the menu, so that a place is available for images to be displayed
    def dash(t, x: int = 0, y: int = 0, middle: str = "both", color="Black"):
        #imports the text type and style and size
        score_font = pygame.font.Font("Assets\Fonts\cheese-font - Copy\Cheese-R2mM.ttf", 100)
        #allows the program to use this text type
        text = score_font.render(t, 1, pygame.Color(color))
        #postion of where the text will be displayed
        if middle == "both":
            rect_middle = text.get_rect(center=((Game.WIDTH // 2, Game.HEIGHT //2 - 300)))
            #displays the "text" on the window as a place holder
            Game.screen.blit(text, rect_middle)
        else:
            Game.screen.blit(text, (x, y))
        #updates the window so the place holder is available on the window
        pygame.display.update()
        return text

    #defines the text displayed for the score when the user dies
    def score_text(t, x: int = 0, y: int = 0, middle: str = "both", color="White"):
        #makes the score global so that the function can use the score
        global SCORE
        #imports the text type and style and sizer
        score_font = pygame.font.Font("Assets\Fonts\cheese-font - Copy\Cheese-R2mM.ttf", 40)
        #allows the program to use this text type
        text = score_font.render(t, 1, pygame.Color(color))
        #postion of where the text will be displayed
        if middle == "both":
            #displays the "text" on the window as a place holder
            rect_middle = text.get_rect(center=((Game.WIDTH // 2 + 100, Game.HEIGHT //2 - 85)))
            Game.screen.blit(text, rect_middle)
        else:
            Game.screen.blit(text, (x, y))
        #updates the window so the place holder is available on the window
        pygame.display.update()
        return text
    
    #function created so that a game over window is created when the user dies in game
    def game_over():
        #makes the score_defeat global so that it canbe used by the function
        global score_defeat
        #displays the gameover background and postions it at 0, 0
        screen.blit(gameOver_menu, (0, 0))
        #creates a postion for the image to be displayed
        Game.dash(" ")
        #displays the score the player had when they dies
        for s in score_defeat:
            #retrives the number the list where the score is saved
            Game.score_text("Score: " + str(max(score_defeat)))

        #when the loop is running certain key can be pressed to preform certain tasks
        running = True
        while running:
            for event in pygame.event.get():
                #leaves the game when the quit feature is selected
                if event.type == pygame.QUIT:
                    #makes running false so the loop doesnt carry on looping
                    running = False
                    pygame.quit()
                    sys.exit(1)
                #retrives all the keys that could be pressed
                if event.type == pygame.KEYDOWN:
                    #if the escape button is pressed the music pauses 
                    #and the user returns to the start menu
                    if event.key == pygame.K_ESCAPE:
                        #pauses the music
                        mixer.music.pause()
                        #user returns to the start menu
                        Game.start_menu()
                    #when the spacebar is pressed the user restarts the game
                    if event.key == pygame.K_SPACE:
                        #the music plays
                        mixer.music.play()
                        #clears the list where the score is stored and restarts the score from 0 again
                        score_defeat.clear()
                        score_defeat.append(int(0.5))
                        #initilizes the game 
                        playing.mouseLoop()
                    #takes the user to the rules menu when "R" key is pressed
                    if event.key == pygame.K_r:
                        #music pauses
                        mixer.music.pause()
                        #clears the list where the score is stored and restarts the score from 0 again
                        score_defeat.clear()
                        score_defeat.append(int(0.5))
                        #takes the user to the rules menu
                        Game.game_rules()

    #function that creastes the rules menu
    def game_rules():
        #displays the rules menu background and postions is at 0, 0 
        screen.blit(rules_menu, (0, 0))
        #creates a postion for the image to be displayed
        Game.dash(" ")
        
        #when the loop is running certain key can be pressed to preform certain tasks 
        running = True
        while running:
            for event in pygame.event.get():
            #leaves the game when the quit feature is selected
                if event.type == pygame.QUIT:
                    #makes running false so the loop doesnt carry on looping
                    running = False
                    pygame.quit()
                    sys.exit(1)
                #retrives all the keys that could be pressed
                if event.type == pygame.KEYDOWN:
                    #when the escape key is pressed the user retruns to the start menu
                    if event.key == pygame.K_ESCAPE:
                        #retruns the suer to the start menu
                        Game.start_menu()

#class created for all mouse changes and edits
class MOUSE:
    #initilizes the mouse class
    def __init__(self):
        #sets postion of the first 3 parts of the body 
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        #sets the motion of the characters
        self.direction = Vector2(1, 0)
        #variable to keep the body from continuously adding to itself
        self.new_block = False

        #imports the images of the mouse(head of the body) for the postions up, down, left and right
        self.head_up = pygame.image.load("Assets\Mice\Gray\Robo_mouse_gray-up.png").convert_alpha()
        self.head_down = pygame.image.load("Assets\Mice\Gray\Robo_mouse_gray-down.png").convert_alpha()
        self.head_left = pygame.image.load("Assets\Mice\Gray\Robo_mouse_gray-left.png").convert_alpha()
        self.head_right = pygame.image.load("Assets\Mice\Gray\Robo_mouse_gray-right.png").convert_alpha()

        #imports the images of of the cats(tail of the body)
        self.tail_up = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.tail_down = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.tail_right = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.tail_left = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()

        #imports the images of the cats between the head and tail and the postions for vertical and horizontal body parts
        self.body_vertical = pygame.image.load("Assets\Cats\Robo_Cat_Simese.png").convert_alpha()
        self.body_horizontal = pygame.image.load("Assets\Cats\Robo_Cat_Simese.png").convert_alpha()

        #imports images to display when the body turns (up/down)left or (up/down)right
        self.body_turnLeft = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.body_turnRight = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.body_bottomRight = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        self.body_bottomLeft = pygame.image.load("Assets\Cats\Robo_Cat_Grey.png").convert_alpha()
        #sound imported for when the head eats the cheease
        self.crunch_sound = pygame.mixer.Sound("Assets\Sounds\cheeseEat.wav")
        #sound imported for when the head eats the health
        self.health_sound = pygame.mixer.Sound("Assets\Sounds\HealthPickUp.wav")
        #sound imported for when the head eats the poison
        self.poison_sound = pygame.mixer.Sound("Assets\Sounds\PoisonPickUp.wav")
    
    #function to display the head and tail of the body
    def draw_mouse(self):
        self.update_head_image()
        self.update_tail_image()

        #loop used to go through the body one black at a time along with the blocks position
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            #displays the mouse(head of the body) 
            if index == 0:
                screen.blit(self.head, block_rect)
            #display the cat(tail of the body)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                #position of the body through indies
                pre_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                #displays the body between the tail and head
                if pre_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif pre_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    #displays the part of the body when the body turna the corner
                    if pre_block.x == -1 and next_block.y == -1 or pre_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_turnLeft, block_rect)
                    elif pre_block.x == -1 and next_block.y == 1 or pre_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bottomLeft, block_rect)
                    elif pre_block.x == 1 and next_block.y == -1 or pre_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_turnRight, block_rect)
                    elif pre_block.x == 1 and next_block.y == 1 or pre_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_bottomRight, block_rect)
    
    #function to update the head image and the directino it faces
    def update_head_image(self):
        head_relation = self.body[1] - self.body[0]
        #displays the left facing image
        if head_relation == Vector2(1, 0): 
            self.head = self.head_left
        #displays the right facing image
        elif head_relation == Vector2(-1, 0): 
            self.head = self.head_right
        #dislays the up facing image
        elif head_relation == Vector2(0, 1): 
            self.head = self.head_up
        #displays the down facing image
        elif head_relation == Vector2(0, -1): 
            self.head = self.head_down

    #function to pdate the tail image and the direction it faces
    def update_tail_image(self):
        tail_relation = self.body[-2] - self.body[-1]
        #displays the left facing image
        if tail_relation == Vector2(1, 0): 
            self.tail = self.tail_left
            #displays the right facing image
        elif tail_relation == Vector2(-1, 0): 
            self.tail = self.tail_right
            #dislays the up facing image
        elif tail_relation == Vector2(0, 1): 
            self.tail = self.tail_up
            #displays the down facing image
        elif tail_relation == Vector2(0, -1): 
            self.tail = self.tail_down
    
    #function to add to the body when the cheese is eaten
    def move_mouse(self):
        #chnages the new_block to flase to add a block
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            #return new_block back to flase so that is doesnt continuously add a new body part
            self.new_block = False
        else:
            #leave sthe vody the way it is 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    #function to add a new block
    def add_block(self):
        self.new_block = True
    
    #plas the sound when eating the cheese
    def play_crunch(self):
        self.crunch_sound.play()

    #plays a sound when the poison is eaten
    def play_poison(self):
        self.poison_sound.play()

    #plays a sound when the health power up is eaten
    def play_health(self):
        self.health_sound.play()

    #reset postion for when the user dies
    def reset(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(1, 0)

#class created for changing and editing the cheese
class CHEESE:
    #initilizes the the cheese class
    def __init__(self):
        #function to place the cheese on a random poistion on the window
        self.randomize()
    
    #functon to displasy the cheese image
    def draw_cheese(self):
        cheese_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(cheese,cheese_rect)

    #function to randomise the positin of the cheese
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

#class created for cganging and editing the poison 
class POISON:
    #initilizes the the poison class
    def __init__(self):
        #function to place the poison on a random poistion on the window
        self.randomize()
    
    #functon to displasy the poison image
    def draw_poison(self):
        poison_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(poison,poison_rect)

     #function to randomise the positin of the poison
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

#class created for cganging and editing the health power up
class HEALTH:
    #initilizes the the health class
    def __init__(self):
        #function to place the health power up on a random poistion on the window
        self.randomize()
    
    #functon to displasy the health image
    def draw_health(self):
        health_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(health,health_rect)

     #function to randomise the positin of the health power up
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)

#class created for to run all code in the mouse, cheese, poison and health classes
class MAIN:
    #initilizes the Main class
    def __init__(self):
        #give the cheese, poison, health and mouse class varibale in the main class to run the code
        self.mouse = MOUSE()
        self.cheese = CHEESE()
        self.poison = POISON()
        self.health = HEALTH()

    #function that updates the windows for when the mouse moves or dies
    def update(self):
        self.mouse.move_mouse()
        self.check_collition()
        self.body_collition()

    #function that displays the cheese, poison, health icon, score and mouse and body
    def draw_elements(self):
        self.cheese.draw_cheese()
        self.poison.draw_poison()
        self.health.draw_health()
        self.mouse.draw_mouse()
        self.draw_score()

    #function to check the collison
    def check_collition(self):
        #make sthe score available to this function 
        global SCORE
        #make sthe lives available to this function
        global LIVES
        #if the cheese and mouse are in the same image it adds 1 to the score
        #and respawns the cheese, poison and health power up
        if self.cheese.pos == self.mouse.body[0]:
            self.cheese.randomize()
            self.poison.randomize()
            self.health.randomize()
            #when the cheese and mouse are in the same postion a cat is added to the body
            self.mouse.add_block()
            #adds 1 to the score
            SCORE += 1
            #inserts the score values to a list for when the user dies
            score_defeat.append(SCORE)
            #speed of the mouse changes when they pic up the cheese
            if SCORE > 0:
                #random speed set every time they mouse and cheese collide
                pygame.time.set_timer(SCREEN_UPDATE, (random.randint(70, 160)))
                #cheese eating sound
                self.mouse.play_crunch()

        #incase the cheese spawns on the body it wil respawn in a random position again
        for block in self.mouse.body[1:]:
            if block == self.cheese.pos:
                self.cheese.randomize()

        #if the mouse position and poistion are the same
        #the poison, cheese and healh power up respawn in new postions
        if self.poison.pos == self.mouse.body[0]:
            self.poison.randomize()
            self.cheese.randomize()
            self.health.randomize()
            #plays the poison eating sound
            self.mouse.play_poison()
            #removes lives fom the snake
            LIVES -= 1

        #if the mouse postions and health power up position are the same
        #the cheese, poisona dnd health power up respawns in a new postions
        if self.health.pos == self.mouse.body[0]:
            self.health.randomize()
            self.cheese.randomize()
            self.poison.randomize()
            #plays the health power up sound
            self.mouse.play_health()
            #adds a life
            LIVES += 1
        
        #if the user has no more lives it takes the user to the game over menu
        if LIVES == 0:
            self.game_over()

    #function to check if the mouse(head) collidews with the body(cats) and takes the user to the game over menu
    def body_collition(self):
        if not 0 <= self.mouse.body[0].x < 20 or not -1 < self.mouse.body[0].y < 20:
            self.game_over()
            
        for block in self.mouse.body[1:]:
            if block == self.mouse.body[0]:
                self.game_over()

    #function to define what happens when the user dies
    def game_over(self):
        #Makes the Sccore, mouse_score and lives avaliavle for use by this function
        global SCORE
        global mouse_scores
        global LIVES
        global mouse_lives
        #restes the mouse location when the user dies
        if self.body_collition:
            self.mouse.reset()
            #sets the score back to 0
            SCORE = mouse_score
            #set sthe lives back to 2
            LIVES = mouse_lives
            #keeps the speed of the mouse random
            pygame.time.set_timer(SCREEN_UPDATE, (random.randint(80, 150)))
            #pasues the music when the user dies
            mixer.music.pause()
            #takes the user to the game over menu
            Game.game_over()

    #draws the score on the window where the user play the game
    def draw_score(self):
        global SCORE
        score_text = ("Score: " + str(SCORE))
        score_surface = score_font.render(score_text, True, (0, 0, 0))
        score_x = int(cell_size * cell_number - 680)
        score_y = int(cell_size * cell_number - 760)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

#class created for the running of the game and its menus
class GAMELOOP():  

    #function to keep the game running
    def mouseLoop(self):
        running = True
        while running:
            #gets all the features from pygame
            for event in pygame.event.get():
                #gets the Quit feature and closes the window and game
                if event.type == pygame.QUIT:
                    #makes running false so the loop doesnt carry on looping
                    running = False
                    pygame.quit()
                    sys.exit(1)
                
                #gets all the keys from pygame
                if event.type == pygame.KEYDOWN:
                    #if the user presses the escape game when in the start menu the game closes
                    if event.key == pygame.K_ESCAPE:
                        Game.start_menu()
        
                #updates the window continuously
                if event.type == SCREEN_UPDATE:
                    main_game.update()
        
                #gets all the keys from pygame
                if event.type == pygame.KEYDOWN:
                    #if the user presses the up arrow or "W" is pressed the head and body moves up(vertically)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if main_game.mouse.direction.y != 1:
                            main_game.mouse.direction = Vector2(0, -1)
                    #if the user presses the down arrow or "S" is pressed the head and body moves up(vertically)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if main_game.mouse.direction.y != -1:
                            main_game.mouse.direction = Vector2(0, 1)
                    #if the user presses the right arrow or "D" is pressed the head and body moves up(vertically)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if main_game.mouse.direction.x != -1:
                            main_game.mouse.direction = Vector2(1, 0)
                    #if the user presses the left arrow or "A" is pressed the head and body moves up(vertically)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if main_game.mouse.direction.x != 1:
                            main_game.mouse.direction = Vector2(-1, 0)

            #changes the background back on the 20 intervile of the score
            if SCORE < 20:
                screen.blit(original_checkers, (0, 0))
            if SCORE >= 20:
                screen.blit(blue_checkers, (0, 0))
            if SCORE >= 40:
                screen.blit(gray_checkers, (0, 0))
            if SCORE >= 60:
                screen.blit(red_checkers, (0, 0))
            if SCORE >= 80:
                screen.blit(purple_checkers, (0, 0))
            if SCORE >= 100:
                screen.blit(green_checkers, (0, 0))

            #displays all the images on the window
            main_game.draw_elements()
            #updates the window
            pygame.display.update()
            #sest the frames per second that that most devoces can use the game
            clock.tick(60)

#adjusts the timing of SFX and music
pygame.mixer.pre_init(44100,-16,2,512)

#initilizes the music feature
mixer.init()
#loads the music within the assest folder
mixer.music.load("Assets\Sounds\distraction dance meme but it&#x27;s a remix.mp3")
#sets the volume of the music as to ensure it is not too loud
mixer.music.set_volume(0.3)
#sets the music to pause until a condition is met in other sections of the code
mixer.music.pause()

#initilizes pygame
pygame.init()

#variables to create the window
cell_size = 40
cell_number = 20

#creates window that will display all graphics and motions set within other sections of the code
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

#variable set for the frames per second
clock = pygame.time.Clock()

#imports the cheese image
cheese = pygame.image.load("Assets\Power ups\Cheese.png").convert_alpha()

#imports the poison image
poison = pygame.image.load("Assets\Power ups\Poison-icon.png").convert_alpha()

#imports the health image
health = pygame.image.load("Assets\Power ups\health-icon.png").convert_alpha()

#imports the font used for the score
score_font = pygame.font.Font("Assets\Fonts\cheese-font - Copy\Cheese-R2mM.ttf", 50)

#imports a blue checkerd back ground for in game use
blue_checkers = pygame.image.load("Assets\Backgrounds\Blue chekcers.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
blue_checkers = pygame.transform.scale(blue_checkers, (800, 800))

#imports a brown checkerd back ground for in game use
original_checkers = pygame.image.load("Assets\Backgrounds\Checkered floor.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
original_checkers = pygame.transform.scale(original_checkers, (800, 800))

#imports a gray checkerd back ground for in game use
gray_checkers = pygame.image.load("Assets\Backgrounds\Gray chekcers.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
gray_checkers = pygame.transform.scale(gray_checkers, (800, 800))

#imports a green checkerd back ground for in game use
green_checkers = pygame.image.load("Assets\Backgrounds\Green checkers.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
green_checkers = pygame.transform.scale(green_checkers, (800, 800))

#imports a purple checkerd back ground for in game use
purple_checkers = pygame.image.load("Assets\Backgrounds\Purplechekcers.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
purple_checkers = pygame.transform.scale(purple_checkers, (800, 800))

#imports a red checkerd back ground for in game use
red_checkers = pygame.image.load("Assets\Backgrounds\Red chekcers.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
red_checkers = pygame.transform.scale(red_checkers, (800, 800))

#imports the start menu background
start_menu = pygame.image.load("Assets\Backgrounds\startMenu.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
start_menu = pygame.transform.scale(start_menu,(800, 800))

#imports the rules menu background
rules_menu = pygame.image.load("Assets\Backgrounds\Rules.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
rules_menu = pygame.transform.scale(rules_menu,(800, 800))

#imports the game over menu background
gameOver_menu = pygame.image.load("Assets\Backgrounds\GameOVer Menu.bmp").convert_alpha()
#adjusts the image to fit the menu and game windows
gameOver_menu = pygame.transform.scale(gameOver_menu,(800, 800))

#imports the icon of the window
mouse = pygame.image.load("Assets\Mice\mouse-icon.png")

#displays the icon nect to the window caption
pygame.display.set_icon(mouse)

#sets the caption of the window
pygame.display.set_caption("Dash")

#Score to keep track of the users progress within the game
SCORE = 0
#sets the score to always be 0 until they collect cheese which will increase the score
score_defeat = [int(0.5)]
#used to reset the score to 0 when the user dies in game
mouse_score = SCORE

#lives create for the user to nnot die immediatly when havven eaten the posion
LIVES = 2
#resest the Lives when the user dies
mouse_lives = LIVES

#Sets a timer for the amount of frames per second
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, (150))

#MAIN class is defined via a variable called main_game
main_game = MAIN()

#Game loop defined by a variable called playing
playing = GAMELOOP()

#initilizes the whole code from here and above
Game.start_menu()