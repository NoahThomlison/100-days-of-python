from selenium import webdriver

chrome_driver_path = r"C:\Users\User\Documents\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.ca/dp/B089DTMHW4/ref=ods_gw_tpr_apr_d_h1_vicc_sr/?pf_rd_r=V162C5JKRC2F6VD84M5M&pf_rd_p=fd2d7a5b-5333-49d1-9797-6c63416a6e5c&pd_rd_r=21833713-ca30-4269-abbe-667638407b34&pd_rd_w=lgE27&pd_rd_wg=bLuCD&ref_=pd_gw_unk")
price = driver.find_element_by_class_name("a-price-whole")
print(price)