from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象，DashScopeEmbeddings不传model默认用的是 text-embeddings-v1模型
model = DashScopeEmbeddings()

# 调用embed_query（单个） 和 embed_documents（批量）方法，向模型提问
res = model.embed_query("我喜欢你")  # 向模型提问
res2 = model.embed_documents(["我喜欢你", "我不喜欢你"])  # 批量向模型提问

print(res)
print(res2)  