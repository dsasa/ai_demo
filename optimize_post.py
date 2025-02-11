from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化语言模型
llm = ChatOpenAI(model_name="gpt-4")

# 定义优化提示词模板
optimization_template = """
根据以下用户反馈优化社交媒体帖子内容：
主题：{topic}
平台：{platform}
用户反馈：点赞数{likes}，评论数{comments}
"""
optimization_prompt = PromptTemplate(
    input_variables=["topic", "platform", "likes", "comments"],
    template=optimization_template
)

# 用户反馈数据
user_feedback = {"likes": 100, "comments": 20}

# 生成优化后的帖子文本
topic = "人工智能"
platform = "微博"
optimized_response = llm.invoke(optimization_prompt.format(
    topic=topic, platform=platform, likes=user_feedback["likes"], comments=user_feedback["comments"]
))

print(optimized_response)