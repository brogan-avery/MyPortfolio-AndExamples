"""
created on: April 17 2020

@author: Brogan Avery

tile:Pet Game

Desc: creates and displays a pygame GUI
"""
import pygame
import PickYourPet
from AnimalClass import *
import AnimalClass as ac
import SubClasses as sc
from SubClasses import *
from pygame.locals import *
import sqlite3
from sqlite3 import Error
import time
from CustomExceptions import WindowXOut
#___________________________________METHODS___________________________

# take in the coordinates and a variable
# renders the text( which is the value of the var_name variable) and then displays it to the screen via the pygame blit method.
def display_text(x,y,var_name):
    rendered_var = font_styling.render(var_name,True,(18, 14, 151)) #uses a declared font(style and size) with the pygame render method. parameters represent the text variable, sets visible to true, gives text RGB color value
    screen.blit(rendered_var, (x, y)) # displays the rendered text on screen

# the next 2 methods display the image of the pet when "moving" to the right or left. they take in a value for coordinates but for some reason
# do not take in the variable that is assigned to the image. I don't know if it has to do with the way images are loaded and referenced/used or what, but every pygame
# tutorial says this is the way to do it.
def move_pet_img_right(x,y):
    screen.blit(pet_img_right,(x,y)) # this is where it references the image's variable name and then displays it to the xy location

def move_pet_img_left(x,y):
    screen.blit(pet_img_left,(x,y))

def make_sound(noise):
    pygame.mixer.Sound.play(noise) #pygame method to play sound from a wav file

# called after the pet dies, writes to a file to create a death certificate
# returns a message to indicate to user that certificate was made
def make_death_cert():
    with open('deathCertificate.txt', 'w') as file:
        file.write(
            "         STATE OF PET-SYLVANIA \n         DEPARTMENT OF HEALTH \n         Certificate of DEATH \n\n")
        file.write("               NAME:   " + sc.pet.get_name() + "\n\n")
        file.write("               ANIMAL:   " + sc.pet.get_species() + "\n\n")
        file.write("               SEX:   " + sc.pet.get_sex() + "\n\n")
        file.write("               D.O.B:   " + sc.pet.get_birthdate() + "\n\n")
        file.write("               LIVED UNTIL :   Age " + str(sc.pet.get_age()) + "\n\n")
        if sc.pet.get_age() < 25:
            your_effort = "   Your pet did not even make it to 25. You did poorly"
        elif sc.pet.get_age() <= 50:
            your_effort = "   Your pet lived a short life, but it was a ok try"
        elif sc.pet.get_age() <= 80:
            your_effort = "   Your pets life was pretty good"
        elif sc.pet.get_age() <= 99:
            your_effort = "   Your pets lived a long and happy life, impressive."
        elif sc.pet.get_age() == 100:
            your_effort = "   Your pet died old and happy. You rock!"
        file.write(your_effort)
    return"A death certificate has been made for your pet."

#tries to make a connection to a database
def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error:
        print("Could not connect to database.")

