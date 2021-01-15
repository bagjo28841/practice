### Shell

---

운영체제와 소통하는 수단, 인터페이스 ex) 마우스

셀에는 Bash (리눅스, 유닉스) / 프롬프트(윈도우)

## Git

---

분산 버전관리 시스템 - 코드 버전 관리 용이(최종최종의최종..)

3년전 MS가 인수해서 더 성장해옴

- 역사를 기록하기 때문에 문제가 생겼을 때 과거로 돌아갈 수 있음
- 과거 버전과 지금 버전을 비교해서 차이점을 알려줌(추가/삭제된 부분)
- 차이가 무엇인지, 수정이유 등을 log로 남길 수 있고,
- 현재 파일들을 안전한 상태로 과거 모습으로 복원도 가능,
- 각 버전별로 차이점만 저장해서 사이즈도 크지 않음!

#### Git 작업 흐름

Working directory(지금 작업한 파일)-- add명령어로 추가(버전관리 맡아줘) --> INDEX(staging area 볼 수 없고 깃이 가지고 있는 공간, 우리가 보는 화면에는 변화 없음) --commit(전체x, create a snapshot)--> HEAD(쌓인 커밋들) --push(로컬-> 온라인)--> Github(온라인)

```python
$ git add helloworld.py
$ git commit -m #메세지
$ git config --global user.name"John" #관리자
# - shortname -- longname
```

README 개발자 약속

1. 오픈소스(모두가 같이 만들어감) 프로젝트 - Tensorflow
2. 개발자의 이력서 & 연습장 

git을 기반으로 한 서비스 - github(개인only), gitlab(SSAFY), bitbucket

터미널 명령어 뿐 아니라 다른 걸로도 할 수 있지만(SourceTree 등) 터미널로 씁니다

Ctrl L 화면 clear

shell을 사용할때 가장 중요한 건 경로! 원하는데까지 들어가서 우클릭해야함

----

1. **git init** 시점 초기화가 제일 먼저 -> 꼭 (master)가 생겨야함! 있는지 늘 확인할것

   (브랜치의 가장 기본 이름이 master)

   **git status** On branch master No commits yet Untracked files: 

2. add

3. branch