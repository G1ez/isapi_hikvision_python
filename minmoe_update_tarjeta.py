import requests
from requests.auth import HTTPDigestAuth

# Config
DEVICE_IP   = "192.168.110.166"
USER        = "admin"
PASS        = "User2837."
EMP_NO      = "P00041"
OLD_CARD    = "1234567890"
NEW_CARD    = "9876543210"

def delete_card(card_no):
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CardInfo/Delete?format=json"
    payload = {"CardInfoDelCond": {"CardNoList": [{"cardNo": card_no}]}}
    return requests.put(url, auth=HTTPDigestAuth(USER, PASS), json=payload, timeout=10)

def setup_card(card_no):
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CardInfo/SetUp?format=json"
    payload = {"CardInfo": {"employeeNo": EMP_NO, "cardNo": card_no, "cardType":"normalCard", "checkCardNo": True, "checkEmployeeNo": True}}
    return requests.put(url, auth=HTTPDigestAuth(USER, PASS), json=payload, timeout=10)

def main():
    d = delete_card(OLD_CARD); print("DEL:", d.status_code, d.text)
    s = setup_card(NEW_CARD); print("ADD:", s.status_code, s.text)

if __name__ == "__main__":
    main()
