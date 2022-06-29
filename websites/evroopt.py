from websites.parser import Parser
import aiohttp
from bs4 import BeautifulSoup


class EvrooptParser(Parser):
    def __init__(self, settings):
        self.settings = settings

    async def get_category(self):
        async with aiohttp.ClientSession() as session:
            response = await session.get(self.settings.get("catalog_url"))
            html = await response.text()

            print(html)
            soup = BeautifulSoup(html, "lxml")

            category_html = [
                element.find("a") for element in soup.find_all("div", class_="title")
            ]

            category = [
                int(ctg.split("/")[:-1].replace(".html")) for ctg in category_html
            ]

            print(category)
