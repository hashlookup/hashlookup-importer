# hashlookup-importer

Directory importer for a hashlookup server.

# Usage

~~~
usage: hashlookup-importer.py [-h] [-v] [-s SOURCE] [-p PARENT] [--parent-meta PARENT_META [PARENT_META ...]] [-d DIR] [-u] [-e]

Directory importer for hashlookup server

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  -s SOURCE, --source SOURCE
                        Source name to be used as meta
  -p PARENT, --parent PARENT
                        Parent SHA-1 of the import
  --parent-meta PARENT_META [PARENT_META ...]
                        Add metadata to parent, format is key,value
  -d DIR, --dir DIR     Directory to import
  -u, --update          Update hash if it already exists. default is not to update existing hashlookup record but to delete existing records and update.
  -e, --skip-exists     Skip import of existing hashlookup record
~~~

