@echo off
cd resources
python-3.6.4.exe /passive PrependPath=1
python -m pip install pypiwin32
echo 安装完成
pause
