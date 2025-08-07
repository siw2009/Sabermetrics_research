주제 : 야구에서의 새로운 평가 선수지표 만들기

### 참고 문헌
~~[로지스틱 회귀 - wikipedia](http://ko.wikipedia.org/wiki/%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1_%ED%9A%8C%EA%B7%80)~~ -> [이게더 이해하기 쉬움](https://wikidocs.net/22881)\
-> 그래도 이해 안되면 딥러인 개념 이해용 영상들을 보면 됨  

[모르는 용어있을때 검색 - 머신러닝 용어집](https://developers.google.com/machine-learning/glossary?hl=ko)

[pandas참조용 - pandas공식](https://pandas.pydata.org/docs/reference/index.html)

[회귀계수 해석법 - tistory](https://bluediary8.tistory.com/157)\
[크로스 엔트로피 함수](https://velog.io/@rcchun/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%81%AC%EB%A1%9C%EC%8A%A4-%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BCcross-entropy)\
[베르누이 분포](https://datascienceschool.net/02%20mathematics/08.02%20%EB%B2%A0%EB%A5%B4%EB%88%84%EC%9D%B4%EB%B6%84%ED%8F%AC%EC%99%80%20%EC%9D%B4%ED%95%AD%EB%B6%84%ED%8F%AC.html)


### 딥러닝 개념 이해용{아래부터 보는걸 추천}
[트렌스포머](https://youtu.be/g38aoGttLhI?si=6FR8NSpRfclspLd8)\
[백프로파게이션2](https://youtu.be/HKqdFQfXVhw?si=OKyEVeNtblkSvkPf)\
[백프로파게이션](https://youtu.be/tkH7KgLZc0E?si=YYTlYq7MbtqdE1qd)\
[경사하강법](https://youtu.be/8861RzFOFs8?si=kK6KAGg5YuiTHf3d)\
[뉴럴네트워크](https://youtu.be/wrguEHxk_EI?si=SAo0gbOsBtzyahrB)\
[LLM](https://youtu.be/HnvitMTkXro?si=0atF_nHY-4EwcTTa)\
[어텐션](https://youtu.be/_Z3rXeJahMs?si=ieoN6M-nCKcM03aB)

---
## 지금 해야되는 일
 - [ ] 할일/ 배울것 정리하기


## 역할
 - 석현 : 총괄
 - 동현 : 모델 구현
 - 인우 : 모델 구현
 - 시온 : 데이터 전처리

---
## 단계
1. 세이버 메트릭스 지표선정
	- 효과적인 변수 식별
2. 로지스틱 회귀모델을 통한 HPA 산출 방법론 개발
	- 안타와 비안타를 종속변수
	- 세이버 메트릭스 데이터를 독립변수
	- HPA 계산 공식(할푼리 형태) -> 회귀계수 해석으로 알아냄
	- 성능 검증 -> 실제 야구선수로 성능검증?
3. 기존 타율과 개발된 HPA의 성능비교
	 - **컨택 히터**나 장타자 등 특정 유형의 타자에 따라 차별적인 가치를 지니는지 비교
	 - HPA활용될 수 있는 방안 찾기
