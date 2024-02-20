# Postgres Bulk Data Copy

This project provides a utility for efficiently copying large amounts of data into a PostgreSQL database using the bulk data copy feature. It is designed to handle high-volume data imports and exports, making it ideal for scenarios such as data migration, data warehousing, and ETL (Extract, Transform, Load) processes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

# Prerequisites

- Python 3.6+ : `brew install python3`
- pip3 : `brew install pip3`
- psycopg2 library : `brew install psycopg2`
  - if it failes with `ssl not found` then run
  ```shell
  env LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib" pip --no-cache install psycopg2
  ```

# Install pip requirements
```shell
pip install -r requirements.txt
```

## Usage

### Update postgres connection details
```
    conn = psycopg2.connect(
        host='<DB_HOST>',
        port=<DB_PORT>,
        user='<DB_USER>',
        password='<DB_PASSWORD>',
        database='<DB_NAME>'
    )
```


### Update DB table details
- Update 
  - `file_name` :  csv file name which should contain all the table columns without csv header
  - `table_name`: Table name
  - `table_columns`: All the column names from the table to be copied

### Run
```shell
arch -arm64 python3 bulk-copy.py
```
