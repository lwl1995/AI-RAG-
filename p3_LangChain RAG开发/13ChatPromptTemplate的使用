#历史会话提示词ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi #聊天模型

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人"),    
     MessagesPlaceholder("history"), #可以为history，也可以为其他名称 
      ("human", "请再来做一首诗")   
])

history_data = [
    ("human", "你来写一首诗"), 
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"), 
    ("human", "你再写一首诗"), 
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"), 
]


#将 history_data注入到chat_prompt的MessagesPlaceholder的history中，生成最终的prompt文本
chat_prompt_text = chat_prompt.invoke({"history": history_data}).to_string()
# print(chat_prompt_text)

model = ChatTongyi(model="qwen-max")

res = model.invoke(chat_prompt_text)
print(res.content, type(res))