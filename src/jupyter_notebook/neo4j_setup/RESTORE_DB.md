# Restoring the Database

There is a `neo4j.dump` file located at `/var/lib/neo4j/data/dumps`. This is the 4.4.5 version of the database. To restore the database, run the following command:

```bash
sudo neo4j stop
```

```bash
sudo neo4j-admin load --from=/var/lib/neo4j/data/dumps neo4j --overwrite-destination=true
```

```bash
sudo neo4j-admin database migrate neo4j --force-btree-indexes-to-range
```

```bash
sudo neo4j start
```

```bash
sudo neo4j status
```