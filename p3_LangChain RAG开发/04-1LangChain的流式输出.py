from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")


#通过stream方法进行流式输出
res = model.stream(input="你是谁呀") # 向模型提问


for chunk in res:
    print(chunk, end="", flush=True)  # 输出模型的回答  