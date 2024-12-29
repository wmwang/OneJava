# 使用 OpenJDK 15 作为基础镜像
FROM openjdk:15

# 设置容器的工作目录
WORKDIR /app

# 将脚本添加到容器中 (可选)
COPY run-java.sh /app/run-java.sh

# 确保脚本可执行
RUN chmod +x /app/run-java.sh

# 设置默认命令
CMD ["/app/run-java.sh"]


## docker build -t java15-runner .
## docker run --rm -v /path/to/java-files:/host-java-files java15-runner

