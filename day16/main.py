# from turtle import Screen, Turtle

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# for _ in range(50):
#     timmy.forward(10)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

pokemons = ["Pikachu", "Squirtle", "Charmander"]
pokemons_type = ["Electric", "Water", "Fire"]


table = PrettyTable()
table.add_column("Pokemon Name", pokemons)
table.add_column("Type", pokemons_type)
table.align = "l"

print(table)
