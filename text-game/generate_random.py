import random
import string
from story import Option

def generate_next_options(story):
    story.options = [Option("选项1" + random_string(5)), Option("选项2" + random_string(5)), Option("选项3" + random_string(5))]

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
