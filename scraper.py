from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
import pandas as pd
import glob, os

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("-—incognito")
chromedriver_path = 'C:\\Users\\yokai\\Downloads\\chromedriver_win32\\chromedriver.exe'
def create_webdriver():
 return webdriver.Chrome(executable_path=chromedriver_path, chrome_options=driver_option)

browserURL = ("http://github.com/collections/")
browserURL += (input("Input Collection Name e.g. Programming Languages (you can find them from https://github.com/collections) "))


# Open the webdriver & website
browser = create_webdriver()
#getting the browser output of browserURL and replacing the whitespace with a hyphen
browser.get(browserURL.replace(" ", "-"))

# finding all elements in the page with <h1> and a class of h3-1h condensed (all the collections happen have the same tag and class)
collection = browser.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")

#coll = collection
collection_list = {}
for coll in collection:
 coll_name = coll.text # Collection name
 coll_url = coll.find_elements_by_xpath("a")[0].get_attribute('href') # Collection URL
 collection_list[coll_name] = coll_url

# getting the data
collection_df = pd.DataFrame.from_dict(collection_list, orient = 'index')

# table thingys
collection_df["Collection Name"] = collection_df.index
collection_df = collection_df.reset_index(drop=True)

# to string we go
collection_df.to_string()

# printing the output of collection_df
print(collection_df)

# names of the directory
directory =  ("output")
# grabs the same path of the executing python file
parent_dir = (os.path.dirname(os.path.realpath(__file__)) + "/")

#joins the two variables together
path = os.path.join(parent_dir, directory)

# creates the path and prints the action.
os.mkdir(path)
print("Directory '% s' created" % directory)

# prints the csv file in the Directory named Output.
collection_df.to_csv(path + "\\" + "Collection-List.csv")

# Closes Connection
browser.quit()
