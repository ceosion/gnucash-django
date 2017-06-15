FROM eclipse/ubuntu_python:2.7

RUN sudo apt update && sudo apt install -y libmysqlclient-dev firefox
