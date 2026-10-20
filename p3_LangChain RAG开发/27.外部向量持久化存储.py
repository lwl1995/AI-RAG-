from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings  #阿里云文本转向量的模型
from langchain_community.document_loaders import CSVLoader

#Chroma向量数据库（轻量级的）
#确保langchain-chroma  chroma这两个库安装了，如没有安装请pip install langchain-chroma   pip install chroma

vector_store = Chroma(
    collection_name="test",  #指定当前向量存储的名字，类似于数据库的表名称
    embedding_function=DashScopeEmbeddings(),  #嵌入模型
    persist_directory=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\chroma_db",  #指定向量存储的路径文件夹
    )

loader = CSVLoader(
    file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\info.csv",
     encoding="utf-8",    # 指定编码为utf-8
     source_column="source"     # 指定本条数据的来源是哪里
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
    filter={"source": "黑马程序员"} # 检索的过滤条件，source=“黑马程序员”的文档才会被检索出来
)
print("检索结果：",results)