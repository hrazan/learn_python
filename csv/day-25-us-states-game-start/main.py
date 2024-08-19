from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
screen = Screen()
turtle = Turtle()

screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def write_state(state_name, state_pos_x, state_pos_y):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.goto(state_pos_x, state_pos_y)
    text.write(state_name)

guessed_states = []
all_states = data["state"].str.lower().to_list()
states_left = 50
while len(guessed_states) < 50:
    answer = screen.textinput(title=f'{states_left}/50 Guess the State', prompt="What's another state name?").lower()
    print(answer)

    if answer == "exit":
        break

    if answer in all_states:
        guessed_states.append(answer)
        true_answer_data = data[data["state"].str.lower() == answer]
        states_left -= 1
        true_answer_name = true_answer_data["state"].item()
        true_answer_pos_x = true_answer_data["x"].item()
        true_answer_pos_y = true_answer_data["y"].item()
        print("True!")
        print(true_answer_data)
        write_state(true_answer_name, true_answer_pos_x, true_answer_pos_y)

states_to_learn = [state for state in all_states if (state not in guessed_states)]
states_to_learn_data_dict = {
    "state" : states_to_learn
}
states_to_learn_data = pd.DataFrame(states_to_learn_data_dict)
states_to_learn_data.to_csv("states_to_learn.csv")