# Script for scraping unpaid house bills

import account_info as passes
import requests
import re

USER_AGENT_STR = "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"

regex_pattern = r"<span class=\"amountInfo red\">(.+)</span>"

def get_tauron():
    ticket = ""
    client_id = passes.tauron_info["client_id"]
    step1_url = "https://logowanie.tauron.pl/"
    step2_url = "https://logowanie.tauron.pl/login"
    step7_url = "https://ebok.tauron.pl/wyborKlienta/id/" + client_id
    with requests.Session() as s:
        r = s.get(step1_url)
        if(r.status_code == 200):
            r = s.post(step2_url, data = {"username":passes.accounts_info["tauron"]["login"], "password":passes.accounts_info["tauron"]["password"], "service":""})
            if(r.status_code == 200):
                with open("./response.html", mode ="wb") as localfile:
                    localfile.write(r.content)
                r = s.get(step7_url)
                if(r.status_code == 200):
                    value = re.findall(regex_pattern, r.text)
                    print(value[0])

if __name__ == "__main__":
    get_tauron()