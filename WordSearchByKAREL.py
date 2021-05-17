from gtts import gTTS
from playsound import playsound

from karel.stanfordkarel import *

"""
File: WordSearchByKAREL.py
--------------------
The overall aim of this program is for Karel to create a word
search with a high degree of randomness and then have him find 
the hidden words. In this version which is appended due to 
humanistic limitations, Karel knows four words; KAREL, PYTHON, 
CHOCO and SHREYASI (That's me :D). Once the human user is given
a chance to try and solve the puzzle, Karel will search out all
the words he knows. Overall I found this task especially
challenging due to the high degree of forethought and perspective
of the whole map which is required in creating a word search.

 Watch Karel create and solve his own word search!

 ****To Hide The Words*****
 
 One of the most interesting parts about creating an algorithm
 for this word search was learning how non-systematic word
 searches actually are. When creating a word search there is no
 simple equation that can be applied. While they can be placed
 completely randomly one at a time, one of the short failings of 
 this method is that it could allow for the creation of a game
 where there is no space to possibly fit the last few words
 (especially on a 10 by 8 map). To overcome this problem I 
 taught Karel a way of hiding the words which combines
 strategic placing and still maintains a good degree of randomness. 
 Of course this is also helped by the fact that four 
 words are not too many to hide :).

 First Karel hides the word SHREYASI. He places it upright and
 randomly chooses a column to put it in. However, because of
 the length of this words I made him strongly favor the sides
 of the game as this caused less disruption in the placing of
 the other words. 

 To place CHOCO, Karel randomly chooses a row, checks where
 SHREYASI is placed and with his remaining options randomly
 selects a location

 To place PYTHON and KAREL, which I made bounded together (this
 decision was made not because placing them randomly separately
 was impossible, but simply because the code was becoming
 outrageously long and without variables etc, it would not have
 been worth the effort), Karel will randomly choose any spot on
 the board (minus spots which are too close to the edge for the
 bounded words to fit) then check if there are any letters
 already in the way. If there are words in the way it will just
 look again (with the algorithm created I can be %100 sure
 there will be space for the PYTHON KAREL hybrid). If it finds
 an empty spot it writes in the words.

 The algorithm for finding if the area where Karel is going to
 write the KAREL PYTHON hybrid was very interesting to create.
 If I were to make the word search completely random this is
 exactly the algorithm I would use, however I figured If I did
 it once, I could demonstrate I had the ability without
 coding myself to death :). To check for emptiness I introduced
 what I called the error beeper. If Karel ever came across a
 letter in its path it would place an error beeper at the letter
 it stood (one beeper above the identification beeper). The
 continuation of the search is all dependent on the absence
 of this error beeper and if the search ended with an error beeper
 in existence it would look for a brand new location for the words
 while remembering to put the error beeper away first of course :).
 Though this process may seem simple, keeping the error beepers
 in place without Karel confusing an error beeper with the 
 identification beeper of a letter was harder than it seemed
 especially due to Karel's lack of coordinates. Its also important
 to note that while Karel places PYTHON and KAREL together he is
 oblivious to this fact and will search for both words
 independently.
 ****

 ****To Find The Words****
 
 As you may notice, in the bottom left hand side of each letter
 is a pile of beepers. Seeing as Karel, until this moment was
 illiterate, this is how he identified letters. Each letter
 has a number equivalent which is represented by the stack.
 However, while this may seem simple, reading and remembering
 what he reads are more challenging. To check if a letter is the
 one Karel is looking for, he will place the beepers temporarily
 to the side. If he is looking for a letter with 8 beepers he
 will repeat the step remove beeper if it exists 7 times. Then if
 there are no more beepers he knows there were 7 or less beepers
 and this is not his letter. If there are still beepers he will
 move one more beeper over. If at this point there are no more
 beepers he knows that before there were exactly 8 beepers on the
 spot and this is the word he was looking for. Being the well 
 trained robot he is, Karel will always return the beepers from
 where he got them.

 The actual searching for specific words was by far the most code
 consuming function. This is because it required large amounts of
 deeply nested codes and while much of the code was similar it could
 not be simplified because of the restrictions placed on this 
 assignment.

 To make life easier I made each word have a designated direction.
 In my mind I can clearly visualize how I would confront the
 problem of not knowing the direction before hand but if I had
 done this the already long codes for searching for words would
 have been increased exponentially not to mention the added
 dilemma of how to be sure these new words would all fit into
 the map. I approximated the added code would be about 7x the
 current code which due to the unfortunate demands of my other
 classes was not my best option.

 Once Karel was sufficiently convinced he had found the word he
 made an attempt to circle it. Due to the very large nature of
 the pixels and my lack of intrinsic aesthetic skills, the circling
 doesnt always look as professional as I would like it to. 
 
 ****

 ****How To Run****
 
 To run word search Karel you MUST run it on a 54x61 blank world.

 There are two ways of running Word Search Karel; the fast way 
 and the slow way.

 In the slow way you can see Karel's general movements and from
 this get an insight into the algorithms which occur behind the
 scenes in creating this puzzle. 

 In the fast version, it is supposed to simulate an actual word
 search game. It will draw the puzzle in what seems to be an
 instant, give the viewer some time to try and solve the problem
 and then show the solution. I also added in a real silly intro
 and end screen shot which makes me smile :). To run this, note
 out the section in run titled "slow run" and run Karel at
 full speed

 ****Final Note****
 
 A final note on style. In this program I tried my best to keep
 a readable code which was efficient and well programmed. 
 However due to the long nature of a complicated program in
 Karel and the absolute necessity of deeply embedded clauses
 it was not always as stylistic as I would have liked it to be.

 Moreover, a comment on these notes is that they only cover the
 broader algorithms which dealt with the bigger issues that I
 faced. There are numerous difficulties which were overcome that
 had a more minor role in the overall function of the puzzle.
 (such as how to circle SHREYASI with a rectangle of the same
 width considering its different locations in the game)

 **************************************************************

"""

