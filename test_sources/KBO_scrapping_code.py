import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from io import StringIO
import time

T = time.time()
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx" # 크롤링할 사이트 url
save_path = "./datasets/데이터2.xlsx" # 파일 저장 경로

years = list(range(1982, 2026))
pages = [1, 2]

driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

missing_value = {}
all_df_list = []

for year in years:
    select_year = Select(driver.find_element(By.ID, "cphContents_cphContents_cphContents_ddlSeason_ddlSeason"))
    select_year.select_by_value(str(year))
    time.sleep(0.35)
    for page in pages:
        if page == 1:
            try:
                select_page = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo1")
                select_page.click()
            except Exception as e:
                print(e)
                print(page, year)
                missing_value[page] = year
                continue

        if page == 2:
            try:
                select_page = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo2")
                select_page.click()
            except Exception as e:
                print(f'{e}')
                print("="*30)
                print(page, year)
                print("="*30)
                missing_value[page] = year
                continue
        time.sleep(0.35)
        table = driver.find_element(By.CLASS_NAME, "record_result")
        html = table.get_attribute('outerHTML')
        df_list = pd.read_html(StringIO(html))
        df = df_list[0]
        print(df.head())
        df['연도'] = year
        df['장'] = page
        all_df_list.append(df)
        time.sleep(0.7)

all_data = pd.concat(all_df_list, ignore_index=True)

all_data.to_excel(save_path, index=False)

driver.quit()
print(missing_value)

print(f'{time.time()-T} 초')