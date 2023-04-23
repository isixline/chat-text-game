from engine import game_loop
from story import Story
from story import Event
from story import Option

if __name__ == '__main__':
    story = Story()
    story.backGroud = "《未来之城》：小明是一名在未来城市生活的居民，这座城市拥有许多超级科技和令人惊叹的景观。但是，一些神秘的事件开始发生，使城市的秩序陷入混乱，小明需要与其他人一起合作，揭开这些神秘事件背后的真相并拯救这座城市。"

    while True:
        game_loop(story)