# import the random library

import random

NUM_LETTERS = 21  # this denotes the number of alphabets that we will use


def main():
    """
    Creates a puzzle and solves it.
    Assumes that Karel starts in the bottom left of a large, empty world.

    There are four basic steps to it
    1. Display the Introduction message
    2. Creates the puzzle
    3. Solves the puzzle
    4. Displays the end message
    
    """
    text_val_1 = "Welcome to the World of KAREL. Here, KAREL is going to perform Word Search. There are four words " \
                 "hidden in a grid consisting of random alphabets. Dive right in to check if our little KAREL can do it"
    # Here are converting in English Language
    language = 'en-us'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val_1, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # KAREL1.mp3
    obj.save("KAREL1.mp3")

    # Play the KAREL1.mp3 file
    playsound("KAREL1.mp3")
    display_intro_message()
    create_puzzle()
    text_val_2 = "Ooo! That's a lot of letters... WELL, Let's hope for the best, KAREL!  you can do it !"
    # Here are converting in English Language
    language = 'en-us'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val_2, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # KAREL2.mp3
    obj.save("KAREL2.mp3")

    # Play the KAREL2.mp3 file
    playsound("KAREL2.mp3")
    delay()
    solve_puzzle()
    display_end_message()
    text_val_3 = "Finally KAREL solved the puzzle . Hope you guys liked it . Thank you!"
    # Here are converting in English Language
    language = 'en-us'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val_3, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # KAREL3.mp3
    obj.save("KAREL3.mp3")

    # Play the KAREL3.mp3 file
    playsound("KAREL3.mp3")


def display_end_message():
    """
    Displays the end message for the user....
    " Thank You "

    At first KAREL clears the canvas though XD

    """
    reach_starting_point()
    clear_canvas()
    reach_starting_point()
    for i in range(3):
        move_up()
    for i in range(2):
        move_to_next_letter()
    write_YOU()
    for i in range(3):
        move_to_next_letter()
    move_up()
    move_to_next_letter()
    write_THANK()
    reach_starting_point()
    delay()


def write_YOU():
    draw_Y()
    move_to_next_letter()
    draw_O()
    move_to_next_letter()
    draw_U()
    move_to_next_letter()
    draw_dots()


def write_THANK():
    draw_T()
    move_to_next_letter()
    draw_H()
    move_to_next_letter()
    draw_A()
    move_to_next_letter()
    draw_N()
    move_to_next_letter()
    draw_K()
    move_to_next_letter()
    draw_dots()


