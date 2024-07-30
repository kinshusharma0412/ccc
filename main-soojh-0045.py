cookie="PHPSESSID=so6083fbvr482o1ucn6r3nmd2b; _ga=GA1.1.1174720631.1722351036; _gcl_au=1.1.78494881.1722351036; gads=ID=9878d010898e03d7:T=1722351036:RT=1722351036:S=ALNI_MafpebmhcTGkoCQwB4Wj_wViGAdgA; gpi=UID=00000eadd184cecd:T=1722351036:RT=1722351036:S=ALNI_MZUzTjsixmmbWiQGyWY2i6ArIzbTg; __eoi=ID=c542ed143be9e44a:T=1722351036:RT=1722351036:S=AA-Afja5r70hDBIZokWQtd0P-0CE; _ga_HPSLFXFRWN=GS1.1.1722351036.1.0.1722351038.58.0.0; FCNEC=%5B%5B%22AKsRol_rOuZN-kTWhtgyAeVj5wCCBn8UaBAp_B3XncDu4A4jit2UfZ3aVc-OyPmGWjzyKIEqmxBl19roHoO-xcIKvbpPbNdmpf3ZAd4LPz3mjmXwp1StAhj4DrQtHAJY0Uqd0CN42q0SI_3hOKp5gjQgRcH2IYjgKQ%3D%3D%22%5D%5D"
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