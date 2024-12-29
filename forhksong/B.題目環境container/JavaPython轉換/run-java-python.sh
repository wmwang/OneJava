#!/bin/bash

# 检查是否挂载了宿主机文件夹
if [ -z "$(ls /host-files 2>/dev/null)" ]; then
  echo "未找到任何挂载的文件夹。请确保正确挂载。"
  exit 1
fi

# 编译并运行 Java 文件
for java_file in /host-files/*.java; do
  if [ -f "$java_file" ]; then
    echo "编译 Java 文件: $java_file"
    javac "$java_file"
    # 提取类名并运行
    class_name=$(basename "$java_file" .java)
    echo "运行 Java 类: $class_name"
    java -cp /host-files "$class_name"
  fi
done

# 检测并运行 Python 文件
for python_file in /host-files/*.py; do
  if [ -f "$python_file" ]; then
    echo "运行 Python 文件: $python_file"
    python3 "$python_file"
  fi
done
