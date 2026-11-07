# 컴퓨팅 실습 — 오늘 뭐 볼까?

컴퓨팅 실습 수업의 10강 과제로 만든 영화 취향 대시보드입니다.

- 영화 100편의 장르와 과제용 예시 평점을 CSV에서 읽습니다.
- 장르·최소 평점·목록 표시 개수를 사이드바에서 선택합니다.
- 선택 조건에 맞는 전체 영화의 평점 구간별 개수를 막대·꺾은선·면적 그래프로 보여줍니다.
- 평점은 실제 관객 평가가 아닌 예시 값이며, 장르는 비교를 위한 대표 분류입니다.

## 실행

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

`streamlit_app.py`와 `movies.csv`를 같은 폴더에 두세요.

## 파일

- `streamlit_app.py`: 영화 대시보드
- `movies.csv`: 영화 100편의 제목·장르·예시 평점
- `requirements.txt`: 실행 패키지
- `10강_실습과제.ipynb`: 과제 설명·코드·진행 체크리스트

기존 9강 앱은 이번 영화 앱으로 교체했습니다. 이전 코드는 Git 커밋 이력에서 확인할 수 있습니다.

[Streamlit 앱](https://jhbae003-my-streamlit-app-streamlit-app-ekqc9z.streamlit.app/)
