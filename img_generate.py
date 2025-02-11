from openai import OpenAI

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_image(prompt):
    response = client.images.generate(prompt=prompt,
    n=1,
    size="512x512")
    return response.data[0].url

# 定义主题
topic = "人工智能"

# 生成图片
image_url = generate_image(f"生成一个与{topic}相关的图片")
print(image_url)