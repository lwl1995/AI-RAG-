from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

# StrOutputParser是langchain的内置简单字符串解析器，可以将AIMessage类型转换为基础字符串，也可以将StrOutputParser加入chain中作为组件存在
parser = StrOutputParser()  
model = ChatTongyi(model="qwen-max")
prompt= PromptTemplate.from_template("我邻居姓：{lastname}，刚生了{gender},请起名")

# prompt作为输入给第一个model,第一个model输出返回AIMessage,再将AIMesage作为输入给parser,parser返回str字符串,再将str作为输入给第
# 二个model,第二个model返回AIMessage
chain = prompt | model | parser | model 
res = chain.invoke({"lastname": "张", "gender": "男"})
print(res.content)