import random
import string
from story import Event
# from generate_random import generate_next_event
from generate_open_ai import generate_next_options


def game_loop(story):
    while True:
        print([obj.text for obj in story.events])

        # 获取当前情节
        generate_next_options(story)
        current_event = story.get_current_event()
        options = story.options

        # 输出当前情节文本
        print(current_event.text)

        # 输出选项
        for i, option in enumerate(options):
            print(f"{i + 1}. {option.text}")

        # 获取玩家输入的选项序号
        choice = input("请选择一个选项：")

        # 处理玩家输入的选项
        try:
            choice_num = int(choice) - 1
            if choice_num < 0 or choice_num >= len(options):
                raise ValueError
        except ValueError:
            print("请输入有效的选项序号！")
            continue

        # 更新玩家的当前情节和选择
        story.add_event(Event(options[choice_num].text))
