# _Seminar 2_

## Conținut 

- sockets, TCP vs UDP
- client & server UDP
- client & server TCP
***

### Sockets, TCP vs UDP

În cadrul internetului există mai multe noduri client/server care comunică între ele.
**Un socket** este o structură software în cadrul unul nod de rețea al unui computer care servește drept endpoint (interfață) pentru a trimite și primi date în cadrul rețelei; structura și proprietățile unui socket sunt definite printr-un API pentru arhitectura rețelei; socketurile sunt create doar în timpul unui proces al unei aplicații care ruleaza in nodul respectiv.

Astfel, extern, un socket este identificat de alte gazde prin **adresa de socket**, care este compusă din 3 părți:
- protocolul de transport (UDP/TCP)
- adresa IP
- portul (**0 - 65535**)

**Tipuri de conexiuni** - TCP/UDP
- **TCP** (Transmission Control Protocol) 
    - orientată pe conexiune
    - o conexiune este necesară înainte de a comunica
    - three way handshake - conexiunea este full duplex iar ambele părți sunt conștiente de conexiune și alocă resurse 
    - există mecanisme care detectează ce date au fost pierdute pentru a reîncerca trimiterea acestora
- **UDP** (User Datagram Protocol) 
    - fără conexiune
    - nu știm dacă pachetul va ajunge la destinație
    - best effrot
    - nu retrimite date în cazul în care s-au pierdut

🤔 DNS folosește UDP - o cerere UDP de la client, un răspuns UDP de la server (mai rapid)

Rulând exemplele de cod sursă pentru client & server TCP/UDP vom putea analiza traficul folosind Wireshark. Vom selecta _interfața loopback/adaptor pentru interfața loopback_ drept filtru de interfață pentru capturarea traficului - **adresa de loopback (sau localhost)** este o adresă internă care rutează înapoi către sistemul local - adresa aceasta în IPv4 este **127.0.0.1**.
