cookie="PHPSESSID=kr2jltpdomth56p4qtu3p20h1h; _ga=GA1.1.1261091745.1722361216; _gcl_au=1.1.1517820066.1722361216; FCNEC=%5B%5B%22AKsRol8Ko-T7Kf1EW309HwHu8uPL9xB3Ap5iDT-Z5dBbg0unPL6smP2LWuCsVcEPvjB-xM2L7WUNLJHfRJMnS_zj7I4jx_g8BHAK4hJKn70WghxnAVFkVkKa4TnoHmVuIjN5SKDn-OzGMzVtDw5JdjOm8vaWR2HKVg%3D%3D%22%5D%5D; gads=ID=725e248d2e27d61c:T=1722361190:RT=1722361552:S=ALNI_MYMQStq6CbRPLzMdsjrFmSG81F5sQ; gpi=UID=00000eade1b9cdef:T=1722361190:RT=1722361552:S=ALNI_Mbfd0Ng3olxGGXZNQdJbn0GfCAaQw; __eoi=ID=052c07b420779279:T=1722361190:RT=1722361552:S=AA-AfjYXFjlAoVkZJjIsMwRbSBfL; _ga_HPSLFXFRWN=GS1.1.1722361215.1.1.1722361587.49.0.0"
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