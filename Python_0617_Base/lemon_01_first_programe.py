with open("game_file.txt", mode="r", encoding="utf8") as read_game_file:
    a = read_game_file.read()
    map(tuple, a)
    print(a,type(a))
