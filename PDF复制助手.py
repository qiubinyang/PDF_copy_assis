import main
import requests
import tkinter.messagebox
import re
import pickle

version = 1.3
# base_url = "http://localhost:8899"
base_url = "http://106.14.182.45:8899"

# try:
#     text=requests.get("http://txt.go.sohu.com/ip/soip").text
#     ip=re.findall(r'\d+.\d+.\d+.\d+',text)
#     requests.post(base_url+'/signin',data={"ip":ip})
# except:
#     tkinter.messagebox.showerror("错误", "服务器连接失败，请检查网络连接，或联系qiubinyang98@163.com修复")
#     exit()
#
# new_version = requests.get(base_url+'/get_version')
# if float(new_version.text) != version:
#     tkinter.messagebox.showinfo("更新",requests.get(base_url+'/upgrade_message').text)
#     exit()

# 配置文件
config = {
    "show_broadcast_message": 1 # 是否展示发布广播，只有第一次展示
}
try:
    with open('config','rb') as f:
        config = pickle.load(f)
except IOError:
    with open('config','wb') as f:
        pickle.dump(config,f)

main = main.main().show()