# minmoe_imagen.py ESTE ARCHIVO SE USA PARA IMPORTAR UNA IMAGEN DEL ORDENADOR AL DISPOSITIVO (CABE ACLARAR QUE DEBEMOS USAR accesos/enrolar/) PARA DENTRO DE AHÍ REGISTRAR LA IMAGEN EN LOS DISPOSITIVOS
# Sincroniza rostro a varios MinMoe usando FDLib/FaceDataRecord con faceURL (blackFD)
import os, requests
from requests.auth import HTTPDigestAuth

# ===== Config =====
DEVICES = [
    #{"ip": "192.168.110.166", "user": "admin", "pwd": "User2837."},
    {"ip": "192.168.110.186", "user": "admin", "pwd": "User2837."},
]
EMP_NO     = "P00041"        # FPID = employeeNo
NAME       = "Prueba Sky glez"
FDID       = "1"             # suele ser 1
FACELIB    = "blackFD"       # este es el que funcionó
PC_LAN_IP  = "192.168.110.182"
IMAGE_PATH = r"C:\HikvisionTest\glez.jpg"
IMAGE_URL  = f"http://{PC_LAN_IP}:8000/glez.jpg"  # sirviendo con: python -m http.server 8000
TIMEOUT_S  = 20
USE_HTTPS  = False           # pon True si tu equipo exige HTTPS

def _check_image_ok(path):
    if not os.path.exists(path): raise FileNotFoundError(path)
    if os.path.getsize(path) > 200*1024: raise ValueError("Imagen >200KB; comprímela.")

def _base(ip): return f"{'https' if USE_HTTPS else 'http'}://{ip}"
def _session(user, pwd): return HTTPDigestAuth(user, pwd)

def push_face_url(ip, user, pwd):
    url = f"{_base(ip)}/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json"
    payload = {"faceURL": IMAGE_URL, "faceLibType": FACELIB, "FDID": FDID, "FPID": EMP_NO, "name": NAME}
    r = requests.post(url, auth=_session(user, pwd), json=payload,
                      headers={"Content-Type":"application/json"}, timeout=TIMEOUT_S, verify=not USE_HTTPS)
    return r

def main():
    _check_image_ok(IMAGE_PATH)
    ok, fail = [], []
    for d in DEVICES:
        try:
            r = push_face_url(d["ip"], d["user"], d["pwd"])
            if r.status_code == 200:
                print(f"[{d['ip']}] OK faceURL -> {FACELIB}")
                ok.append(d["ip"])
            else:
                print(f"[{d['ip']}] faceURL -> {r.status_code} {r.text.strip()}")
                fail.append(d["ip"])
        except requests.RequestException as e:
            print(f"[{d['ip']}] error: {e}")
            fail.append(d["ip"])
    print("\n==== Resumen ===="); print("OK   :", ok); print("FAIL :", fail)

if __name__ == "__main__":
    main()
