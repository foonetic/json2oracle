# json2oracle

Makes anchor smart contracts for oracles based on a JSON schema.

##### Usage:
```
usage: main.py [-h] oracle_schema_path contract_template_path space
positional arguments:
  oracle_schema_path    Path to oracle schema
  contract_template_path
                        Path to contract template
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
| Name        | Description                     |
| ----------- | -----------                     |
| name        | Name of the oracle              |
| fields      | List of data fields             |
| space       | Amount of space to allocate     |