cookie="PHPSESSID=67ps77os0u1a840rs12kl6rbva; _ga=GA1.1.1991488544.1722222143; _gcl_au=1.1.959035380.1722222143; gads=ID=bf160aa16c8286fb:T=1722222147:RT=1722222147:S=ALNI_MZk1Y1yB16Dd0V6e1PITlumacMB_w; gpi=UID=00000eab513eac9c:T=1722222147:RT=1722222147:S=ALNI_Mb5eVnhErhs3VhYrZW8p6a9Sa0UEw; __eoi=ID=b88b9bfeaa971206:T=1722222147:RT=1722222147:S=AA-AfjYbF3RvZEJUBKU5bJBUTDNQ; _ga_HPSLFXFRWN=GS1.1.1722222142.1.1.1722222173.29.0.0; FCNEC=%5B%5B%22AKsRol88ZkPQT9K7fgljIX59Spk_WikYhDqOOd248dDqS-d8G_UBCfHUH0cEJASvRTMIdY1M5YItMnLS3kCiaW9rD6qTnjSVmW2h9QAICF6TAMVx4Auni37r8VRKjrUDKc-5-UNAdmOX6Ohpk4A7OHQ8xQxsylh9Xg%3D%3D%22%5D%5D"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
#@st.cache_data
def my():
	while True:
	    try:
	        url = "https://mycutebaby.in/contest/participant/669bc381bf80d"
	
	        params = {
	          'utm_medium': "w_7_24"
	        }
	
	        headers = {
	          'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	          'Cookie': cookie
	        }
	
	        response = requests.get(url, params=params, headers=headers)
	
	        ##st.write(response.text)
	        soup=BeautifulSoup(response.text,"html.parser")
	        try:
	            s=soup.select("h4.v_info")[0].text
	            st.write(s)
	            print(s)
	        except:
	            pass
	        s=soup.select("meta#token_key")[0]['value']
	        st.write(s)
	        print(s)
	        open("db.txt","w").write(s)
	    except:
	        try:
	            s="9UyjIsVR"#open("db.txt","r").read(
	        except:
	            s=""
	        st.write(s)
	    url = "https://mycutebaby.in/contest/daily_vote/"
	
	
	    params = {
	              'n': "669bc381bf80d",
	              'captcha': "asdsdad",
	              'key': s,
	              'v': "Sharma ab"
	            }
	    headers = {
	              'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	            #  'Accept-Language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	              'Referer': "https://mycutebaby.in/contest/participant/669bc381bf80d",
	            #  'Sec-Fetch-Dest': "empty",
	            #  'Sec-Fetch-Mode': "cors",
	            #  'Sec-Fetch-Site': "same-origin",
	              'X-Requested-With': "XMLHttpRequest",
	            #  'sec-ch-ua': ""Not-A.Brand";v="99", "Chromium";v="124"",
	            #  'sec-ch-ua-full-version-list': ""Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"",
	            #  'sec-ch-ua-mobile': "?1",
	            #  'sec-ch-ua-model': ""M2102J20SI"",
	            #  'sec-ch-ua-platform': ""Android"",
	            #  'sec-ch-ua-platform-version': ""12.0.0"",
	              'Cookie': cookie
	            }
	
	    response = requests.get(url, params=params, headers=headers)
	
	    st.write(response.text)
	    print(response.text)
	    time.sleep(5*60)
my()