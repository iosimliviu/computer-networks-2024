# _Seminar 6_

## Conținut

- servere cu comunicare bidirecțională
- serializare de unități de transfer

---

**Servere cu comunicare bidirecțională**

În mod normal, un server TCP așteaptă conexiuni de la clienți, acceptă conexiunile și comunică cu clienții. În cadrul acestui scenariu, informația circulă unidirecțional.

Într-un server TCP bidirecțional, serverul și clientul pot trimite și primi date simultan și în orice moment, fără a fi nevoie să aștepte ca una dintre părți să termine de trimis date. Acest tip de server este adesea folosit în aplicații care necesită comunicații bidirecționale în timp real, precum aplicații de chat.

Astfel, diferența principală între un server TCP unidirecțional și un server TCP bidirecțional este că un server TCP unidirecțional poate comunica doar într-o singură direcție, adică doar de la server către client sau doar de la client către server, în timp ce un server TCP bidirecțional poate comunica în ambele direcții.

În exemplul **bidirectional-basic-tcp** serverul acceptă conexiuni de la clienți și trimite mesajele primite de la un client către ceilalți clienți conectați. Astfel este indicată comunicarea bidirecțională. Exemplul poate fi privit și precum o aplicație de tip chat în care un utilizator trimite un mesaj către un grup, iar serverul e responsabil de a redirecționa mesajele către toți ceilalți utilizatori care sunt parte din acel grup.

**Serializare de unități de transfer**
O unitate de transfer în comunicarea client-server reprezintă o cantitate fixă de date care este transmisă între un server și un client în cadrul unei sesiuni de comunicare. Această unitate este adesea denumită și pachet de date sau mesaj.

Serializarea și deserializarea datelor este un proces important în comunicarea client-server, deoarece permite transmiterea datelor structurate între dispozitivele care utilizează limbaje de programare diferite sau care rulează pe platforme diferite. Prin serializare, datele pot fi transmise într-un format standardizat, astfel încât să poată fi interpretate și utilizate corect de către dispozitivul receptor.

Pentru serializarea și deserializarea datelor este folosită în exemplul dat librăria [**pickle**](<[https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)>)**.** În exemplul **udp-transfer-unit**, sunt definite clase pentru a ajuta la identificarea structurii obiectelor care sunt serializate/deserializate. Serverul și clientul comunică conform unui protocol custom definit, în cadrul căruia sunt prezente acțiunile:

- connect
- send
- list
- disconnect

Fiecare comandă are asociată o anumită prelucrare. În esență, serverul ține evidența unei “baze de date” (pentru fiecare client care trimite requesturi către el) în cadrul căreia clientul poate adăuga și citi diferite informații, la cerere.
