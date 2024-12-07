# Script for scraping unpaid house bills

import account_info as passes
import requests

USER_AGENT_STR = "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"

def get_tauron():
    ticket = ""
    client_id = ""
    step1_url = "https://logowanie.tauron.pl/"
    step2_url = "https://logowanie.tauron.pl/login"
    step3_url = "https://ebok.tauron.pl/?ticket=" + ticket
    step4_url = "https://ebok.tauron.pl/login/ticket/" + ticket
    step5_url = "https://ebok.tauron.pl"
    step6_url = "https://ebok.tauron.pl/wyborKlienta"
    step7_url = "https://ebok.tauron.pl/wyborKlienta/id/" + client_id
    r = requests.get(step1_url)
    print(r.status_code)
    if(r.status_code == 200):
       print(r.headers)
       print(r.cookies)



if __name__ == "__main__":
    get_tauron()