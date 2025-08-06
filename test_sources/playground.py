import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 1. 드라이버 경로와 url 설정
driver_path = "C:\\Users\\ziont\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # 본인 chromedriver.exe 경로로 수정
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx"

# 2. 연도, 장 정보
years = list(range(1982, 2026))  # 1982~2025
pages = ['1', '2']               # 각 연도의 두 장

# 3. 웹드라이버 열기
driver = webdriver.Chrome(driver_path)
driver.get(url)
time.sleep(3)  # 초기 로딩

all_df_list = []

for year in years:
    # 연도 선택 (드롭다운의 id/name은 실제로 확인 후 맞게 수정)
    select_year = Select(driver.find_element(By.NAME, "cphContents_cphContents_cphContents_ddlSeason_ddlSeason"))  # 연도 셀렉터 id확인
    select_year.select_by_value(str(year))
    time.sleep(1.5)
    for page in pages:
        select_page = Select(driver.find_element(By.CLASS_NAME, "")) # 장 셀렉터 id확인
        select_page.select_by_value(page)
        time.sleep(1.5)
        # 표 가져오기
        table = driver.find_element(By.NAME, "cphContents_cphContents_cphContents_ddlSeason_ddlSeason") # 실제 표의 id/class 확인
        html = table.get_attribute('outerHTML')
        df = pd.read_html(html)[0]
        df['연도'] = year
        df['장'] = page
        all_df_list.append(df)
        time.sleep(0.7)  # 서버 과부하 방지

# 4. 전체 데이터 DataFrame로 합치기
all_data = pd.concat(all_df_list, ignore_index=True)

# 5. 엑셀로 저장
save_path = r"C:\Users\ziont\OneDrive\문서\R&E\R&E데이터.xlsx"
all_data.to_excel(save_path, index=False)

driver.quit()
print(f"모든 작업 완료! {save_path} 에 저장되었습니다.")