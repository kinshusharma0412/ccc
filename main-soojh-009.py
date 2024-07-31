cookie="PHPSESSID=3jjbgvg6mildisipha3drsqafl; _ga=GA1.1.1465642771.1722221768; _gcl_au=1.1.362847526.1722221768; gads=ID=01e697b1c7589c86:T=1722221773:RT=1722221773:S=ALNI_MYM72gCzT9J1eQ0XS1zAhpzFaWuxA; gpi=UID=00000eab5072a592:T=1722221773:RT=1722221773:S=ALNI_Ma9Tf6wzTTk0A2y5rhaXWREBfJCRg; __eoi=ID=e663214d31ddf727:T=1722221773:RT=1722221773:S=AA-AfjZgnJh3EHQ-uSYtWsCxDiHF; _ga_HPSLFXFRWN=GS1.1.1722221768.1.1.1722221775.53.0.0; FCNEC=%5B%5B%22AKsRol_FcWbmnuZcWSQTLi5THEC_Km--SWXnIB-7SkVzv8oEQ9syLu8SFHlcJ_PK4v6McpmTEZHgEsBBnDAIjr21jfmE50nLL4Y_1ObKTEFxH4GNnbvUOcImG_7vO7E_A7EKpRxGCbFVn2U0p_xXx_X2E3JaQI4jWg%3D%3D%22%5D%5D"
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