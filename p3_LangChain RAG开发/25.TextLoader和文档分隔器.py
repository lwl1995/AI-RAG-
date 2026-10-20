from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  #递归文档分割器

loader = TextLoader(file_path=r"D:\vscodeSpace\AI大模型RAG与智能体开发\p3_LangChain RAG开发\data\Python基础语法.txt", encoding="utf-8")
documents = loader.load()   #[document]
splitter= RecursiveCharacterTextSplitter(
        chunk_size=500,  # 分段的最大字符数
        chunk_overlap=50,  # 分段之间允许重叠的字符数
        separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],   # 文本自然段落分隔的依据符号
        length_function=len,  # 计算文本长度的函数，默认是len()
)
split_docs = splitter.split_documents(documents)   

print("分割后文档数量：", len(split_docs))
for doc  in split_docs:
    print("分割后的内容--------------------------" + doc.page_content)