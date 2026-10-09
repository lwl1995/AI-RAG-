#  langchain_ollama
from langchain_ollama import OllamaLLM

# model: 模型名称
model = OllamaLLM(model="qwen3:4b")

# 调用invoke方法(一次性返回完整结果)，向模型提问
res = model.invoke(input = "你是谁呀")
print(res)  # 输出模型的回答