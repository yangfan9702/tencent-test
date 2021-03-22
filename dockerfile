#!/bin/bash

FROM python:3.7-slim

WORKDIR /


COPY . /

RUN chmod +x /run.sh \
&& pip install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


CMD ["./run.sh"]