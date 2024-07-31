cookie="PHPSESSID=sp3vtjq0o5rlkpfsmf4fdr152b; _ga=GA1.1.548355211.1722364929; _gcl_au=1.1.1453237345.1722364929; gads=ID=f67858118fd183d3:T=1722364928:RT=1722364928:S=ALNI_Ma6LcJZn5WwQNSXSZjF9smxDgB_cg; gpi=UID=00000eade5ec0e08:T=1722364928:RT=1722364928:S=ALNI_Ma9C_Rlz_kOqmt6aQ-LqEI_APQwZw; __eoi=ID=c9deec390535be98:T=1722364928:RT=1722364928:S=AA-AfjYP7feVbDwn6X0MgmUB9WWl; FCNEC=%5B%5B%22AKsRol_Ffi72dZ_egwfAggZV8jlfoa0PhNtF0keWL4VffVMjtF-FsYHkkVCm9O-uFlcV9DARdtYGsqZB4IUnvVnYURVfnw2NTW3jmXeyo9CLK849mppkUe7fcGqhYEF5nBpfH0QdA2D3jaFveTuarhfayM_0nYQ77Q%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722364928.1.1.1722364949.39.0.0"
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