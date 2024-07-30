cookie="PHPSESSID=ulr5vk12m34ivn48ipsjvnm987; _ga=GA1.1.1517960425.1722342729; _gcl_au=1.1.1587766970.1722342729; gads=ID=1204e7c2a4568106:T=1722342734:RT=1722344948:S=ALNI_MaOrdnVn905pYa-A0FndMvCnmI4og; gpi=UID=00000eadbcbd1d43:T=1722342734:RT=1722344948:S=ALNI_MZCFuUJ9Df8u4sDju_55UtTTxUA3A; __eoi=ID=871430ba4aab1644:T=1722342734:RT=1722344948:S=AA-AfjZqBeEXIO3CgJTliHJnanpX; _ga_HPSLFXFRWN=GS1.1.1722344725.4.1.1722345017.60.0.0; FCNEC=%5B%5B%22AKsRol9GmaAQ-x56MuoDMkJnCIRe0o3PF-exO9fOzgA4QQ2zK3IXLoHTAUxP-IbLtrAglmW7_KCvLQm2UWng6gvoGPeVFJUlHpvoqTrOSoNdHbN0bg2djsBIq4ldCG80xEYn_x6TvzehzTqyX3bpdBdaK3VDWbEFwg%3D%3D%22%5D%5D"
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