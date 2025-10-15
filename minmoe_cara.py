# minmoe_cara.py - Variante FaceData/Record XML
import requests
from requests.auth import HTTPDigestAuth

DEVICE_IP = "192.168.110.186"
USER = "admin"
PASS = "User2837."
EMP_NO = "P00041"
NAME   = "Prueba Sky glez"

def main():
    auth = HTTPDigestAuth(USER, PASS)

    # --- Captura la cara directamente desde el dispositivo ---
    cap_url = f"http://{DEVICE_IP}/ISAPI/AccessControl/CaptureFaceData"
    cap_xml = """<?xml version="1.0" encoding="UTF-8"?>
    <CaptureFaceDataCond version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
        <captureInfrared>false</captureInfrared>
        <dataType>binary</dataType>
    </CaptureFaceDataCond>"""
    print("[*] Capturando cara...")
    cap = requests.post(cap_url, auth=auth, data=cap_xml.encode("utf-8"),
                        headers={"Content-Type": "application/xml"}, timeout=20)
    if cap.status_code != 200 or not cap.content:
        print("Captura fallida:", cap.status_code, cap.text)
        return
    print("[+] Imagen capturada OK, tamaño:", len(cap.content), "bytes")

    # --- Registra el rostro directamente al usuario (FaceData/Record) ---
    reg_url = f"http://{DEVICE_IP}/ISAPI/AccessControl/FaceData/Record"
    reg_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <FaceDataRecord version="2.0" xmlns="http://www.isapi.org/ver20/XMLSchema">
        <faceID>{EMP_NO}</faceID>
        <employeeNo>{EMP_NO}</employeeNo>
        <name>{NAME}</name>
        <isCover>true</isCover>
        <faceDataType>binaryData</faceDataType>
    </FaceDataRecord>"""

    files = {
        "FaceDataRecord": ("metadata.xml", reg_xml.encode("utf-8"), "application/xml"),
        "faceImage": ("face.jpg", cap.content, "application/octet-stream"),
    }
    print("[*] Registrando rostro...")
    r = requests.post(reg_url, auth=auth, files=files, timeout=20)
    print("[+] Respuesta:", r.status_code, r.text)

if __name__ == "__main__":
    main()
