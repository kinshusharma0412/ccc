cookie="PHPSESSID=gc9tfgkeupgr3jd0nh2a294hm9; _ga=GA1.1.1972093374.1722348943; _gcl_au=1.1.681675863.1722348943; gads=ID=c3bf4cc6ede7eb1a:T=1722348944:RT=1722348944:S=ALNI_MYRptEL25YCipD1fxliSatj5SSoNw; gpi=UID=00000eadca09c8e9:T=1722348944:RT=1722348944:S=ALNI_Mbwc39B3nkOAtpiHz9WsUPhq1UmUA; __eoi=ID=05a566842059c936:T=1722348944:RT=1722348944:S=AA-AfjZKrOel1CCdRp3NpP0dqt4q; _ga_HPSLFXFRWN=GS1.1.1722348942.1.0.1722348949.53.0.0; FCNEC=%5B%5B%22AKsRol8vh1Bs15XeUQlhn86EFalK_vV-Z3GbjkJnQthkJ1VWWZ77cUi_N8gGoUAu_QzcRCqvHAtO43DwCzVVzGXpU7ud7o3NHbUj1lp5bNqizKAEsQgKqqWR91OOqxaMbAkJ3WxoJWWqKrGyarRaQ0XQq5KeNwtSoA%3D%3D%22%5D%5D"
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