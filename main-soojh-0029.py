cookie="PHPSESSID=ajeqrat89b8j66sim28j5mht08; _ga=GA1.1.1521716561.1722342475; _gcl_au=1.1.68401307.1722342475; gads=ID=3448e11e9abf86db:T=1722342476:RT=1722342476:S=ALNI_MaH0RLpBQXr9UB1CLwsKuydHBToZQ; gpi=UID=00000eadbc5a85df:T=1722342476:RT=1722342476:S=ALNI_MbXQ_1t5Zrz9d1Hdpv6Jgl-xX7h1Q; __eoi=ID=2f484a45368f085d:T=1722342476:RT=1722342476:S=AA-AfjYOsRGmrdZqCQTeJQkn89Mw; _ga_HPSLFXFRWN=GS1.1.1722342474.1.0.1722342483.51.0.0; FCNEC=%5B%5B%22AKsRol-3OOXWrewQvcuNY2w2LUAE8krbP3GqH4oHkycg_ObHe5UD2--QhfxntTjRHSZ6Y6ujmuoQWrDTw-wnEK9cm-ZGe0j6Kzc6dW7SocxdS9kpXgzYdr2ObLXG3kCWAkNXDp48fk9w6n9FIoSu5Uj1rw0Ua3H_Mg%3D%3D%22%5D%5D"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
@st.cache_data
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
	
	        #st.write(response.text)
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
	        #st.write(s)
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