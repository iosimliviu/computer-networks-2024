# _Seminar 3_

## Conținut 

- socket server complet python TCP/UDP
- multicast și broadcast
- TCP tunnel
***

**Broadcast** - procesul de a trimite un pachet de la un host către toate hosturile dintr-o rețea.

- un sender, mai mulți receiveri;
- are loc exclusiv în rețeaua locală
- doar în IPv4 - în IPv6 există **anycast** - comunicarea cu mașini vecine (one to nearest)

**Multicast** - concept al sistemelor distribuite ce ilustrează comunicarea de grup în cadrul unei rețele (one-to-many, many-to-many). În cadrul multicast, pachetele sunt trimise către mașinile care vor să îl primească. Există mai multe tipuri de multicast:

- IP multicast - este folosit protocolul IP pentru trimiterea datelor
- UDP multicast - este folosit protocolul UDP pentru trimiterea datelor

Deși UDP nu este considerat a fi un protocol de încredere, deoarece nu există garanția livrării mesajelor, UDP multicast este rapid, lightweight și alegerea făcută în, spre exemplu, multe scenarii de streaming, spre exemplu Netflix ori o conferință online, ce ar fi transmisă către toți utilizatorii care vor să o urmărească.

**Tunneling** - redirecționarea traficului de la un port ocupat către un port disponibil; acest proces permite conexiunilor făcute către un port local (pe desktopul curent) să fie transmise către un computer remote printr-un canal securizat.

**TCP tunneling:** 

- presupunem că vrem să ne conectăm la un server, dar dintr-un motiv sau altul destinația nu e reachable (ex. e blocat de firewall)
- se stabilește o conexiune normală TCP între mine (C1 - client 1) și serverul pe care vreau să-l accesez - S2 (să spunem pe portul 80, care nu e reachable)
- pachetul TCP este încapsulat drept data pentru un alt pachet TCP care merge spre portul 22 (S1) (care e reachable) - data e criptat, secure shell, nimeni nu poate vedea ce e acolo (nici firewall)

![](https://github.com/liviuiosim/computer-networks-2024/blob/main/seminar_3/assets/tunnel1.png)

- S1 primește pachetul, obține conținutul, care este un alt pachet TCP (așa cum a fost încapsulat) și, conform acestuia, îl redirecționează mai departe către S2 și schimbă în antet C1 cu S1 pentru că altfel nu ar fi acceptat

![](https://github.com/liviuiosim/computer-networks-2024/blob/main/seminar_3/assets/tunnel2.png)

- S2 returnează index.html către S1 care trimite către C1, încapsulând din nou pachetul TCP drept un response mascat de la S1 (în realitate răspunsul vine de la S2)

![](https://github.com/liviuiosim/computer-networks-2024/blob/main/seminar_3/assets/tunnel3.png)
