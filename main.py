
# Read the list of names
# The readlines() method returns a list containing each line in the file as a list item.
with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

# Read the template letter
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    template_letter = letter_file.read()

# Replace the [name] placeholder and save the letters
for name in names:
    stripped_name = name.strip() # Remove any leading/trailing whitespace
    new_letter = template_letter.replace('[name]', stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)