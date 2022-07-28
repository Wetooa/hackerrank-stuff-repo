def minion_game(string):
    # your code goes here
    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    stuart = 0
    kevin = 0
    for x in range(len(string)):
        if string[x] not in vowels:
            stuart += len(string) - x
        else:
            kevin += len(string) - x
    
    if stuart > kevin:print(f"Stuart {stuart}")
    elif kevin > stuart:print(f"Kevin {kevin}")
    else:print("Draw")
            

minion_game(input())