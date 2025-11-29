from ollama import chat
from ollama import ChatResponse
import pandas as pd

EMOTION_CLASSES = [
    '伤心',
    '生气',
    '关心',
    '惊讶',
    '开心',
    '平静',
    '厌恶'
]

MODELS = ["qwen3:0.6b", "qwen3:8b"]


# 创建聊天完成请求
def chat_with_llm(prompt, model="qwen3:0.6b"):  
    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response['message']['content']

# 
if __name__ == "__main__":
    dialogue_dataset = pd.read_csv('data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset.csv')
    for index, row in dialogue_dataset.iterrows():
        dialogue = row['text']
        label = row['label']
        
        # 提示词需优化
        prompt = """
           你是一个情感分类器，请根据以下对话内容，判断对话者的情感类别。
           对话内容: {dialogue}
           情感类别: {emotion_classes}
        """
        
        response = chat_with_llm(prompt)
        print(f"[{label}]{dialogue}\n{response}\n")
