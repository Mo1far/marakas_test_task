# -*- coding: utf-8 -*-
from amazon_scraper.settings import INPUT_KEYWORDS_FILE


def get_keywords():
    with open(INPUT_KEYWORDS_FILE, 'r', encoding='utf-8') as file:
        keywords = [line.strip() for line in file]
    return keywords


def transform_keywords_to_urls(keywords_list):
    urls_list = []

    for keyword in keywords_list:
        urls_list.append(f'https://www.amazon.com/s?k={keyword.replace(" ", "+")}')
    return urls_list


def get_start_urls():
    keywords = get_keywords()
    urls = transform_keywords_to_urls(keywords)
    return urls
