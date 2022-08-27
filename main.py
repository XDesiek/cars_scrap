import pandas as pd
from car import Car
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import *
from utils import only_numbers
from xpath import Xpath

def main():
    xpath=Xpath()
    webd_path = 'chromedriver.exe'

    driver = webdriver.Chrome(webd_path)

    driver.get('https://cars.skoda-auto.com/456/pl-pl/carSearch')

    driver.implicitly_wait(30)


    accept_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    accept_button.click()
    del accept_button



    cars=[]
    number_of_car=0
    # repair the link
    for a in range(1,3):
        for n in range(6):    
            car_element = driver.find_element(By.CSS_SELECTOR,(f"#car-search-item-{number_of_car}"))
            number_of_car+=1

        
        
            # getting all info
            car_element.click()

            car=Car()
            # gettin all of the car info 
            car.link = driver.current_url
            car.model=driver.find_element(By.XPATH, xpath.carmodel).text
            car.engine=driver.find_element(By.XPATH,xpath.carengine).text
            car.price=only_numbers(driver.find_element(By.XPATH,xpath.carprice).text)
            car.installment=only_numbers(driver.find_element(By.XPATH,xpath.carinstallment).text)
            car.prod_year=driver.find_element(By.XPATH,xpath.carprod_year).text
            car.vin=driver.find_element(By.XPATH,xpath.carvin).text
            car.color=driver.find_element(By.XPATH,xpath.carcolor).text
            cars.append(car)

            driver.get('https://cars.skoda-auto.com/456/pl-pl/carSearch')
            driver.implicitly_wait(10)
            if a%6>0:
                for more_page_results in range(a%6):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    driver.find_element(By.ID,"result-page-more-results-btn").click()
                    driver.implicitly_wait(10)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



    
    
    # sleep (11)
    carlinks=[]
    carmodels=[]
    carengines=[]
    carprices=[]
    carinstallments=[]
    carprod_years=[]
    carvins=[]
    carcolors=[]
    inf=[carlinks,carmodels,carengines,carprices,carinstallments,carprod_years,carvins,carcolors]


    for car in cars:
        inf=car.car_info(inf)


    cardic={"link":inf[0],"model":inf[1],"engine":inf[2],"price":inf[3],"installment":inf[4],"prod_year":inf[5],"vin":inf[6],"color":inf[7]}
    cardf=pd.DataFrame(cardic)
    print(cardf)
    

    cardf.to_excel("car_excel.xlsx")
















































































































































































    # try:
    #     SCROLL_PAUSA_TIME = 3
    #     driver.get(subcategory_url)
    #     last_height = driver.execute_script("return document.body.scrollHeight")
    #     while True:
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(SCROLL_PAUSA_TIME)
    #         new_height = driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             time.sleep(3)
    #             break
    #         last_height = new_height








 # .get_attribute('href')
  









    # driver.close()


if __name__ == '__main__':
    main()