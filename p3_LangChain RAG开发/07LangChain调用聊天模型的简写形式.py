from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 得到模型对象，qwen3-max就是聊天模型
model = ChatTongyi(model="qwen3-max")

#准备消息列表
messages = [ 
    # SystemMessage(content="你是一个边塞诗人"),
    # HumanMessage(content="写一首唐诗"),
    # AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。") ,
    # HumanMessage(content="按照你上一个回复的格式，再写一首唐诗")

    # 将上述聊天内容进行简写，简写的格式为（角色, 内容），角色只能分为三种：system、human、ai
    ("system","你是一个边塞诗人"),
    ("human","写一首唐诗"),
    ("ai","锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。") ,
    ("human","按照你上一个回复的格式，再写一首唐诗")

]               

#调用stream方法进行流式输出
res = model.stream(input=messages) # 向模型提问

#for循环迭代打印输出，通过.content属性获取消息内容
for chunk in res:
    print(chunk.content, end="", flush=True)  # 输出模型的回答