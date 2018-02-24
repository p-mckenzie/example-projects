from selenium import webdriver
import time
import pandas as pd
import re

#initialize dataframe to store scraped data
df = pd.DataFrame(columns=['year', 'title', 'ratings', 'madeit', 'reviews', 'photos', 'submitter_description',
                 'ingredients', 'readyin', 'servings', 'calories', 'fat', 'carbohydrate', 'protein'])

#start Selenium webdriver
driver = webdriver.Chrome('')

# go to Hall of Fame site
driver.get('http://allrecipes.com/recipes/14452/everyday-cooking/special-collections/hall-of-fame/')

# get links to each of the main Hall of Fame pages
main_pages = [x.get_attribute('href').split('?internalSource')[0] for x in driver.find_elements_by_partial_link_text('Hall of Fame')]

# remove current page if necessary (to avoid self-links)
try:
    main_pages.remove(driver.current_url)
except:
    pass

for link in main_pages:
    year = link.split('/')[-2]
    #navigate to Hall of Fame - year page
    driver.get(link)
    
    #get links to all 20 recipes in page    
    recipes = [element.get_attribute('href').split('?internalSource')[0] for element in 
                   driver.find_elements_by_xpath("//div[@class='fixed-recipe-card__info']//a")]
    recipes = set([url for url in recipes if '/recipe/' in url])
    assert len(recipes)==20 #just a quick check
    
    time.sleep(5)
    
    for recipe_link in recipes:
        #navigate to recipe
        driver.get(recipe_link)
        
        #initialize series to hold recipe facts
        s = pd.Series(index=['year', 'title', 'ratings', 'madeit', 'reviews', 'photos', 'submitter_description',
                 'ingredients', 'readyin', 'servings', 'calories', 'fat', 'carbohydrate', 'protein'])
        s.loc['year'] = year
        
        try:
            s.loc['title'] = driver.find_elements_by_xpath("//h1[@class='recipe-summary__h1']")[0].text
        except:
            pass
        
        try:
            s.loc['ratings'] = driver.find_elements_by_xpath("//div[@class='rating-stars']")[0].get_attribute('data-ratingstars')
        except:
            pass
        
        try:
            s.loc['madeit'] = driver.find_elements_by_xpath("//span[@class='made-it-count ng-binding']")[0].text
        except:
            pass
        
        try:
            s.loc['reviews'] = driver.find_elements_by_xpath("//span[@class='review-count']")[0].text.split()[0]
        except:
            pass
        
        try:
            s.loc['photos'] = driver.find_elements_by_xpath("//span[@class='picture-count-link']")[0].text.split()[0]
        except:
            pass
        
        try:
            s.loc['submitter_description'] = driver.find_elements_by_xpath("//div[@class='submitter__description']")[0].text
        except:
            pass
        
        try:
            s.loc['ingredients'] = [element.text for element in driver.find_elements_by_xpath("//span[@class='recipe-ingred_txt added']")]
        except:
            pass
        
        try:
            s.loc['readyin'] = driver.find_elements_by_xpath("//span[@class='ready-in-time']")[0].text
        except:
            pass
        
        try:
            s.loc['servings'] = driver.find_elements_by_xpath("//span[@class='servings-count']//span")[0].text
        except:
            pass
        
        try:
            s.loc['calories'] = driver.find_elements_by_xpath("//span[@class='calorie-count']//span")[0].text
        except:
            pass
        
        for string in ['fatContent', 'carbohydrateContent', 'proteinContent']:
            try:
                s.loc[re.split(r"[A-Z]", string)[0]] = driver.find_elements_by_xpath("//span[@itemprop='{}']".format(string))[0].text
            except:
                pass
            
        df = df.append(s, ignore_index=True)
        time.sleep(5)

driver.quit()
df.to_csv('allrecipes.csv')