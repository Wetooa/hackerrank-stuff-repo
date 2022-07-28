# sheeeet op solution done in under 10 mins and probably the most efficent solution out there
# basically, the first part of the print statement checks the word count of a in the original word
# then since the world will probably be multiplied, the code gets the floor of n / len(word)
# for example if n = 10 and len(word) = 3, then the word will be repeated thrice, so we get the count of that
# however, what if n would not repeated the entire word? then thats were the next part of the print statement comes in
# it checks for the modulo of n / len(word), in the previous case, that would result in 1
# this means that the first word would be repeated as the last character
# therefore we would just have to use a string method in python to get the part of the string that will not be fully repeated and get "a"'s count
# in the cases where the full string will be repeated at the end, that that would just result in word[0:0] which would check for nothing

word = input().strip()
n = int(input().strip())

print(word.count("a") * (n // len(word)) + word[0:n % len(word)].count("a"))