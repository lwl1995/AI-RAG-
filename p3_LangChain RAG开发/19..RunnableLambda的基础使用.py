from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda



#创建模型
model = ChatTongyi(model="qwen-max")

str_parser =  StrOutputParser()

#创建第一个prompt模板
first_prompt = PromptTemplate.from_template("我邻居姓：{lastname}，刚生了{gender},请起名,仅告知我姓名即可，不要其他信息")

#创建第二个prompt模板
second_prompt = PromptTemplate.from_template("姓名：{name}，请帮我解析含义")

#函数的入参：AiMessage-->字典dict （{“name”: “…”}）
my_func = RunnableLambda(lambda ai_meg : {"name":ai_meg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser
res = chain.invoke({"lastname": "张", "gender": "男"})
print(res)