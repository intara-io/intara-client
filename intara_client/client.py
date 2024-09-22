import time

import requests


class IntaraClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.api_url = "https://api.intara.io/api/"
        self.client = requests.Session()
        self.client.headers.update(
            {
                "Authorization": f"Token {self.api_key}",
                "Content-Type": "application/json",
            }
        )

    def serp(self, keyword: str, location_code: int = 2840) -> dict:
        if isinstance(keyword, str):
            keyword = [keyword]

        url = self.api_url + f"research/serp/"
        querystring = {
            "keyword": keyword,
            "location_code": location_code,
        }
        response = self.client.get(url, params=querystring, timeout=90)
        return response.json()

    def msv(self, keyword: str, location_code: int = 2840) -> dict:
        if isinstance(keyword, str):
            keyword = [keyword]

        url = self.api_url + f"research/msv/"
        querystring = {
            "keyword": keyword,
            "location_code": location_code,
        }

        response = self.client.get(url, params=querystring, timeout=90)
        return response.json()

    def alpha_parser(
        self, url: str, industry: str, disable_cache: bool = False
    ) -> dict:
        url = self.api_url + f"research/alpha-url-parser/?url={url}&industry={industry}"
        if disable_cache:
            response = self.client.get(url + "&disable_cache=true")
        else:
            response = self.client.get(url, timeout=90)

        while response.json().get("status") == "pending":
            print("Waiting for response...")
            time.sleep(3)
            response = self.client.get(url, timeout=90)
        return response.json()
