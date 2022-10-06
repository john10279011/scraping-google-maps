from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

sportname = []
sportwebsite = []
sportnumber = []

#districts
alberta = 'https://www.google.com/search?q=outdoor+sport+stores+in+alberta&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBuVItaOhEC_r6nVec60yHH4JZQ14Q%3A1644119991608&ei=t0f_YZrOJI2VgQaNrLrACA&oq=outdoor+sport+stores+in+alberta&gs_l=psy-ab.12...0.0.0.443524.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.iHBcwJpCwow#rlfi=hd:;si:;mv:[[53.9182893,-112.5160959],[48.7778474,-118.3948867]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
britishcolumbia = 'https://www.google.com/search?q=outdoor+sport+stores+in+british+columbia&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBvYPmiMCY4PzbNT28X0ug3fimXH5A%3A1644120470922&ei=lkn_YYPiN4WckgWv6YKQAw&oq=outdoor+sport+stores+in+british+columbia&gs_l=psy-ab.12...0.0.0.17160.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.WhDtDUV5mIw#rlfi=hd:;si:;mv:[[50.8009263,-116.9049669],[48.292415,-123.8789954]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
manitoba = 'https://www.google.com/search?q=outdoor+sport+stores+in+manitoba&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBtcP7ezOede9Kmoyuk30SDmUkmjPg%3A1644120490507&ei=qkn_YeCtHo7BgQamkrbwDQ&oq=outdoor+sport+stores+in+manitoba&gs_l=psy-ab.3..0i22i30k1.20357.21944.0.24724.8.8.0.0.0.0.523.1257.2-1j0j1j1.3.0....0...1c.1.64.psy-ab..5.3.1256...33i22i29i30k1.0.2gxeV4uHj1M#rlfi=hd:;si:;mv:[[50.172367099999995,-96.69218509999999],[49.7997855,-100.14958039999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
newbrunswick = 'https://www.google.com/search?q=outdoor+sport+stores+in+new+brunswick&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBst0SNRM_OpESuLlMgwA0Z2ky-gHg%3A1644120517654&ei=xUn_YZK1J8n2gQb33rHYDA&oq=outdoor+sport+stores+in+new+brun&gs_l=psy-ab.1.0.33i160k1l2.34173.36065.0.39295.8.8.0.0.0.0.555.878.3-1j0j1.2.0....0...1c.1.64.psy-ab..6.2.877...33i22i29i30k1.0.4TtOyIed5Sg#rlfi=hd:;si:17244139067564695184,l,CiVvdXRkb29yIHNwb3J0IHN0b3JlcyBpbiBuZXcgYnJ1bnN3aWNrkgEUb3V0ZG9vcl9zcG9ydHNfc3RvcmWqARwQASoYIhRvdXRkb29yIHNwb3J0IHN0b3JlcygA;mv:[[47.72469770000001,-64.3938076],[45.121547,-66.791681]]'
newfoundland = 'https://www.google.com/search?q=outdoor+sport+stores+in+newfoundland+and+labrador&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBufKyCFr6w612gGPaTsCnWZZAlNNg%3A1644120558772&ei=7kn_Yd3NLomSaNDbosgD&oq=outdoor+sport+stores+in+newfoundland+and+&gs_l=psy-ab.1.0.33i160k1.34473.39919.0.42469.14.12.0.0.0.0.493.1683.3-1j3.4.0....0...1c.1.64.psy-ab..10.4.1680...33i22i29i30k1.0.MsxGcKQLBG4#rlfi=hd:;si:;mv:[[53.6786889,-51.8546695],[47.16983,-67.7783522]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
novascotia='https://www.google.com/search?q=outdoor+sport+stores+in+new+scotia&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBuPOxefr7QN6w-Z7QsiGjcufIsgqg%3A1644120603787&ei=G0r_YbPDL5aA8gLBzL-oBw&oq=outdoor+sport+stores+in+new+scotia&gs_l=psy-ab.3..33i22i29i30k1.29124.31494.0.31890.7.7.0.0.0.0.359.985.3-3.3.0....0...1c.1.64.psy-ab..4.3.983...35i39k1j33i160k1.0.RAzBG58vuLs#rlfi=hd:;si:;mv:[[46.303478299999995,-59.99577329999999],[44.551763099999995,-64.7035277]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
ontario = 'https://www.google.com/search?q=outdoor+sport+stores+in+ontario&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBsPhQqEt2PWhbQK2yGgh14SmrVCJw%3A1644120637964&ei=PUr_YYeoOpn2sAe4vZPIBA&oq=outdoor+sport+stores+in+ontario&gs_l=psy-ab.3..33i22i29i30k1l5.27847.29368.0.30426.7.7.0.0.0.0.353.959.3-3.3.0....0...1c.1.64.psy-ab..4.3.957...0i22i30k1.0.PKyX5MLz8OU#rlfi=hd:;si:;mv:[[46.7286307,-75.1197483],[42.7180804,-84.8612084]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
princeedward = 'https://www.google.com/search?q=outdoor+sport+stores+in+prince+edward+island&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBuA8f9TN90Jelewq2iKbbJFzoDw0g%3A1644120670182&ei=Xkr_YZTMCoaIxc8P1qe8wAI&oq=outdoor+sport+stores+in+prince+ed&gs_l=psy-ab.1.1.33i160k1l4j33i21k1.20688.23589.0.27184.9.9.0.0.0.0.473.1228.3-2j1.3.0....0...1c.1.64.psy-ab..6.3.1226...0i22i30k1.0.ZWoEJpijQqs#rlfi=hd:;si:;mv:[[46.2771104,-63.1307934],[46.240161699999994,-63.1582407]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
quebeck = 'https://www.google.com/search?q=outdoor+sport+stores+in+prince+quebec&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBugZ3Dxy7AxXnbqKwBw1cA616XSpA%3A1644120730950&ei=mkr_YYW5Oa3BlwTlg6yQBA&oq=outdoor+sport+stores+in+prince+quebec&gs_l=psy-ab.12...0.0.0.13857.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.crM7Pn0DrYw#rlfi=hd:;si:;mv:[[46.9139457,-71.1589401],[46.719706099999996,-71.3603673]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'
saskatchewan = 'https://www.google.com/search?q=outdoor+sport+stores+in+prince+saskatchewan&rlz=1C1CHBF_enKE923KE927&biw=1280&bih=587&sz=0&tbm=lcl&sxsrf=APq-WBvdfgd4PKcVUB0Vrjpbfe24cuZkyg%3A1644120747410&ei=q0r_YfirGIyagQaq4aGgAg&oq=outdoor+sport+stores+in+prince+saskatch&gs_l=psy-ab.1.0.33i160k1.21746.25438.0.27493.8.8.0.0.0.0.360.1232.2-3j1.4.0....0...1c.1.64.psy-ab..4.4.1230...33i22i29i30k1.0.vkmPKL6BYGo#rlfi=hd:;si:;mv:[[55.3994911,-103.4989483],[49.5802309,-123.84813849999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e16!2m1!1e3!3sIAE,lf:1,lf_ui:10'

