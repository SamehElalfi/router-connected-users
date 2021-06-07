import requests, json, urllib3
from time import sleep
from win10toast import ToastNotifier

# Disable SSL warning
# urllib3 print warning if the requests didn't use https
urllib3.disable_warnings()

def getUsers():
    r = requests.get('http://192.168.1.1/api/system/device_count', verify=False)
    content = r.content[12:-2]
    json_code = json.loads(content)

    return json_code['ActiveDeviceNumbers']


if __name__ == "__main__":
    ActiveDeviceNumbers = getUsers()
    print(f"Starting count connected users. Current users: {ActiveDeviceNumbers}")
    toast = ToastNotifier()
    toast.show_toast("Connected Users Counter", f"Starting count connected users. Current users: {ActiveDeviceNumbers}", duration=10)
    
    while 1:
        sleep(10)

        usersCount = getUsers()
        if ActiveDeviceNumbers < usersCount:
            ActiveDeviceNumbers = usersCount
            toast.show_toast("New User Detected", f"Current connected users is: {usersCount}", duration=10)
            print("Current connected users:", ActiveDeviceNumbers)


print('exiting')