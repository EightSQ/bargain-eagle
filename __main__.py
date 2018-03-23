import api_access
import offer_evaluator
from mailing import mail

CONFIG_FILE = "tasks/call0.xml"

def main():
    with open(CONFIG_FILE) as f:
        cfg = f.read()
        f.close()
    try:
        api_response = api_access.call(cfg)
        good_offers = offer_evaluator.findGoodOffers(api_response)
        if good_offers: mail(good_offers)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

