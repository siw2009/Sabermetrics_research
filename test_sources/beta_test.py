import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score

# 1. 가상 데이터 생성 (100명 타자)
np.random.seed(42)
n = 100
data = pd.DataFrame({
    'OBP': np.random.uniform(0.25, 0.45, n),      # 출루율
    'SLG': np.random.uniform(0.30, 0.60, n),      # 장타율
    'ISO': np.random.uniform(0.05, 0.25, n),      # 순수 장타력 (SLG - AVG 대체)
    'BB_K': np.random.uniform(0.2, 1.5, n),       # 볼넷/삼진 비율
    'BABIP': np.random.uniform(0.25, 0.4, n),     # 인플레이 타구 안타 비율
    'is_hit': np.random.binomial(1, 0.28, n)      # 실제 안타 여부 (0 or 1, 28% 확률로)
})

# 2. 학습용 / 테스트용 분할
X = data.drop(columns=['is_hit'])
y = data['is_hit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 3. 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. 예측 및 평가
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

print("정확도:", accuracy_score(y_test, y_pred))
print("AUC:", roc_auc_score(y_test, y_pred_proba))

# 5. 새 타자 예측 예시
new_player = pd.DataFrame({
    'OBP': [0.38],
    'SLG': [0.52],
    'ISO': [0.19],
    'BB_K': [1.2],
    'BABIP': [0.34]
})
prob = model.predict_proba(new_player)[0,1]
print("예측된 안타 확률 (Hit Probability):", round(prob, 3))
