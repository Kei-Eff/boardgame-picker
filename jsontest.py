import json

# y = json.loads("test.json")

with open("test.json", "r") as json_file:
    y = json.load(json_file)
    filtered = filter(lambda game: 2 in game["players"], y["boardgames"])
    print(list(filtered))

with open("test.json", "r") as file:
    filterGenre = filter(lambda game: game["genre"] == "Mystery", y["boardgames"])
    print(list(filterGenre))

# print(y["boardgames"])