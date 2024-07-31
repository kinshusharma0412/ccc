cookie="PHPSESSID=j52tnfcmtjlbnke9etq8n357i6; _ga=GA1.1.1616028564.1722343074; _gcl_au=1.1.1150766058.1722343074; _ga_HPSLFXFRWN=GS1.1.1722344374.2.1.1722344803.60.0.0; gads=ID=9f6d64436e009a75:T=1722343074:RT=1722344802:S=ALNI_MbVeWdORQsK_XdokIjcyMFtvRS9Uw; gpi=UID=00000eadbd9d26d4:T=1722343074:RT=1722344802:S=ALNI_MbxeHvU2lwVVBYhhTb1v7Lr3yOVjA; __eoi=ID=c66d5c2dc43e3919:T=1722343074:RT=1722344802:S=AA-AfjYd4cLyViJ-eJawWsFkqs1h; FCNEC=%5B%5B%22AKsRol8VF1SVsi8qfMsCFyd-oQqEvCEo6k3BU1FGX9jtyTvgsjbBFPlTCEk8IF3xx40-bJLWbFmIfDX4ZFzJtgD5EvlTkk8hARj2HJMMvH0CiEdMl6n7tGXVB570zzwyxCkZWH3zEOdicF431PgMZ1eLNQIMkxnJsw%3D%3D%22%5D%5D"
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