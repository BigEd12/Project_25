import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")
# Add an image to turtle
image = "blank_states_img.gif"
screen.addshape(image)
screen.screensize(725, 491)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
remaining_states = state_list

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 correct", "Make your guess:").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if answer_state not in guessed_states ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        remaining_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
