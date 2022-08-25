# Unipressed

**Please visit the [project website](https://multimeric.github.io/Unipressed/) for more comprehensive documentation.**

## Introduction

Unipressed (Uniprot REST) is an API client for the protein database [Uniprot](https://www.uniprot.org/).
It provides thoroughly typed and documented code to ensure your use of the library is easy, fast, and correct!

### Example
Let's say we're interested in very long proteins that are encoded within a chloroplast, in any organism:


```python
import json
from unipressed import Uniprotkb

for record in Uniprotkb.search(
    query={
        "and_": [
            {"organelle": "chloroplast"},
            {"length": (5000, "*")}
        ]
    },
    fields=["length", "gene_names"]
).each_record():
    display(record)
```


    {'primaryAccession': 'A0A088CK67',
     'genes': [{'geneName': {'evidences': [{'evidenceCode': 'ECO:0000313',
          'source': 'EMBL',
          'id': 'AID67672.1'}],
        'value': 'ftsH'}}],
     'sequence': {'length': 5242}}


### Advantages

* Detailed type hints for autocompleting queries as you type
* Autocompletion for return fields
* Documentation for each field
* Automatic results parsing, for `json`, `tsv`, `list`, and `xml`
* Built-in pagination, so you don't have to handle any of that yourself!
* Most of the API is automatically generated, ensuring very rapid updates whenever the API changes
* Thoroughly tested, with 41 unit tests and counting!

## Usage

### Installation

If you're using poetry:
```bash
poetry add unipressed
```

Otherwise:
```bash
pip install unipressed
```

### Dataset Clients

The `unipressed` module exports a client object for each UniProt dataset:


```python
# TODO: once https://github.com/Textualize/rich/issues/2485 and https://github.com/Textualize/rich/issues/2486
# are closed, we can change to using Rich's pretty printing

# This replaces the default Jupyter print with pprint, which elides deep nested objects for concision
import pprint
printer = pprint.PrettyPrinter(depth=1, indent=4)
for key in ["text/html", "text/markdown"]:
     get_ipython().display_formatter.formatters[key].for_type(object, printer.pformat)
```


```python
from unipressed import Uniprotkb, Uniparc
```

With one of these clients, you can search the dataset:


```python
records = Uniprotkb.search({
    "length": (5000, 6000)
}).each_record()

# Show the first record
next(records)
```




{   'annotationScore': 5.0,
    'comments': [...],
    'entryAudit': {...},
    'entryType': 'UniProtKB reviewed (Swiss-Prot)',
    'extraAttributes': {...},
    'features': [...],
    'genes': [...],
    'keywords': [...],
    'organism': {...},
    'primaryAccession': 'Q96RW7',
    'proteinDescription': {...},
    'proteinExistence': '1: Evidence at protein level',
    'references': [...],
    'secondaryAccessions': [...],
    'sequence': {...},
    'uniProtKBCrossReferences': [...],
    'uniProtkbId': 'HMCN1_HUMAN'}



You can request a single record by ID:


```python
Uniprotkb.fetch_one("Q96RW7")
```




{   'annotationScore': 5.0,
    'comments': [...],
    'entryAudit': {...},
    'entryType': 'UniProtKB reviewed (Swiss-Prot)',
    'extraAttributes': {...},
    'features': [...],
    'genes': [...],
    'keywords': [...],
    'organism': {...},
    'primaryAccession': 'Q96RW7',
    'proteinDescription': {...},
    'proteinExistence': '1: Evidence at protein level',
    'references': [...],
    'secondaryAccessions': [...],
    'sequence': {...},
    'uniProtKBCrossReferences': [...],
    'uniProtkbId': 'HMCN1_HUMAN'}



You can also request multiple records:


```python
printer._depth = 2
```


```python
Uniprotkb.fetch_many(["A0A0C5B5G6", "A0A1B0GTW7"])
```




[   {   'annotationScore': 5.0,
        'comments': [...],
        'entryAudit': {...},
        'entryType': 'UniProtKB reviewed (Swiss-Prot)',
        'extraAttributes': {...},
        'features': [...],
        'geneLocations': [...],
        'genes': [...],
        'keywords': [...],
        'organism': {...},
        'primaryAccession': 'A0A0C5B5G6',
        'proteinDescription': {...},
        'proteinExistence': '1: Evidence at protein level',
        'references': [...],
        'sequence': {...},
        'uniProtKBCrossReferences': [...],
        'uniProtkbId': 'MOTSC_HUMAN'},
    {   'annotationScore': 5.0,
        'comments': [...],
        'entryAudit': {...},
        'entryType': 'UniProtKB reviewed (Swiss-Prot)',
        'extraAttributes': {...},
        'features': [...],
        'genes': [...],
        'keywords': [...],
        'organism': {...},
        'primaryAccession': 'A0A1B0GTW7',
        'proteinDescription': {...},
        'proteinExistence': '1: Evidence at protein level',
        'references': [...],
        'secondaryAccessions': [...],
        'sequence': {...},
        'uniProtKBCrossReferences': [...],
        'uniProtkbId': 'CIROP_HUMAN'}]



### ID Mapping

Unipressed also provides one other unique client, which is designed for mapping identifiers. You provide the source and destination database (both of which will autocomplete in VS Code), and a list of identifiers for the source database.


```python
from unipressed import IdMappingRequest
request = IdMappingRequest(
    source="UniProtKB_AC-ID", dest="Gene_Name", ids={"A1L190", "A0JP26", "A0PK11"}
).submit()
list(request.each_result())
```




[   {'from': 'A0PK11', 'to': 'CLRN2'},
    {'from': 'A0JP26', 'to': 'POTEB3'},
    {'from': 'A1L190', 'to': 'SYCE3'}]



Note that, if you submit a large number of IDs, you might need to add a `sleep()` call between submitting the request and retrieving the results:

### Query Syntax

You can't go wrong by following the type hints.
I strongly recommend using something like [`pylance`](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) for [Visual Studio Code](https://code.visualstudio.com/), which will provide automatic completions and warn you when you have used the wrong syntax.

If you already know how to use the Uniprot query language, you can always just input your queries as strings:
```python
UniprotkbSearch(query="(gene:BRCA*) AND (organism_id:10090)")
```


However, if you want some built-in query validation and code completion using Python's type system, then you can instead use a dictionary.
The simplest query is a dictionary with a single key: 
```python
UniprotkbSearch(query={ "family": "kinase"})
```
For brevity, for the rest of this section we will omit everything but the value of the `query` argument.

You can compile more complex queries using the `and_`, `or_` and `not_` keys.
These first two operators take a list of query dictionaries: 
```python
{
    "and_": [
        {"family": "kinase"},
        {"organism_id": "9606"},
    ]
}
```

Most "leaf" nodes of the query tree (ie those that aren't operators like `and_`) are strings, integers or floats, which you input as normal Python literals as you can see above.
For string fields, you also have access to wildcards, namely the `*` character. 
For example, if you want every human protein belonging to a gene whose name starts with `PRO`, you could use:
```python
{
    "and_": [
        {"gene": "PRO*"},
        {"organism_id": "9606"},
    ]
}
```

A few query fields are *ranges*, which you input using a tuple with two elements, indicating the start and end of the range.
If you use the literal `"*"` then you can leave the range open at one end. 
For example, this query returns any protein that is in the range $(5000, \infty)$
```python
{"length": (5000, "*")}
```

Finally, a few query fields take dates.
These you input as a Python `datetime.date` object.
For example, to find proteins added to UniProt since July 2022, we would do:
```python
from datetime import date

UniprotkbSearch(query={"date_created": (date(2022, 7, 1), "*")})
```

### Use with Visual Studio Code
To get VS Code to offer suggestions, press the `Trigger Suggest` shortcut which is usually bound to `Ctrl + Space`.
In particular, code completion generally won't work *until* you open a string literal using a quotation mark.

Secondly, to get live access to the documentation, you can either use the `Show Hover` shortcut, which is usually bound to `Ctrl + K, Ctrl + I`, or you can install the [`docs-view`](https://marketplace.visualstudio.com/items?itemName=bierner.docs-view) extension, which lets you view the docstrings in the sidebar without interfering with your code.
