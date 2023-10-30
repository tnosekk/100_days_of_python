# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


with open(
    "/Users/tomek/Documents/Courses/100_days_of_python/day24/Mail Merge Project Start/Input/Names/invited_names.txt"
) as guest_names:
    names = guest_names.readlines()


with open(
    "/Users/tomek/Documents/Courses/100_days_of_python/day24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
) as text:
    letter_content = text.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(
            f"/Users/tomek/Documents/Courses/100_days_of_python/day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(new_letter)
