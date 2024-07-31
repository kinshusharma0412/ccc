cookie="PHPSESSID=sg7kngvmm9j25gq3sf245fh9pf; _ga=GA1.1.287393721.1722398561; _gcl_au=1.1.186630642.1722398562; gads=ID=74804753a499721a:T=1722398564:RT=1722398564:S=ALNI_Mb3lBv3TiB718U_F8cNSeyUcXnBTQ; gpi=UID=00000eae12c77683:T=1722398564:RT=1722398564:S=ALNI_MbfkCxA9hjuSV0sVKIbR31MyR5QWw; __eoi=ID=428ca982163ea5d9:T=1722398564:RT=1722398564:S=AA-AfjYueP4fRY86XOHm-zdQ09Wi; popup_fb=yes; _ga_HPSLFXFRWN=GS1.1.1722398561.1.1.1722398792.56.0.0; FCNEC=%5B%5B%22AKsRol_xpj8vTcha6C5kWon2b7JKYEw11e7dHjJ9Ec-A-wDOYa-NiZBeIXWeMcO0xO4xZytCGek72QM2kmSG2f88zjuC21OMxzYlQDAquWcVor0KXPqX5796BSmrvfJNH51BkZzhMEGEXaxW_NcTE9kF0mt4kjlatQ%3D%3D%22%5D%5D"
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