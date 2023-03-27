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

## 2023-03-27

Get all schools with matching municipality name:
```sql
MATCH (m:Municipality)-[:PART_OF]-(s:School) RETURN m.name, s.name;
```

Get all municipalities with schools for that municipality:
```sql
MATCH (m:Municipality) OPTIONAL MATCH (m)<-[:PART_OF]-(s) RETURN {municipality: m.name, schools :collect(s.name)};
```

Been trying to fuzzy match the evaluation names to the school names.

Tried https://github.com/RobinL/fuzzymatcher , takes extremely long time to run, no result yet as it takes so long.

Using thefuzz instead:
https://github.com/seatgeek/thefuzz  

The idea is to create a lookup table with all the school names and the unique names from the evaluation names using thefuzz.  
Then use the lookup table to merge the evaluation names to the school names with pandas.

The scorer `partial_ratio` seems to yield the most promising results.




