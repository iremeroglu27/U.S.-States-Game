import turtle
import pandas

FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")


image = "./day 25 CsvFiles/U.S. States Game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv("./day 25 CsvFiles/U.S. States Game/50_states.csv")
all_states = data.state.to_list()
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("black")

count = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f" {count}/50 Guess The State", prompt="What's another states name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./day 25 CsvFiles/U.S.-States-Game/states_to_learn.csv")

        break
    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        count += 1
        state_data = data[data.state == answer_state]
        position = (state_data.x.item(), state_data.y.item())
        t.goto(position)
        t.write(f"{answer_state}", align="center", font=FONT)      
        
