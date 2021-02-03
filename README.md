# crud-python-click
A CRUD terminal program, created with click framework

### Requires
Python3

### Installation
1. Download as ZIP
2. Extract files
3. In the folder, open a terminal
4. `virtualenv --python=python3 venv`
5. `pip install --editable`
6. `source venv/bin/activate`
7. And ready to use

### Usage
Commands:
`pv --help`

`pv clients --help` and you see:
```bash
(venv) napoli:crud-python-click/ (main) $ pv clients
Usage: pv clients [OPTIONS] COMMAND [ARGS]...

  Manages the clients lifecycle

Options:
  --help  Show this message and exit.

Commands:
  create  Creates a new client
  delete  Deletes a client
  list    List all clients
  update  Updates a client

```
