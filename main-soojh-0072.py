cookie="PHPSESSID=55sso4q9hhodrhlgkdd3dbfsgi; _ga=GA1.1.1969317102.1722367504; _gcl_au=1.1.682936974.1722367504; gads=ID=aafea975587da594:T=1722367504:RT=1722367504:S=ALNI_MYD7-TxIz5Qu_cOV_h5ds-i4cypeg; gpi=UID=00000eade7336fa2:T=1722367504:RT=1722367504:S=ALNI_Mbrn1tHQSGvugxtMnvgmlrexsNpYQ; __eoi=ID=4d8197daa1427a7c:T=1722367504:RT=1722367504:S=AA-AfjYgHHMzSejjx1lhJtwsjaeb; FCNEC=%5B%5B%22AKsRol-uyfy4WQWtC6BKSAlA7mUP47qWubybhKfw1PaOB7cZfzuK4cg_xAcs8UmldjO12U1omxD81RB0BjdOdEaypZhRZH8mV6iwdTEWZAF9urq4Oz0yBLsjRd01sLCyrQNNpaQOu4HNLvN-PMS9eKLHO4HgJdTuzw%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722367503.1.1.1722367524.39.0.0"
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