from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\pdf2.pdf",  # 必填 前面加`r`，防止`\`转义
    mode = "single",  # 默认是page模式，每个页面形成一个Document文档对象；'single模式'不管有多少页，只返回一个Document文档对象
    password = "itheima",  # 非必填，pdf文件的密码，如果没有密码就不传
)

for doc in loader.load():
    print(doc)