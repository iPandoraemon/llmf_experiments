from ollama import chat
from ollama import ChatResponse

# 创建聊天完成请求
def chat_with_llm(prompt, model="qwen3:8b"):
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response['message']['content']

# 调用示例
if __name__ == "__main__":
    response = chat_with_llm("解释什么是大模型量化")
    print(response)
