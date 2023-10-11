from lexicon.lexicon import LEXICON_RU
from constants.constants import rules

ATTEMPTS = 3


class User:
    def __init__(self) -> None:
        self.in_game = False
        self.attempts = ATTEMPTS
        self.total_games = 0
        self.bot_winning_games = 0
        self.user_winning_games = 0
        self.user_winning_rounds = 0
        self.bot_winning_rounds = 0

    def reset_game(self) -> None:
        self.in_game = False
        self.attempts = ATTEMPTS
        self.user_winning_rounds = 0
        self.bot_winning_rounds = 0

    def check_answer(self, user_answer: str, bot_answer: str) -> str:

        self.attempts -= 1

        if user_answer == bot_answer:
            return LEXICON_RU['round_dead_heat']

        elif rules[bot_answer] == user_answer:
            self.bot_winning_rounds += 1
            return LEXICON_RU['round_bot']

        else:
            self.user_winning_rounds += 1
            return LEXICON_RU['round_user']

    def get_winner(self) -> str:
        self.total_games += 1

        if self.bot_winning_rounds == self.user_winning_rounds:
            return LEXICON_RU['dead_heat']

        if self.bot_winning_rounds > self.user_winning_rounds:
            self.bot_winning_games += 1
            return LEXICON_RU['bot_is_winner']

        else:
            self.user_winning_games += 1
            return LEXICON_RU['user_is_winner']


class Users:
    def __init__(self) -> None:
        self.users: dict[int, User] = {}

    def get_user_by_id(self, user_id: int) -> User:
        return self.users[user_id]

    def add_user(self, user_id: int) -> None:
        self.users[user_id] = User()

    def is_user_exist(self, user_id: int) -> bool:
        return user_id in self.users.keys()


users = Users()




