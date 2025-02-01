# 使用最新的 Eclipse Temurin JDK 21 作為基底映像
FROM ubuntu:20.04

# 安裝 JDK 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --config java

# 安裝 JDK 21
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives --config java

# 設置預設 JDK (可根據需要修改)
ENV JAVA_HOME /usr/lib/jvm/java-21-openjdk-arm64 # 或其他 JDK 路徑
ENV PATH $JAVA_HOME/bin:$PATH

# 安裝 Python 3
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python2 python3 && \
    rm -rf /var/lib/apt/lists/*
# 設置工作目錄
WORKDIR /app

# 複製編譯後的 JAR 檔案到容器內部
COPY JavaCompileController-0.0.1-SNAPSHOT.jar app.jar

# 暴露 8080 端口
EXPOSE 8080

# 運行 Spring Boot 應用
CMD ["java", "-jar", "app.jar"]
