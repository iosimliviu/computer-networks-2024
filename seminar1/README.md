# _Seminar 1_

## Conținut 

- Intro - modelul OSI 101
- ping
- netstat
- route
- traceroute/tracert
- netcat
- wireshark
- tshark
***

### Intro - Modelul OSI 101

Rețelele de calculatoare permit ca computerele să comunice între ele indiferet de unde se află în lume. Arhitectura acestora este abstractizată în 7 nivele, conform modelului OSI (Open Systems Interconnection).
![modelul OSI](https://images.ctfassets.net/fczckc3dt6mv/6Vkx9BWaUVDLfs9XVBos1S/d1e0274ac1766b9da3d4b6bcbcde3569/f-gooden_22-01_OSIModel.png)

- **Application**
        - la acest nivel se regăsesc protocoalele HTTP (_Hyper Text Transfer Protocol_), smtp (_Simple Mail Transfer Protocol_), ftp (_File Transfer Protocol_), responsabile pentru inițierea cererilor și obținerea răspunsurilor
- **Presentation**
        - nivel translator, se asigură ca un stream de biți, care poate fi, spre exemplu, o imagine JPEG, este codificat într-un format standard care poate fi folosit în cadrul nivelului Application
- **Session**
        - responsabil cu managementul conexiunii dintre 2 computere
        - user authentication/authorisation → dacă userul are acces la server sau nu
- **Transport**
        - în cadrul acestui nivel se regăsesc protocoalele TCP (_Transmission Control Protocol_) și UDP (User Datagram Protocol)
        - gestionează streamurile de date de la un computer către un alt computer - determină cum va fi segmentată informația
- **Network**
        - protocolul IP (_Internet Protocol_)
        - reprezintă locul în care se află pachetele înainte să ajungă în nivelul Transport
        - fiecare computer are un IP unic care îl identifică
        - pachetele au adresa IP în header
- **Data Link**
        - conectează un nod fizic cu altul prin protocoale precum Ethernet sau WiFi
- **Physical**
        - hardware
        - fibra optică, spre exemplu, transporta lumina de la punctul A la punctul B. aceasta, trecând prin toate nivelele arhitecturii de rețea, ajunge să fie transpusă în pixelii de pe ecran, ori vibrațiile dintr-o boxă


### ping
= **Pa**cket **IN**ternet **G**roper

- utilitate folosită pentru _troubleshooting privind probleme de internet_
- verifică conectivitatea dintre 2 calculatoare
- **testează**
    - dacă un host/server e disponibil
    - conectivitatea la internet
    - existența problemelor DNS (Domain Name System)
- **mecanism**
    - A trimite un pachet de date peste protocolul **ICMP (Internet Control Message Protocol)** - _echo request_
    - la primirea pachetului, B îl trimite înapoi - _echo reply_
    - testul este rulat pentru pachete multiple
    - în mod default, Windows trimite 4 requesturi
- **partial packet loss** - congestie a rețelei, cabluri stricate, hardware stricat
- **complete packet loss**
    - dacă nu primim nimic - timeout - adresa nu e disponibilă (nu există/nu e pornită/nu e conectată la rețea); firewall ar putea să blocheze ping
    - destination host unreachable
    - ping could not find the host - DNS issue
- **explicații suplimentare**
    - **icmp_seq**=1 al câtelea pachet este pachetul trimis
    - **ttl**(_time to live_) câte **segmente de rețea** mai poate naviga pachetul înainte de a fi aruncat; este un mecanism de a evita **pachete zombie** (care navighează etern un traseu ciclic în rețea)
    - **time** - o metrică de calitate a rețelei, reprezintă timpul necesar pentru un pachet să **parcurgă rețeaua de la A la B și înapoi la A**

### netstat
- utilitar de linie de comandă folosit pentru a afișa conexiunile curente și utilizarea porturilor pe computer
- **netstat -n** → arată doar IP-urile în format numeric (outputul e mult mai rapid pentru că nu folosește DNS ca sș atribuie nume pentru reprezentarea numerică)
- **netstat -a** → conexiuni stabilite, porturi deschise care asculta conexiuni
- **netstat -b** → ce program e folosit pentru a face conexiunile (necesită admin)

### route
- **route print** - tabelul pe care calculatorul îl foloseste pentru a gestiona pachetele (cuprinde informații referitoare la interfețe, IPv4, IPv6)
- se pot adauga elemente noi în rețea

### traceroute/tracert
- similar cu ping, folosește protocolul ICMP pentru a stabili o conexiune cu un host extern
- nu spune doar dacă adresa e disponibilă, ci arată fiecare pas folosit pentru a ajunge la destinație (reteaua globală de internet e legată prin mai multe routere - un pachet, pentru a ajunge de la calculatorul nostru la serverul google, care sa presupunem că e în Germania, trebuie să treacă prin mai multe noduri)
- ttl (time to live) - scade cu fiecare hop prin care pachetul trece
- cum e determinat? prin ttl 
    - prima dată calculatorul trimite un pachet cu ttl = 1.
    - ttl scade și ajunge 0, iar calculatorul primește un răspuns “ttl exceeded”, dar notează adresa care i-a dat răspunsul
    - incrementeaza ttl până găsește IP-ul la care voia să trimită inițial pachetul → realizează astfel drumul pe care îl parcurge pachetul
- maxim 30 hops pe Windows

## **netcat**

- utilitar pentru securitatea rețelelor
- 2 calculatoare trimit date între ele via TCP și UDP și via nivelul **Network**
- poate opera ca un client pentru a iniția conexiuni cu servere sau poate să fie și server/listener în anumite condiții
- poate fi folosit drept chat, port scanning etc.
- testarea conectivității între calculatoare

## wireshark
- program pentru capturarea traficului de pe mașina curentă
- permite aplicarea filtrelor, selectarea interfețelor ce vor fi ascultate

## tshark
- variantă de wireshark pentru terminal
