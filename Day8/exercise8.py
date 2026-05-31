def calculate_love_score(name1, name2):
    both = name1.lower() + name2.lower()
    true = sum([both.count(letter) for letter in "true"])
    love = sum([both.count(letter) for letter in "love"])

    print(str(true) + str(love))
