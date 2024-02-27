import turtle
import pandas as pd
import time

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.setup(width=750, height= 550)
screen.title = "State guessing game"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#this part of the project works on getting the coordinates of the states from the map

# def get_coords(x,y):
#     print(x,y)

# screen.onscreenclick(get_coords)
# turtle.mainloop()

class Guess(turtle.Turtle):
    def __init__(self, x=None, y=None, text=None):
        super().__init__()
        self.create_instance(x, y, text)

    def create_instance(self,x,y,text):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(text, move=False, align="center", font=('Arial', 9, 'normal'))

score_count = 0
guess_all_states = False
states_guessed = []

while not guess_all_states:

    answer = screen.textinput(title=f"Guess the State {score_count}/{len(data['state'])}", prompt="What is the name of another state?")
    user_response = answer.title()
    print(user_response)

    for state_name in data['state']:

        if user_response == state_name and user_response not in states_guessed:
            x_coord = data[data['state'] == state_name]['x'].values
            y_coord = data[data['state'] == state_name]['y'].values
            score_count += 1

            state = Guess(x_coord[0], y_coord[0], user_response)
            states_guessed.append(user_response)
            print(states_guessed)

        elif user_response == state_name and user_response in states_guessed:
            already_guessed = Guess(0, 0, "You have already named this state")
            time.sleep(1.5)
            already_guessed.clear()
            guess_all_states = False

        if score_count == 50:
            game_over = Guess(0, 0, "Congratulations, you have guessed them all!!")
            guess_all_states = True

        if user_response == 'Exit':
            guessed_count = Guess(0,0,f"You have guessed a total of {len(states_guessed)} states")
            states_not_guessed = [state for state in data['state'] if state not in states_guessed]
            not_guessed_states_df = pd.DataFrame({'Missed States': states_not_guessed})
            not_guessed_states_df.to_csv('missed_states.csv')
            guess_all_states = True


screen.exitonclick()