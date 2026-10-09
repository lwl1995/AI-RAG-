# 优先使用apikey调用线上云模型，ollama本地大模型作为备用
from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    # api_key已经在系统环境变量中配置了，所以在这就隐藏了api_key="sk-ws-H.PDXLPDL.xK6h.MEYCIQCRpxDm7_HWCvUK4eMbn4l39YoDPEekI4wgGAk7pf4R6wIhANEXdY4GZBFIqVt8DcLEPZPP_-jDD76pIaW2X_nfXxGB",
    base_url="https://ws-ycwxmb7d3zz9ckgu.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "你能做什么"}]
completion = client.chat.completions.create(
    model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    if not chunk.choices: 
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)