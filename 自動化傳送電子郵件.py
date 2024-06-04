import smtplib #smtplib 用於發送電子郵件
from email.mime. multipart import MIMEMultipart
from email.mime. text import MIMEText

#email.mime.multipart.MIMEMultipart & email.mime.text.MIMEText 用於構建電子郵件內容

def send_email(subject, body, to_email):
    from_email  = "gmail"
    app_password =  "password"


    # 創建郵件對象
    msg = MIMEMultipart() #MIMEMultipart() 創建郵件對象，允許添加文本跟附件
    msg['From'] =  from_email#設置發件人
    msg['To'] = to_email#收件人
    msg['Subject'] = subject#主題


    # 添加郵件內容
    msg.attach(MIMEText(body, 'plain'))#將郵件正文改為純文本

    try: # 使用 Gmail 的 SMTP 伺服器發送郵件
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # 開啟安全連接
        server.login(from_email, app_password)  # 登錄
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)  # 發送郵件
        server.quit()  # 關閉連接
        print("Email sent successfully!")
    except Exception as e:#過程中發生異常時，會產生一個 Exception 物件，代號e
        print(f"Failed to send email: {e}")

# 開始
subject = "Test Email"
body = "This is a test email sent from Python."
to_email = "recipient_email@example.com"

send_email(subject, body, to_email)