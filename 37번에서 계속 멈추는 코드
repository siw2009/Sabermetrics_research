import time
import pandas as pd
from selenium import webdriver
#Chrome 브라우저를 제어하는 데 필요한 브라우저 특정 행동 구성(라이브러리, 서브패키지, 서브패키지, 모듈, 클래스)
from selenium.webdriver.chrome.options import Options
#요소를 찾는 방법 (ID, NAME, CLASS_NAME 등등)
from selenium.webdriver.common.by import By
#특정 조건이 맞을 때까지 최대 지정 시간 동안 기다리는 클래스(이 코드에서는 15초)
from selenium.webdriver.support.ui import WebDriverWait
#기다릴 조건들을 정의해 놓은 함수 모음(ex. 요소가 클릭 가능할때 : element_to_be_clikable)
from selenium.webdriver.support import expected_conditions as EC
#가상 파일 생성
from io import StringIO

#옵션 설정 - '사람이면 클릭하시오' 이런거 우회할때도 쓰는데 mlb에는 다행히 그런거 없음
chrome_options = Options()
chrome_options.add_argument("window-size=1920,1080")

#객체 생성 - options = chrome_options
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

url = "https://www.mlb.com/stats/all-time-totals"
driver.get(url)


try:
    close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']")))
    close_btn.click()
    print("팝업 닫기 완료")
except:
    print("팝업 없음")

def scrape_all_pages(save_path):
    data_list = []
    page_num = 1

    while True:
        for i in range(3):
            try:
                table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bui-table")))
                rows = table.find_elements(By.CSS_SELECTOR, "tr")
                if len(rows) > 1: 
                    html = table.get_attribute("outerHTML")
                    df = pd.read_html(StringIO(html))[0]
                    break
                else:
                    print(f"[경고] Page {page_num} 빈 데이터")
                    time.sleep(1)
            except Exception as e:
                print(f"[오류] Page {page_num} 테이블 로드 실패 → 재시도 {i+1}, {e}")
                time.sleep(1)

        data_list.append(df)
        print(f"[페이지 {page_num}] 수집 행 수: {len(df)}")

        
        if page_num % 5 == 0:
            pd.concat(data_list, ignore_index=True).to_excel(save_path, index=False)
            print(f"[임시 저장] {page_num}페이지까지 저장 완료")

        try:
            first_cell = table.find_element(By.CSS_SELECTOR, " tbody tr td").text
            next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='next page button']")))
            if "disabled" in next_btn.get_attribute("class"):
                print(" 마지막 페이지 도달")
                break
            next_btn.click()
            wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "tbody tr td").text != first_cell)
            page_num += 1
        except Exception as e:
            print('이동 실패')
            break
        


print("스크래핑 시작")
save_path = "C:\\Users\\ziont\\OneDrive\\문서\\MLB.xlsx"  
all_data = scrape_all_pages(save_path)


if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_excel(save_path, index=False)
    print(f" 최종 저장 완료: {save_path} / 총 {len(final_df)}행")
else:
    print(" 수집된 데이터가 없습니다.")

driver.quit()
