cookie="PHPSESSID=3mi1rt2ag3rc7nmp9cr8mdapr1; _ga=GA1.1.1541071956.1722352759; _gcl_au=1.1.221887699.1722352759; popup_fb=yes; gads=ID=9419f51d2d6e2d6c:T=1722352763:RT=1722358870:S=ALNI_MZngdEeaIgsiekt5Tp7yGi0Tma1Lg; gpi=UID=00000eadd517b1f4:T=1722352763:RT=1722358870:S=ALNI_MY-oRDvoDX1v1baFA7Dc7jID6zbpQ; __eoi=ID=6bb10f1b4c0f6f12:T=1722352763:RT=1722358870:S=AA-AfjZQEtXnJQ7mWiCnaKNdW-95; FCNEC=%5B%5B%22AKsRol-x4bM1ci4ge44lE5LZTl2iSBcAe0y9bMpvrR2Sf8DjnPSSiRwH40WwKIBsOg8i6b5TSuuwh1MGchrfNZFYW5aU1kTyzQbdalAuMYN10umU60JI5zS8J9lfHy5sh9G1sUIBFJ44hPe6rRNVjj6l_5p_cL8GyA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722358554.7.1.1722358887.42.0.0"
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