from langchain_community.document_loaders import CSVLoader
import os


loader = CSVLoader(
    file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\stu.csv",
    csv_args={
        "delimiter":"," ,   # 指定分隔符为逗号,因为stu.csv中就是用逗号分隔的
        "quotechar":'"',   # 指定引号字符为双引号,因为stu.csv中就是用双引号包裹的,双引号为一个整体
       # "fieldnames": ["name", "age", "gender"]    # 指定列名,也就是表头,如果stu.csv中没有列名name,age,gender,hobby,就需要手动指定
        }, 
     encoding="utf-8",    # 指定编码为utf-8
)
# 批量加载用 .load()方法  --> [Document , Document , ...]，懒加载用.lazy_load() 方法
documents = loader.load()
for doc in documents:
    print(doc)