def solve_puzzle():
    """
    Solves the puzzle by finding the four words and creating a boundary line around them

    """
    move_up()
    create_boundary(8, 'row')
    move_to_next_letter()
    move_up()
    create_boundary(6, 'column')
    for i in range(2):
        move_up()
    move_to_next_letter()
    create_boundary(5, 'row')
    for i in range(5):
        move_to_next_letter()
    move_down()
    create_boundary(5, 'column')
    reach_starting_point()


def create_boundary(n, direction):
    """
    This function takes two inputs
    n := number of alphabets present in the word
    direction := either along row or column

    """
    if right_is_clear():
        turn_right()
        for i in range(2):
            move()
    if right_is_clear():
        turn_right()
        for i in range(2):
            move()
        turn_around()
    else:
        turn_left()
    if direction == 'row':
        if n == 8:
            for i in range(53):
                paint_corner(BLACK)
                move()
            paint_corner(BLACK)
            turn_around()
            move_to_wall()
            turn_right()
            for i in range(8):
                move()
            turn_right()
            for i in range(53):
                paint_corner(BLACK)
                move()
            paint_corner(BLACK)
            turn_around()
            move_to_wall()
            turn_left()
            for i in range(6):
                move()
            turn_left()
        if n == 5:
            for i in range(35):
                move()
                paint_corner(BLACK)
            turn_left()
            for i in range(8):
                paint_corner(BLACK)
                move()
            turn_left()
            while corner_color_is(BLANK):
                paint_corner(BLACK)
                move()
            turn_left()
            for i in range(6):
                move()
            turn_left()
            for i in range(2):
                move()

    if direction == 'column':
        turn_left()
        if n == 6:
            while front_is_clear():
                paint_corner(BLACK)
                move()
            paint_corner(BLACK)
            turn_right()
            for i in range(7):
                move()
            turn_right()
            while corner_color_is(BLANK):
                paint_corner(BLACK)
                move()
            turn_around()
            for i in range(2):
                move()
            turn_left()
            for i in range(5):
                move()
            turn_around()
        if n == 5:
            while front_is_clear():
                paint_corner(BLACK)
                move()
            paint_corner(BLACK)
            turn_around()
            while corner_color_is(BLACK):
                move()
            turn_around()
            move()
            turn_right()
            for i in range(6):
                move()
                paint_corner(BLACK)


def create_puzzle():
    """
    Creates the puzzle in a number of steps, basically
    1. At first, KAREL places the four words "SHREYASI", "CHOCO", "PYTHON", "KAREL"
    2. Fills up the rest of the world with random letters

    """
    move_up()
    write_SHREYASI()
    for i in range(2):
        move_up()
    for i in range(2):
        move_to_next_letter()
    write_KAREL()
    move_down()
    write_CHOCO()
    reach_starting_point()
    move_to_next_letter()
    move_up()
    move_up()
    write_PYTHON()
    reach_starting_point()
    fill_blank_spaces()  # KAREL fills the empty slots now with random letters
    reach_starting_point()


def move_down():
    """
    This function is used by KAREL to move down to the next spot for writing a letter along a column

    """
    turn_right()
    for i in range(8):
        move()
    turn_left()


def write_CHOCO():
    """
    KAREL writes the word "CHOCO" which is one of the four words in the puzzle

    It writes one alphabet at a time and moves up by one slot

    """
    draw_C()
    move_up()
    draw_H()
    move_up()
    draw_O()
    move_up()
    draw_C()
    move_up()
    draw_O()


def write_PYTHON():
    """
    KAREL writes the word "PYTHON" which is one of the four words in the puzzle

    It writes one alphabet at a time and moves up by one slot

    """
    draw_N()
    move_up()
    draw_O()
    move_up()
    draw_H()
    move_up()
    draw_T()
    move_up()
    draw_Y()
    move_up()
    draw_P()


def fill_blank_spaces():
    """
    This function helps KAREL to randomly fill in the empty slots
    and completes the puzzle

    """
    for i in range(40):
        move_till_no_letters_present()
        randomly_draw_letters()


