# minimoe_update_imagen.py
# Borra rostro (FPID) y vuelve a subirlo a blackFD (faceURL)
import requests, os
from requests.auth import HTTPDigestAuth

DEVICE_IP  = "192.168.110.186"
USER       = "admin"
PWD        = "User2837."
EMP_NO     = "P00041"
NAME       = "Prueba Sky glez"
FDID       = "1"
FACELIB    = "blackFD"
PC_LAN_IP  = "192.168.110.182"
IMAGE_URL  = f"http://{PC_LAN_IP}:8000/glez.jpg"
USE_HTTPS  = False

def _base(): return f"{'https' if USE_HTTPS else 'http'}://{DEVICE_IP}"
def _auth(): return HTTPDigestAuth(USER, PWD)

def delete_face():
    # Borra por FPID en la FaceLib
    url = f"{_base()}/ISAPI/Intelligent/FDLib/FDSearch/Delete?format=json&FDID={FDID}&faceLibType={FACELIB}"
    payload = {"FPID": [{"value": EMP_NO}]}
    return requests.put(url, auth=_auth(), json=payload, timeout=15, verify=not USE_HTTPS)

def upload_face():
    url = f"{_base()}/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json"
    payload = {"faceURL": IMAGE_URL, "faceLibType": FACELIB, "FDID": FDID, "FPID": EMP_NO, "name": NAME}
    return requests.post(url, auth=_auth(), json=payload, headers={"Content-Type":"application/json"},
                         timeout=20, verify=not USE_HTTPS)

def main():
    d = delete_face(); print("DEL:", d.status_code, d.text)
    u = upload_face(); print("ADD:", u.status_code, u.text)

if __name__ == "__main__":
    main()
