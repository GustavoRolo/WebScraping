import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Configurações do servidor SMTP

class EmailSettings:

    def ProsendEmailduct(textProduct):
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        SMTP_USERNAME = 'gustavorolo69@gmail.com'
        SMTP_PASSWORD = 'ffqwmzmebrosqzwh'

        # Cria a mensagem
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = 'gustavorolo69@gmail.com'
        msg['Subject'] = 'Atualização de Produtos'

        # Adiciona o corpo do e-mail
        body = textProduct
        msg.attach(MIMEText(body, 'plain'))


        # Conecta no servidor SMTP
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Envia a mensagem
        smtp_server.sendmail(SMTP_USERNAME, 'gustavorolo69@gmail.com', msg.as_string())

        # Desconecta do servidor SMTP
        smtp_server.quit()

