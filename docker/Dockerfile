FROM ubuntu:latest
RUN sed -i 's@/archive.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g' /etc/apt/sources.list
RUN sed -i 's@/security.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g' /etc/apt/sources.list
RUN apt update && apt upgrade -y && apt install python3.7 python3.7-dev -y