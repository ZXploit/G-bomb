#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class warna:
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('figlet proses pengiriman')
#Input
os.system('figlet [+] Welcome [+]')
print(warna.GREEN + 'A Simple Project Gmail Send Message By Zxc19')
print(warna.WARNING + '''
Pilih server:
1) Gmail

*Saat ini hanya ada server gmail saja karna ini project khusus gmail sender
''' + warna.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(warna.GREEN + 'Email Server: ' + warna.ENDC)
	user = raw_input(warna.GREEN + 'Masukan Email: ' + warna.ENDC)
	pwd = getpass.getpass(warna.GREEN + 'Masukan Password: ' + warna.ENDC)
	to = raw_input(warna.GREEN + 'Target: ' + warna.ENDC)
	subject = raw_input(warna.GREEN + 'Subject (Optional): ' + warna.ENDC)
	body = raw_input(warna.GREEN + 'Isi Pesan: ' + warna.ENDC)
	nomes = input(warna.GREEN + 'Jumlah Kirim Email: ' + warna.ENDC)
	no = 0
	message = 'Dari: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print warna.FAIL + '\nProses Di Batalkan' + warna.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print warna.FAIL + '''Email Atau Password Kamu Salah!! atau silahkan kamu melakukan perizinan pada gmail: https://myaccount.google.com/lesssecureapps' ''' + warna.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print warna.WARNING + 'Berhasil Mengirim ' + str(no+1) + ' email' + warna.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print warna.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Gagal Mengirim "
			server.close()