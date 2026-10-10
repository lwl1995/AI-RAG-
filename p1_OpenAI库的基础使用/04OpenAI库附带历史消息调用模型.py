from openai import OpenAI

# 1.获取client对象，openai类对象
client = OpenAI(
    # api_key已经在系统环境变量中配置了，所以在这就隐藏了 
    # api_key="sk-ws-H.PDXLPDL.xK6h.MEYCIQCRpxDm7_HWCvUK4eMbn4l39YoDPEekI4wgGAk7pf4R6wIhANEXdY4GZBFIqVt8DcLEPZPP_-jDD76pIaW2X_nfXxGB",  
    base_url="https://ws-ycwxmb7d3zz9ckgu.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
# 2.调用模型
response = client.chat.completions.create(
    model="qwen-max",  # 您可以按需更换为其它深度思考模型
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},# 用户问
        {"role": "assistant", "content": "好的"},     # 系统答
        {"role": "user", "content": "小红有3只宠物猫"},# 用户问
        {"role": "assistant", "content": "好的"},     # 系统答
        {"role": "user", "content": "总共有几个宠物？"}# 用户问
    ],
        stream=True  
)
# 3.获取模型返回的结果：循环读取流式返回的每一段结果，逐字打印
for chunk in response:
    print(
          chunk.choices[0].delta.content, 
          end="",   # 每一段之间以空格分隔 
          flush=True# 立刻刷新缓冲区
          )
