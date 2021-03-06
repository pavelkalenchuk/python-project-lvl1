"""Script for start a game 'Prime'."""
#!/usr/bin/env python3 # noqa:E265

from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Start the game 'Prime'."""
    run_game(prime)


if __name__ == '__main__':
    main()
