# Logbook Olof

## 2023-03-23

https://www.scb.se/contentassets/a6271ac340ba48deb6dd41a6cb655c1c/vad-ar-ett-index.pdf - Vad är ett index?

https://www.skolverket.se/skolutveckling/statsbidrag/statsbidrag-for-likvardig-skola-2022  
`Index per skolenhet statsbidrag för likvärdig skola 2022.pdf`  
Högre andel som inte förväntas bli behöriga till gymnasiet, mer pengar.  

https://www.skolverket.se/skolutveckling/statistik/sok-statistik-om-forskola-skola-och-vuxenutbildning?sok=SokA  
För att söka statistik om skolor

Försökt få ut vettig data från den gamla datan i MSSQL.  
Startat upp lokal Neo4j med den nya datan.

## 2023-03-24

Listor över regioner, kommuner och skolor.
```sql
MATCH (n:Region) RETURN n.name;
```
```sql
MATCH (n:Municipality) RETURN n.name;
```
```sql
MATCH (n:School) RETURN n.name;
```

® fungerar som separator i csv-filerna.