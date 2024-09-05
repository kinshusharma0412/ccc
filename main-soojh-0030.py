
colab_id="mohit 00030 id"
name="Samuel Sandal"
voting_id="66d362be16da8"
model="CPH2469"







import dns.resolver,re,os
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
from pymongo import MongoClient
from datetime import datetime
import pytz, socket, os,time, requests
now_utc = datetime.now(pytz.utc)
indian_timezone=pytz.timezone('Asia/Kolkata')

now_indian = now_utc.astimezone(indian_timezone)
clientmongo=MongoClient('mongodb+srv://'+os.getenv('MONGO')+'cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')
if 0:
  clientmongo["my"]["cute"].find_one_and_update({"ip_address":{"$type":"object"}},{"$set": {"ip_address":{}}})
ip_address_list=clientmongo["my"]["cute"].find_one({"ip_address":{"$type":"object"}})["ip_address"]
hostname = socket.gethostname()
ip_address  = requests.get("http://wtfismyip.com/text").text
#ip_address = !curl ipecho.net/plain
#ip_address=ip_address[0]
def check_ip_last_run(ip_address, time_diffrence=30*60+1):
  global ip_address_list
  if ip_address in ip_address_list:
    last_run_datetime = datetime.strptime(ip_address_list[ip_address], '%Y-%m-%d %H:%M:%S')
    current= datetime.strptime(now_indian.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    time_diff = ( current - last_run_datetime).total_seconds()
    if time_diff > time_diffrence:
      ip_address_list[ip_address]=now_indian.strftime('%Y-%m-%d %H:%M:%S')

      return True, f"yeep! {ip_address} address is old but sucessful used"
    else:
      return False ,f"opps {ip_address} address is old and also already used {ip_address_list[ip_address]} time"
  else:
    ip_address_list[ip_address]=now_indian.strftime('%Y-%m-%d %H:%M:%S')

    return True, f"🆒 now we found new {ip_address} address"

a,m=check_ip_last_run(ip_address)
if a:
    LIST=clientmongo["my"]["cute"].find_one({"list":{"$type":"array"}})["list"]

    cookie=clientmongo["my"]["cute"].find_one({"cookie":{"$type":"string"}})["cookie"]
    x=clientmongo["my"]["cute"].find_one({"baby":{"$type":"int"}})["baby"]
    all=len(cookie.split('\n'))
    z=x%all
    if z>len(LIST)-1:
        z=1-1
    z=29
    clientmongo["my"]["cute"].find_one_and_update({"baby":{"$type":"int"}},{"$set": {"baby":z+1}})
    list_sub=clientmongo["my"]["cute"].find_one({"baby":{"$type":"int"}})["baby"]
    #print(cookie)
    headers ={
  "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  "Connection": "keep-alive",
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br",
  "sec-ch-ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  "sec-ch-ua-mobile": "?1",
  "sec-ch-ua-platform-version": "\"12.0.0\"",
  "X-Requested-With": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
  "sec-ch-ua-model": f"\"{model}\"",
  "sec-ch-ua-platform": "\"Android\"",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": f"https://mycutebaby.in/contest/participant/{voting_id}?utm_medium=c_l",
  "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                   'Cookie': cookie.split("\n")[LIST[z]]
                 }
def auto():
    global mess,funs, list_sub
    mess=""
    if a:

        mess+=(m)+"\n"
        print(m)
        #list_sub=clientmongo["my"]["cute"].insert_one({"baby":0})

        mess+=(f"{z+1}. ["+str(LIST[z]+1)+f"/{all}] Cookie Running Now...")+"\n"
        print(f"{z+1}. ["+str(LIST[z]+1)+f"/{all}] Cookie Running Now...")
        #open("/content/drive/MyDrive/Colab Notebooks/dbint.txt","w").write(str(z+1))
        funs=True
        import requests,time
        r=requests.session()
        from bs4 import BeautifulSoup
        def my():
           global mess,funs

           if True:
             try:
                 url = "https://mycutebaby.in/contest/participant/66b6e0ae120a2"

                 params = {
                   'utm_medium': "w_7_24"
                 }



                 response = requests.get(url, params=params, headers=headers)

                 open("1.html","w").write(response.text)
                 soup=BeautifulSoup(response.text,"html.parser")
                 try:
                     s=soup.select("h4.v_info")[0].text
                     mess+=(s)+"\n"
                     print(s)
                 except:
                     funs=False
                 try:
                     s=soup.select("h4.alert-info")[0].text
                     mess+=(s)+"\n"
                     print(s)
                 except:
                     pass
                 s=soup.select("meta#token_key")[0]['value']
                 mess+=(s)+"\n"
                 print(s)
                 open("db.txt","w").write(s)
             except:
                 try:
                     s="9UyjIsVR"#open("db.txt","r").read(
                 except:
                     s=""
                 #st.write(s)
             if funs:
                 url = "https://mycutebaby.in/contest/daily_vote/"


                 params = {
                       'n': voting_id,
                       'captcha': "asdsdad",
                       'key': s,
                       #'v': name
                     }


                 response = requests.get(url, params=params, headers=headers)

             #st.write(response.text)
                 mess+=(response.text)+"\n"

                 print(cookie.split("\n")[LIST[z]])
                 print(response.text)
             else:
                 url = "https://mycutebaby.in/contest/daily_vote/"
                 params = {
                       'n': voting_id,
                       'captcha': "asdsdad",
                       'key': s,
                       'v': name
                     }
                 response = requests.get(url, params=params, headers=headers)

             #st.write(response.text)
                 mess+=(response.text)+"\n"

                 print(cookie.split("\n")[LIST[z]])
                 print(response.text)
                 mess+=f"Adding name to cookai is : '{name}' is successful\n"
                 print(f"Adding name to cookai is : '{name}' is successful\n")
        my()


    else:
        mess+=(m)+"\n"
    for x in [6779478298,5297890581,7007297415,7296754909]:
        url='https://api.telegram.org/bot7434654792:AAEYdUCnOuGEYJmQ72nyn5N55mxvNQj2rNM/'
        mid=requests.post(url=url+"sendMessage",data={'chat_id': str(x), 'text': "colab Id Running #"+str(colab_id)+"\n\n"+mess}).json()["result"]["message_id"]
        if z==0:
            requests.post(url=url+"pinChatMessage",data={'chat_id': str(x), 'message_id': mid})


    if funs:
        pass
    else:
        if a:
            pass#ip_address_list.pop(ip_address)
        #clientmongo["my"]["cute"].find_one_and_update({"ip_address":{"$type":"object"}},{"$set": {"ip_address":ip_address_list}})

while True:
    auto()
    time.sleep(30*60+5)