cookie="PHPSESSID=ma9chl4i7ptdahfeffeqqosso7; _ga=GA1.1.45168009.1722357118; _gcl_au=1.1.22109727.1722357118; gads=ID=c500986d8ec8b2da:T=1722357139:RT=1722357139:S=ALNI_MY3Ft7WLQF8F5t96cHFFNy0byExuQ; gpi=UID=00000eaddb68c926:T=1722357139:RT=1722357139:S=ALNI_MZx_hbPMxwExITr9g-YtfLqrEGMaw; __eoi=ID=105d0848e787e9c1:T=1722357139:RT=1722357139:S=AA-AfjZuzLRN7zOVtJ30UF61eZ4g; _ga_HPSLFXFRWN=GS1.1.1722357118.1.1.1722357160.18.0.0; FCNEC=%5B%5B%22AKsRol9kp5rf5jhicErFaZzHjZ3kJixRNrU3kS5-Fo6OlUBJfSA8uKNgHGPu4Zed1Uicw_sU0HZj7o98nzHJ0lRVm5D9ErIVYGgqYzx3-iRj2NmFCv0MKx8grF_ioTuVeKeSXPr6c7W2DzBQKIsuQ6BKQOLgmZfY2g%3D%3D%22%5D%5D"
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