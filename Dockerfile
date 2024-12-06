FROM python:3.10-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git wget ffmpeg libsndfile1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码文件
COPY . .

# 暴露端口
EXPOSE 8089

# 启动 Flask 应用
CMD ["python", "app.py"]