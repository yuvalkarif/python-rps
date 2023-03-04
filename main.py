import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Rock Paper Scissors Game")
turtle_pen = turtle.Turtle()
turtle_pen.hideturtle()

# Load the images for rock, paper, and scissors
rock_img = "rock.gif"
paper_img = "paper.gif"
scissors_img = "scissors.gif"
screen.addshape(rock_img)
screen.addshape(paper_img)
screen.addshape(scissors_img)

# Define the game logic
def determine_winner(player_choice, computer_choice):
    if player_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif player_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    elif player_choice == computer_choice:
        return "It's a tie!"
    else:
        return "Computer wins!"

# Set up the game options
options = ["rock", "paper", "scissors"]
user_choice = None

# Create the player's choice buttons using images
rock_btn = turtle.Turtle()
rock_btn.shape(rock_img)
rock_btn.penup()
rock_btn.goto(-210, 0)

paper_btn = turtle.Turtle()
paper_btn.shape(paper_img)
paper_btn.penup()
paper_btn.goto(0, 0)

scissors_btn = turtle.Turtle()
scissors_btn.shape(scissors_img)
scissors_btn.penup()
scissors_btn.goto(210, 0)

# Define functions to handle button clicks
def choose_rock(x, y):
    global user_choice
    user_choice = "rock"
    play_game()

def choose_paper(x, y):
    global user_choice
    user_choice = "paper"
    play_game()

def choose_scissors(x, y):
    global user_choice
    user_choice = "scissors"
    play_game()

# Add event listeners to the buttons
rock_btn.onclick(choose_rock)
paper_btn.onclick(choose_paper)
scissors_btn.onclick(choose_scissors)

# Draw the game results on the screen
def play_game():
    computer_choice = random.choice(options)
    turtle_pen.clear()
    turtle_pen.goto(-200, -150)
    turtle_pen.write("You chose: " + user_choice.capitalize(), font=("Comic Sans MS", 16, "bold"))
    turtle_pen.goto(-200, -200)
    turtle_pen.write("Computer chose: " + computer_choice.capitalize(), font=("Comic Sans MS", 16, "bold"))
    turtle_pen.goto(-200, -250)
    turtle_pen.write(determine_winner(user_choice, computer_choice), font=("Comic Sans MS", 20, "bold"))

# Keep the screen open until the user closes it
screen.mainloop()
