# 实验: 大模型的文本情感分类

## 1. 实验目的

采用本地化部署或API调用的大模型, 设计提示词, 完成中文文本的情感分类任务, 分析影响大模型的情感分类任务的因素

## 2. 创建虚拟环境

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

## 3. 下载数据集

数据集: 简体中文口语情感分类数据集

### 3.1 下载方式一: 打开链接, 手动下载

链接:[https://www.modelscope.cn/datasets/zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/files](https://www.modelscope.cn/datasets/zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/files)

注意将csv文件保存到`data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset`路径

### 3.2 下载方式二: 命令行下载


```terminal
modelscope download --dataset zhangzhihao/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset --local_dir data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset
```

## 4. 大模型分类实验内容

采用本地化部署大模型或API调用大模型, 完成中文语义情感分类任务, 分析提示词设计技巧, 分析模型的分类任务性能

### 4.1 如果是Ollama本地部署的模型

以 `local_emotion_cls.py` 脚本为基准, 设计一个函数 `evaluate_result`, 能够将大模型的分类结果, 跟原始数据集 `data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset.csv` 中的 `label` 列进行比较, 得出分类的准确率

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

### 4.2 如果是API调用模型

⚠️这种方式花钱, 建议采用本地部署

同上, 以 `api_emotion_cls.py` 脚本为基准, 设计一个函数 `evaluate_result`, 能够将大模型的分类结果, 跟原始数据集 `data/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset/Simplified_Chinese_Multi-Emotion_Dialogue_Dataset.csv` 中的 `label` 列进行比较, 得出分类的准确率

## 5. 实验要求

1. 完成大模型分类任务, 保存大模型分类的输出结果, 保存为 `llm_cls_responses.csv`, 表包含三列, 列名必须是: 
   - `label`: 原始数据的分类标签
   - `llm1_cls`: 模型1的分类标签
   - `llm2_cls`: 模型2的分类标签
2. 根据 `llm_cls_responses.csv`, 计算模型的分类准确率
3. 分析影响模型分类准确率性能的原因
4. 分析提示词设计对大模型结构化输出的影响
5. 使用[exp_prompt_emotion_cls/实验报告_学号-姓名.md](exp_prompt_emotion_cls/实验报告_学号-姓名.md), 完成实验报告的撰写并提交
6. 实验报告提交到学习通, 作业含2个文件 (不打包):
   - 实验报告_学号-姓名.md  (❗️在文件名中填入您的学号和姓名)
   - llm_cls_response.csv
