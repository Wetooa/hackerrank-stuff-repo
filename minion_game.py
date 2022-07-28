def minion_game(string):
    # your code goes here
    string = string.lower()
    current = ""
    vowels = ["a", "e", "i", "o", "u"]
    stuart = 0
    kevin = 0
    all_words = []
    for x in range(len(string)):
        for y in range(x, len(string)):
            current += string[y]
            if current[0] in vowels: kevin += 1
            else:stuart += 1
        current = ""
    if stuart > kevin:print(f"Stuart {stuart}")
    elif kevin > stuart:print(f"Kevin {kevin}")
    else:print("Draw")
            

minion_game("Banana")