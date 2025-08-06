import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from io import StringIO

driver_path = "C:\\Users\\ziont\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)

years = list(range(1982, 2026))
pages = ['1', '2']

all_df_list = []

for year in years:
    select_year = Select(driver.find_element(By.ID, "cphContents_cphContents_cphContents_ddlSeason_ddlSeason"))
    select_year.select_by_value(str(year))
    time.sleep(1.5)

    for page in pages:
        if page == '1':
            try:
                btn = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo1")
                btn.click()
            except Exception as e:
                print(f"연도 {year} 페이지 1 버튼 클릭 실패: {e}")
               
        elif page == '2':
            try:
                btn = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo2")
                btn.click()
            except Exception:
                
                print(f"연도 {year}는 2페이지가 없음.")
                continue

        time.sleep(1.5)

        
        table = driver.find_element(By.CLASS_NAME, "record_result")
        html = table.get_attribute('outerHTML')

        try:
            df_list = pd.read_html(StringIO(html))
            if len(df_list) == 0:
                print(f"연도 {year} 페이지 {page}에서 못찾음.")
                continue
            df = df_list[0]
            print(df.head())
        except Exception as e:
            print(f"연도 {year} 페이지 {page}에서 오류: {e}")
            continue

        df['연도'] = year
        df['장'] = page
        all_df_list.append(df)
        time.sleep(0.7)

all_data = pd.concat(all_df_list, ignore_index=True)
save_path = "C:\\Users\\ziont\\OneDrive\\문서\\R&E\\R&E데이터.xlsx"
all_data.to_excel(save_path, index=False)

driver.quit()
print(f" {save_path} 에 저장됨.")
