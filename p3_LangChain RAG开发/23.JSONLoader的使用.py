from langchain_community.document_loaders import JSONLoader


loader = JSONLoader(
    file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\stu_json_lines.json", #前面加`r`，防止`\`转义
    jq_schema=".name" , #表示从根获取name的值
    text_content=False,  # 告知JSONLoader，我要获取的内容不是字符串
    json_lines=True,  # 告知JSONLoader，这是一个jsonlines文件，每一行都是一个json对象
)

documents = loader.load()
for doc in documents:
    print(doc)
    # 哈哈