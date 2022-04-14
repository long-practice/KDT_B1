# KDT_B1


# 모듈 설치, 환경 설정


# 데이터 전처리
- 화자별 디렉토리 내에 있는 디렉토리를 각각 지정하여 전처리를 진행
- 예를 들어 남1에 남1_소설1, 남1_동화1, 남1_어학1과 같이 3가지 디렉토리가 있으면 아래와 같이 전처리 진행

  ` python preprocess.py --num-workers [화자 수] --name build --in_dir ./kaist-audio-book/wav/남1/남1_소설1 out_dir ./kaist-audio-book/wav/남1/남1_소설1 ` <br>
  ` python preprocess.py --num-workers [화자 수] --name build --in_dir ./kaist-audio-book/wav/남1/남1_동화1 out_dir ./kaist-audio-book/wav/남1/남1_동화1 ` <br>
  ` python preprocess.py --num-workers [화자 수] --name build --in_dir ./kaist-audio-book/wav/남1/남1_어학1 out_dir ./kaist-audio-book/wav/남1/남1_어학1 `

# 모델 학습
- Tacotron2 학습

  ` python train_tacotron2.py `<br>
<br>

- Vocoder 학습

  ` python train_vocoder.py`
