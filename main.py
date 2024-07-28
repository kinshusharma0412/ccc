import requests
import streamlit as st
from bs4 import BeautifulSoup
List="""147.75.34.92:9400
8.223.31.16:80
47.90.205.231:33333
35.185.196.38:3128"""
session = requests.Session()
for x in List.split("\n"):
	try:
		proxies = { 
              "https" : "https://"+x, 
            }
		url = "https://mycutebaby.in/contest/participant/669bc381bf80d"
		
		params = {
		  'utm_medium': "l_7_24"
		}
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  "Cookie":"PHPSESSID=ivlv0ppd0h1ha30e30q26a84eg; _ga=GA1.1.1211826256.1722176624; _gcl_au=1.1.234226407.1722176624; _ga_HPSLFXFRWN=GS1.1.1722177180.2.1.1722177181.59.0.0; gads=ID=04abd6c58736efe7:T=1722176682:RT=1722177184:S=ALNI_MbJdy7ZamvMnOjf4sSDsJL6jbYqGg; eoi=ID=c2b4a41812be9d70:T=1722176682:RT=1722177184:S=AA-AfjYEgMTmpBjpFyfHUf45hQ80; FCNEC=%5B%5B%22AKsRol_08qH2-e6uaKHIZCrvpNU6ifg6HAPVQMaBii7sgVmKU09y5t1_lHMxU5wKunxXoGoNsaU9PbbALAxZqlEaiu0jwHHczFk59rNN4OpevtoWNe7BVEdQmF8qEUxO8iae3tH-1NhIZrUAfTTPzNzxGukhTyGCdw%3D%3D%22%5D%5D"
		}
		
		response = session.get(url, params=params, headers=headers)#,proxies=proxies)
		
		soup=BeautifulSoup(response.text,"html.parser")
		try:
			s=soup.select("meta#token_key")[0]['value']
		except Exception as e:
			print(e)
		
		
		url = "https://mycutebaby.in/contest/daily_vote/"
		print(s)
		params = {
		  'n': "669bc381bf80d",
		  'captcha': "asdsdad",
		  'key': s,
		  'v': "Sharmasharmasharma"
		}
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'X-Requested-With': "XMLHttpRequest",
		  'Referer': "https://mycutebaby.in/contest/participant/669bc381bf80d?utm_medium=l_7_24",
		  "Cookie":"PHPSESSID=ivlv0ppd0h1ha30e30q26a84eg; _ga=GA1.1.1211826256.1722176624; _gcl_au=1.1.234226407.1722176624; _ga_HPSLFXFRWN=GS1.1.1722177180.2.1.1722177181.59.0.0; gads=ID=04abd6c58736efe7:T=1722176682:RT=1722177184:S=ALNI_MbJdy7ZamvMnOjf4sSDsJL6jbYqGg; eoi=ID=c2b4a41812be9d70:T=1722176682:RT=1722177184:S=AA-AfjYEgMTmpBjpFyfHUf45hQ80; FCNEC=%5B%5B%22AKsRol_08qH2-e6uaKHIZCrvpNU6ifg6HAPVQMaBii7sgVmKU09y5t1_lHMxU5wKunxXoGoNsaU9PbbALAxZqlEaiu0jwHHczFk59rNN4OpevtoWNe7BVEdQmF8qEUxO8iae3tH-1NhIZrUAfTTPzNzxGukhTyGCdw%3D%3D%22%5D%5D"
		}
		
		response = session.get(url, params=params, headers=headers)#,proxies=proxies)
		st.write(response.text)
	except:
		print(1234)
