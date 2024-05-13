# _Seminar 11_

## Conținut

- exemplu transfer fișier prin TCP
- pseudo-ftp
- FTP

---

**FTP (File Transfer Protocol)** = protocol de rețea utilizat pentru transferul fișierelor între calculatoarele conectate la o rețea

- cu ajutorul FTP, utilizatorii pot transfera fișiere între computerele lor sau între un computer și un server, utilizând un client FTP (de exemplu, [**FileZilla**](https://filezilla-project.org/)) sau prin comenzi scrise în linie de comandă
- FTP folosește un model client-server
  - clientul se conectează la server
  - clientul furnizează numele de utilizator și o parolă
  - daca se realizează autentificarea, clientul poate naviga prin directoarele serverului, descărca ori încărca fișiere

FTP este un protocol de rețea vechi, în standardele moderne încercându-se înlocuirea treptată a acestuia cu protocoale mai sigure și mai rapide, cum ar fi SFTP (Secure File Transfer Protocol) și FTPS (FTP over SSL/TLS). Acestea protejează datele de autentificare și criptează conținutul ce circulă între client și server.
