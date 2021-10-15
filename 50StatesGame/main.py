import turtle
import pandas

NUMBER_OF_STATES = 50

class USStatesGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        image = './blank_states_img.gif'
        self.screen.addshape(image)
        self.db = pandas.read_csv('50_states.csv')
        turtle.shape(image)
        self.states = []
        self.init_prompt()

    def get_correct_guesses(self):
        return len(self.states)

    def get_prompt_title(self):
        correct_guesses = self.get_correct_guesses()

        if correct_guesses == 0:
            return 'Guess the state?'

        return f'Correct Guesses: {correct_guesses}/{NUMBER_OF_STATES}'

    def add_state(self, state_data):
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.setposition(int(state_data.x), int(state_data.y))
        text.write(state_data.state.values[0])
        self.states.append(state_data)


    def init_prompt(self):
        while len(self.states) < NUMBER_OF_STATES:
            answer = self.screen.textinput(title=self.get_prompt_title(), prompt="What's another state's name?")
            capitalized_name = ' '.join(list(map(lambda string: string.capitalize(), answer.split(' '))))
            solution = self.db[self.db['state'] == capitalized_name]

            if len(solution) > 0:
                self.add_state(solution)
            else:
                print(f'Not found {answer.capitalize()}')



turtle.mainloop()