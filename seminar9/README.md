# _Seminar 9_

## Conținut

- HTTP
- exemplu simplu & custom de server HTTP
- REST, Flask

---

#### HTTP

**HTTP (Hypertext Transfer Protocol)** = protocol de comunicare folosit pentru transferul de informații între clienți și servere pe Internet

- este utilizat în principal pentru accesarea paginilor web și pentru a transmite date între browser (ce reprezintă clientul) și serverul web care găzduiește site-ul

**Mod de funcționare:**

- clientul trimite o **cerere** către server prin intermediul unui browser web, care include un anumit tip de **metodă HTTP** (cum ar fi GET sau POST), precum și o **adresă URL** (Uniform Resource Locator) - care specifică locația resursei dorite
- serverul primește această cerere și răspunde cu un cod de status (ce poate fi de succes sau eroare) și datele cerute (dacă este cazul)

**Caracteristifci HTTP**

- HTTP este considerat în mod general un protocol _connectionless_, în sensul în care nu este păstrată constant o conexiune între client și server - după ce clientul a stabilit o conexiune, a trimis o cerere și a primit un răspuns, conexiunea este imediat încheiată (conexiunea este realizată prin intermediul _TCP_)
- în loc să mențină o conexiune permanentă între client și server, HTTP stabilește o **conexiune temporară numită "session"** pentru fiecare cerere
- această abordare fără conexiune face ca protocolul HTTP să fie _ușor și eficient_, deoarece nu necesită stabilirea și menținerea unei conexiuni constante între client și serve; acest lucru permite serverului să gestioneze mai multe cereri simultan și să economisească resurse de rețea
- HTTP este de asemenea un **protocol fără stare (stateless)**, ceea ce înseamnă că fiecare cerere și răspuns HTTP sunt independente și nu păstrează informații de stare între ele (de exemplu, dacă un client web face o cerere la un server web și primește un răspuns, acest răspuns nu va avea nicio legătură cu cererile ulterioare)

#### Exemplu simplu & custom de server HTTP

- în cadrul seminarului sunt prezentate 2 modalități de a realiza un server HTTP:
  - prima - cea simplă, servește un fîșier index.html pe ruta "/"
  - a doua - custom, permite accesarea resurselor din directorul curent și definește un răspuns special de eroare în cazul în care nu sunt regăsite resursele cerute

#### REST, Flask

**REST (Representational State Transfer)** = arhitectură utilizată în dezvoltarea aplicațiilor web, care se bazează pe protocoalele HTTP și HTTPS pentru a permite comunicația între client și server. REST se bazează pe ideea că orice resursă (cum ar fi o pagină web sau o imagine) poate fi accesată prin intermediul unui URL unic.

- pentru implementarea unui exemplu simplu REST a fost utilizat frameworkul [Flask](https://flask.palletsprojects.com/en/2.2.x/)
