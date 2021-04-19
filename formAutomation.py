from selenium import webdriver
import time

def blowTheForm():
    
    web=webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver.exe') #atau lain
    web.get('url')

    time.sleep(4)

    fillNama=web.find_element_by_xpath('xpath')
    fillNama.send_keys('MyName')

    clickKelas=web.find_element_by_xpath('xpath')
    clickKelas.click()

    fillNIM=web.find_element_by_xpath('xpath')
    fillNIM.send_keys('test')

    clickSubmit=web.find_element_by_xpath('xpath')
    clickSubmit.click()
    
    get_confirmation_div_text=web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
    print(get_confirmation_div_text.text)
    if((get_confirmation_div_text.text)=='Tanggapan Anda telah direkam.'): #atau bahasa inggirs
        print('Jadi deh')
    else:
        print('FeelsbadMan')
