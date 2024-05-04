from flask import *
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
app = Flask(__name__)
yy='azertyuiopmlkjhgfdsqwxcvbn'
@app.route("/")
def ap():
    email = request.args.get("email")
    if '@' in email:
        m = check_gmail(email)
    try:
        return(m)
    except:
        return("None")
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    cookies = {
      '__Host-GAPS': host,
  }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["AEThLlz4luDk2yFWsQRU_KlZsoYtu6wNeZxocOIcj1BG20WA078YKjPYBHlgL8qq82PZDts7UWS0jQ2QmOU-Fh9UrfhgvRXgjlgxmWn2VptjYAi-emfCuzIezrd4IbKkWLbdSPxnA_mTSmtNVuiqJU_VZfR-KE3MtZf8qft2oqLdafTBloXqbn65aQv_o_DuwIR7pG6MmB_g","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data
  )
    print(response.text)
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    print(tl)
    print(host)
    return tl,host
  except Exception as e:
    print(e)
    tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    tl,host=tll()
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,proxies = {
"https":"http://1pbojyp6x45ccdi:cusks5nlvup5477@rp.proxyscrape.com:6060"}
  );print(response.text)
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '[["gf.uar",2' in response.text or 'gf.uar",3' in response.text:
        return 'bad'
    else:
        return(response.text)
  except Exception as e:
      e = f"this is error{e}"
      return(e)
app.run(host="0.0.0.0",port=8080)
