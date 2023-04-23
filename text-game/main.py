from engine import game_loop
from story import Story
from story import Event
from story import Option

if __name__ == '__main__':
    story = Story()
    story.add_event(Event("游戏背景"))

    while True:
        game_loop(story)