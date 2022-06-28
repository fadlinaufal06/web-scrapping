from selenium import webdriver
from bs4 import BeautifulSoup as soup
from firebase_setup import post
webs = ["https://sipp.pn-bandaaceh.go.id/list_perkara/search", "https://sipp.pn-medankota.go.id/list_perkara/search", "http://sipp.pn-palembang.go.id/list_perkara/search", "http://pn-padang.go.id:8060/", "https://sipp.pn-pekanbaru.go.id/", "http://sipp.pn-jambi.go.id/", "https://sipp.pn-bengkulu.go.id/", "https://sipp.pn-tanjungpinangkota.go.id/", "https://sipp.pn-pangkalpinang.go.id/", "https://sipp.ptun-bandarlampung.go.id/", "http://www.sipp.pn-serang.go.id/", "http://sipp.pn-jakartapusat.go.id/", "http://sipp.pn-bandung.go.id/", "https://sipp.pn-yogyakota.go.id/", "https://sipp.pn-semarangkota.go.id/", "http://sipp.pn-surabayakota.go.id/", "http://sipp.pn-pontianak.go.id/", "http://sipp.pn-samarinda.go.id/", "http://sipp.pn-banjarmasin.go.id/", "https://sipp.pn-palangkaraya.go.id/", "https://sipp.pn-tanjungselor.go.id/", "https://sipp.pn-denpasar.go.id/", "https://sipp.pn-kupang.go.id/", "http://sipp.pn-mataram.go.id/", "https://sipp.pn-gorontalo.go.id/", "http://sipp.pn-mamuju.go.id/", "https://sipp.pn-palu.go.id/", "https://sipp.ptun-manado.go.id/", "http://sipp.pn-kendari.go.id/", "http://sipp.pn-makassar.go.id/", "https://sipp.pn-ternate.go.id/", "https://sipp.pn-ambon.go.id/", "http://sipp.pn-manokwari.go.id/", "http://sipp.pn-jayapura.go.id/"]

DRIVER_PATH='./chromedriver.exe'
# data = []
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
for web in webs :
    try :
        driver = webdriver.Chrome(DRIVER_PATH, chrome_options=options)
        driver.get(web)
        searchBox = driver.find_element_by_id('search-box')
        searchBox.send_keys('telkom')
        searchBox.submit()

        source = driver.page_source
        driver.close()

        page = soup(source, 'html.parser')
        rows = page.find_all('tr')
        rows.pop(0)
        rows.pop(len(rows)-1)
        for row in rows :
            row_data = {}
            columns = row.find_all('td')
            row_data['nomorPerkara'] = columns[1].text
            row_data['tanggalRegister'] = columns[2].text
            row_data['klasifikasi'] = columns[3].text
            row_data['paraPihak'] = columns[4].text
            row_data['statusPerkara'] = columns[5].text
            row_data['lamaProses'] = columns[6].text
            row_data['detail'] = columns[7].a.get('href')
            post(row_data)
        print(web, 'done')
    except Exception as e :
        print(e)
