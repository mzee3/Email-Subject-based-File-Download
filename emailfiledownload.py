#imaplib module is used for imap (internet message access protocol)
#email module is used to handle email messages


import imaplib
import email
import os

#user note: you will have to set up imap access in your email account so that this works
#in my use case i had to set up something called app password for it to work

#this section includes parameters needed for the script to work, the parameters are stored in variables and are called when required
email_host = "imap.gmail.com" # email provider host
email_user = "email@gmail.com" # users email id
email_password = "password" # users password for email id 
target_subject = "subject" # subject to look for in the mails
download_folder =r'C:\Users\xxxxx\Desktop\yyyyy' # file location ( r' at start denotes raw string) (enter your dest file location)

#print(email_user, email_password)

#connect to server
server= imaplib.IMAP4_SSL(email_host)
server.login(email_user, email_password)

#select inbox
server.select("INBOX")

#search mails to check for given subject
status, data = server.search(None,'(SUBJECT "%s")' % target_subject)

if status == "OK":
    #iterate through matching emails
    for num in data[0].split():
        #fetch the email
        status, data = server.fetch(num, '(RFC822)')

        #parse email
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        #check for attachments
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if filename:
                download_path = os.path.join(download_folder, filename)

                # Ensure the download folder exists
                os.makedirs(download_folder, exist_ok=True)

                # Download the attachment
                with open(download_path, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                    print(f"Attachment {filename} downloaded successfully!")

#CLose imap connection
server.close()
server.logout()