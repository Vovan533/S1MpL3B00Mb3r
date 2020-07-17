# imports
try:
    from termcolor import colored, cprint
    import requests, random, time, os
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
print('\nVersion: 0.6.5')
# functions
email = '@mail.ru'
for x in range(12):
    email = random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')) + email
import sms_services
services = sms_services.services
# print('' + colored(str(len(services)), 'blue') + ' services avaliable')


def smsBomber():
    global services
    global headers
    global proxy
    proxy = {}
    threads = 3
    pr = input('\n' + colored('Use proxy?', 'cyan') + ' (Y/N)' + colored(' >> ', 'grey'))
    if pr == 'Y' or pr == 'y':
        print(colored('\nSetup proxy...', 'yellow'))
        def get_proxy():
            curl = requests.get(
                'https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true'
            ).text
            if 'limit' in curl:
                print('\n' + colored(':/', 'red') + '\nProxy limitation error')
                return {}
            print('\nUsing Proxy: ' + curl)
            return {"http": curl, "https": curl}
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
        number = '7' + number[1:]
    if len(number) != 10:
        print('\n' + colored(':/', 'red') + '\nInvalid phone number (Example: XXXXXXXXXX)')
        return ''
    d = True
    count = ''
    while d:
        count = input('\n' + colored('Input number of SMS to spam', 'cyan') + colored(' >> ', 'grey'))
        try:
            count = int(count)
        except ValueError:
            print('\n' + colored(':/', 'red') + '\nInvalid input')
            return ''

        if 1 <= count <= 1000:
            d = False
        else:
            print('\n' + colored(':/', 'red') + '\nMin: 10, Max: 1000')

    th = input('\n' + colored('Input number of threads', 'cyan') + ' (min: 1 max: 10)' + colored(' >> ', 'grey'))
    try:
        th = int(th)
        if 0 < th <= 10:
            threads = th
    except ValueError:
        print('\n' + colored(':/', 'red') + '\nInvalid input')
        return ''
    global sh_err
    sh_err_i = input('\n' + colored('Show errors code?', 'cyan') + ' (Y/N)' + colored(' >> ', 'grey'))
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

    global curc
    curc = 0
    global suc
    suc = 0
    global cc
    cc = random.randint(0, len(services))
    #cc = -1
    global cth
    cth = 0
    while True:
        if curc > count - 1:
            break

        
        # iteration


        def iter():
            global cc
            global services
            global curc
            global cth
            global suc
            global sh_err
            global proxy
            cc += 1
            if cc >= len(services):
                cc = 0
                cprint('\nNew cycle, timeout 5sec\n', 'yellow')
                time.sleep(5)
            print('sending ' + services[cc]['name'] + '...')
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
            if 'headers' in services[cc]:
                headers.update(services[cc]['headers'])
            params = {}
            uyt = 'params'
            if 'params' in services[cc]:
                uyt = 'params'
            elif 'json' in services[cc]:
                uyt = 'json'
            for k, v in services[cc][uyt].items():
                if isinstance(v, str):
                    params[k] = v.format(target=number, cc=country, ccc='8', email=email, semail=email.split('@')[0])
            services[cc]['url'].format(target=number, cc=country, ccc='8', email=email, semail=email.split('@')[0])
            try:

                if services[cc]['method'] == 'GET':
                    r = requests.get(services[cc]['url'],
                        params=params,
                        headers=headers,
                        timeout=30,
                        proxies=proxy,
                        verify=True)
                elif services[cc]['method'] == 'POST':
                    if 'json' in services[cc]:
                        r = requests.post(services[cc]['url'],
                                      json=params,
                                      headers=headers,
                                      timeout=10,
                                      proxies=proxy,
                                      verify=True)
                    elif 'params' in services[cc]:
                        r = requests.post(services[cc]['url'],
                            data=params,
                            headers=headers,
                            timeout=10,
                            proxies=proxy,
                            verify=True)
                if services[cc]['identifier'] in r.text:
                    suc += 1
                    if sh_err:
                        print(colored('Successfully send', 'green') + ' (Code: ' + r.text + ')')
                    else:
                        cprint('Successfully send', 'green')
                else:
                    if sh_err:
                        print(colored('Failed to send', 'red') + ' (Error code: ' + r.text + ')')
                    else:
                        print(colored('Failed to send', 'red'))
            except Exception as ex:
                cprint('Failed to send', 'red')
                print('Error: ' + str(ex))
            cc += 1
            curc += 1
            cth = cth - 1

        if cth < threads:
            cth += 1
            iter()

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
