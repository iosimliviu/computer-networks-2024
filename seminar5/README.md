# _Seminar 5_

## Conținut

- clase de rețea
- adresa IPv4
- subnetare
- VSLM
- mininet

---

**Clase de rețea**

În spațiul adreselor IPv4 există 5 clase - A, B, C, D și E. Fiecare clasă are un interval specific de adrese IP (care dictează numărul dispozitivelor ce se pot afla în cadrul rețelei). Clasele A, B și C sunt cele care sunt folosite de majoritatea dispozitivelor de pe internet. Clasele D și E sunt pentru utilizări speciale.

![](https://github.com/iosimliviu/computer-networks-2024/blob/main/seminar5/assets/tabel_clase_ip.png)

(**notă**: adresele din intervalul 127.0.0.0-127.255.255.255 sunt considerate adrese de loopback și sunt utilizate pentru testarea și depanarea rețelelor de calculatoare - sunt rezervate pentru utilizarea în rețelele locale și nu sunt disponibile pentru a fi atribuite dispozitivelor de rețea)

**Adrese speciale:**

- 0.0.0.0 - adresa locală pentru toate interfețele de rețea
- 255.255.255.255 - adresa locală pentru broadcast pentru toate interfețele de rețea
- adrese nerutabile (conform [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)) ce aparțin rețelelor private
  - 10.x.x.x
  - 192.168.x.x
  - 172.16.x.x - 172.31.x.x

**Adresa IPv4** este compusă din două părți:

- rețea - număr unic, determină clasa rețelei
- host - atribuită fiecărui host, îl identifică în cadrul rețelei

Spre exemplu, pentru adresa 192.168.1.14, partea de **rețea** e reprezentată primii 3 octeți - **192.168.1**, iar **hostul** de cel de-al patrulea octet, respectiv **14.** Părțile de rețea și de host nu sunt mereu aceleași, dar se determină folosind masca de rețea.

Masca de rețea este o adresă IP specială ce este formată dintr-un șir continuu de 1 urmat de un șir continuu de 0:
11111111.11111111.11111111.00000000 = 255.255.255.0

11111111.11111111.11111111.00000000 ≡ /24

- /24 poartă numele de prefixul rețelei și reprezintă numărul
  de 1 din masca rețelei
- O reprezentare completă a unei adrese IP, ce cuprinde rețeaua din care face parte devine:
  141.85.241.139/24

**Adresa de rețea**

Prin aplicarea operației de AND pe biți între mască și adresa IP se obține adresa de rețea:

![](https://github.com/iosimliviu/computer-networks-2024/blob/main/seminar5/assets/retea_masca.png)

- **adresele de rețea** au toți biții din partea de host setați pe 0; astfel, partea de rețea se determină luând în considerare biții din adresa IP ce corespund biților de 1 din mască
  - în exemplul dat, adresa de rețea este 141.85.241.0
- **adresele de broadcast** au toți biții din partea de host setați pe 1; astfel, pentru a determina adresa de broadcast, toți biții din adresa IP care corespund biților de 0 din mască devin 1, restul se păstrează
  - în exemplul dat, adresa de broadcast este 141.85.241.255
- primul host este adresa de rețea + 1, iar ultimul host este adresa de broadcast - 1
  - în exemplul dat, primul host este 141.85.241.1, iar ultimul este 141.85.241.254

**Subnetare**

Procesul de subnetare (subnetting) constă în a împărți o rețea mai mare în mai multe rețele ce respectă un set de cerințe.

În general, o rețea IP este împărțită în subrețele prin utilizarea unei măști de subrețea, care identifică numărul de biți din adresa IP care vor fi utilizați pentru identificarea subrețelelor și numărul de biți care vor fi utilizați pentru identificarea dispozitivelor individuale în cadrul fiecărei subrețele.

- 2 tipuri de subnetare:

  - în subneturi egale
  - optimă (cu pierdere minimă de adrese)

- pentru mai multe detalii despre subnetare, puteți urmări [aceasta serie de pe YouTube](https://www.youtube.com/watch?v=5WfiTHiU4x8&list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF)

**VSLM (Variable Length Subnet Mask)**

- permite reducerea pierderii de adrese
- permite crearea de subnet-uri ce nu mai au măști de aceeași lungime; la fiecare alocare de subrețea se recalculează masca de rețea necesară pentru a aloca un anumit număr de hosturi

**Mininet**

= emulator de rețea, alături de o mașină virtuală linux

- utilizat pentru **SDN** (Software-defined networking) - abordare modernă pentru construirea, gestionarea și operarea rețelelor de calculatoare. În loc să folosească echipamente de rețea tradiționale (cum ar fi switch-uri și routere), SDN se bazează pe software pentru a defini și controla comportamentul rețelei.
