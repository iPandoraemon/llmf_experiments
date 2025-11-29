

## 1. 创建虚拟环境

用VS code或 (Code-based的IDE, 以下简称"Code")打开本实验的文件夹, 在Code中打开终端, 创建虚拟环境
```terminal
python -m venv .venv
```

激活虚拟环境
```terminal
source .venv/bin/activate
```

安装所需的依赖包
```terminal
pip install -r requirements.txt
```

## 2. 下载数据集

数据集: 简体中文口语情感分类数据集

### 下载方式一: 打开链接, 手动下载

链接:[https://www.modelscope.cn/datasets/zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/files](https://www.modelscope.cn/datasets/zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/files)

注意将csv文件保存到`data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset`路径

### 下载方式二: 命令行下载


```terminal
modelscope download --dataset zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset --local_dir data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset
```

## 如果是Ollama本地部署的模型

那么, 可以参考`local_emotion_cls.py`demo脚本, 设计一个函数`evaluate_result`, 能够将大模型的分类, 跟原始数据集`data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset.csv`中的`label`列进行比较, 得出分类的准确率

分类准确率计算公式:
$$Accuracy = \frac{分类结果匹配label的个数}{总样本}$$

模型选用: 根据自己的机子性能, 选用2个模型进行实验, 可以从以下模型选用 (但不限于):
- `qwen:0.6b`
- `qwen:1.7b`
- `qwen:4b`
- `qwen:8b`
- `qwen:14b`
- `qwen:30b`

建议两个模型的参数量区别大一点, 例如选用: `qwen:0.6b`和`qwen:4b`, 以确保实验能够较容易的体现模型参数量对性能的提升

## 如果是API调用模型

⚠️这种方式花钱, 建议采用本地部署
