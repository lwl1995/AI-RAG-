#  langchain_cummunity
from langchain_community.llms.tongyi import Tongyi

#不用qwen3-max模型，因为qwen3-max模型为聊天对话模型，使用qwen-max大语言模型
#Tongyi类的参数说明：
# model: 模型名称，api_key为API密钥(因为在环境变量中配置了，所以在这里隐藏了api_key。
model = Tongyi(model="qwen-max") 

#调用invoke方法，向模型提问
res = model.invoke(input = "你是谁呀")
print(res)  # 输出模型的回答