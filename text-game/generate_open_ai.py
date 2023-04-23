import json
import os
import openai
from dotenv import load_dotenv
from story import Event, Option

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_next_options(story):
    systemSetUp = f'你是一个交互式文本游戏引擎。游戏背景为{story.backGroud}。请你生成下一步情节及选项，并放入 JSON 中，示例：{{"current": "当前情节", "options": ["选项1", "选项2", "选项3"]}}。仅返回 JSON'

    messages = [
        {'role': 'system', 'content': systemSetUp}
    ]
    for i, event in enumerate(story.events):
        if i % 2 == 0:
            messages.append({'role': 'system', 'content': event.text})
        else:
            messages.append({'role': 'user', 'content': event.text})

    print("messages: \n", messages)

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    print("response: \n", response.choices[0].message.content)
    content = json.loads(response.choices[0].message.content)
    print("content: \n", content)
    story.add_event(Event(content['current']))
    story.options = [Option(text) for text in content['options']]