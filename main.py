PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./INPUT/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/letter_for{name.strip()}.txt", "w") as output:
            output.write(new_letter)