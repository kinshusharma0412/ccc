cookie="PHPSESSID=nhokough1b4l8c28e9vmu851ch; _ga=GA1.1.1331768196.1722339499; _gcl_au=1.1.135421727.1722339499; gads=ID=f0512182913726e2:T=1722339501:RT=1722341268:S=ALNI_MaHdWSq2_oMcO_jzVWvJHl1xo6Shw; gpi=UID=00000eadb6672fa7:T=1722339501:RT=1722341268:S=ALNI_MaCNQZ41zTCZf9HaeCrrK2ZMRSZ6g; __eoi=ID=50e4bfc0745baa53:T=1722339501:RT=1722341268:S=AA-AfjbVPKWEnAgGJJYX0LyQWs6N; popup_fb=yes; _ga_HPSLFXFRWN=GS1.1.1722341266.3.1.1722341502.44.0.0; FCNEC=%5B%5B%22AKsRol8Z9ZEG86QVFZrwsLDaeuAHBng89wLpv5yveXNW7JEYuZ8xwMQIJDlKCbmmL9wPATFk5rImGUvygHhi0FWLXU8TOmYwhn6ovhqJmaflWG7DW9dsNkIuCQ7icIChRPDRBFnhr6gZPHgLGzsfWH4bZ_lNngc6dA%3D%3D%22%5D%5D"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
@st.cache
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