#导入通用提示词类(在zero-shot思想下，可以使用PromptTemplate)，few-shot思想下，需要更换为FewShotPromptTemplate(后续学习)
from langchain_core.prompts import PromptTemplate 
from langchain_community.llms.tongyi import Tongyi #导入大语言模型类

promptTemplate = PromptTemplate.from_template(
        "我的邻居姓{lastname},刚生了{gender}，你帮我起个名字，简单回答"
)

model = Tongyi(model="qwen-max")  # 创建大语言模型对象

# 下面的意思为：将提示词promptTemplate放入到model中
chain = promptTemplate | model 

res = chain.invoke(input= {"lastname": "张", "gender": "女"})  # 向模型提问
print(res)  # 输出模型的回答

