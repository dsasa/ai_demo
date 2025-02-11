import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

try:
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),  # 从环境变量获取API密钥
        base_url=os.getenv('OPENAI_BASE_URL')
    )
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "写一篇500字的科幻小说"}]
    )
    
    print(completion.choices[0].message.content)

except Exception as e:
    print(f"发生错误: {str(e)}")