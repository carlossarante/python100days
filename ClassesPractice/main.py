# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pickachu', 'Boulbasour', 'Squirtle'])
table.add_column('Type', ['Electric', 'Water', 'Water'])
table.align = 'l'

print(table)