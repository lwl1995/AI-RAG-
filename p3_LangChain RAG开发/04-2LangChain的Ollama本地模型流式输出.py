from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")  # 模型名称

# 向模型提问，开启流式输出
res =  model.stream(input="你是谁呀")    

for chunk in res:
    print(chunk, end="", flush=True)  # 输出模型的回答