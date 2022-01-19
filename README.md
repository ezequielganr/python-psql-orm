# PSQL ORM

## Installation :pushpin:

To install the library you must make a ```git clone``` of the repository, create a virtual environment and install the dependencies and configure your database in ```config.json``` file

## User guide :dart:

Simple example of use

### Fetch all data

```
import psql

PSQL_TABLE = 'users'

res = psql.get(PSQL_TABLE)
print(res)
```

### Find all data of a condition

```
import psql

PSQL_TABLE = 'users'

cond = 'state=1'

res = psql.where(PSQL_TABLE, cond)
print(res)
```

### Search for a data by its condition

```
import psql

PSQL_TABLE = 'users'

cond = 'id=2'

res = psql.find(PSQL_TABLE, cond)
print(res)
```

### Insert into database

```
import psql

PSQL_TABLE = 'users'

fields = ('name', 'phone')

data = ('Oliver James', '+541122334455')

res = psql.insert(PSQL_TABLE, fields, data)
print(res)
```

### Update in database

```
import psql

PSQL_TABLE = 'users'

fields = ('name', 'phone')

data = ('Oliver James', '+541122334455')

cond = 'id=4'

res = psql.update(PSQL_TABLE, fields, data, cond)
print(res)
```

### Delete in database

```
import psql

PSQL_TABLE = 'users'

cond = 'id=2'

res = psql.delete(PSQL_TABLE, cond)
print(res)
```

## License :memo:

This repository is made for demonstration purposes
