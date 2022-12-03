play = {"X": "Rock", "Y": "Paper", "Z": "Scissor",
        "A": "Rock", "B": "Paper", "C": "Scissor"}
point = {"Rock": 1, "Paper": 2, "Scissor": 3}


def get_play(player_play):
    return play.get(player_play)


def get_score(opponent, player):
    opponent_play, player_play = get_play(opponent), get_play(player)
    if opponent_play == player_play:
        return point.get(player_play) + 3
    elif (player_play == "Rock" and opponent_play == "Paper") or (player_play == "Paper" and opponent_play == "Scissor") or (player_play == "Scissor" and opponent_play == "Rock"):
        return point.get(player_play) + 0
    return point.get(player_play) + 6


def total_score():
    score = 0
    new_score = 0
    with open("StrategyGuide") as strategies:
        for strategy in strategies:
            score = score + get_score(strategy[0], strategy[2])
            new_score = new_score + new_strategy(strategy[0], strategy[2])
            # print(new_strategy(strategy[0], strategy[2]))
    return score, new_score


def new_strategy(opponent, player):
    opponent_play, player_play = get_play(opponent), get_play(player)
    if player == "X":
        return 0 + loosing_point(opponent_play)
    elif player == "Y":
        return 3 + point.get(opponent_play)
    return 6 + winning_point(opponent_play)


def winning_point(opponent):
    if opponent == "Rock":
        return point.get("Paper")
    elif opponent == "Paper":
        return point.get("Scissor")
    return point.get("Rock")


def loosing_point(opponent):
    if opponent == "Rock":
        return point.get("Scissor")
    elif opponent == "Paper":
        return point.get("Rock")
    return point.get("Paper")


print(total_score())