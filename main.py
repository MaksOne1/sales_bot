from websites.evroopt import EvrooptParser
import asyncio

evroopt_settings = {
    "website_url": "https://e-dostavka.by/",
    "catalog_url": "https://e-dostavka.by/catalogue",
}

EvrooptParserEntity = EvrooptParser(evroopt_settings)


loop = asyncio.get_event_loop()
loop.run_until_complete(EvrooptParserEntity.get_category())
loop.close()
