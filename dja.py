INPUT_PATH  = "./datasets/MLB_dataset_clean.csv"   
OUTPUT_XLSX = './datasets/MLB_dataset2.xlsx'
NAME_COL = "PLAYERPLAYER"                        
NUM_COLS = ["AB","BB","SO","SB","CS","AVG"]   

# from google.colab import drive
# drive.mount('/content/drive', force_remount=True)

import os, numpy as np, pandas as pd
# from google.colab import files



def read_excel_all_sheets(path):
    xls = pd.ExcelFile(path)
    frames = []
    for sh in xls.sheet_names:
        df = pd.read_csv(path, sheet_name=sh)
        df["__sheet__"] = sh
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

if not os.path.isfile(INPUT_PATH):
    raise SystemExit(f"[ERROR] 파일을 찾을 수 없음: {INPUT_PATH}")

ext = os.path.splitext(INPUT_PATH)[1].lower()
if ext in [".xlsx",".xls"]:
    df = read_excel_all_sheets(INPUT_PATH)
elif ext == ".csv":
    df = pd.read_csv(INPUT_PATH, low_memory=False); df["__sheet__"] = "csv"
else:
    raise SystemExit(f"[ERROR] 지원하지 않는 확장자: {ext}")

print(f"[INFO] 로드 완료: {INPUT_PATH} | 행 {len(df)}  열 {len(df.columns)}")
print("[INFO] 일부 열:", df.columns.tolist()[:20])


if NAME_COL not in df.columns:
    print(f"[WARN] 이름 컬럼이 없음: {NAME_COL}  → 빈 컬럼 생성")
    df[NAME_COL] = pd.NA

for c in NUM_COLS:
    if c not in df.columns:
        print(f"[WARN] 수치 컬럼이 없음: {c}  → 빈 컬럼 생성")
        df[c] = pd.NA
    df[c] = pd.to_numeric(df[c], errors="coerce")


AB = "AB"; BB = "BB"; SO = "SO"; SB = "SB"; CS = "CS"

def safe_ratio(num, den):
    den2 = den.replace(0, np.nan)
    return num / den2

den_ab_bb = df[AB] + df[BB]
den_sb_cs = df[SB] + df[CS]

df["BBBB/(ABAB+BBBB)"]         = safe_ratio(df[BB], den_ab_bb)
df["SOSO/(ABAB+BBBB)"]         = safe_ratio(df[SO], den_ab_bb)
df["(SBSB+CSCS)/(ABAB+BBBB)"]  = safe_ratio(den_sb_cs, den_ab_bb)
df["SBSB/(SBSB+CSCS)"]         = safe_ratio(df[SB], den_sb_cs)


ratio_cols = ["BBBB/(ABAB+BBBB)","SOSO/(ABAB+BBBB)","(SBSB+CSCS)/(ABAB+BBBB)","SBSB/(SBSB+CSCS)"]
keep_cols  = [NAME_COL] + NUM_COLS + ratio_cols + [c for c in ["__sheet__"] if c in df.columns]

result = df[keep_cols].copy()



drop_subset = [NAME_COL, AB, BB, SO, SB, CS] + ratio_cols
existing = [c for c in drop_subset if c in result.columns]
before = len(result)
# result = result.dropna(subset=existing, how="any")
after = len(result)
print(f"[INFO] 결측 제거: {before} → {after} 행")

os.makedirs(os.path.dirname(OUTPUT_XLSX), exist_ok=True)
with pd.ExcelWriter(OUTPUT_XLSX) as w:
    result.to_excel(w, index=False, sheet_name="result")

print(f"[DONE] 드라이브 저장 완료 → {OUTPUT_XLSX} (행 {len(result):,}개)")
# files.download(OUTPUT_XLSX)
