"""Script for start a game 'calculator'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Start the game 'calculator'."""
    run_game(calc)


if __name__ == '__main__':
    main()
