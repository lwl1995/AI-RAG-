from openai import OpenAI

# 1.获取client对象，openai类对象
client = OpenAI(
    # api_key已经在系统环境变量中配置了，所以在这就隐藏了   
    base_url="https://ws-ycwxmb7d3zz9ckgu.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
# 2.调用模型
response = client.chat.completions.create(
    model="qwen3-max",  # 您可以按需更换为其它深度思考模型
    messages=[
       {"role": "system", "content": "你是一个Python编程专家"},
        {"role": "assistant", "content": "好的，我是编程专家"},
        {"role": "user", "content": "输出1-10的数字，使用python代码"}
        ],
        stream=True  # 开启流式输出（一字一字返回，类似ChatGPT打字效果）
)
# 3.获取模型返回的结果
# print(response.choices[0].message.content) 此代码未结果直接出现
# 下面为：循环读取流式返回的每一段结果，逐字打印
for chunk in response:
    print(
          chunk.choices[0].delta.content, 
          end="",   # 每一段之间以空格分隔
          flush=True# 立刻刷新缓冲区
          )