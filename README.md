# 인스타그램 만들기





--------

### 공부할것 / 궁금한것
1. 간단한 리눅스 명령어들,
2. 가상환경체크??에서 python -m <- 용도
3. 파이썬 환경변수 입력/출력 방법 (.env? env.sh?)


### 개발환경 세팅 순서
1. 가상환경 설정
2. `django-admin startproject myapp .` 프로젝트 생성
3. `settings.py`에 `STATICFILES_DIRS`, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT` 경로 설정
4. 전역으로 사용될 `static 파일` 및 `template 파일` 경로 설정
5. `layout.html` 및 기타 static 파일 추가
6. `.gitignore` 추가
7. `myapp/urls.py`에 static media urlpattern 추가
8. `django-debug-toolbar` 패키지 추가 [Docs](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)
9. `myapp/settings` 파일을 개발환경과 배포환경에 맞게 분기처리하기
10. 9번 작업 후 `manage.py / asgi.py / wsgi.py` 파일의 `DJANGO_SETTINGS_MODULE` 경로 수정

### 회원유저 모델 커스텀
1. `python manage.py startapp accounts`를 통해서 accounts 앱 생성
2. `settings.py` 에서 기본 유저 모델 변경
   - `AUTH_USER_MODEL = "accounts.User"` 추가
3. `from django.contrib.auth.models import AbstractUser` 으로 User class 상속하기
    ```python
    # accounts/models.py
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class User(AbstractUser):
        webiste_url = models.URLField(blank=True)
        bio = models.TextField(blank=True)
    ```


### 앱( python manage.py startapp {앱이름} ) 생성 후 먼저 해야할 것들
1. `urls.py` 파일 생성 후 작성
    ```python
    from django.urls import path

    app_name = '{앱이름}'
    urlpatterns = []
    ```
2. `프로젝트 폴더 내 settings.py` INSTALLED_APPS 내에 로컬 앱 추가