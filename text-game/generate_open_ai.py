import json
import os
import openai
from dotenv import load_dotenv
from story import Event, Option

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_next_options(story):
    systemSetUp = f'你是一个交互式文本游戏引擎。游戏背景为“{story.get_current_event().current}”。请你生成对应的下一步情节next和选项options，仅返回并严格按 JSON 格式返回，示例：{{"next": "", "options": ["", "", ""]}}'

    messages = [
        {'role': 'system', 'content': systemSetUp}
    ]
    print("messages: \n", messages)

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    print("response: \n", response.choices[0].message.content)
    content = json.loads(response.choices[0].message.content)
    story.add_event(Event(content["next"], [Option(option) for option in content["options"]]))