def display_intro_message():
    """
    Displays the Introduction message
    " WELCOME TO WORD SEARCH WITH KAREL "
                     --- BY SHREYASI
    """
    write_SHREYASI()
    for i in range(6):
        move_to_next_letter()
    write_BY()
    move_up()
    move_to_next_letter()
    write_SEARCH()
    for i in range(3):
        move_to_next_letter()
    write_WORD()
    for i in range(3):
        move_to_next_letter()
    write_KAREL()
    draw_dots()
    for i in range(5):
        move_to_next_letter()
    write_TO()
    for i in range(3):
        move_to_next_letter()
    write_WELCOME()
    delay()
    clear_canvas()  # Clears the Canvas after displaying the Introductory message to create the puzzle
    reach_starting_point()  # Reaches the starting point to start creating puzzle
    delay()  # Delays the process so that there is a gap between the four basic processes


def write_SHREYASI():
    """
    Writes the word "SHREYASI" as a part of the Introductory message

    This function will also be used while creating the puzzle
    Places the word "SHREYASI" along a row


    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_S()
    move_to_next_letter()
    draw_H()
    move_to_next_letter()
    draw_R()
    move_to_next_letter()
    draw_E()
    move_to_next_letter()
    draw_Y()
    move_to_next_letter()
    draw_A()
    move_to_next_letter()
    draw_S()
    move_to_next_letter()
    draw_I()
    move_to_next_letter()


def write_BY():
    """
    Writes the word "BY" as a part of the Introductory message

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_B()
    move_to_next_letter()
    draw_Y()
    move_to_next_letter()


def delay():
    """
    This function is basically meant to delay the timing between the four basic processes in main() function

    """
    for i in range(5000):
        turn_left()


def move_up():
    """
    This function is used by KAREL to move up to the next spot for writing a letter along a column
    
    """
    turn_left()
    for i in range(8):
        move()
    turn_right()


def write_SEARCH():
    """
    Writes the word "SEARCH" as a part of the Introductory message

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_S()
    move_to_next_letter()
    draw_E()
    move_to_next_letter()
    draw_A()
    move_to_next_letter()
    draw_R()
    move_to_next_letter()
    draw_C()
    move_to_next_letter()
    draw_H()
    move_to_next_letter()


def write_WORD():
    """
    Writes the word "WORD" as a part of the Introductory message

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_W()
    move_to_next_letter()
    draw_O()
    move_to_next_letter()
    draw_R()
    move_to_next_letter()
    draw_D()
    move_to_next_letter()


def write_TO():
    """
    Writes the word "TO" as a part of the Introductory message

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_T()
    move_to_next_letter()
    draw_O()
    move_to_next_letter()


def write_KAREL():
    """
    Writes the word "KAREL" as a part of the Introductory message

    This function will also be used while creating the puzzle
    Places the word "KAREL" along a row

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_K()
    move_to_next_letter()
    draw_A()
    move_to_next_letter()
    draw_R()
    move_to_next_letter()
    draw_E()
    move_to_next_letter()
    draw_L()
    move_to_next_letter()


def write_WELCOME():
    """
    Writes the word "WELCOME" as a part of the Introductory message

    Draws a single letter at a time, then moves to the next spot to write the next letter...
    
    """
    draw_W()
    move_to_next_letter()
    draw_E()
    move_to_next_letter()
    draw_L()
    move_to_next_letter()
    draw_C()
    move_to_next_letter()
    draw_O()
    move_to_next_letter()
    draw_M()
    move_to_next_letter()
    draw_E()
    move_to_next_letter()
    draw_dots()


def reach_starting_point():
    """
    Reaches the starting point i.e. the 1st row and 1st column of KAREL's world

    """
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_around()


def clear_one_row():
    """
    KAREL clears one row at a time. It basically has to perform two functions:
    1. Clear the colors present in the corners
    2. Pick beepers if present

    """
    while front_is_clear():
        paint_corner(BLANK)
        while beepers_present():
            pick_beeper()
        move()
    paint_corner(BLANK)


