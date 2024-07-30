cookie="PHPSESSID=nr8p1pv2bjaarkikdkihef35a7; _ga=GA1.1.992282590.1722231443; _gcl_au=1.1.299747628.1722231443; gads=ID=63406e80924903ed:T=1722231445:RT=1722231445:S=ALNI_MY3v8oh9x_6EGQh0Z2XSahPgSciag; gpi=UID=00000eab65ec028a:T=1722231445:RT=1722231445:S=ALNI_MZA3IRLh68o2a-YZYDr8cjW8qJnTg; __eoi=ID=73cab37ab50e2084:T=1722231445:RT=1722231445:S=AA-Afja2Vftve49BNiJbWkQ4GiFD; _ga_HPSLFXFRWN=GS1.1.1722231443.1.0.1722231449.54.0.0; FCNEC=%5B%5B%22AKsRol8xGtWTWF4IzWiLshADtNiJdTgUWXtbhomdtw900ZALj2Zg22rHMkkcylC_yE8eA6n33NpTHDOrD51n3dOav95gbfuZgA2jcGNlqTQRSYBzUt765FWotvV2qmTpMk9Gx8imbyT5-YgMcb7l9xJhXOhk2E4RAg%3D%3D%22%5D%5D"
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