from selenium import webdriver
import time

def blowTheForm():
    
    web=webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSccjkIfuzP5gIH398GyM_06W5u7bldK90GAEWh64SxAdZ-uuA/viewform?fbzx=3436350974529355520')

    time.sleep(4)

    fillNama=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fillNama.send_keys('Josep Lois Castilo Gultom')

    clickKelas=web.find_element_by_xpath('//*[@id="i9"]/div[3]/div')
    clickKelas.click()

    fillNIM=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fillNIM.send_keys('test')

    clickSubmit=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    clickSubmit.click()
    
    get_confirmation_div_text=web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
    print(get_confirmation_div_text.text)
    if((get_confirmation_div_text.text)=='Tanggapan Anda telah direkam.'):
        print('Jadi deh')
    else:
        print('FeelsbadMan')