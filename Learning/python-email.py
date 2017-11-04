# -*- coding: utf-8 -*-

## smtp

import smtplib

smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
#(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')

smtpObj.starttls()
#(220, b'2.0.0 Ready to start TLS')

smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
#(235, b'2.7.0 Accepted')

smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
#{}

smtpObj.quit()
#(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')


#Provider SMTP server domain name
#Gmail                       smtp.gmail.com
#Outlook.com/Hotmail.com     smtp-mail.outlook.com
#Yahoo Mail                  smtp.mail.yahoo.com
#AT&T                        smpt.mail.att.net (port 465)
#Comcast                     smtp.comcast.net
#Verizon                     smtp.verizon.net (port 465)


## imap

import pprint
import pyzmail
import imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
#'my_email_address@gmail.com Jane Doe authenticated (Success)'

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])

print(UIDs)
#[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
#Hello!'

message.get_addresses('from')
#[('John Doe', 'john@doe.com')]

message.get_addresses('to')
#[(Jane Doe', 'jdoe@example.com')]

message.get_addresses('cc')
#[]

message.get_addresses('bcc')
#[]

print(message.text_part != None)
#True

message.text_part.get_payload().decode(message.text_part.charset)
#'Follow the money.\r\n\r\n-Ed\r\n'

print(message.html_part != None)
#True

message.html_part.get_payload().decode(message.html_part.charset)
#'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>Al<br></div>\r\n'

#Provider                IMAP server domain name
#Gmail                   imap.gmail.com
#Outlook.com/Hotmail.com imap-mail.outlook.com
#Yahoo Mail              imap.mail.yahoo.com
#AT&T                    imap.mail.att.net
#Comcast                 imap.comcast.net
#Verizon                 incoming.verizon.net

pprint.pprint(imapObj.list_folders())
#[(('\\HasNoChildren',), '/', 'Drafts'),
# (('\\HasNoChildren',), '/', 'Filler'),
# (('\\HasNoChildren',), '/', 'INBOX'),
# (('\\HasNoChildren',), '/', 'Sent'),
#--snip-
# (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
# (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)

imapObj.select_folder('INBOX', readonly=True)
imapObj.search(['ALL'])
imapObj.search(['ON 05-Jul-2015'])
imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])
imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com'])
imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])
imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])
imapObj.search(['FROM alice@example.com', 'FROM bob@example.com'])

imapObj.select_folder('INBOX', readonly=False)

UIDs = imapObj.search(['SINCE 05-Jul-2015'])
print(UIDs)
#[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

print(message.text_part != None)
#True
message.text_part.get_payload().decode(message.text_part.charset)
#'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'

print(message.html_part != None)
#True

message.html_part.get_payload().decode(message.html_part.charset)
#'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2015'])
print(UIDs)
#[40066]

imapObj.delete_messages(UIDs)
#{40066: ('\\Seen', '\\Deleted')}

imapObj.expunge()
#('Success', [(5452, 'EXISTS')])

imapObj.logout()
   
