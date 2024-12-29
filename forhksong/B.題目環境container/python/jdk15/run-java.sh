#!/bin/bash

# 检查是否挂载了 host 文件夹
if [ -z "$(ls /host-java-files)" ]; then
  echo "未找到任何挂载的 Java 文件夹。请确保正确挂载。"
  exit 1
fi

# 编译所有 Java 文件
javac /host-java-files/*.java

# 找到包含 main 方法的 Java 文件并运行
MAIN_CLASS=$(grep -lr "public static void main" /host-java-files | sed 's/.*\/\(.*\)\.java/\1/')
if [ -n "$MAIN_CLASS" ]; then
  echo "运行主类: $MAIN_CLASS"
  java -cp /host-java-files $MAIN_CLASS
else
  echo "未找到包含 main 方法的 Java 文件。"
fi
