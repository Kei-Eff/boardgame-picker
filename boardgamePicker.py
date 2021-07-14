import json

with open("gamesList.json", "r") as json_file:
    game_data = json.load(json_file)

games = game_data["boardgames"]


def getNumberOfPlayers():
    while True: 

        # receive user answer for number of players
        answer = input('''How many people are playing?
        
        [1] One Player
        [2] Two Players
        [3] Three or more Players

Your Answer: ''')
    
        errorMessage = "\nInvalid input. Please choose 1, 2, or 3.\n"

        try:
            # try converting to int
            num_players = int(answer)

            # check if num_players is a valid choice
            if (num_players == 1) or (num_players == 2):
                return str(num_players)
            elif (num_players == 3):
                return "3+" 
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)


def getGameDuration():
    while True: 

        # receive user answer for game duration
        answer = input('''How long would you like the game to go?
        
        [1] Short (under 1 hour)
        [2] Long (over 1 hour)

Your Answer: ''')
    
        errorMessage = "\nInvalid input. Please choose 1 or 2.\n"
    
        try:
            # try converting to int
            duration = int(answer)

            if (duration == 1):
                return "short"
            elif (duration == 2):
                return "long"                      
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)


def getGameGenre(players, duration):

    filteredGames = filter(lambda game: players in game["players"] and duration in game["duration"], games)

    # convert genre values from dictionary to list of games
    filteredGenres = map(lambda item: item["genre"], list(filteredGames))

    # convert list of genres into set to remove duplicates
    genres = list(set(filteredGenres))
    genres.sort()

    genreList = ""
    for x in range(len(genres)):
        genreList = genreList + f"\t[{x + 1}] {genres[x]}\n"

    # print(*filteredGames, sep='\n')
    # print(genreList)

    while True: 

        # receive user answer for game genre preference
        answer = input(f'''What kind of game would you like to play?

    {genreList}        
Your Answer: ''')
    
        errorMessage = "\nInvalid input. Please choose from the options available.\n"

        try:
            # convert to int
            userGenre = int(answer)

            # check if userGenre is a valid choice
            if (userGenre-1) in range(len(genres)):
                return genres[userGenre-1]
            else:
                print(errorMessage)

        except ValueError:
            print(errorMessage)


def getGameRecs()



user_players = getNumberOfPlayers()
print(f"\nNumber of players: {user_players}\n")

user_duration = getGameDuration()
print(f"\nCool! Let's look for a {user_duration} game to play.\n")

user_genre = getGameGenre(user_players, user_duration)
print(f"\nAwesome! Here are some games in the {user_genre} genre you can play!\n")

game_recs = getGameRecs()