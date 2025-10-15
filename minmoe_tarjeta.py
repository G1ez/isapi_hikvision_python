import requests
from requests.auth import HTTPDigestAuth

# Config
DEVICE_IP   = "192.168.110.166"
USER        = "admin"
PASS        = "User2837."
EMP_NO      = "P00041"
CARD_NO     = "1234567890"  # Ajusta a tu tarjeta

# Alta/SetUp de tarjeta
def main():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CardInfo/SetUp?format=json"
    payload = {
        "CardInfo": {
            "employeeNo": EMP_NO,
            "cardNo": CARD_NO,
            "cardType": "normalCard",
            "checkCardNo": True,
            "checkEmployeeNo": True
        }
    }
    r = requests.put(url, auth=HTTPDigestAuth(USER, PASS), json=payload, timeout=10)
    print(r.status_code, r.text)

if __name__ == "__main__":
    main()
