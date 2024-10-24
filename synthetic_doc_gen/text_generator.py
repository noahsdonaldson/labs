from faker import Faker
import random
import inflect

fake = Faker()

def fullName():
    name = fake.unique.name()
    return name

def createDate():
    date = fake.date()
    return date

def shortSentence():
    sentence = fake.sentence(3)
    return sentence
    

def dollarAmount():
   amount_left = fake.random_int(min=100, max=1000)
   amount_right = ".00"
   amount = str(amount_left) + amount_right
   return amount

def writtenAmount(amount):
   p = inflect.engine()
   p.number_to_words(amount)
   written_amount = p.number_to_words(amount) + " dollars and zero cents"

   return written_amount


def address():
  number = ''.join(random.choices('0123456789', k=3))
  st = fake.street_name()

  return number+" "+st

def cityStateZip():
  city = fake.city()
  state = fake.state()
  postal = fake.postalcode()

  return city+" "+state+" "+postal

def checkNumber():
  check = ''.join(random.choices('0123456789', k=4))
  return check

def accountNumber():
  account = ''.join(random.choices('0123456789', k=8))
  return account

def batesNumber():
  basesnumber = ''.join(random.choices('abcdefg' + '0123456789', k=12))
  batesnumber = "Bates Number: " + basesnumber
  return batesnumber

def deposit_name():
  name = fake.sentence(2)
  return name

def cash_drawer():
    cash_drawer = fake.random_int(min=1, max=100)
    if cash_drawer < 9:
        cash_drawer = "00" + str(cash_drawer)
    elif cash_drawer < 99:
         cash_drawer = "0" + str(cash_drawer)
    else:
        cash_drawer = str(cash_drawer)
    return cash_drawer

def user():
   user = fake.random_int(min=111111, max=999999)
   user = "v" + str(user)
   return user

def random_text():
    rnd_1 = random.randint(11, 99)
    rnd_2 = random.randint(11111111, 99999999)
    rnd_3 = random.randint(11, 99)
    rnd_4 = random.randint(11, 99)
    rnd_5 = random.randint(1,9)
    rnd_int = random.randint(1, 25)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rnd_letter = alphabet[rnd_int]
    random_text = str(rnd_1) + "     " + str(rnd_2) + "    " + rnd_letter + " "+ str(rnd_3) + ":" + str(rnd_4) + ":" + str(rnd_5)+ " "  + rnd_letter + " " + rnd_letter + " " + rnd_letter
    return random_text

def depositAmount():
   amount_left = fake.random_int(min=1000, max=10000)
   amount_right = ".00"
   amount = str(amount_left) + amount_right
   return amount