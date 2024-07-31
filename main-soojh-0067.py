cookie="PHPSESSID=blj0t11jp8251ujcboeq67889u; _ga=GA1.1.754369253.1722358512; _gcl_au=1.1.970261734.1722358512; popup_fb=yes; gads=ID=b1676cfd5a3b9841:T=1722358531:RT=1722363499:S=ALNI_MYOSjdg5c-j30_E-kEtIpN3TbfALw; gpi=UID=00000eaddeff2b09:T=1722358531:RT=1722363499:S=ALNI_MaUHM7UFW37ZlrCIYeRLQ_Oqd4qsQ; __eoi=ID=4c9ec12f95ed43cb:T=1722358531:RT=1722363499:S=AA-Afja8eCmyWvugE9p-JarD02_-; _ga_HPSLFXFRWN=GS1.1.1722363495.5.1.1722363644.44.0.0; FCNEC=%5B%5B%22AKsRol8pzzQmYgMrKqvIp0Qi4-oktkk61TBZQH4m-iNTITmW77xOPcJNhZhRS3fuxD94UlJdrI9FsfenppomgANRC4aediXRIh-MLGD6xkiajlxP2Wr65S5Gjp2HkQRWKS0T84iwWv6dg03Br-bhPkpaDVq2VlIljw%3D%3D%22%5D%5D"
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