cookie="PHPSESSID=2b0965i4gdbr95nue6s2hspquh; _ga=GA1.1.1643404590.1722223183; _gcl_au=1.1.1452397702.1722223183; gads=ID=948aca77d3e00c93:T=1722223184:RT=1722223184:S=ALNI_MYc0xMi5w09gIBMdj9ZDfyptBfZIQ; gpi=UID=00000eab52534692:T=1722223184:RT=1722223184:S=ALNI_MaYWF7KyZBaoZhA4aE1eZvJ36zrzA; __eoi=ID=f757a1662c201fd7:T=1722223184:RT=1722223184:S=AA-AfjZLigZ7kXKAN8yTpFg8TpdH; _ga_HPSLFXFRWN=GS1.1.1722223182.1.1.1722223203.39.0.0; FCNEC=%5B%5B%22AKsRol9eZXWZ3B6vWv4LOTe68zD0C44-6J49ZfSSRPLLKmDn_e58W2DbDlJil8L6b5NjG37TXoklzPEEwdKO6cVPSUzahIUI41mqWkddCOlFKEDqXcBeoFmex7konb6Z9QyV5uQn7COTDTJqB2z1Qh6iHRVO0GQLzQ%3D%3D%22%5D%5D"
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