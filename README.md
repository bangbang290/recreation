# 레트로 워크숍 오락실 — GitHub 업로드용

이 폴더의 파일 4개를 GitHub 저장소 첫 화면(최상위)에 그대로 올리세요.
ZIP 자체나 바깥 폴더를 올리는 것이 아니라 압축을 푼 안쪽 파일 4개를 올립니다.

| 파일 | 역할 |
| --- | --- |
| app.py | Streamlit 실행 파일 |
| index.html | 게임 화면, 명대사 사진 23장, 정답, 진행요원 점수판 |
| requirements.txt | 설치할 Python 패키지 |
| README.md | 이 안내문 |

이미지는 index.html 안에 포함되어 있습니다. 별도의 이미지 폴더나 설정 폴더는 필요 없습니다.

## 1. GitHub에 처음 올리기

1. GitHub에 로그인하고 새 저장소(New repository)를 만듭니다.
2. 저장소 이름은 예를 들어 retro-workshop으로 입력합니다. 공개 범위는 사용 목적에 맞게 선택합니다.
3. Create repository를 누릅니다.
4. 빈 저장소 화면의 uploading an existing file을 누릅니다.
   이미 파일이 있는 저장소라면 Add file → Upload files를 선택합니다.
5. 압축을 푼 app.py, index.html, requirements.txt, README.md 4개를 모두 드래그합니다.
6. Commit changes를 눌러 저장합니다.
7. 저장소 첫 화면에 파일 4개가 바로 표시되는지 확인합니다.

## 2. Streamlit에 연결하기

1. https://share.streamlit.io 에서 로그인합니다.
2. Create app을 선택하고 GitHub 저장소에서 배포하는 방식을 선택합니다.
3. Repository: 방금 만든 본인 계정/retro-workshop을 선택합니다.
4. Branch: GitHub에 표시되는 기본 브랜치를 선택합니다(보통 main).
5. Main file path: app.py 를 입력합니다.
6. Advanced settings에서 Python 3.11을 선택합니다.
7. Deploy를 누르고 설치가 끝날 때까지 기다립니다.

이 패키지는 업로드할 소스 파일입니다. GitHub 업로드나 Streamlit 배포를 대신 수행한 상태는 아닙니다.

## 3. 행사 시작 전 설정

1. 게임 화면 오른쪽 위 진행요원 창 열기를 누릅니다. 팝업이 차단되면 허용합니다.
2. 진행요원 창 → 진행 설정에서 워크숍 이름, 팀 이름, 정답 배점을 설정합니다.
3. 3초 듣고 노래 맞추기는 진행 설정에 준비한 유튜브 링크를 넣으면 됩니다.
4. 빔프로젝터 연결 후 Windows + P → 확장을 선택합니다.
5. 게임 창만 빔프로젝터로 옮기고 진행요원 창은 노트북에 둡니다.

복제 모드에서는 진행요원 창의 점수와 정답이 직원들에게 보일 수 있습니다.

## 4. 포함된 게임

- 3초 듣고 노래 맞추기: 등록한 유튜브 영상을 새 탭에서 엽니다. 영상 자체가 문제 재생을 담당합니다.
- 명대사 퀴즈: 사진만 먼저 표시 → 직원들이 손들고 대사 맞히기 → 정답 공개 → 사진 아래 원문 대사 표시.
  사진과 정답 23쌍이 등록되어 있으며, 다음 문제로 넘어가면 정답은 다시 숨겨집니다.
- 세 번째 게임은 준비 중 표시입니다. 웹캠 기능은 아직 포함하지 않았습니다.

점수와 미공개 정답은 진행요원 전용 창에서 확인합니다.
같은 PC의 두 창을 사용하는 방식이며, 서로 다른 PC의 진행요원과 점수를 공유하지 않습니다.
계정 기반 보안 기능이 아니라 행사 화면을 나누는 기능입니다.
설정·점수는 현재 브라우저에 저장됩니다. 행사 전후 진행 설정에서 백업을 다운로드하세요.

## 5. 업로드 전 바로 확인

index.html을 Chrome 또는 Edge에서 열면 게임 화면을 바로 사용할 수 있습니다.
Streamlit 로컬 실행이 필요하다면 Python 3.11 환경에서 다음을 실행합니다.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 공식 안내

- GitHub 파일 업로드: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Streamlit 배포: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
