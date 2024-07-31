cookie="PHPSESSID=i424uftsg2plult14usqoh0285; _ga=GA1.1.476322913.1722357016; _gcl_au=1.1.2137267842.1722357016; gads=ID=92105170ed050bb8:T=1722357018:RT=1722357018:S=ALNI_MYkSUt8hbgHIiKgLTnox6bhDndPqg; gpi=UID=00000eaddb27d410:T=1722357018:RT=1722357018:S=ALNI_MZr-lkEXXdmJ0WL2otFOOXVnCTT_Q; __eoi=ID=fda4444132bcc1c7:T=1722357018:RT=1722357018:S=AA-AfjakJVVpEHTNsVMjQUWyURzY; FCNEC=%5B%5B%22AKsRol8EBs1hQnaPFsq89S394htABojnJVbfs_BA68NaWfY8Zfv_A5GDlO2eAFJB0kmkKmqEgUHt73b9ch7YBwjH1FAYf6cnWajPkbMP2RSZ46OaJFgJm8KsCficJVyn2dntBmeqEiBC7h2ldEZENDXyBO-F6nVriA%3D%3D%22%5D%5D; _ga_HPSLFXFRWN=GS1.1.1722357016.1.1.1722357131.60.0.0"
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