def reach_first_column():
    """
    KAREL reaches the first column

    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()


def clear_canvas():
    reach_starting_point()
    while left_is_clear():
        clear_one_row()
        reach_first_column()
    clear_one_row()


def randomly_draw_letters():
    """
    KAREL uses this function to randomly draw any alphabet
    It makes use of the random module to perform it

    """
    flag = random.randint(0, NUM_LETTERS - 1)
    # the flag variable is like an indicator storing the number of the  letter to store
    if flag == 0:
        draw_A()
    elif flag == 1:
        draw_B()
    elif flag == 2:
        draw_C()
    elif flag == 3:
        draw_D()
    elif flag == 4:
        draw_E()
    elif flag == 5:
        draw_F()
    elif flag == 6:
        draw_H()
    elif flag == 7:
        draw_I()
    elif flag == 8:
        draw_J()
    elif flag == 9:
        draw_K()
    elif flag == 10:
        draw_L()
    elif flag == 11:
        draw_M()
    elif flag == 12:
        draw_N()
    elif flag == 13:
        draw_O()
    elif flag == 14:
        draw_P()
    elif flag == 15:
        draw_R()
    elif flag == 16:
        draw_S()
    elif flag == 17:
        draw_T()
    elif flag == 18:
        draw_U()
    elif flag == 19:
        draw_W()
    else:
        draw_Y()


def draw_dots():
    """
    KAREL draws three dots "..." to enhance the beauty of a word in few cases

    """
    for i in range(2):
        paint_corner(PINK)
        move()
        move()
    paint_corner(PINK)
    turn_around()
    for i in range(4):
        move()
    turn_around()


def draw_A():
    """
    KAREL draws letter 'A' in blue color and represents it by putting one beeper at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    put_beeper()
    paint_bottom_of_A()
    for i in range(4):
        paint_corner(BLUE)
        move()
    move_to_next_row()
    paint_head_of_A()
    move_back_to_beeper()


def paint_bottom_of_A():
    # KAREL paints the bottom of letter 'A'
    paint_row_of_A()
    move_to_next_row()
    paint_row_of_A()
    move_to_next_row()


def paint_row_of_A():
    # KAREL will paint a row of letter 'A' which repeats itself
    # This is done in order to write the same code again for rows which have the same function
    paint_corner(BLUE)
    for i in range(3):
        move()
    paint_corner(BLUE)
    move()


def paint_head_of_A():
    # KAREL will paint the head or the upper portion of letter 'A'
    paint_row_of_A()
    move_to_next_row()
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    move()


def draw_B():
    """
    KAREL draws letter 'B' in black color and represents it by putting two beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(2):
        put_beeper()
    paint_part1_of_B()
    move_to_next_row()
    paint_row_of_B()
    move_to_next_row()
    paint_part2_of_B()
    move_back_to_beeper()


def paint_part1_of_B():
    # KAREL paints the part of letter 'B' which is repeated twice
    paint_row_of_B()
    move_to_next_row()
    paint_corner(BLACK)
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()


def paint_part2_of_B():
    paint_corner(BLACK)
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()
    move_to_next_row()
    paint_row_of_B()


def paint_row_of_B():
    # KAREL will paint a row of letter 'B' which repeats itself
    # This is done in order to write the same code again for rows which have the same function
    for i in range(3):
        paint_corner(BLACK)
        move()
    move()


def draw_C():
    """
    KAREL draws letter 'C' in cyan color and represents it by putting 3 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(3):
        put_beeper()
    paint_part1_of_C()
    paint_row3_of_C()
    move_to_next_row()
    paint_part2_of_C()
    move_back_to_beeper()


def paint_part1_of_C():
    # KAREL paints the part of letter 'C' which is repeated
    paint_row1_of_C()
    move_to_next_row()
    paint_row2_of_C()
    move_to_next_row()


def paint_part2_of_C():
    paint_row2_of_C()
    move_to_next_row()
    paint_row1_of_C()


def paint_row1_of_C():
    move()
    for i in range(2):
        paint_corner(CYAN)
        move()
    move()


def paint_row2_of_C():
    paint_corner(CYAN)
    for i in range(3):
        move()
    paint_corner(CYAN)
    move()


def paint_row3_of_C():
    paint_corner(CYAN)
    for i in range(4):
        move()


def draw_D():
    """
    KAREL draws letter 'D' in dark grey color and represents it by putting 4 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(4):
        put_beeper()
    paint_row1_of_D()
    for i in range(3):
        move_to_next_row()
        paint_row2_of_D()
    move_to_next_row()
    paint_row1_of_D()
    move_back_to_beeper()


def paint_row1_of_D():
    for i in range(3):
        paint_corner(DARK_GRAY)
        move()
    move()


def paint_row2_of_D():
    paint_corner(DARK_GRAY)
    for i in range(3):
        move()
    paint_corner(DARK_GRAY)
    move()


def draw_E():
    """
    KAREL draws letter 'E' in gray color and represents it by putting 5 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(5):
        put_beeper()
    paint_row1_of_E()
    move_to_next_row()
    paint_row2_of_E()
    move_to_next_row()
    paint_row3_of_E()
    move_to_next_row()
    paint_row2_of_E()
    move_to_next_row()
    paint_row1_of_E()
    move_back_to_beeper()


