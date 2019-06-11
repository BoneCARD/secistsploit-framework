FROM python:3
RUN sed -i 's@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g' /etc/apt/sources.list
RUN sed -i 's@/security.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g' /etc/apt/sources.list
RUN apt-get update && apt-get -y install git procps
COPY .devcontainer/.pip /root/.pip
RUN mkdir /workspace
WORKDIR /workspace
RUN pip install pylint
COPY .devcontainer/requirements.txt.temp requirements.txt* /workspace/
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt*; fi
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV SHELL /bin/bash