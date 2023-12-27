# EmailSubjectbasedFileDownload
Introduction :
A scrip that can be used to download files attached to emails with given Subject

I was inspired to create this script when I learned that someone had to manually download and save the files attached to the emails sent by their subordinates. I thought that this was a tedious and time-consuming task that could be automated with a simple script. This is how I came up with the idea and implemented this script.

I plan on doing changes in the future so that this will only check for files in mails sent on the day the script was run or a alteration of this which only checks unread mail.

=========================================================

WARNING: THIS WILL DOWNLOAD ANY FILES IN THE EMAILS, SO BEWARE AND BECAREFULL OF MALWARE AND OTHER UNSAFE FILES, WILL MAKE IT ONLY DOWNLOAD FILES OF GIVEN TYPE IN FUTURE UPDATE

==========================================================

How to use:
1.Use your desired code editor and open the .py file
2.Look for the section which contains the parameters which are email_host, email_user, email_password, target_subject, download_folder
3.Enter the respective details


=========================================================

Points to note:
1. In my case my email host was gmail, for which the email_host is "imap.gmail.com", you will have to find the imap for your email host
2. You may have to enable imap settings for you email account, and then generate an app password which will be used instead of your normal password
3. the target_subject must contain the email subject you are on the lookout for
4. the download folder can be a designated dowmnload address chose by you.
5. If you want to make this easier to use for a routine basis, you can make a .exe version of this file

=========================================================
   Steps to make .exe:
   1. Ensure your details are correct and that you will not require to change it again
   2. Open a command promp or terminal and go to the directory of the .py file
        This can be done by typing cd followed by the directory
        ex: cd C:\Users\xxxxx\Desktop\yyyyy
  3. Enter the following line : " pyinstaller --onefile emailfiledownload.py
  4. voila, you should be ready with your ready to use .exe file
