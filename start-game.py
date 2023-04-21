import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


# print('游戏开始！')
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="随机生成一个游戏主题",
#   n=3,
#   max_tokens=100,
#   temperature=0.5
# )
# for i, choice in enumerate(response.choices):
#     print(f"{i+1}. {choice.text.strip()}")

# choiceIndex = input("请随机选择一个随机游戏背景：")
# choice = response.choices[int(choiceIndex) - 1].text.strip()

backGroud = '《未来之城》：小明是一名在未来城市生活的居民，这座城市拥有许多超级科技和令人惊叹的景观。但是，一些神秘的事件开始发生，使城市的秩序陷入混乱，小明需要与其他人一起合作，揭开这些神秘事件背后的真相并拯救这座城市。'
nextStepFormat = {"current": "当前情节", "options": ["选项1", "选项2", "选项3"]}
systemSetUp = f'你是一个交互式文本游戏引擎。游戏背景为{backGroud}。你的回答为json格式，格式参考{nextStepFormat}'

messages=[
        {'role': 'system', 'content': systemSetUp},
        {'role': 'user', 'content': '你好，我是小明，现在开始游戏'}
    ]

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
)

nextStep = response.choices[0].message.content
print(nextStep.current)
print(nextStep.options)

