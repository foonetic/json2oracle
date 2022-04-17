# json2oracle

Makes anchor smart contracts for oracles based on a JSON schema.

##### Usage:
```
usage: main.py [-h] oracle_schema_path contract_template_path space
positional arguments:
  oracle_schema_path    Path to oracle schema
  contract_template_path
                        Path to contract template
  space                 Space to allocate for the oracle
  ```

##### Example schema:
```
{
    "name": "test_oracle",
    "fields": [{
            "name": "activated",
            "data_type": "bool"
        },
        {
            "name": "balance",
            "data_type": "u64"
        }
    ],
    "space": 10
}
```
##### Required fields:
| Name        | Type                            |
| ----------- | -----------                     |
| name        | Name of the oracle              |
| fields      | List of (name, type)            |
| space       | Amount of space to allocate     |