#creates a new record in the database for the pet in the game just played
def add_record(conn, pet):
    sql = ''' INSERT INTO Records(Name,Species,Sex,BirthDate,FinalAge)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pet)
    return cur.lastrowid

# returns the top 5 highest scores(longest lives) from previous players
def display_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Records ORDER BY FinalAge DESC LIMIT 5") #top 5 longest games
    rows = cur.fetchall()
    return rows

#___________________________WINDOW CREATION/SETUP________________________
if __name__ == '__main__':

    pygame.init()   #Initializes game/game window

#creates window and sets its height and width
    height = 600
    width = 800
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("My PyPet")  #window title

#______________________________IMAGES AND SOUND______________________________
    park_bg = pygame.image.load('park_bg.png') # loads background image

# loads the appropriate images for pet species in and sets them to a variable indicating the direction it will be "moving"
# loads in the appropriate wav file and sets it to a variable for the sound the pet will make
    if sc.pet.get_species() == "dog":
        pet_img_right = pygame.image.load('dogRight.png')
        pet_img_left = pygame.image.load('dogLeft.png')
        noise = pygame.mixer.Sound("bark.wav")
    elif sc.pet.get_species() == "cat":
        pet_img_right = pygame.image.load('catRight.png')
        pet_img_left = pygame.image.load('catLeft.png')
        noise = pygame.mixer.Sound("meow.wav")
    else:
        pet_img_right = pygame.image.load('rodentRight.png')
        pet_img_left = pygame.image.load('rodentLeft.png')
        noise = pygame.mixer.Sound('squeak.wav')

#sets start location(XY) on screen for pet images
    pet_img_right_X = 20
    pet_img_right_Y = 450
    pet_img_left_X = 1590
    pet_img_left_Y = 450
#______________________________TEXT and FORMATTING______________________________
    font_styling = pygame.font.Font('freesansbold.ttf', 20) #this is use to set the font style and size for text, need in pygame

# the following variable represent where a certain text will be displayed.
# some of the text that will be displayed is assigned to variable here,
# other texts are not because they will come directly from a method that will be called in the main game loop and need to be updated each round/loop iteration
    outcome_message_X = 230
    outcome_message_Y = 290

    stats_title= "___Pet Stats___ "
    stats_title_X = 15
    stats_title_Y = 20

#___LABELS___
    name_label = "Name: "
    name_label_X = 30
    name_label_Y = 50

    age_label = "Age: "
    age_label_X = 30
    age_label_Y = 75

    species_label = "Species: "
    species_label_X = 30
    species_label_Y = 100

    sex_label = "Sex: "
    sex_label_X = 30
    sex_label_Y = 125

    birthdate_label = "Birthdate: "
    birthdate_label_X = 30
    birthdate_label_Y = 150

    health_label = "health: "
    health_label_X = 30
    health_label_Y = 175

    hunger_label = "hunger: "
    hunger_label_X = 30
    hunger_label_Y = 200

    happiness_label = "happiness: "
    happiness_label_X = 30
    happiness_label_Y = 225

    cash_label = "cash: "
    cash_label_X = 30
    cash_label_Y = 250

#__VALUES___
    name_value = sc.pet.get_name()
    name_value_X = 140
    name_value_Y = 50

    age_value_X = 140
    age_value_Y = 75

    species_value = sc.pet.get_species()
    species_value_X = 140
    species_value_Y = 100

    sex_value = sc.pet.get_sex()
    sex_value_X = 140
    sex_value_Y = 125

    birthdate_value = str(sc.pet.get_birthdate())
    birthdate_value_X = 140
    birthdate_value_Y = 150

    health_value_X = 140
    health_value_Y = 175

    hunger_value_X = 140
    hunger_value_Y = 200

    happiness_value_X = 140
    happiness_value_Y = 225

    cash_value_X = 140
    cash_value_Y = 250

#______________________________MAIN GAME LOOP___________________________
    running = True #loop exit condition
    while running:

        screen.blit(park_bg,(0,0)) # displays background img

                #GAME EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #with out this, nothing will happen when you try to X out of game window
                running = False
                        #key events: in the event that a key (specified in the line "if event.key == pygame.K_f:",
                        # where K_f represents which key) is pressed, it will trigger a call to a specified method from the Animal class or make_sound()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    sc.pet.perform_action("feed pet food")
                if event.key == pygame.K_d:
                    sc.pet.perform_action("feed discount pet food")
                if event.key == pygame.K_s:
                    sc.pet.perform_action("feed food you scavenged for")
                if event.key == pygame.K_m:
                    sc.pet.perform_action("give medicine")
                if event.key == pygame.K_x:
                    sc.pet.perform_action("give magic potion")
                if event.key == pygame.K_h:
                    sc.pet.perform_action("give home remedy")
                if event.key == pygame.K_p:
                    sc.pet.perform_action("play")
                if event.key == pygame.K_e:
                    sc.pet.perform_action("pet")
                if event.key == pygame.K_t:
                    sc.pet.perform_action("give toy")
                if event.key == pygame.K_z:
                    sc.pet.perform_action("perform pet show")
                if event.key == pygame.K_n:
                    make_sound(noise)

# this section creates the illusion ofmovement by changing the X value 3 pixels over every time the loop runs.
# Uses an original image and a flipped copy to create the illusion that the pet turns around and goes the other way.
# There is probably a lot of better ways to do this when one knows more about graphics and animation, but after spending forever, I had to settle on doing it the following way:
# both the right and left facing images are essentially in constant motion. They both keep going straightuntil they reach a certain x value and then they get reset to
# the point where they started. The distance the image goes before resetting to its start point reflects the time it takes for the other image to move across the screen.
        pet_img_right_X += 3
        pet_img_left_X -= 3
        if pet_img_right_X >= 1780:
            pet_img_right_X = -100
        if pet_img_left_X <= -150:
            pet_img_left_X = 1725

#these make the call to the methods which displays the image
        move_pet_img_right(pet_img_right_X, pet_img_right_Y)
        move_pet_img_left(pet_img_left_X, pet_img_left_Y)

#the following all call the method to display some text
        display_text(stats_title_X, stats_title_Y, stats_title)

        display_text(name_label_X, name_label_Y, name_label)
        display_text(age_label_X, age_label_Y, age_label)
        display_text(species_label_X, species_label_Y, species_label)
        display_text(sex_label_X, sex_label_Y, sex_label)
        display_text(birthdate_label_X, birthdate_label_Y, birthdate_label)
        display_text(health_label_X, health_label_Y, health_label)
        display_text(hunger_label_X, hunger_label_Y, hunger_label)
        display_text(happiness_label_X, happiness_label_Y, happiness_label)
        display_text(cash_label_X, cash_label_Y, cash_label)

        display_text(name_value_X, name_value_Y, name_value)
        display_text(age_value_X, age_value_Y, str(sc.pet.get_age()))
        display_text(species_value_X, species_value_Y, species_value)
        display_text(sex_value_X, sex_value_Y, sex_value)
        display_text(birthdate_value_X, birthdate_value_Y, birthdate_value)
        display_text(health_value_X, health_value_Y, str(sc.pet.get_health()))
        display_text(hunger_value_X, hunger_value_Y, str(sc.pet.get_hunger()))
        display_text(happiness_value_X, happiness_value_Y, str(sc.pet.get_happiness()))
        display_text(cash_value_X, cash_value_Y, ("$ " + str(sc.pet.get_cash())))

        display_text(outcome_message_X, outcome_message_Y, sc.pet.get_outcome_message())

#Every time the loop runs, the method from the animal class to check for death is called.
# If the method returns true, the game ends and the windowautomatically closes
        if sc.pet.check_for_death() == True:
            running = False

#updates any changes made during loop iteration
        pygame.display.update()
#__________________________________________________________________________________________________
# the following will only happen after the game screen is closed (outside main loop)
# the ifstatementchecks to see if the game closed because the user hit the close window button or
# if the window closed because the pet died and triggered the game to end

#if the user clicked the close widow button, it will throw a custom error telling the user they quit
# the game early and no more of the code will beexecuted
    if running == False and sc.pet.check_for_death() == False:
        raise WindowXOut()

    time.sleep(2) # this method makes pauses. It is used some throughout the program for DRAMATIC effect and to enhance game play.

# prints a different message depending on the pet's cause of death
    if sc.pet.get_age() >= 100:
        print("YOU WIN")
    else:
        print("GAME OVER")

    time.sleep(1)

    print(make_death_cert()) #make call to method to create the death certificate. Prints the return which tells user it was created.

    time.sleep(1)

# this section calls the methods to connect to a database, add the pet's info to a new record and then prints the top 5 player's scores
    print("See how you compare to other players:")

    conn = create_connection("PyPetRecords.db")
    with conn:
        pet = (sc.pet.get_name(),sc.pet.get_species(),sc.pet.get_sex(),sc.pet.get_birthdate(),sc.pet.get_age())
        pet_record = add_record(conn, pet)
        rows = display_records(conn)
        for row in rows:
            print(row)
    conn.close()