def paint_row1_of_E():
    for i in range(4):
        paint_corner(GRAY)
        move()


def paint_row2_of_E():
    paint_corner(GRAY)
    for i in range(4):
        move()


def paint_row3_of_E():
    for i in range(3):
        paint_corner(GRAY)
        move()
    move()


def draw_F():
    """
    KAREL draws letter 'F' in green color and represents it by putting 6 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(6):
        put_beeper()
    for i in range(2):
        paint_row1_of_F()
        move_to_next_row()
    paint_row2_of_F()
    move_to_next_row()
    paint_row1_of_F()
    move_to_next_row()
    paint_row3_of_F()
    move_back_to_beeper()


def paint_row2_of_F():
    for i in range(3):
        paint_corner(GREEN)
        move()
    move()


def paint_row1_of_F():
    paint_corner(GREEN)
    for i in range(4):
        move()


def paint_row3_of_F():
    for i in range(4):
        paint_corner(GREEN)
        move()


def draw_H():
    """
    KAREL draws letter 'H' in magenta color and represents it by putting 8 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(8):
        put_beeper()
    for i in range(2):
        paint_row1_of_H()
        move_to_next_row()
    paint_row2_of_H()
    move_to_next_row()
    paint_row1_of_H()
    move_to_next_row()
    paint_row1_of_H()
    move_back_to_beeper()


def paint_row2_of_H():
    for i in range(4):
        paint_corner(MAGENTA)
        move()


def paint_row1_of_H():
    paint_corner(MAGENTA)
    for i in range(3):
        move()
    paint_corner(MAGENTA)
    move()


def draw_I():
    """
    KAREL draws letter 'I' in green color and represents it by putting 9 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(9):
        put_beeper()
    for i in range(4):
        paint_row1_of_I()
        move_to_next_row()
    paint_row1_of_I()
    move_back_to_beeper()


def paint_row1_of_I():
    move()
    paint_corner(ORANGE)
    for i in range(3):
        move()


def draw_J():
    """
    KAREL draws letter 'J' in green color and represents it by putting 10 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(10):
        put_beeper()
    paint_row1_of_J()
    move_to_next_row()
    paint_row2_of_J()
    move_to_next_row()
    for i in range(2):
        paint_row3_of_J()
        move_to_next_row()
    paint_row3_of_J()
    move_back_to_beeper()


def paint_row3_of_J():
    for i in range(3):
        move()
    paint_corner(PINK)
    move()


def paint_row2_of_J():
    move()
    paint_corner(PINK)
    for i in range(2):
        move()
    paint_corner(PINK)
    move()


def paint_row1_of_J():
    move()
    for i in range(3):
        paint_corner(PINK)
        move()


def draw_K():
    """
    KAREL draws letter 'K' in red color and represents it by putting 11 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(11):
        put_beeper()
    paint_row1_of_K()
    move_to_next_row()
    paint_row2_of_K()
    move_to_next_row()
    paint_row3_of_K()
    move_to_next_row()
    paint_row2_of_K()
    move_to_next_row()
    paint_row1_of_K()
    move_back_to_beeper()


def paint_row2_of_K():
    paint_corner(RED)
    for i in range(2):
        move()
    paint_corner(RED)
    move()
    move()


def paint_row1_of_K():
    paint_corner(RED)
    for i in range(3):
        move()
    paint_corner(RED)
    move()


def paint_row3_of_K():
    for i in range(2):
        paint_corner(RED)
        move()
    move()
    move()


def draw_L():
    """
    KAREL draws letter 'L' in green color and represents it by putting 12 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(12):
        put_beeper()
    paint_row1_of_L()
    for i in range(4):
        move_to_next_row()
        paint_row2_of_L()
    move_back_to_beeper()


def paint_row2_of_L():
    paint_corner(YELLOW)
    for i in range(4):
        move()


def paint_row1_of_L():
    for i in range(4):
        paint_corner(YELLOW)
        move()


