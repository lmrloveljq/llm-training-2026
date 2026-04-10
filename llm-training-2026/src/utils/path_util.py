import os
from pathlib import Path
current_path=os.path.abspath(__file__)
print("这个文件的绝对路径是：",current_path)
print("这个文件的上一级文件夹是：",os.path.dirname(__file__))
current_path=os.path.dirname(current_path)
root_path=os.path.dirname(current_path)
data_dir=os.path.join(root_path,'data')
log_dir=os.path.join(root_path,'logs')
os.makedirs(data_dir,exist_ok=True)
os.makedirs(log_dir,exist_ok=True)
__all__=["root_path","data_dir","log_dir"]