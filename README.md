# WORD-SEARCH-WITH-KAREL

In the 1970s, a Stanford graduate student named Rich Pattis decided that it would be easier to teach the fundamentals of programming if students could somehow learn the basic ideas in a simple environment free from the complexities that characterize most programming languages. Rich designed an introductory programming environment in which students teach a robot to solve simple problems. That robot was named Karel, after the Czech playwright Karel Čapek, whose 1923 play R.U.R. (Rossum’s Universal Robots) gave the word robot to the English language.

Karel, a friendly rectangular white robot with two black feet.
Karel the Robot was quite a success. Karel has been used in introductory computer science courses all across the world and has been taught to millions of students. Many generations of Stanford students learned how programming works with Karel, and it is still the gentle introduction to coding used at Stanford.

![alt text](https://compedu.stanford.edu/karel-reader/docs/images/ch1/karelLarge.png)


# What is Karel?

Karel is a very simple robot living in a very simple world. By giving Karel a set of commands, you can direct it to perform certain tasks within its world. The process of specifying those commands is called programming. Initially, Karel understands only a very small number of predefined commands, but an important part of the programming process is teaching Karel new commands that extend its capabilities.

Karel programs have much the same structure and involve the same fundamental elements as Python, a major programming language. The critical difference is that Karel’s programming language is extremely small and as such the details are easy to master. Even so, you will discover that solving a problem can be challenging.

By starting with Karel, you can concentrate on solving problems from the very beginning. Problem solving is the essence of programming. And because Karel encourages imagination and creativity, you can have quite a lot of fun along the way.


# Karel's World

Karel’s world is defined by rows running horizontally (east-west) and columns running vertically (north-south). The intersection of a row and a column is called a corner. Karel can only be positioned on corners and must be facing one of the four standard compass directions (north, south, east, west). A sample Karel world is shown below. Here Karel is located at the corner of 1st row and 1st column, facing east.

The world has 4 rows and 6 columns. Karel is at the bottom left corner, row 1 column 1, facing east. There are walls in a rectangle near the bottom right corner around the positions in row 1 columns 4, 5, and 6. There is a beeper in row 1 column 2.
Several other components of Karel’s world can be seen in this example. The object in front of Karel is a beeper. As described in Rich Pattis’s book, beepers are “plastic cones which emit a quiet beeping noise.” Karel can only detect a beeper if it is on the same corner. The solid lines in the diagram are walls. Walls serve as barriers within Karel’s world. Karel cannot walk through walls and must instead go around them. Karel’s world is always bounded by walls along the edges, but the world may have different dimensions depending on the specific problem Karel needs to solve.

![alt text](https://compedu.stanford.edu/karel-reader/docs/images/ch1/world.png)



# MY PROJECT

The overall aim of this program is for Karel to create a word
search with a high degree of randomness and then have him find 
the hidden words. In this version which is appended due to 
humanistic limitations, Karel knows four words; KAREL, PYTHON, 
CHOCO and SHREYASI (That's me :D). Once the human user is given
a chance to try and solve the puzzle, Karel will search out all
the words he knows. Overall I found this task especially
challenging due to the high degree of forethought and perspective
of the whole map which is required in creating a word search.
