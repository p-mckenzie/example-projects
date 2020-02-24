# import credentials
import petfinder_API_auths

# import packages
import pandas as pd
import requests

def get_bearer_code():
    # get temporary access code w/ credentials
    print("Getting bearer code.")
    
    return requests.post("https://api.petfinder.com/v2/oauth2/token",
             {'grant_type':'client_credentials',
                      'client_id':petfinder_API_auths.key,
                      'client_secret':petfinder_API_auths.secret}).json()['access_token']

bearer_code = get_bearer_code()

# collect all pets
pets = []
page = 1
while True:
    while True:
        response = requests.get("https://api.petfinder.com/v2/animals", 
                       headers={'Authorization': 'Bearer {}'.format(bearer_code)},
                                       params={'limit':100,
                                              'status':'adoptable',
                                               'location':'Raleigh, NC',
                                              'page':page}
                                       )
        # make sure results are accurate
        if response.status_code==401:
            # need new access code
            bearer_code = get_bearer_code()
        elif response.status_code==200:
            # data delivered successfully
            break
        elif response.status_code==429:
            # hack to make outer while loop stop
            page = response.json()['pagination']['total_pages']
            break
        else:
            # who knows?
            raise Exception("Unknown status code: {} at page {}".format(response.status_code, page))
                
    # log data
    pets += response.json()['animals']
    if page==response.json()['pagination']['total_pages']:
        break
    if page%100==0:
        print(page)
    page += 1
    
# save data (just in case)
pets = pd.DataFrame(pets)
pets['url'] = pets['url'].str.split('\?referrer_id').str[0]
pets.to_csv('pets.csv')

# import data
pets = pd.read_csv('pets.csv', index_col=0)

# webscrape for full text fields
from lxml import etree

htmlparser = etree.HTMLParser()

print("Scraping to:", len(pets))
for indx, pet_url in pets['url'].iteritems():
    # set user-agent to ANY other value so it doesn't "look" like Python
    response = requests.get(pet_url, headers={'User-Agent': 'Custom'}, stream=True)

    response.raw.decode_content = True
    tree = etree.parse(response.raw, htmlparser)
    
    try:
        pets.loc[indx, 'description'] = tree.xpath("//div[@class='card-section']//div[@class='u-vr4x']")[0].text.strip()
    except IndexError:
        pass
    if indx%100==0:
        print(indx)
        
# save complete data
pets.to_csv('pets_new.csv')