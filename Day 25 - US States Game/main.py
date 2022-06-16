import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")


writer = turtle.Turtle()
writer.ht()
writer.pu()
writer.color("black")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Variables
num_guessed_states = 0
guessed_states = []
answer_data = pandas.read_csv("50_states.csv")
states_list = answer_data['state'].to_list()

while num_guessed_states < 50:
    answer_state = screen.textinput(title=f"{num_guessed_states}/50 States Named",
                                    prompt="What's another state's name").title()
    if (answer_state in states_list) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        guessed_x = int(answer_data[answer_data.state == answer_state].x)
        guessed_y = int(answer_data[answer_data.state == answer_state].y)
        writer.goto(x=guessed_x, y=guessed_y)
        writer.write(arg=answer_state.title(), align="center")
        num_guessed_states = len(guessed_states)

    elif answer_state == "Exit":
        break

states_to_learn = [state for state in states_list if state not in guessed_states]
print(states_to_learn)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
