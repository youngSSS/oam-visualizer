#!/bin/bash

# sh 파일의 절대경로
path=$(cd "$(dirname "$0")"; pwd)
cd $path

# 가상환경 진입
source $path/venv/bin/activate

# Python 실행
python3 parser.py

# uml output 폴더 진입
cd ./result

# uml output 파일 실행
plantuml yaml_data.uml

# 결과
open OAM.png
