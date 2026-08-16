def read_file():
    players = []
    with open('bowling.txt', 'r', encoding='utf-8') as f:
        for line in f:
            field = line.rstrip('\n').split(';')
            scores = [int(score) for score in field[2:]]
            players.append({'surname':field[0], 'name': field[1], 'scores': scores
            })
    return players

def calculate_total_score(player):
    return sum(player['scores'])

def combine_players_scores(players):
    for player in players:
        player['total_score'] = calculate_total_score(player)

def print_leaderboard(players):
    players.sort(key=calculate_total_score, reverse=True)
    for player in players:
        print(f"{player['surname']} {player['name']} {player['total_score']}")

def print_players_with_most_tens_and_zeros(players):
    most_tens_count = 0
    most_zeros_count = 0
    players_with_most_tens = []
    players_with_most_zeros = []

    for player in players:
        tens_count = sum(score == 10 for score in player['scores'])
        zeros_count = sum(score == 0 for score in player['scores'])

        if tens_count > most_tens_count:
            most_tens_count = tens_count
            players_with_most_tens = [player]
        elif tens_count == most_tens_count:
            players_with_most_tens.append(player)

        if zeros_count > most_zeros_count:
            most_zeros_count = zeros_count
            players_with_most_zeros = [player]
        elif zeros_count == most_zeros_count:
            players_with_most_zeros.append(player)

    print("Players with the most '10's:")
    for player in players_with_most_tens:
        print(f"{player['surname']} {player['name']}")

    print("Players with the most '0's:")
    for player in players_with_most_zeros:
        print(f"{player['surname']} {player['name']}")


def main():
    players = read_file()
    combine_players_scores(players)
    print_leaderboard(players)
    print_players_with_most_tens_and_zeros(players)

if __name__ == '__main__':
    main()