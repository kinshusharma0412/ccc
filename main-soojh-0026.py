cookie="PHPSESSID=nmmt0uhv7pcbcssv3f8hmiokmt; _ga=GA1.1.506881778.1722339142; _gcl_au=1.1.1745465135.1722339142; gads=ID=e7a03a041d104eb1:T=1722339144:RT=1722339614:S=ALNI_MaF5f2srIE_GyXWanGIrSFmQIT6DA; gpi=UID=00000eadb421346e:T=1722339144:RT=1722339614:S=ALNI_MaxuQoEsOsh3AG1QXB0MPA7ojvm_Q; __eoi=ID=beb3cdf74f908301:T=1722339144:RT=1722339614:S=AA-AfjakcA-MvZBIbry-Xn-K1Gh_; FCNEC=%5B%5B%22AKsRol8whvTYzbC-X5ZuphH8QitRNZ0-vFsox16fj4r_I65TFMfryzEVrK4_V6U43U2esG7-NlYwB5o278zW3dkCYKKS2yDLCoVW4bHtQP7YRmVwg2whGQalYT8GAfDvBJ8Mu3SpGDMkN5wkV2D6o9ltOhvb3BNtAw%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722339141.1.1.1722339679.60.0.0"
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