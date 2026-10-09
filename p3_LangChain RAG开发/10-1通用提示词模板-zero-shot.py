#导入通用提示词类模板(在zero-shot思想下，可以使用PromptTemplate)，few-shot思想下，需要更换为FewShotPromptTemplate(后续学习)
from langchain_core.prompts import PromptTemplate #导入通用提示词类模板
from langchain_community.llms.tongyi import Tongyi #导入大语言模型类

promptTemplate = PromptTemplate.from_template(
        "我的邻居姓{lastname},刚生了{gender}，你帮我起个名字，简单回答"
)

#调用.format方法注入信息即可
prompt_text = promptTemplate.format(lastname="张", gender="女")

model = Tongyi(model="qwen-max")  # 创建大语言模型对象

res = model.invoke(input=prompt_text)  # 向模型提问

print(res)  

