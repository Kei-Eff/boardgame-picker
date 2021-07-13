import json

with open("gamesList.json", "r") as json_file:
    data = json.load(json_file)

filtered = filter(lambda game: 2 in game["players"], data["boardgames"])
print(list(filtered))

# with open("test.json", "r") as file:
#     filterGenre = filter(lambda game: game["genre"] == "Mystery", y["boardgames"])
#     print(list(filterGenre))

# print(y["boardgames"])