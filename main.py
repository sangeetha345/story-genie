import random

def genie_fairy_tale():
    characters = ["a young prince", "a brave knight", "a clever fox", "a wise wizard", "a curious girl"]
    settings = ["in an enchanted forest", "in a faraway kingdom", "in a hidden valley", "on a misty mountain", "near a magical lake"]
    conflicts = ["must find a lost treasure", "has to rescue a friend", "discovers a hidden secret", "breaks a wicked spell", "faces a fierce dragon"]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    return f"Once upon a time, {character} {setting} {conflict}."

def genie_sci_fi_adventure():
    characters = ["a space explorer", "an AI companion", "a cyborg pilot", "a fearless scientist", "an alien diplomat"]
    settings = ["aboard a starship", "on a distant planet", "in a mysterious space station", "in a galaxy far away", "on a deserted asteroid"]
    conflicts = ["discovers a hidden alien civilization", "encounters a space-time anomaly", "battles a rogue AI", "searches for a rare element", "faces a powerful alien warlord"]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    return f"In the future, {character} {setting} {conflict}."

def genie_mystery():
    characters = ["a detective", "a journalist", "an amateur sleuth", "a police officer", "a private investigator"]
    settings = ["in a quiet town", "at a grand mansion", "by a foggy river", "in an old library", "in a bustling city"]
    conflicts = ["must solve a strange disappearance", "investigates a suspicious death", "finds a hidden clue", "uncovers a long-lost secret", "confronts a mysterious stranger"]

    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)

    return f"In a suspenseful tale, {character} {setting} {conflict}."

def main():
    print("Welcome to the Story Genie!")
    print("Here are three different stories for you:")
    print("\nFairy Tale:")
    print(genie_fairy_tale())
    print("\nSci-Fi Adventure:")
    print(genie_sci_fi_adventure())
    print("\nMystery Story:")
    print(genie_mystery())

# Run the main function to display stories
main()
