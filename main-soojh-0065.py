cookie="PHPSESSID=6h977vt1dqodq2pb53k2otfh7q; _ga=GA1.1.1627831417.1722362247; _gcl_au=1.1.770318529.1722362247; gads=ID=e5cc992cf0fa804d:T=1722362247:RT=1722362247:S=ALNI_MZDu7HUocCM_buBTW3cAdeVwZqMjQ; gpi=UID=00000eade38f0a3a:T=1722362247:RT=1722362247:S=ALNI_MZwPXgqxNP2Fn8XyGry-8ISfz3ptw; __eoi=ID=192f43c3d7dfb2d8:T=1722362247:RT=1722362247:S=AA-AfjYn1az6WLJrOD3o1ZXalDTs; FCNEC=%5B%5B%22AKsRol8OtgZEiV8y1U9pZu6bqzS-RwujgQtQxhjWj7hw_jrh9qluWl6tXdztceKc99mWNnM-aKEZISuoQMB2J4tmZH0NlX0Wgh8tlXyjpuGgogcYkzibAk6M5irxAKTpcKm8xKNCjmKttKKd2YBBedtzLyaPGvbcvg%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722362246.1.1.1722362289.17.0.0"
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