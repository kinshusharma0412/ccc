cookie="PHPSESSID=bn0431tusgsi63po18n0a3htcp; _ga=GA1.1.734562310.1722396962; _gcl_au=1.1.1073208796.1722396962; gads=ID=008544a696edea36:T=1722396965:RT=1722396965:S=ALNI_MZNQUWr3VO1wuypmbedZ5Ps0Az11w; gpi=UID=00000eae113044fb:T=1722396965:RT=1722396965:S=ALNI_MbF8QNUJbDR6R84na_oQ9kyMhsNyw; __eoi=ID=2b8423cb92cea434:T=1722396965:RT=1722396965:S=AA-Afjbj3W3REObeexsA0EBvknfl; FCNEC=%5B%5B%22AKsRol-5DRhPBCYJIgWRcqR6UigncWDLQH9POA6GYGLNQECemYCOb0Ii72NKL-MS1IOBAdemOd-tM3YIB7n5MR6D7tq8hKAYg5E5tSoMAiJcsFYzgfspTqSWBb8RXtbmmXKZsdIFLuZzjuOXJSH8Sl5t2R-z4aAkbw%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722396962.1.0.1722396990.32.0.0"
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