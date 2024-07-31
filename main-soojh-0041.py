cookie="PHPSESSID=1l4reate8n7r62eqi3posd944s; _ga=GA1.1.403990057.1722349739; _gcl_au=1.1.435794574.1722349739; gads=ID=0b5452de5192051d:T=1722349739:RT=1722349739:S=ALNI_MZsUBhgTnBPND6o9beb9KgE43Jiag; gpi=UID=00000eadcd0aaa09:T=1722349739:RT=1722349739:S=ALNI_MZGeTNwt1zMmcqjgnLt5FWMHmmTww; __eoi=ID=1f5ded2656858ea9:T=1722349739:RT=1722349739:S=AA-AfjbPgEKRLvC5WR-rEsmhQdAk; _ga_HPSLFXFRWN=GS1.1.1722349739.1.0.1722349743.56.0.0; FCNEC=%5B%5B%22AKsRol8nvrGUTG9YVGxIOxcrvLXk725I2SnWWNcDfSfi371TudhkNYxGs9S8EmgVU45oH1bgptmGJIHBqXtfhROE-VW6LWDCp157QM2DYQvRYXeU1giYLxWqPh5dUOQc1gCBt5hLeVa97X7E2F1bvPdo571FFB5IGw%3D%3D%22%5D%5D"
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