# 使用官方 OpenJDK 8 镜像作为基础镜像
FROM openjdk:18-jdk

# 设置容器的工作目录
WORKDIR /app

# 将运行脚本添加到容器中（可选）
COPY run-java.sh /app/run-java.sh

# 确保运行脚本可执行
RUN chmod +x /app/run-java.sh

# 设置默认命令
CMD ["/app/run-java.sh"]


## docker run --rm java18m-runner java -version 
## docker build -t java18m-runner .
## docker run --rm -v ./code:/host-java-files java18m-runner

