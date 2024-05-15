# _Seminar 12_

## Conținut

- XML-RPC
- JSON-RPC

---

**XML-RPC (XML Remote Procedure Call)** = protocol de comunicare și set de reguli pentru transmiterea de date între aplicații pe internet

- este o tehnică de comunicare utilizată în special în dezvoltarea aplicațiilor web, ce permite apelarea metodelor sau funcțiilor de la distanță prin intermediul unor cereri și răspunsuri XML
- prin intermediul RPC se poate invoca cod de la distanță pe un calculator ce se află în rețea ca și cum ar fi fost rulat de pe mașina respectivă
- XML-RPC se bazează pe formatul **XML** pentru a structura datele și pe HTTP pentru a le transmite între client și server
- protocolul definește o convenție pentru codificarea și decodificarea datelor în format XML, astfel încât acestea să poată fi transmise și interpretate de către diferite aplicații ori platforme
- _mod de funcționare_:
  - clientul trimite o cerere către un server care expune anumite metode sau funcții, specificând parametrii necesari
  - serverul primește cererea, execută metoda corespunzătoare și returnează rezultatul înapoi către client (răspunsul este, de asemenea, formatat în XML)

Un avantaj al XML-RPC este faptul că este un protocol simplu și ușor de implementat, făcându-l potrivit pentru interacțiunea între diferite tehnologii și platforme. Cu toate acestea, XML-RPC poate avea o performanță mai scăzută în comparație cu alte protocoale mai moderne, cum ar fi JSON-RPC sau gRPC.

În cazul **JSON-RPC**, procesul este similar, un request către server având 3 componente:

- method -> numele funcției ce va fi apelată pe server
- params -> argumentele ce vor fi pasate funcției apelate
- id -> string ori număr ce servește drept referință pentru răspunsul serverului

Serverul, odată ce invocă funcția, trimite un răspuns format din:

- rezultat/eroare
- id -> corespunzător cererii căreia îi răspunde

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*w6NQUXL3Q5kiQcbCz1PpOg.png)
