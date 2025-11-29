
## 环境搭建

在终端检查Python版本号:
```Terminal
% python --version
Python 3.13.5
```

查看Python的位置:
```Terminal
% which python
/opt/anaconda3/bin/python
```

创建venv虚拟环境：
```Terminal
% python -m venv .venv
```

## 激活虚拟环境

使用venv激活虚拟环境：
```Terminal
% source .venv/bin/activate
```

## 创建依赖文件requirements.txt

### 方式一: 根据需要,安装需要的依赖包
1. 在虚拟环境中安装openai库：
```Terminal
% pip install ollama
```

如果是pip环境,直接导出依赖：
```Terminal
% pip freeze > requirements.txt
```

### 方式二: 从requirements.txt安装依赖
1. 确保虚拟环境已激活,并将需要的依赖包列表放在requirements.txt文件中
2. 然后执行：
```Terminal
% pip install -r requirements.txt
``` 

## 运行Python脚本

1. 确保虚拟环境已激活
2. 执行：
```Terminal
% python local_api_call.py
```

## 实验报告提交要求

1. 按照以上内容，根据[实验报告模板](/exp_private_deploy/实验报告_学号-姓名.md)的要求完成实验并撰写实验报告；
2. 提交报告文件格式：Markdown格式（[实验报告_学号-姓名.md](/exp_private_deploy/实验报告_学号-姓名.md)，实验报告的文件名填入学号和姓名）；
3. 提交至：学习通作业。
4. ⚠️注意：敏感信息应该匿名处理，例如API key，可以用“MY_API_KEY”替换，并在适当位置添加注释。
