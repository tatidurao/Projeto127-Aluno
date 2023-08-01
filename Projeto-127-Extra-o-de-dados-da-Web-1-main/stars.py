from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(START_URL)

scarped_data = []

time.sleep(10)

def scrape():

    #soup = BeautifulSoup(driver.page_source, "html.parser")
    #soup = BeautifulSoup(driver.page_source, )
    #soup = BeautifulSoup(driver, "html.parser")
    
    #bright_star_table = soup.find("", attrs={"class", "wikitable"})
    #bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    #bright_star_table = soup.find("table", attrs={"class", ""})
        
        # Localize <tbody>
    table_body = bright_star_table.find('tbody')

        # Localize <tr>
    table_rows = table_body.find_all('tr')
    for  row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_cols:
            

           
            data = col_data.text.strip()
            

            temp_list.append(data)

            
        scarped_data.append(temp_list)

scrape()        

stars_data = []

for i in range(0,len(scarped_data)):
              Star_names = scarped_data[i][1]
              Distance = scarped_data[i][3]
              Mass = scarped_data[i][5]
              Radius = scarped_data[i][6]
              Lum = scarped_data[i][7]

              required_data = [Star_names, Distance, Mass, Radius, Lum]
              stars_data.append(required_data)



#Defina o cabeçalho
headers = ['Star_names', 'Distance', 'Mass', 'Radius', 'Luminosity']

#Defina o dataframe do pandas
star_df_1 = pd.DataFrame(stars_data, columns= headers)

#Converta para CSV
#star_df_1.to_csv('.csv', index=True, index_label="id")
#star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
#star_df_1.to_csv('scraped_data.csv', index=True, ")
