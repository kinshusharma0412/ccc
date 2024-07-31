cookie="PHPSESSID=i043qctkeqdapu9p1ts1u7qe8s; _ga=GA1.1.686506216.1722349285; _gcl_au=1.1.99742857.1722349286; gads=ID=e879c87d4e59cc17:T=1722349288:RT=1722350119:S=ALNI_MbHmNqyjfASj6RQCZN3gyhAombU_g; gpi=UID=00000eadcc1d429d:T=1722349288:RT=1722350119:S=ALNI_MZ4Dl5zMvd8QT29UEc-Wf0EtUSNYQ; __eoi=ID=f9f1704ec408d00f:T=1722349288:RT=1722350119:S=AA-AfjZgxevi7RZdblcGvoA2dz2e; _ga_HPSLFXFRWN=GS1.1.1722350119.2.0.1722350127.52.0.0; FCNEC=%5B%5B%22AKsRol8QHkerQoQiAIFe-EEZlGxwTb2_uKmaUGkBtfqvK47DeXjxFiuTFFbn-8vm_1ydq4QyEpJURAiOxA-EnlpX0bpJl4-qExWkBcTrEDktenW8-e8tnnkWPHEcHG-lfMceBal6ZfWth8_M0sqV0GpOxPPU-F1-3A%3D%3D%22%5D%5D"
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