def draw_M():
    """
    KAREL draws letter 'M' in green color and represents it by putting 13 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(13):
        put_beeper()
    for i in range(2):
        paint_row1_of_M()
        move_to_next_row()
    for i in range(2):
        paint_row2_of_M()
        move_to_next_row()
    paint_row3_of_M()
    move_back_to_beeper()


def paint_row2_of_M():
    paint_corner(BLACK)
    for i in range(2):
        move()
    paint_corner(BLACK)
    for i in range(2):
        move()
    paint_corner(BLACK)


def paint_row1_of_M():
    paint_corner(BLACK)
    for i in range(4):
        move()
    paint_corner(BLACK)


def paint_row3_of_M():
    for i in range(2):
        paint_corner(BLACK)
        move()
    for i in range(2):
        move()
        paint_corner(BLACK)


def draw_N():
    """
    KAREL draws letter 'N' in black color and represents it by putting 14 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(14):
        put_beeper()
    for i in range(2):
        paint_row1_of_N()
        move_to_next_row()
    paint_row2_of_N()
    move_to_next_row()
    paint_row3_of_N()
    move_to_next_row()
    paint_row1_of_N()
    move_back_to_beeper()


def paint_row2_of_N():
    paint_corner(BLACK)
    for i in range(2):
        move()
    for i in range(2):
        paint_corner(BLACK)
        move()


def paint_row1_of_N():
    paint_corner(BLACK)
    for i in range(3):
        move()
    paint_corner(BLACK)
    move()


def paint_row3_of_N():
    for i in range(2):
        paint_corner(BLACK)
        move()
    move()
    paint_corner(BLACK)
    move()


def draw_O():
    """
    KAREL draws letter 'O' in yellow color and represents it by putting 15 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(15):
        put_beeper()
    paint_row1_of_O()
    move_to_next_row()
    for i in range(3):
        paint_row2_of_O()
        move_to_next_row()
    paint_row1_of_O()
    move_back_to_beeper()


def paint_row1_of_O():
    for i in range(2):
        move()
        paint_corner(YELLOW)
    move()
    move()


def paint_row2_of_O():
    paint_corner(YELLOW)
    for i in range(3):
        move()
    paint_corner(YELLOW)
    move()


def draw_P():
    """
    KAREL draws letter 'P' in red color and represents it by putting 16 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(16):
        put_beeper()
    for i in range(2):
        paint_row1_of_P()
        move_to_next_row()
    paint_row2_of_P()
    move_to_next_row()
    paint_row3_of_P()
    move_to_next_row()
    paint_row2_of_P()
    move_back_to_beeper()


def paint_row2_of_P():
    move()
    for i in range(3):
        paint_corner(RED)
        move()


def paint_row1_of_P():
    move()
    paint_corner(RED)
    for i in range(3):
        move()


def paint_row3_of_P():
    move()
    paint_corner(RED)
    for i in range(2):
        move()
    paint_corner(RED)
    move()


def draw_Y():
    """
    KAREL draws letter 'Y' in black color and represents it by putting 25 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(25):
        put_beeper()
    for i in range(3):
        paint_row1_of_Y()
        move_to_next_row()
    paint_row2_of_Y()
    move_to_next_row()
    paint_row2_of_Y()
    move_back_to_beeper()


def paint_row1_of_Y():
    for i in range(2):
        move()
    paint_corner(BLACK)
    move()
    move()


def paint_row2_of_Y():
    move()
    paint_corner(BLACK)
    for i in range(2):
        move()
    paint_corner(BLACK)
    move()


def draw_W():
    """
    KAREL draws letter 'W' in dark gray color and represents it by putting 23 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(23):
        put_beeper()
    paint_row1_of_W()
    move_to_next_row()
    for i in range(3):
        paint_row2_of_W()
        move_to_next_row()
    paint_row3_of_W()
    move_back_to_beeper()


def paint_row1_of_W():
    for i in range(2):
        move()
        paint_corner(DARK_GRAY)
        move()


def paint_row3_of_W():
    paint_corner(DARK_GRAY)
    for i in range(4):
        move()
    paint_corner(DARK_GRAY)


def paint_row2_of_W():
    for i in range(2):
        paint_corner(DARK_GRAY)
        move()
        move()
    paint_corner(DARK_GRAY)


