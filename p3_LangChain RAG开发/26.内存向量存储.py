from langchain_core.vectorstores import InMemoryVectorStore  #向量存储
from langchain_community.embeddings import DashScopeEmbeddings  #阿里云文本转向量的模型
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(),  #指定向量化模型
)

loader = CSVLoader(
    file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\info.csv",
     encoding="utf-8",    # 指定编码为utf-8
     source_column="source",     # 指定本条数据的来源是哪里
)
documents = loader.load()

#向量存储的新增、删除、检索
vector_store.add_documents(
        documents=documents,  #被添加的文档，类型为list[document]
        ids=["id"+str(i) for i in range(1, len(documents)+1)] # 给添加的文档提供id（字符串）  list[str] id1/id2/id3/id4/id5/id6/id7/id8/id9/id10
)  

#删除 传入[id,id...]
vector_store.delete(ids=["id1", "id2"])  #删除id1/id2/id3对应的信息

#检索 返回类型list[document]
results = vector_store.similarity_search(
    query="python是不是简单易学？",  # 检索的内容
    k=3,  # 检索的结果数量
)
print("检索结果：",results)