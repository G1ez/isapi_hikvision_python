import requests
from requests.auth import HTTPDigestAuth

# Config
DEVICE_IP   = "192.168.110.186"
USER        = "admin"
PASS        = "User2837."
EMP_NO      = "P00041"
FP_ID       = 1  # plantilla a reemplazar

def delete_fingerprint():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/FingerPrint/Delete?format=json"
    payload = {"FingerPrintCond": {"employeeNo": EMP_NO, "fingerPrintID": FP_ID}}
    return requests.put(url, auth=HTTPDigestAuth(USER, PASS), json=payload, timeout=10)

def capture_fingerprint():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CaptureFingerPrint?format=json"
    payload = {"CaptureFingerPrintCond": {"employeeNo": EMP_NO, "fingerPrintID": FP_ID, "captureIntervals": 3, "enableCtrlBeep": True}}
    return requests.post(url, auth=HTTPDigestAuth(USER, PASS), json=payload, timeout=30)

def main():
    d = delete_fingerprint(); print("DEL:", d.status_code, d.text)
    c = capture_fingerprint(); print("CAP:", c.status_code, c.text)

if __name__ == "__main__":
    main()