districts = [alberta,britishcolumbia,manitoba,newbrunswick,newfoundland,novascotia,ontario,princeedward,quebeck]

def scrapedata():
    try:
        website = driver.find_element_by_xpath("(//a[contains(@class,'ab_button CL9Uqc')])[1]").get_attribute('href')
        sportwebsite.append(website)
    except:
        website = 'N/A'
        sportwebsite.append(website)
        
    try:
        number = driver.find_element_by_xpath("//span[contains(@class,'LrzXr zdqRlf kno-fv')]").text
        sportnumber.append(number)
    except:
        number = "N/A"
        sportnumber.append(number)
        
        
def nextpage():
    driver.find_element_by_xpath("//span[contains(@style,'display:block;margin-left:53px')]").click()
    
def scrape():
    time.sleep(4)
    driver.implicitly_wait(10)
    names = driver.find_elements_by_xpath("//div[contains(@class,'dbg0pd OSrXXb eDIkBe')]")
    
    for name in names:
        sportname.append(name.text)
        
        ActionChains(driver).click(name).perform()
        time.sleep(4)
        scrapedata()
        time.sleep(1)
     
     
for i in range(0,8):
    driver.get(districts[i])
    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(@class,'B7V4Ld')]").click()

    try:
        for i in range(1,20):
            scrape()
            time.sleep(5)
            nextpage()
    except:
        pass
    
try:
    driver.get(saskatchewan)
    time.sleep(5)
    driver.find_element_by_xpath("//button[contains(@class,'B7V4Ld')]").click()

    try:
        for i in range(1,20):
            scrape()
            time.sleep(5)
            nextpage()
    except:
        pass
except:
    print('fuken sakastchewan')


data = pd.DataFrame(
    {
        'name':sportname,
        'phone':sportnumber,
        'link':sportwebsite
    }
)
#data.to_csv("sports.csv")
print(data)