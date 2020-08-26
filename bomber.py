# imports
try:
    from termcolor import colored, cprint
    import requests, random, time, os
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    print('\n' + ':/' + "\nError: Error: some dependencies are not installed!\nPrint 'pip install -r requirements.txt'")
    exit()
# print logo
cprint(
'''
  /$$$$$$  /$$                         /$$          
 /$$__  $$|__/                        | $$          
| $$  \__/ /$$ /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$ 
|  $$$$$$ | $$| $$_  $$_  $$ /$$__  $$| $$ /$$__  $$
 \____  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$| $$$$$$$$
 /$$  \ $$| $$| $$ | $$ | $$| $$  | $$| $$| $$_____/
|  $$$$$$/| $$| $$ | $$ | $$| $$$$$$$/| $$|  $$$$$$$
 \______/ |__/|__/ |__/ |__/| $$____/ |__/ \_______/
                            | $$                    
                            | $$                    
                            |__/                    
''', 'green')
cprint(
'''
 /$$$$$$$                          /$$                          
| $$__  $$                        | $$                          
| $$  \ $$  /$$$$$$  /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$$$  /$$__  $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
|_______/  \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                
''', 'yellow')

lv = colored('<3', 'red')
vv = colored('@v533', 'magenta')
aa = colored('Ar1na', 'magenta')
print('Made with ' + lv + ' by ' + vv + "\n\nSpecial for " + aa)
clr = ['magenta', 'red', 'green', 'blue', 'yellow']
s = 0
print("\nVersion: 0.7.4")
# functions
email = '@mail.ru'
for x in range(12):
    email = random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')) + email
import sms_services
services = sms_services.services
# print('' + colored(str(len(services)), 'blue') + ' services avaliable')


def get_proxy():
    curl = requests.get(
        'https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true'
    ).text
    if 'limit' in curl:
        print('\n' + colored(':/', 'red') + '\nProxy limitation error')
        return {}
    print('\nUsing Proxy: ' + curl)
    return {"http": curl, "https": curl}


def smsBomber():
    proxy = {}
    threads = 3

    pr = input('\n' + colored('Use proxy?', 'cyan') + ' (Y/N)' + colored(' >> ', 'grey'))
    if pr == 'Y' or pr == 'y':
        print(colored('\nSetup proxy...', 'yellow'))
        proxy = get_proxy()

    country = input('\n' + colored('Input country code', 'cyan') + ' (Example: 7)' + colored(' >> ', 'grey'))
    try:
        if 0 > int(country) or int(country) > 999:
            print('\n' + colored(':/', 'red') + '\nInvalid country code (Example: 7)')
            return ''
    except ValueError:
        print('\n' + colored(':/', 'red') + '\nInvalid country code (Example: 7)')
        return ''

    number = input('\n' + colored('Input number to be spammed', 'cyan') + ' (Example: XXXXXXXXXX)' + colored(' >> ', 'grey'))
    if number[0] == '+':
        number = number[1:]
    if number[0] == '8':
        number = number[1:]
    if len(number) != 10:
        print('\n' + colored(':/', 'red') + '\nInvalid phone number (Example: XXXXXXXXXX)')
        return ''


    count = input('\n' + colored('Input number of SMS to spam', 'cyan') + colored(' >> ', 'grey'))
    try:
        count = int(count)
    except ValueError:
        print('\n' + colored(':/', 'red') + '\nInvalid input')
        return ''

    if 1 > count or count > 1000:
        print('\n' + colored(':/', 'red') + '\nMin: 1, Max: 1000')
        return ''

    th = input('\n' + colored('Input number of threads', 'cyan') + ' (min: 1 max: 10)' + colored(' >> ', 'grey'))
    try:
        th = int(th)
        if 0 < th <= 10:
            threads = th
    except ValueError:
        print('\n' + colored(':/', 'red') + '\nInvalid input')
        return ''

    sh_err_i = input('\n' + colored('Show errors code?', 'cyan') + ' (Y/N)' + colored(' >> ', 'grey'))
    global sh_err
    sh_err = False
    if sh_err_i == 'Y' or sh_err_i == 'y':
        sh_err = True

    stri = 'off'
    if proxy != {}:
        stri = proxy['http']
    print('\n' + colored('Number: ', 'cyan') + str(country) + str(number) + '\n' + colored('SMS count: ', 'cyan') + str(count) + colored('\nProxy: ', 'cyan') + str(stri) + colored('\nThreads: ', 'cyan') + str(threads) + colored('\nShowErrors: ', 'cyan') + str(sh_err))
    st = input('Start bombing? (Y/N) >> ')

    if st != 'Y' and st != 'y':
        print(colored('\nBombing cenceled!', 'yellow'))
        return ''

    global suc
    suc = 0

    cc = random.randint(0, len(services))
    # cc = -1

    def bomb(p):
        global suc, sh_err
        pp = p.iter()
        if 'Suc' in pp:
            if sh_err:
                print(colored('Successfully send', 'green') + ' (Code: ' + pp.split('#')[1] + ')')
            else:
                cprint('Successfully send', 'green')
            suc += 1
        elif 'error' in pp:
            if sh_err:
                print(colored('Failed to send', 'red') + ' (Error code: ' + pp.split('#')[1] + ')')
            else:
                print(colored('Failed to send', 'red'))
        else:
            cprint('Failed to send', 'red')
            print('Error: ' + pp.split('#')[1])

    from smsBomber import smsBomber

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for i in range(count):
            if cc >= len(services):
                cc = 0
                cprint('\nNew cycle, timeout 5sec\n', 'yellow')
                time.sleep(5)
            p = smsBomber(cc=country, number=number, proxy=proxy, serv=services[cc])
            # print('sending ' + services[cc]['name'] + '...')
            executor.submit(bomb, p)
            cc += 1

    print(colored('\n:D', 'green') + '\nBomb is ended!' + colored('\n\nSuccesfuly send: ', 'cyan') + str(suc) + '\n')


def update():
    print('\n' + colored('Updating...', 'magenta') + '\n')
    print('Removing previous version...')
    os.chdir(os.path.dirname(os.getcwd()))
    os.system('rm -rf S1MpL3B00Mb3r')
    print('Install new version from github...')
    os.system('git clone https://github.com/Vovan533/S1MpL3B00Mb3r.git')
    print('\n' + colored(':D', 'yellow') + '\nUpdate finished, restart programm')
    exit()


# loop
txt = '\nSelect feature >>\n' + colored('01', 'cyan') + colored(' - ', 'grey') + colored('SMS bomber', 'cyan') + "\n" + colored('02', 'yellow') + colored(' - ', 'grey') + colored('Email bomber', 'yellow') + "\n" + colored('03', 'green') + colored(' - ', 'grey') + colored('WhatsApp bomber', 'green') + "\n" + colored('00', 'magenta') + colored(' - ', 'grey') + colored('Update', 'magenta') + "\n" + colored('99', 'red') + colored(' - ', 'grey') + colored('Exit', 'red') + '\n\n'
while True:
    inp = input(txt)
    if inp == '99':
        print(colored('\nBye', 'blue') + '!')
        exit()
    elif inp == '00' or inp == '0':
        update()
    elif inp == '01' or inp == '1':
        smsBomber()
    elif inp == '02' or inp == '2':
        print('\n' + colored(':(', 'red') + '\nFuture not avaliable yet')
    elif inp == '03' or inp == '3':
        print('\n' + colored(':(', 'red') + '\nFuture not avaliable yet')
    else:
        print('\n' + colored(':/', 'red') + '\nInvalid input')
