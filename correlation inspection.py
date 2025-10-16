# from google.colab import drive
import pandas as pd
import matplotlib.pyplot as plt

# 1. 구글 드라이브 마운트
# drive.mount('/content/drive')

# 2. 데이터 경로 지정 (경로는 자신의 구글 드라이브 내 위치로 맞춰야 합니다)
# 예시: 'MyDrive/경로/스탯티즈.xlsx'
# file_path = '/content/drive/MyDrive/Colab Notebooks/스탯티즈.xlsx'
file_path = './datasets/스탯티즈.xlsx'

# 3. 엑셀 파일 읽기
df = pd.read_excel(file_path, engine='openpyxl')

# 4. 필요한 열만 추출
cols = ['AVG', 'OPS', 'R/ePA', 'wRC+', 'WAR']
df = df[cols]

# 5. 상관계수 계산
corr_ops = df['AVG'].corr(df['OPS'])
corr_repa = df['AVG'].corr(df['R/ePA'])
corr_wrc = df['AVG'].corr(df['wRC+'])
corr_war = df['AVG'].corr(df['WAR'])

print(f"AVG와 OPS의 상관계수: {corr_ops:.3f}")
print(f"AVG와 R/ePA의 상관계수: {corr_repa:.3f}")
print(f"AVG와 wRC+의 상관계수: {corr_wrc:.3f}")
print(f"AVG와 WAR의 상관계수: {corr_war:.3f}")

# 6. 그래프화
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
pairs = [('OPS', corr_ops), ('R/ePA', corr_repa), ('wRC+', corr_wrc), ('WAR', corr_war)]

for ax, (var, corr) in zip(axs.flatten(), pairs):
    ax.scatter(df['AVG'], df[var])
    ax.set_xlabel('AVG')
    ax.set_ylabel(var)
    ax.set_title(f'AVG vs {var} (corr={corr:.3f})')

plt.tight_layout()
plt.show()