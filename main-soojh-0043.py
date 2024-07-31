cookie="PHPSESSID=48drht3sldd9jmeak0q6tcgp37; _ga=GA1.1.131684793.1722350790; _gcl_au=1.1.57549256.1722350790; gads=ID=e824a08c219d2b4e:T=1722350790:RT=1722350790:S=ALNI_MZRycGflwoqDy8xh5tBIRjXrQfaMQ; gpi=UID=00000ebc97378726:T=1722350790:RT=1722350790:S=ALNI_MbQVuNQx42X4HHlXtivFYOl4Fjq6A; eoi=ID=e800a1cc7b3d4112:T=1722350790:RT=1722350790:S=AA-AfjaCq2TLw489ISwqACdSZT4A; _ga_HPSLFXFRWN=GS1.1.1722350789.1.1.1722350798.51.0.0; FCNEC=%5B%5B%22AKsRol8jHXMhSGvx7yu-4YzprzLC2ERMkucsm_Sao6mw0L-8VbmGdeGsMIMEUWnUEthcJKyWI7OTHNfkKuovao3NQp_wZJc4cmqoLsihGaVJmHW7mYFijiKHzV70y0-WLB2HPe3Sv_KNyvQZIovxzM2esfkcZdaw%3D%3D%22%5D%5D"
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