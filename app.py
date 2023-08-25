import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto("http://www.python.org")


    visible_text = await page.evaluate('''
        () => {
            return document.body.innerText;
        }
    ''')


    print(visible_text)

    await browser.close()



asyncio.get_event_loop().run_until_complete(main())
