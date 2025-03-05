#Importing the library
import PyPDF2
import pandas as pd
import re

#Creating PDF object and save in variable 
pdfFileObj = open(r"creditcard.pdf",'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)

# extracting text from page 
txt = pageObj.extractText()
#print(txt)
# closing the pdf file object 
pdfFileObj.close()

#Extracting Pay Date
def extract_pay_date(txt):
    pay_date = re.findall('due\s*on\s*:\s*([0-9]{2}\s*[A-z]+\s*[0-9]{4})', txt)[0]
    return pay_date

#Extracting Customer Number
def extract_cust_num(txt):
    cust_num = re.findall('Customer\s*Number\s*([0-9]+)',txt)[0]
    return cust_num
#Extracting Amount Due
def extract_amt(txt):
    amt = re.findall('Amount([$0-9.]+)',txt)[1]
    return amt

#Extracting Credit Card Limit
def extract_card_lim(txt):
    card_lim = re.findall('Card\s*Limit([0-9]+)',txt)[0]
    return card_lim

#Extracting Card Number
def extract_card_num(txt):
    card_num = re.findall('Card\s*Number([0-9*]+)',txt)[0]
    return card_num
#Extracting Customer Name¶
def extract_name(txt):
    date = extract_pay_date(txt)
    name = re.findall('%s([A-z\s*]+)'%date,txt)[0]
    return name

#Appending extracted values in a list
name, card_num, card_lim, amt, cust_num, pay_date = ([] for i in range(6))

name.append(extract_name(txt))
card_num.append(extract_card_num(txt))
card_lim.append(extract_card_lim(txt))
amt.append(extract_amt(txt))
cust_num.append(extract_card_num(txt))
pay_date.append(extract_pay_date(txt))


d = {
    'Customer Name': name,
    'Card Number': card_num,
    'Card Limit': card_lim,
    'Amount Due': amt,
    'Customer Number': cust_num,
    'Pay Date': pay_date
}
print(pd.DataFrame(d))
#pay_date.append(extract_pay_date(txt))
print("Done")
