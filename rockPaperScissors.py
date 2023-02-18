# Exercise #22: Rock, Paper, Scissors

def rpsWinner(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        return "player one"
    elif player1 == "rock" and player2 == "paper":
        return "player two"
    elif player1 == "paper" and player2 == "rock":
        return "player one"
    elif player1 == "paper" and player2 == "scissors":
        return "player two"
    elif player1 == "scissors" and player2 == "paper":
        return "player one"
    elif player1 == "scissors" and player2 == "rock":
        return "player two"
    else:
        return "tie"

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
