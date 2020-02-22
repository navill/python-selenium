# google_search.py
- Google에 접속하여 자동으로 검색어 입력
- HtmlTestRunner를 이용해 unittest 결과를 HTML로 출력
    ```python
    # HtmlTestRunner 설치
    $ pip install html-testRunner
    # unittest의 결과를 저장할 디렉토리
    $ mkdir reports
    ```


# 자동 로그인(POM_project/login.py)
- 자동으로 페이지에 접속하여 아이디 및 패스워드 입력
- 접속한 페이지에서 로그아웃
    - Expected Conditions: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions