cookie="PHPSESSID=e2jps01029r9o53h9bmfkdcd8k; _ga=GA1.1.1029603550.1722335468; _gcl_au=1.1.1105661299.1722335468; gads=ID=2a07e4301c451f8c:T=1722335467:RT=1722335467:S=ALNI_MYd8MiB49uaQyT18Kyh3Xq7fDb-Dg; gpi=UID=00000eadab8b3b72:T=1722335467:RT=1722335467:S=ALNI_MZ1YeVDzx351LEKEr7u0mpbFUPRtA; __eoi=ID=74a148c6aeddf929:T=1722335467:RT=1722335467:S=AA-AfjaLYANekJTmDaBR0TtRTkF_; _ga_HPSLFXFRWN=GS1.1.1722335442.2.1.1722335471.31.0.0; FCNEC=%5B%5B%22AKsRol9bNQKC_m7jW4-VNzwkineSiEHfzQoNLoEYWV-o1LhG53HwMl1R60sF32qErZgoR_KQrjDhXGCJ-ody3jUn_39O0DV34Fh-WXqFww8EXp75LX-eZKeJKn6SdxfEDtooATJtSWGNAgr7j3nyxZGbOiJw8vpXew%3D%3D%22%5D%5D"
import requests,time
import streamlit as st
from bs4 import BeautifulSoup
@st.cache_data
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
	            #st.write(s)
	            print(s)
	        except:
	            pass
	        s=soup.select("meta#token_key")[0]['value']
	        #st.write(s)
	        print(s)
	        open("db.txt","w").write(s)
	    except:
	        try:
	            s="9UyjIsVR"#open("db.txt","r").read(
	        except:
	            s=""
	        ##st.write(s)
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
	
	    #st.write(response.text)
	    print(response.text)
	    time.sleep(5*60)
my()