# from .exceptions import *
import random


class GuessAttempt(object):
    pass


class GuessWord(object):
    pass


class HangmanGame(object):
    def __init__(self, word_list=['rmotr', 'python', 'awesome'], number_of_guesses=5):
        self.WORD_LIST = word_list
        self.number_of_guesses = number_of_guesses

    def select_random_word(self, list_of_words):
        return random.choice(list_of_words)


a = HangmanGame()
# print(a.WORD_LIST)
print(a.WORD_LIST)
# print(a.number_of_guesses)
print(a.select_random_word(['hi', 'there', 'how', '1', '2',3,4,5,6,7,8,9,0]))
