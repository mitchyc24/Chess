from chess import Chess
import json

def main():
    with open("config.json", "r") as config:
        settings = json.load(config)

    game = Chess(settings)
    game.run()


if __name__ == "__main__":
    main()