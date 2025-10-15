# minmoe_registro_01.py  (VARIANTE 1)
import requests, datetime
from requests.auth import HTTPDigestAuth

DEVICE_IP = "192.168.110.186"
USER = "admin"
PASS = "User2837."
EMP_NO = "P00041"
NAME = "Prueba Sky glez"

def main():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/UserInfo/SetUp?format=json"
    now = datetime.datetime.now().replace(microsecond=0).isoformat()
    end = (datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=365*5)).isoformat()
    payload = {
        "UserInfo": {
            "employeeNo": EMP_NO,
            "name": NAME,
            "userType": "normal",
            "Valid": {
                "enable": True,
                "beginTime": now,
                "endTime": end,
                "timeType": "local"
            },
            "faceEnabled": True,
            "cardEnabled": True,
            "fingerPrintEnabled": True
        }
    }
    r = requests.put(
        url,
        auth=HTTPDigestAuth(USER, PASS),
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=15
    )
    print(r.status_code, r.text)

if __name__ == "__main__":
    main()
