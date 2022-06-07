# KDT_B1

- **동화책 읽어주는 AI 모델 머찌니** <br>
- 다양한 목소리로 동화책을 읽어주는 모델
- 주요기술: TTS(Text To Speech)<br>
<br>

# 데이터
- 카이스트 오디오북 데이터 셋(https://aihub.or.kr/opendata/kaist-audiobook)
  - 총 58,559개의 wav 음성 파일 (44.1kHz, mono)
  - 영어 제외 총 11명의 화자에 대한 음성 데이터
  - 70시간 내외의 음성 길이
  - 음성 데이터 녹음시 각 장르에 맞는 내레이션 기법 및 정확한 감정선이 표현될 수 있도록 오디오 연출<br>
<br>


# 모듈 설치, 환경 설정


# 데이터 전처리
- 데이터 전처리는 `./kaistaudiobook/build.py`확인
  1. Rescaling: 모든 값들을 -1 ~ 1 사이로 정규화
  2. Trimming: 앞뒤 음성이 나오지 않는 부분을 삭제
  3. 16비트 음성데이터를 8비트로 변환
  4. 최종적으로 멜스펙트로그램과 선형 스펙트로그램을 생성, npy파일 생성
  5. 기존 음성 값, 멜스펙트로그램, 선형 스펙트로그램 값을 npz파일로 저장<br>
<br>

- 화자별 디렉토리 내에 있는 디렉토리를 각각 지정하여 전처리를 진행
- 예를 들어 m1에 m1_novel1, m1_fairytale1, m1_language_study1과 같이 3가지 디렉토리가 있으면 아래와 같이 전처리 진행
  ` python preprocess.py --name build --in_dir ./kaist-audio-book/wav/m1/m1_novel1 out_dir ./kaist-audio-book/wav/m1/m1_novel1 ` <br>
  ` python preprocess.py --name build --in_dir ./kaist-audio-book/wav/m1/m1_fairytale1 out_dir ./kaist-audio-book/wav/m1/m1_fairytale1 ` <br>
  ` python preprocess.py --name build --in_dir ./kaist-audio-book/wav/m1/m1_language_study1 out_dir ./kaist-audio-book/wav/m1/m1_language_study1 `

# 모델 학습
- Tacotron2 학습

  ` python train_tacotron2.py `<br>
<br>

- Vocoder 학습

  ` python train_vocoder.py`
  
<br> 

# 웹 페이지 구성

https://github.com/long-practice/KDT_B1_2
