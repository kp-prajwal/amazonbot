import requests
import math
from bs4 import BeautifulSoup
import smtplib

#URL can be of any product
URL = 'https://www.amazon.in/dp/B07Y2Y9CR4/ref=s9_acsd_al_bw_c2_x_2_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=F8V6EPFP6CNW73MAV3ZT&pf_rd_t=101&pf_rd_p=a7a97da8-0f2b-4b09-96bd-b3f7973ededc&pf_rd_i=21474843031'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#input 
print('You can\'t send a mail to yourself in this case')
from_email= input('Enter your mail : ')
pass_word = input('Enter the password(do not worry, I would not know) : ')
to_email = input('Enter the mail of your friend/ your secondary email account : ')



def check_price():
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content,'html.parser')
  title = soup.find(id='productTitle').get_text().strip()
  price = soup.find(id='priceblock_ourprice').get_text()

  price = price[0:7]
  final_price = ''
  numbers_only = []
  
  for i in price: #To eliminate the Rs. symbol and decimals. 
    if i.isdigit():
      numbers_only.append(i)

  for i in numbers_only: #Converts string to int
    final_price+=i

  price = int(final_price)
  if price > 2400:
    send_email()

  print(title)
  print(price)



def send_email():
  server = smtplib.SMTP('smtp.gmail.com', 587 ) 
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(from_email, pass_word)
  subject = 'The Prices Fell Down!'
  body = title +'Check the link for your boat earphones product!\n The link is: \nhttps://www.amazon.in/dp/B07Y2Y9CR4/ref=s9_acsd_al_bw_c2_x_2_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=F8V6EPFP6CNW73MAV3ZT&pf_rd_t=101&pf_rd_p=a7a97da8-0f2b-4b09-96bd-b3f7973ededc&pf_rd_i=21474843031\n\nThis was sent using Python and not the Gmail Client!'
  msg= f'Subject:{subject}\n\n{body}'
  server.sendmail(
    from_email,
    to_email,
    msg
  )
  print("Email has been sent")
  server.quit()

check_price()