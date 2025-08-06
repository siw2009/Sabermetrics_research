"""import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from io import StringIO

# 1. 드라이버 경로와 url 설정
driver_path = "D:\\Repositories\\rne\\test_sources\\chromedriver-win64\\chromedriver.exe"  # 본인 chromedriver.exe 경로로 수정
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx"

# 2. 연도, 장 정보
years = list(range(1982, 2026))  # 1982~2025
pages = [1, 2]               # 각 연도의 두 장

# 3. 웹드라이버 열기
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)  # 초기 로딩

all_df_list = []

for year in years:
    # 연도 선택 (드롭다운의 id/name은 실제로 확인 후 맞게 수정)
    select_year = Select(driver.find_element(By.ID, "cphContents_cphContents_cphContents_ddlSeason_ddlSeason"))  # 연도 셀렉터 id확인
    select_year.select_by_value(str(year))
    time.sleep(0.6)
    for page in pages:
        if page == 1:
            select_page = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo1") # 장 셀렉터 id확인
            select_page.click()
        if page == 2:
            select_page = driver.find_element(By.ID, "cphContents_cphContents_cphContents_ucPager_btnNo2") # 장 셀렉터 id확인
            select_page.click()
        time.sleep(0.6)
        # 표 가져오기
        table = driver.find_element(By.CLASS_NAME, "record_result") # 실제 표의 id/class 확인
        html = table.get_attribute('outerHTML')
        print(html)
        df = pd.read_html(StringIO(html))[0]
        df['연도'] = year
        df['장'] = page
        all_df_list.append(df)
        time.sleep(0.7)  # 서버 과부하 방지
        print(year, page, '!!!!')

# 4. 전체 데이터 DataFrame로 합치기
all_data = pd.concat(all_df_list, ignore_index=True)

# 5. 엑셀로 저장
save_path = "D:\\Repositories\\rne\\test_sources\\save_file"
all_data.to_excel(save_path, index=False)

driver.quit()
print(f"모든 작업 완료! {save_path} 에 저장되었습니다.")"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from io import StringIO

driver_path = "D:\\Repositories\\rne\\test_sources\\chromedriver-win64\\chromedriver.exe"
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
                
                print(f"연도 {year}는 2페이지가 없습니다. 넘어갑니다.")
                continue

        time.sleep(1.5)

        
        table = driver.find_element(By.CLASS_NAME, "record_result")
        html = table.get_attribute('outerHTML')

        try:
            df_list = pd.read_html(StringIO(html))
            if len(df_list) == 0:
                print(f"연도 {year} 페이지 {page}에서 테이블을 찾지 못했습니다.")
                continue
            df = df_list[0]
            print(df.head())
        except Exception as e:
            print(f"연도 {year} 페이지 {page}에서 테이블 파싱 중 오류: {e}")
            continue

        df['연도'] = year
        df['장'] = page
        all_df_list.append(df)
        time.sleep(0.7)

all_data = pd.concat(all_df_list, ignore_index=True)
save_path = "D:\\Repositories\\rne\\test_sources\\save_file\\테스트.xlsx"
all_data.to_excel(save_path, index=False)

driver.quit()
print(f" {save_path} 에 저장됨.")