def draw_U():
    """
    KAREL draws letter 'U' in green color and represents it by putting 21 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(21):
        put_beeper()
    paint_row1_of_U()
    for i in range(4):
        move_to_next_row()
        paint_row2_of_U()
    move_back_to_beeper()


def paint_row1_of_U():
    move()
    for i in range(2):
        paint_corner(GREEN)
        move()
    move()


def paint_row2_of_U():
    paint_corner(GREEN)
    for i in range(3):
        move()
    paint_corner(GREEN)
    move()


def draw_T():
    """
    KAREL draws letter 'T' in light gray color and represents it by putting 20 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(20):
        put_beeper()
    for i in range(4):
        paint_row1_of_T()
        move_to_next_row()
    paint_row2_of_T()
    move_back_to_beeper()


def paint_row2_of_T():
    move()
    for i in range(3):
        paint_corner(LIGHT_GRAY)
        move()


def paint_row1_of_T():
    for i in range(2):
        move()
    paint_corner(LIGHT_GRAY)
    for i in range(2):
        move()


def draw_R():
    """
    KAREL draws letter 'R' in orange color and represents it by putting 18 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(18):
        put_beeper()
    for i in range(2):
        paint_row1_of_R()
        move_to_next_row()
    paint_row2_of_R()
    move_to_next_row()
    paint_row1_of_R()
    move_to_next_row()
    paint_row2_of_R()
    move_back_to_beeper()


def paint_row2_of_R():
    for i in range(3):
        paint_corner(ORANGE)
        move()
    move()


def paint_row1_of_R():
    paint_corner(ORANGE)
    for i in range(3):
        move()
    paint_corner(ORANGE)
    move()


def draw_S():
    """
    KAREL draws letter 'S' in magenta color and represents it by putting 19 beepers at the starting position
    It's easier for KAREL to draw it row-by-row XD
    """
    for i in range(19):
        put_beeper()
    paint_part1_of_S()
    move_to_next_row()
    paint_part2_of_S()
    move_back_to_beeper()


def paint_part2_of_S():
    move()
    paint_corner(MAGENTA)
    for i in range(3):
        move()
    move_to_next_row()
    for i in range(2):
        move()
    for i in range(2):
        paint_corner(MAGENTA)
        move()


def paint_part1_of_S():
    move()
    for i in range(2):
        paint_corner(MAGENTA)
        move()
    move()
    move_to_next_row()
    for i in range(3):
        move()
    paint_corner(MAGENTA)
    move()
    move_to_next_row()
    for i in range(2):
        move()
    paint_corner(MAGENTA)
    move()
    move()


def move_to_next_row():
    # Method to move to the next row to complete the letter step by step
    turn_around()
    for i in range(4):
        move()
    turn_right()
    move()
    turn_right()


def move_back_to_beeper():
    # KAREL moves back to the location where beeper is present
    turn_around()
    for i in range(4):
        move()
    turn_left()
    move_to_beeper()
    turn_left()


def move_to_next_letter():
    # KAREL moves to the location where it will draw a new letter
    for i in range(4):
        move()
    if front_is_blocked():  # KAREL checks if there is a wall in front of him in which case it goes to the next row
        turn_around()
        move_to_wall()
        turn_right()
        for i in range(8):
            if front_is_clear():  # KAREL moves only if its front is clear
                move()
        turn_right()
    else:
        for i in range(3):
            move()


def move_up_to_next_letter():
    # KAREL moves upwards to the location where it can place new letter
    turn_left()
    move_to_beeper()
    turn_right()


def move_till_no_letters_present():
    """
    KAREL checks if there is a letter present
    If yes, it goes to the next spot

    """
    while beepers_present():
        move_to_next_letter()


def turn_around():
    # KAREL can now turn around easily :)
    for i in range(2):
        turn_left()


def move_to_wall():
    # KAREL will keep on moving till it reaches a wall.... Tiring right!!
    while front_is_clear():
        move()


def turn_right():
    # KAREL can now turn right
    for i in range(3):
        turn_left()


def move_to_beeper():
    # KAREL will move till it finds a beeper
    while no_beepers_present():
        move()


# Time to finally check our word search program.... KAREL, you can do it!!
if __name__ == "__main__":
    run_karel_program('40x40.w')
