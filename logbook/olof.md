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

## 2023-03-29
Upgraded from Neo4j 4.4.5 to 5.6.0. https://neo4j.com/docs/upgrade-migration-guide/current/version-5/migration/migrate-databases/


https://neo4j.com/docs/graph-data-science/current/machine-learning/linkprediction-pipelines/config/

Create a pipe:
```sql
CALL gds.beta.pipeline.linkPrediction.create('pipe2');
```

https://neo4j.com/docs/graph-data-science/current/machine-learning/node-embeddings/fastrp/  
Add a node property:
```sql
CALL gds.beta.pipeline.linkPrediction.addNodeProperty('pipe2', 'fastRP', {
    mutateProperty: 'embedding',
    embeddingDimension: 256,
    randomSeed: 42
});
```

Add features:
```sql
CALL gds.beta.pipeline.linkPrediction.addFeature('pipe2', 'hadamard', {
    nodeProperties: ['embedding', 'zipCode']
}) YIELD featureSteps;
```

Configure the split:
```sql
CALL gds.beta.pipeline.linkPrediction.configureSplit('pipe2', {
    testFraction: 0.25,
    trainFraction: 0.6,
    validationFolds: 3
}) YIELD splitConfig;
```

Adding model candidates:
```sql
CALL gds.alpha.pipeline.linkPrediction.addMLP('pipe2', {
    hiddenLayerSizes: [4, 2],
    penalty: 0.5,
    tolerance: 0.001,
    patience: 2,
    classWeights: [0.55, 0.45],
    focusWeight: {range: [0.0, 0.1]}
}) YIELD parameterSpace;
```

Zip code is a string, so it needs to be converted to a number:
```sql
MATCH (n:School) SET n.zipCode = toInteger(n.zipCode);
```

Project graph:
```sql
CALL gds.graph.project(
    'testGraph1',
    {
        School: {
            properties: 'zipCode'
        }
    },
    {
        PART_OF: {
            orientation: 'UNDIRECTED'
        }
    }
)
```

Estimate memory:
```sql
CALL gds.beta.pipeline.linkPrediction.train.estimate('testGraph1', {
    pipeline: 'pipe2',
    modelName: 'lp-pipeline-model',
    targetRelationshipType: 'PART_OF'
}) YIELD requiredMemory;
```

Next is to train the model.

## 2023-03-30

FastRP algorithm:
https://arxiv.org/pdf/1908.11512.pdf

We've been writing the Project plan.

Reading this book:  
[https://go.neo4j.com/rs/710-RRC-335/images/Graph%20Data%20Science%20For%20Dummies%20Neo4j%202nd%20Edition.pdf?_gl=1*12b2zlb*_ga*MjA2MzQwMjk1Ny4xNjc5NDA0MDM3*_ga_DL38Q8KGQC*MTY4MDE3Njg4My44LjEuMTY4MDE3Njk5Ny41OS4wLjA.](https://go.neo4j.com/rs/710-RRC-335/images/Graph%20Data%20Science%20For%20Dummies%20Neo4j%202nd%20Edition.pdf?_gl=1*12b2zlb*_ga*MjA2MzQwMjk1Ny4xNjc5NDA0MDM3*_ga_DL38Q8KGQC*MTY4MDE3Njg4My44LjEuMTY4MDE3Njk5Ny41OS4wLjA.)

## 2023-03-31

Continued with the Project plan. Pretty much finished.