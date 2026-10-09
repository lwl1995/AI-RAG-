# 使用前得需要提前将ollama启动

# 导入OpenAI官方SDK包
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    # base_url：把请求地址改成阿里云本地ollama大模型固定地址
    base_url="http://localhost:11434/v1", 
   
)

# 发起对话请求
completion = client.chat.completions.create(
    # model：指定模型名称
    model="qwen3:4b",
    # 对话上下文，system角色设定助手身份，user是用户提问
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁，能做什么？"},
    ],
    stream=True  # 开启流式输出（SSE，一字一字返回，类似ChatGPT打字效果）
)

# 循环读取流式返回的每一段结果，逐字打印
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)