from langchain import LangSmith

langsmith = LangSmith()
langsmith.log(prompt=format(topic=topic, platform=platform), response=optimized_response)
langsmith.log(prompt=format(topic=topic, platform=platform), response=user_feedback)

report = langsmith.evaluate()
print(report)