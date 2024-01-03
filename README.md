# Python Record Manager with MySQL Integration

## Overview

This Python application is a record manager designed to seamlessly interact with MySQL databases. It offers a Python console interface for efficiently handling various database operations, such as adding, updating, deleting, and querying records in MySql.

## Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector Python (install using `pip install mysql-connector-python`)

## Setup

1. Install Python 3.x: [Python Downloads](https://www.python.org/downloads/)
2. Install MySQL Server: [MySQL Downloads](https://dev.mysql.com/downloads/)
3. Install MySQL Connector Python: `pip install mysql-connector-python`

## Configuration

1. Open `config.py` and update the MySQL database connection details:

```python
# config.py

mydb = mysql.connector.connect(host="localhost",user="user",passwd="####",port="####",database="Course")
```

## Features

- **Add Record**: Inclusion of a new record into the database.

- **Update Record**: Modification of an existing record in the database.

- **Delete Record**: Removal of a record from the database.

- **View Records**: Displaying all records stored in the database.

## Contributing

Contribute to the project by opening issues or submitting pull requests. Embrace collaboration, and let's enhance this record manager together!

## License

This project is licensed under the MIT License - refer to the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the Python and MySQL communities for their invaluable documentation and support.

Enjoy efficient record management!
