import smtplib as SMTP


def mailSender(sender, password, receiver):
    with SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg="Your book left with no renewal options!!!")
