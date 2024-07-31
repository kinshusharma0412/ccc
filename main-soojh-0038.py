cookie="PHPSESSID=j3i74ivc70f6n2n11psgs1agn4; _ga=GA1.1.875216867.1722322744; _gcl_au=1.1.1453495398.1722322744; popup_fb=yes; gads=ID=ff64a74810ff1e7d:T=1722322745:RT=1722327992:S=ALNI_MZJxx-NQNxme1i-waDrzGKyIUnvUw; gpi=UID=00000ebc78502afc:T=1722322745:RT=1722327992:S=ALNI_MZt1C7zpUwk6dLFEiZSXJung6pvdA; __eoi=ID=8386a3ca1c36b6a5:T=1722322745:RT=1722327992:S=AA-AfjZgpSAPTvXgeRT1JEMrcO0U; FCNEC=%5B%5B%22AKsRol8yuEjqEWrsGQlunelLVk1RENmqTXqVcQD0hhknhwSScJ-b40z_ZRkFIhzQMFTV0pgFvk09-POm7I43llNnHKunv33oxDoEmiuJEyCrUgvOsKJLsdfqMXGyTTFy36PTchdg0TWEvALYwUxCbzgdwfLWph-PPA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722327617.5.1.1722328062.53.0.0"
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