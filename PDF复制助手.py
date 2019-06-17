import main
import requests
import tkinter.messagebox
import re

version = 1.3
# base_url = "http://localhost:8899"
base_url = "http://106.14.182.45:8899"

try:
    text=requests.get("http://txt.go.sohu.com/ip/soip").text
    ip=re.findall(r'\d+.\d+.\d+.\d+',text)
    requests.post(base_url+'/signin',data={"ip":ip})
except:
    tkinter.messagebox.showerror("错误", "服务器连接失败，请检查网络连接，或联系qiubinyang98@163.com修复")
    exit()

new_version = requests.get(base_url+'/get_version')
if float(new_version.text) != version:
    tkinter.messagebox.showinfo("更新",requests.get(base_url+'/message').text)
    exit()

main = main.main().show()