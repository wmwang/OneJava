# 使用 Java 18 作為基礎鏡像
FROM openjdk:18-slim

# 設定工作目錄
WORKDIR /app

# 安裝 Python 3 和必要的套件
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 確認 Java 和 Python 版本
RUN java -version && \
    python3 --version

# 将运行脚本添加到容器中
COPY run-java-python.sh /app/run-java-python.sh

# 确保运行脚本可执行
RUN chmod +x /app/run-java-python.sh

# 默认运行脚本
CMD ["/app/run-java-python.sh"]



## docker run --rm java-python-runner java -version 
## docker build -t java-python-runner .
## docker run --rm -v ./code:/host-java-files java-python-runner

