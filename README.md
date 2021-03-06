# Python-SendEmail-
## 1. 설명
파이썬에서 이메일을 보내는 방법을 다룬다.
## 2. 사용법
1. EmailSend_module.py 파일을 다운받는다.
2. 파일을 프로젝트파일과 같은 경로에 추가한다.
3. 프로젝트에 아래코드를 추가한다.
<pre><code>import EmailSend_module
...
# 메일 객체 생성
mail = EmailSend_module.mail([받는 이메일], [제목], [내용])
# 보내는 사람 객체 생성
sender = EmailSend_module.sender([보내는 이메일], [보내는 이메일 비밀번호], [SMTP서버명])
# 메일 메서드 매개변수로 보내는 사람 객체 전달
mail.send(sender)</code></pre>
4. 모듈 에러시 모듈설치 필요
> cmd->pip install [모듈명]
> 사용되는 모듈: smtplib, email
## 3. 사용 예시
<pre><code>import EmailSend_module

sender_ID = 'clone55@gmail.com'
sender_PW = 'clone55Password'
sender_Provider = 'gmail.com'

receiver_ID = 'clone66@gmail.com'

send_contents = 'Hello Clone66!!'
send_title = 'From Clone55'

mail = EmailSend_module.mail(receiver_ID, send_title, send_contents)
sender = EmailSend_module.sender(sender_ID, sender_PW, sender_Provider)
mail.send(sender)

## 4. 설명
import EmailSend_module는 모듈파일을 프로젝트에 추가하는 역할이다.
EmailSend_module.run()함수는 메일을 보내는 함수다.
sender_ID: 보내는 사람의 이메일 ex)clone55@gmail.com
sender_PW: 보내는 사람의 비밀번호 ex)password55
sender_Provider: 보낸는 사람의 SMTP서버명 ex)gmail.com
receiver_ID: 받는 사람의 이메일
send_contents: 이메일 내용 ex)hello
send_title: 이메일 제목 ex)From python
