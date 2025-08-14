import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO

url = "https://www.mlb.com/stats/all-time-totals"


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get(url)
# 팝업 제거
try:
    close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']")))
    close_btn.click()
    driver.implicitly_wait(10)
except Exception:
    pass

data_list = []
def scrape_all_pages():
    global data_list
    page_num = 1
    
    while True:
        # for i in range(3):
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bui-tableis-desktop-HChWpztF")))
        time.sleep(0.5)
        table = driver.find_element(By.CLASS_NAME, "table-wrapper-mxbeN3qL")
        print('aaaaaaaaaaaaaaaaaaaaaaa')
        print((type(table)))
        html = table.get_attribute('outerHTML')
        df = pd.read_html(StringIO(html))[0]
        print(df)

            # if not df.empty: 
            #     break
            # else:
            #     print(f"")
            #     time.sleep(1)

        data_list.append(df)
        print(f"[페이지 {page_num}] 행 개수: {len(df)}")

        
        try:
            next_btn = driver.find_element(By.CLASS_NAME, "button-E_ZPKDKlpaginationSide-hjd48DIF")
            if 'disabled' in next_btn.get_attribute('class'):
                print("마지막 페이지")
                break
            
            
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-E_ZPKDKlpaginationSide-hjd48DIF')))
            next_btn.click()
            page_num += 1

            
            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bui-table")))
        except Exception:
            print("끝")
            break

    return data_list

print("스크래핑 시작")
all_data = scrape_all_pages()

# ===== 저장 =====
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    save_path = "./datasets/MLB_dataset.xlsx"
    final_df.to_excel(save_path, index=False)
    print(f"데이터 저장 완료: {save_path} / 총 {len(final_df)}행")
else:
    print(" 수집된 데이터가 없습니다.")

driver.quit()
