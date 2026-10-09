from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(model="qwen3-embedding:4b")  # 模型名称

res = model.embed_query("我喜欢你")  # 向模型提问
res2 = model.embed_documents(["我喜欢你", "我不喜欢你"])  # 批量向模型提问

print(res)
print(res2)