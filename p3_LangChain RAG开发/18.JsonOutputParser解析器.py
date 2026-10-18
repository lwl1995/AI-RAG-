from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

#创建解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

#创建模型
model = ChatTongyi(model="qwen-max")

#创建第一个prompt模板
first_prompt = PromptTemplate.from_template("我邻居姓：{lastname}，刚生了{gender},请起名,并封装为json格式给我，key为name")

#创建第二个prompt模板
second_prompt = PromptTemplate.from_template("姓名：{name}，请帮我解析含义")

#构建链
chain = first_prompt | model | json_parser | second_prompt | model | str_parser
res = chain.invoke({"lastname": "张", "gender": "男"})
print(res)