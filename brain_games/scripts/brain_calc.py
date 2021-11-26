"""Script for start a game 'calculator'."""
#!/usr/bin/env python3 # noqa:E265

import brain_games.engine
import brain_games.games.calc


def main():
    """Start a game 'calculator'."""
    brain_games.engine.logic(brain_games.games.calc.game_conditions())

    if __name__ == '__main__':
        main()
