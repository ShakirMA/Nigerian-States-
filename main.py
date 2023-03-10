import turtle
import pandas

screen = turtle.Screen()
screen.title("Nigeria States")
image = "nigerian_map.gif"
screen.addshape(image)
turtle.shape(image)

# turtle.mainloop()
correct_guesses = []

data = pandas.read_csv("36_states.csv")
all_states = data["state"].to_list


while len(correct_guesses) < 37:
    guess = screen.textinput(title=f"{len(correct_guesses)}/37 states correct", prompt="What is another state?").title()

    if guess == "Exit":
        states_not_mentioned = [state for state in all_states if state not in correct_guesses]


        # for state in all_states():
        #     if state not in correct_guesses:
        #         states_not_mentioned.append(state)
        new_data = pandas.DataFrame(states_not_mentioned)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states():
        correct_guesses.append(guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == guess]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(guess)


screen.exitonclick()