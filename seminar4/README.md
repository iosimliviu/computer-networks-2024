# _Seminar 4_

## Conținut

- protocoale text și protocoale binare
- unități de transfer
- protocol custom de comunicație TCP
- protocol custom de comunicație UDP

---

Cele două exerciții prezentate în seminar reprezintă implementări de protocoale custom de comunicație TCP, axându-se, pe rând, pe gestiunea schimbului de mesaje binare și de mesaje text.

- **binary-proto-tcp**:

  - protocolul custom stabilește o structură pentru mesajele primite, definite de clasa **Request**
  - se stabilesc comenzi ce vor altera ori accesa state-ul prezent în server (dicționar cu elemente de tip cheie - valoare)
  - serializarea și deserializarea obiectelor transmise între client și server se realizează folosind librăria **pickle**
  - clientul trimite un obiect serializat (sub formă binară), serverul îl deserializează și procesează comanda conform meniului definit, iar în funcție de aceasta, trimite înapoi un obiect serializat clientului conținând răspunsul cererii, pe care clientul pentru a îl afișa îl deserializează
  - în cazul socket-urilor de tip stream (cum sunt folosite pentru TCP), dacă datele primite depășesc ca mărime bufferul stabilit, datele rămase pot fi accesate la următorul apel al funcției **recv()**
  - din acest motiv, clientul adaugă un bit în plus la mesajul trimis în care stochează mărimea streamului de date
  - state-ul folosește un **lock** pentru a bloca resursa atât timp cât aceasta este modificată

- **text-proto-tcp**
  - similar protocolului custom binar, având definite acțiuni care alterează/accesează un state de tip dicționar cu elemente cheie - valoare
  - accesul la state pentru modificare este unul blocant prin intermediul unui lock
  - pentru partea de codificare/decodificare, în cazul conținutului de tip text se folosesc funcțiile **encode()** și **decode()**, specificând standardul utf-8
  - mesajele în acest caz reprezintă un string, pentru care primul element delimitat de spațiu este lungimea mesajului trimis, următorul comanda, apoi cheia elementului din state și valoarea acestuia