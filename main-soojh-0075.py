cookie="PHPSESSID=c3vv9djlcub4hanqo7pj4pskan; _ga=GA1.1.1641797286.1722393159; _gcl_au=1.1.1572490879.1722393159; gads=ID=1cef096a89d24a5f:T=1722393163:RT=1722393163:S=ALNI_MYvy82gbz5t9pAtRkSbNM8W68l9lQ; gpi=UID=00000eae07ff793e:T=1722393163:RT=1722393163:S=ALNI_MasQDkWnzqNnweXnllQtyEmD_lmMw; __eoi=ID=3ae04a2288861d28:T=1722393163:RT=1722393163:S=AA-AfjZlLgC1Dtl5rRmpiTyDUgZg; FCNEC=%5B%5B%22AKsRol-jHAjwTItbNPq_bJLXOCqbiZmc-dbzFzwc_XA_4A9BeNg2RSOvu9ULGP4-m0zVoijzSniutoA5lkc5GicW-3MuiTLZJNC9KDL4tGFLv1oP09ovYEnhb-qvyjKbYPPM2ldhAQyd2qjei1SclDZmRi9_tSWPhA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722393158.1.1.1722393183.35.0.0"
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