import asyncio
from playwright.async_api import async_playwright, Playwright
from PIL import Image
import streamlit as st

async def run(playwright: Playwright):
    
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("https://mycutebaby.in/contest/participant/669bc381bf80d?utm_medium=w_7_24")
    href_element = await page.query_selector("#v")
    # Ensure the variable 'Name' is defined and contains the desired name
    #Name = "Your mmmmmm"
    await href_element.fill(Name)
    await page.wait_for_timeout(2000)
    #href_element = await page.query_selector("#v")
    #print(await (href_element).inner_html())
    href_element = await(await page.query_selector("#vote_btn")).click()
    await page.wait_for_timeout(3000)

    await page.screenshot(path="screenshot.png", full_page=True)
    img = Image.open('screenshot.png')
    st.image(img)
    print(1)
    # other actions...
    await browser.close()

while True:
	async def main():
		async with async_playwright() as playwright:
			await run(playwright)
	asyncio.run(main())
	time.sleep(5*60)