# 使用官方 OpenJDK 8 镜像作为基础镜像
FROM openjdk:8-jdk

# 设置容器的工作目录
WORKDIR /app

# 将运行脚本添加到容器中（可选）
COPY run-java.sh /app/run-java.sh

# 确保运行脚本可执行
RUN chmod +x /app/run-java.sh

# 设置默认命令
CMD ["/app/run-java.sh"]



## docker build -t java8-runner .
## docker run --rm -v ./code:/host-java-files java8-runner

