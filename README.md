# 인스타그램 만들기1





--------

## 작업순서
1. 가상환경 설정
2. `django-admin startproject myapp .` 프로젝트 생성
3. `settings.py`에 `STATICFILES_DIRS`, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT` 경로 설정
4. 전역으로 사용될 `static 파일` 및 `template 파일` 경로 설정
5. `layout.html` 및 기타 static 파일 추가
6. `.gitignore` 추가
7. `myapp/urls.py`에 static media urlpattern 추가
8. `django-debug-toolbar` 패키지 추가 [Docs](https://django-debug-toolbar.readthedocs.io/en/latest/index.html)
9. `myapp/settings` 파일을 개발환경과 배포환경에 맞게 분기처리하기
10. 9번 작업 후 `manage.py / asgi.py / wsgi.py` 파일 경로 수정