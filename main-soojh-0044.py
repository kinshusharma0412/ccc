cookie="PHPSESSID=ejqq105blbi4le80436tnjfid5; _ga=GA1.1.1778912029.1722350907; _gcl_au=1.1.1563249031.1722350907; gads=ID=d5a4f42a18f0ae0d:T=1722350907:RT=1722350907:S=ALNI_MbjWa8gmurPQcnevJYnGqLxXEDoig; gpi=UID=00000eadd16677d0:T=1722350907:RT=1722350907:S=ALNI_MbD_H5Dmt3TBa-5OtUpKitVaqYUNg; __eoi=ID=2920a0296305ead4:T=1722350907:RT=1722350907:S=AA-Afjar0P-ob0XTO5FY2UmW0sBb; _ga_HPSLFXFRWN=GS1.1.1722350906.1.1.1722350913.53.0.0; FCNEC=%5B%5B%22AKsRol97S4xg0ThG9uzANEuLexlCR-xwIQrcyb9r45xe1aBJHAJwqdTPyHpzD9CX37MKtRR2LCF6B96nvI3yo5FfYlu3ACnPNCLK7LJL-7VfOcp37ybWgmC_PharF_m3zFPNDW0t4kXhS7XRlEeo3P1ZqPDTd52Amw%3D%3D%22%5D%5D"
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