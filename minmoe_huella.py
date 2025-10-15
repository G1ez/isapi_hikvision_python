# minimoe_huella.py (versión completa)
import requests
from requests.auth import HTTPDigestAuth

DEVICE_IP = "192.168.110.186"
USER = "admin"
PASS = "User2837."
EMP_NO = "P00041"

def main():
    url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CaptureFingerPrint"

    payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<CaptureFingerPrintCond version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
    <employeeNo>{EMP_NO}</employeeNo>
    <fingerNo>1</fingerNo>                <!-- 1-10 según el dedo -->
    <captureNum>3</captureNum>            <!-- número de repeticiones -->
    <isCaptureFingerPrint>true</isCaptureFingerPrint>
    <isCover>true</isCover>
    <enableCtrlBeep>true</enableCtrlBeep>
    <cardReaderNo>1</cardReaderNo>        <!-- lector 1 (único) -->
</CaptureFingerPrintCond>"""

    r = requests.post(
        url,
        auth=HTTPDigestAuth(USER, PASS),
        data=payload.encode("utf-8"),
        headers={"Content-Type": "application/xml"},
        timeout=30,
    )
    print(r.status_code, r.text)

if __name__ == "__main__":
    main()
