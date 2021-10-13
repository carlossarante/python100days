def get_invited_names():
    with open("Input/Names/invited_names.txt") as file:
        names = file.readlines()

    names = map(lambda n: n.replace('\n', ''), names)

    return names


def write_letters():
    file = open('./Input/Letters/starting_letter.txt')
    letter_content = file.read()
    file.close()
    invited_names = get_invited_names()

    for name in invited_names:
        with open(f'./Output/ReadyToSend/{name.lower()}.txt', 'w') as file:
            file.write(letter_content.replace('[name]', name))

write_letters()