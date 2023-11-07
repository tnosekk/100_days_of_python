# try:
#     file = open("day30/a_file.txt")
#     a_dictionary = {"key": "value"}
# except FileNotFoundError:
#     file = open("day30/a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3m")

# bmi = round(weight / height**2, 2)
# print(bmi)


fruits = eval(input())


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(4)
