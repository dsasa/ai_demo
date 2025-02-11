from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化语言模型
llm = ChatOpenAI(model_name="gpt-4")

# 定义提示词模板
prompt_template = """
生成一条关于{topic}的社交媒体帖子。
要求：内容吸引人，适合{platform}平台。
"""
prompt = PromptTemplate(input_variables=["topic", "platform"], template=prompt_template)

# 生成帖子文本
# topic = "人工智能"
# platform = "推特"

# 使用invoke方法调用
# response = llm.invoke(prompt.format(topic=topic, platform=platform))
# print(response)


# 定义获取帖子内容的方法
def get_post_content(topic="人工智能", platform="推特"):
    # 生成帖子文本
    response = llm.invoke(prompt.format(topic=topic, platform=platform))
    return response.content  # 确保返回的是字符串

# # 示例调用
# if __name__ == "__main__":
#     print(get_post_content())