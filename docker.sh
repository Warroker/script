#!/usr/bin/bash
docker run -itd \
    --gpus all \
    --ipc=host \    
    --name train \                              #docker名称 需要自己修改
    -p 39622:22 \                               # 映射端口号 需要自己修改
    nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04 # 版本镜像   需要自己修改 最好找devel版本
