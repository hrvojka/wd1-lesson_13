import random
import json
import datetime
from operator import itemgetter


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort(key=itemgetter("score"))


def get_top_scores():
    for score_dict in score_list:
        print(f"NAME: {str(score_dict['player_name'])}, ATTEMPTS: {str(score_dict['score'])},"
              f" DATE: {str(score_dict['date'])}")


class Result:
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date


def level_easy(guess, secret):
    if guess > secret:
        print("Your guess is not correct... try something smaller")
    else:
        print("Your guess is not correct... try something bigger")


def level_hard(guess):
    print(f'{guess} is not the secret number')


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    name = input("Name: ")
    level = input("Choose a level. E for easy, H for hard: ").upper()

    while True:
        attempts += 1
        guess = int(input("Guess: "))

        if secret == guess:
            new_result_object = Result(score=int(attempts), player_name=name, date=str(datetime.datetime.now()))
            score_list.append(new_result_object.__dict__)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break

        else:
            if level == "E":
                level_easy(guess=guess, secret=secret)
            else:
                level_hard(guess=guess)

        wrong_guesses.append(guess)


def main():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores or C) quit?").upper()
        if selection == "A":
            play_game()
        elif selection == "B":
            get_top_scores()
        else:
            break


if __name__ == "__main__":
    main()