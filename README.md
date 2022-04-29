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


<br>


### batch.py
- wav 파일을 일관 이동 및 일괄 이름 변경을 위한 프로그램
- python batch.py -p {파일이 존재하는 폴더경로} -n {파일이 저장될 폴더 이름}
- 저장될 경로는 이미 지정되어 있고 해당 경로에 {파일이 저장될 폴더 이름} 폴더를 만들고(이미 있다면 그대로 사용) {파일이 존재하는 폴더경로} 에서 가져온 순으로 번호를 붙여 저장한다.
