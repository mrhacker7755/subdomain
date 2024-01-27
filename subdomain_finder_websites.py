#!/usr/bin/env python

import requests

print(" SAYTLARNI SUBDOMAINNI TOPIB BERUVCHI SCRIPT by Sadullo")

target = input("website nomini kiriting : ")


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


target_url= target
with open("/home/admin123/Downloads/Subdomain.lst", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Topilgan subdomain nomi  -->" + test_url)

