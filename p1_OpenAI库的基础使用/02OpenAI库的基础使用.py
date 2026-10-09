from openai import OpenAI
# openai库作用：可以调用大模型，一共有如下3个流程：

# 1.获取client对象，openai类对象
client = OpenAI(
    # api_key已经在系统环境变量中配置了，所以在这就隐藏了   
    # api_key="sk-ws-H.PDXLPDL.xK6h.MEYCIQCRpxDm7_HWCvUK4eMbn4l39YoDPEekI4wgGAk7pf4R6wIhANEXdY4GZBFIqVt8DcLEPZPP_-jDD76pIaW2X_nfXxGB",
    base_url="https://ws-ycwxmb7d3zz9ckgu.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    messages=[
       {"role": "system", "content": "你是一个Python编程专家，并且不说废话简单回答"},# system：设定助手的整体行为、角色和规则，为对话提供上下文框架（如指定助手身份、回答风格、核心要求），是全局的背景设定，影响后续所有交互
        {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},# assistant：代表ai助手的回答，可以人为在代码中设定
        {"role": "user", "content": "输出1-10的数字，使用python代码"}# user：代表用户的问题或输入
        ]
)
# 3.获取模型返回的结果
print(response.choices[0].message.content)