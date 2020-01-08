import time
from datetime import datetime as dt

# setting up the intial variables
host_path = "/private/etc/hosts"
redirect = "127.0.0.1"
#
website_list = ["www.facebook.com", "facebook.com",
                "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("Working Hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun Hours...")
        with open(host_path, 'r+') as file:
            # read line by line
            content = file.readlines()
            # to start the file from the beginning
            file.seek(0)
            for line in content:
                # If any of the above is True you get the expression evaluated to True. In this case none of them is True, so you get False.
                if not any(website in line for website in website_list):
                    file.write(line)
            # to delete anything below that point
            file.truncate()
    time.sleep(5)
