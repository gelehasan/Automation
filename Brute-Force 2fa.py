import requests


login_url="http://example.com"
otp_url="http://example/mfa"
dashboard_url="http://example/dashboard"


credentials={
    "username":"username123",
    "password":"text1234"
}



headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://example.com',
    'Connection': 'close',
    'Referer': 'http://example/mfa',
    'Upgrade-Insecure-Requests': '1'
}


# Function for checking if log in has succeeded
def is_loggedin_success(response):
    return "User verfication" in response.text and response.status_code==200

# This function handles log in
def login(session):
    response= session.post(login_url, data=credentials, headers=headers)
    return response


# Function for handling mfa
def test_top(session, otp):
    otp_code={
        "code-1": otp[0],
        "code-2": otp[1],
        "code-3": otp[2],
        "code-4":otp[3]
    }
    response = session.post(otp_url, data=opt_code, headers=headers, allow_redirects=false)
    print("OTP response code recieved", {response.status_code})

    return response