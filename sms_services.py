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
        "identifier": "201"
    }, # MTS TV +
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
        'url': "https://www.kfc.ru/api/account/verify",
        'json':
            {
                'phone': '+{cc}{target}',
            },
        "identifier": "200"
    }, # KFC -+
{
        'name': 'UTAIR',
        'method': "POST",
        'url': "https://b.utair.ru/api/v1/login/",
        'params':
            {
                'login': '{ccc}{target}',
                'confirmation_type': 'call_code'
            },
        "identifier": "200"
    }, # UTAIR -+
{
        'name': 'Tinder',
        'method': "POST",
        'url': "https://api.gotinder.com/v3/auth/login?locale=ru",
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
        'json':
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
    'name': 'Cian',
    'method': 'POST',
    'url': "https://api.cian.ru/sms/v1/send-validation-code/",
    'json': {"phone": "+{cc}{target}", "type": "authenticateCode"},
    "identifier": "200"
}, # Cian +
{
    'name': 'Zvonok.com',
    'method': 'POST',
    'url': "https://zvonok.com/api/demo/",
    'json': {"phone": "{formated}"},
    "identifier": "200"
} # zvonok.com
]