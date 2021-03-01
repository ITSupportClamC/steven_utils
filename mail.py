# coding=utf-8
# 
# send email, with or without attachments.
# 

from os.path import join
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.message import EmailMessage
from steven_utils.file import getFilenameWithoutPath
import logging
logger = logging.getLogger(__name__)



def sendMail(msgText, subject, sender, recipients, mailServer, timeout):
	"""
	Send email to recipients.
	[String] msgText
	[String] subject
	[String] sender (the address that appears in 'from' field)
	[String] recipients (a string containing comma separated addresses)
	[String] mailServer (mail server address)
	[Float] timeout (time out for mail server)
	"""
	msg = MIMEText(msgText)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = recipients

	smtp = smtplib.SMTP(mailServer, timeout=timeout)
	smtp.send_message(msg)
	smtp.quit()



def sendMailWithAttachment( msgText, attachment, subject, sender \
						  , recipients, mailServer, timeout):
	"""
	Send email to recipients.
	[String] msgText
	[String] attachment (full path to the attachment file)
	[String] subject
	[String] sender (the address that appears in 'from' field)
	[String] recipients (a string containing comma separated addresses)
	[String] mailServer (mail server address)
	[Float] timeout (time out for mail server)

	The piece of code comes from:

	https://medium.com/better-programming/how-to-send-emails-with-attachments-using-python-dd37c4b6a7fd
	"""
	def getAttachmentTypes(file):
		"""
		[String] attachment file (full path) 
			=> [Tuple] ( [String] main type
					   , [String] sub type)
		"""
		ctype, encoding = mimetypes.guess_type(file)
		if ctype is None or encoding != None:
			ctype = 'application/octet-stream'

		return ctype.split('/', 1)


	def addAttachment(file, msg):
		"""
		[String] file, [EmailMessage] msg
		"""
		maintype, subtype = getAttachmentTypes(file)

		with open(file, 'rb') as fp:
			msg.add_attachment( fp.read(), maintype=maintype, subtype=subtype
							  , filename=getFilenameWithoutPath(file))


	msg = EmailMessage()
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = recipients
	msg.set_content(msgText)
	addAttachment(attachment, msg)

	smtp = smtplib.SMTP(mailServer, timeout=timeout)
	smtp.send_message(msg)
	smtp.quit()