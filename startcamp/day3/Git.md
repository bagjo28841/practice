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

명령어는 공백으로 구분 -> 항상 띄어쓰기 하고 명령어 써야함



수정(초록색 바 표시), 삭제(빨강색 세모 표시)

----

1. **git init** 시점 초기화가 제일 먼저 

   -> 꼭 (master)가 생겨야함!= 내가 git의 관리를 받고있구나, 이게 있는지 늘 확인할것 

   (브랜치의 가장 기본 이름이 master)

   **git status** On branch master No commits yet Untracked files: (아직 추가안됨)

2. **add** (staging area(=INDEX)에 추가해야 들어감)

   개인 key 등 올리지 말아야 할 것들도 있음! -> add하기 전에 숨김파일 **.gitignore**로 미리 등록!!

   현재 아래의 전체를 다 추가하려면 git add .

   git add startcamp/ 로도 가능

3. **commit**  git commit -m "first commit" 커밋하고

   git status 다시 확인(중간중간 계속 확인할 것)

   commit은 status에 안보이니까 git log로 확인

4. **github**에 업로드

```
git remote add origin https://github.com/bagjo28841/practice.git
```

origin이라는 remote저장소(https://github.com/bagjo28841/practice.git)에 추가(연결)

-> 로컬에 있는 이 폴더랑 온라인(깃허브 레파지토리) 연결

git에 복붙해서 적용하고 git remote -v로 확인해보면 origin이라는 곳에 push할 예정(연결됨)

repository의 처음  push는 git push -u origin master 써줘야함

(두번째 변경사항부터는 git push만 해줘도 됨)

origin이라는 주소에 master branch로 올리겠다

연결 잘못했다면 rm (remove) 가능

> 추가사항:
>
> global 마다 한개의 계정만 가능
>
> windows에서 자격 검색 - 자격 증명 관리 - windows 자격 증명 - 편집/제거 가능
>
> 오프라인에서 다른 사람 컴퓨터를 쓰게 되면 제거하고 push 해야함

5. **branch**



