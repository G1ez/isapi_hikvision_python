import requests, datetime
from requests.auth import HTTPDigestAuth

DEVICE_IP = "192.168.110.186"
USER = "admin"
PASS = "User2837."
EMP_NO = "P00041"
NEW_NAME = "Prueba Sky glezz update2"

def main():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/UserInfo/Modify?format=json"
    now = datetime.datetime.now().replace(microsecond=0).isoformat()
    end = (datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=365*10)).isoformat()

    payload = {
        "UserInfo": {
            "employeeNo": EMP_NO,
            "name": NEW_NAME,
            "userType": "normal",
            "Valid": {
                "enable": True,
                "beginTime": now,
                "endTime": end,
                "timeType": "local"
            },
            "RightPlan": [{"doorNo": 1}],
            "userVerifyMode": "faceOrFpOrCardOrPw"
        }
    }

    r = requests.put(
        url,
        auth=HTTPDigestAuth(USER, PASS),
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    print(r.status_code, r.text)

if __name__ == "__main__":
    main()
