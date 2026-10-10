#历史会话提示词ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi #聊天模型

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人"),    
     MessagesPlaceholder("history"), #可以为history，也可以为其他名称 
      ("human", "请再来做一首诗")   
])

#历史对话
history_data = [
    ("human", "你来写一首诗"), 
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"), 
    ("human", "你再写一首诗"), 
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"), 
]

model = ChatTongyi(model="qwen-max")

#组成链
chain = chat_prompt_template | model

#通过链取调用invoken或stream
# res = chain.invoke({"history": history_data})
# print(res.content)

#流式输出
res = chain.stream({"history": history_data})
for r in res:
    print(r.content, end="", flush=True)


### 组装链的本质：预先定义一条「可复用的流水线」
# chat_prompt_template | model 做的事情：
# 1. 把两个 Runnable 组件绑定在一起，声明好：输入进来，先走模板，再进模型；
# 2. 得到一个可复用的对象 `chain`，这个对象里面只存【流程规则】，不存任何业务数据。
#  👉 组装链阶段，不会执行任何大模型调用、不会渲染 prompt。只是搭管道，没有通水。
# - 组装链（搭管道）：chain = chat_prompt_template | model
# - 执行通水（真正跑逻辑）：chain.stream({"history": history_data})
# 如果你每次都分开写，每次都要手动写两步：先渲染 prompt，再传给模型。一旦链路变长，代码会重复、臃肿。