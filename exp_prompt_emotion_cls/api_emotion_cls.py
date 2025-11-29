import os
import pandas as pd
from openai import OpenAI

# 以下是OpenRouter的免费模型，如果需要用其他平台的，你可以设计自己的模型列表
# 例如，硅基流动的模型列表，SILICONFLOW_MODELS
# 注意：免费的模型，平台可能会做限流
OPENROUTER_MODELS = [
    "qwen/qwen3-coder:free",
    "qwen/qwen3-4b:free",
    "qwen/qwen3-235b-a22b:free"
]

# 在终端执行: export OPENROUTER_API_KEY=你的API KEY
# 然后在代码中调用，以OpenRouter为例: os.environ.get("OPENROUTER_API_KEY")
# 这样就可以避免将API KEY明文写在代码中
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key: # 如果环境变量未设置，则抛出异常
    raise RuntimeError("环境变量 OPENROUTER_API_KEY 未设置，请先在终端中 export。")

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',   # 模型平台，根据实际使用修改
    api_key=api_key  # 调用本机环境变量中的API KEY
)

def chat_with_llm(prompt, model=OPENROUTER_MODELS[0], stream=False):       
    # 发送带有流式输出的请求
    if stream:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", 
                "content": prompt}
            ],
            stream=True  # 启用流式输出
        )
        # 逐步接收并处理响应
        for chunk in response:
            if not chunk.choices:
                continue
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
            if chunk.choices[0].delta.reasoning_content:
                print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
            return response
    else:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", 
                "content": prompt}
            ]
        )
        return response


def main():
    dataset = pd.read_csv('data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset.csv')
    for index, row in dataset.iterrows():
        dialogue = row['text']
        label = row['label']
        print(f"\n原文: {dialogue}, 真实标签: {label}")
        prompt = """
           你是一个情感分类器，请根据以下对话内容，判断对话者的情感类别。
           对话内容: {dialogue}
           情感类别: {emotion_classes}
        """
        response = chat_with_llm(prompt)
        
        if index > 10:
            break
    
    return response


if __name__ == "__main__":
    main()
    
