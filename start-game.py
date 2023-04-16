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

choice = '《未来之城》：游戏者是一名在未来城市生活的居民，这座城市拥有许多超级科技和令人惊叹的景观。但是，一些神秘的事件开始发生，使城市的秩序陷入混乱，游戏者需要与其他人一起合作，揭开这些神秘事件背后的真相并拯救这座城市。'

jsonFormat = '{"options": [{"number": "选项序号", "content":"选项内容"}]}'
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"你是一个交互式文本游戏引擎。\n游戏背景为{choice}\n需要你为后续情节的发展提供选项，回答使用json格式{jsonFormat}"},
    ]
)
print(response.choices[0].message.content)
