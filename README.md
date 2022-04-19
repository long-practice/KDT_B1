# KDT_B1


# 모듈 설치, 환경 설정


# 데이터 전처리
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
