# _Seminar 7_

## Conținut

- autentificare
- SSL
- TLS
- exemple

---

Pentru a crea o pereche cheie - certificat

```bash
openssl genrsa -out serv.key 2048
openssl req -x509 -new -nodes -key serv.key -sha256 -days 1024 -out serv.pem
```
