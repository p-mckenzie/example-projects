# names of superheroes to get images for
superheroes = ['spider-man', 'batman', 'wonder woman', 'flash', 'superman', 'captain america']

# location of the chrome webdriver
loc = 'C:\Program Files\chromedriver.exe'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import os
from urllib.request import urlretrieve
from time import sleep

def main():
    # start Selenium webdriver
    if loc=='':
        print('Error, please enter webdriver address. Stopping.')
    driver = webdriver.Chrome(loc)

    # go to website
    driver.get('https://www.superherostuff.com/')

    for name in superheroes:
        print("Now getting links for:", name)
        # search
        driver.find_element_by_name('search').send_keys(name)

        # send search
        driver.find_element_by_xpath('//button[@class="search-button"]').click()

        while True:
            # scrape links to images (name of superhero must appear in item description to avoid search errors)
            new_links = [x.get_attribute('src') for x in driver.find_elements_by_xpath("//img[@class='product-grid__thumbnail']")
                        if name.lower() in x.get_attribute('alt').lower()]

            # save data
            try:
                links = links + new_links
            except NameError:
                links = new_links
            del new_links

            # paginate or continue to next superhero
            try:
                # for politeness
                sleep(3)

                # navigate to next page
                driver.find_element_by_xpath('//a[@title="Go to next page"]').click()

            except NoSuchElementException:
                # finished pagination so save data
                try:
                    data[name] = links
                except NameError:
                    data = {name:links}
                del links

                # continue to next superhero
                break
    driver.close()
	
	print()
	
    for superhero, link_list in data.items():
        print("Getting {} images for {}.".format(len(link_list), superhero))
		
		# create directory if necessary to hold files
        if not os.path.exists('./{}'.format(superhero)):
            os.mkdir('./{}'.format(superhero))

        # save all the files
        for i in range(len(link_list)):
            urlretrieve(link_list[i], "./{}/{}.jpg".format(superhero, i))
            if i%45==0: # for politeness
                sleep(3)

        sleep(10) # for politeness

if __name__ == "__main__":
    main()