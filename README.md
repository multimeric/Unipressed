```python
from rich.pretty import install
# Use rich to pretty print outputs, but truncate nested objects
install(max_depth=2)
```

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


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'primaryAccession'</span>: <span style="color: #008000; text-decoration-color: #008000">'A0A088CK67'</span>, <span style="color: #008000; text-decoration-color: #008000">'genes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>, <span style="color: #008000; text-decoration-color: #008000">'sequence'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span><span style="font-weight: bold">}</span>
</pre>



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


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
<span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'entryType'</span>: <span style="color: #008000; text-decoration-color: #008000">'UniProtKB reviewed (Swiss-Prot)'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'primaryAccession'</span>: <span style="color: #008000; text-decoration-color: #008000">'Q96RW7'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'secondaryAccessions'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'uniProtkbId'</span>: <span style="color: #008000; text-decoration-color: #008000">'HMCN1_HUMAN'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'entryAudit'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'annotationScore'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'organism'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'proteinExistence'</span>: <span style="color: #008000; text-decoration-color: #008000">'1: Evidence at protein level'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'proteinDescription'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'genes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'comments'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'features'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'keywords'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'references'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'uniProtKBCrossReferences'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'sequence'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'extraAttributes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>
<span style="font-weight: bold">}</span>
</pre>



You can request a single record by ID:


```python
Uniprotkb.fetch_one("Q96RW7")
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
<span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'entryType'</span>: <span style="color: #008000; text-decoration-color: #008000">'UniProtKB reviewed (Swiss-Prot)'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'primaryAccession'</span>: <span style="color: #008000; text-decoration-color: #008000">'Q96RW7'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'secondaryAccessions'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'uniProtkbId'</span>: <span style="color: #008000; text-decoration-color: #008000">'HMCN1_HUMAN'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'entryAudit'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'annotationScore'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'organism'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'proteinExistence'</span>: <span style="color: #008000; text-decoration-color: #008000">'1: Evidence at protein level'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'proteinDescription'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'genes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'comments'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'features'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'keywords'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'references'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'uniProtKBCrossReferences'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'sequence'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
    <span style="color: #008000; text-decoration-color: #008000">'extraAttributes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>
<span style="font-weight: bold">}</span>
</pre>



You can also request multiple records:


```python
install(max_depth=2)
```


```python
Uniprotkb.fetch_many(["A0A0C5B5G6", "A0A1B0GTW7"])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
<span style="font-weight: bold">[</span>
    <span style="font-weight: bold">{</span>
        <span style="color: #008000; text-decoration-color: #008000">'entryType'</span>: <span style="color: #008000; text-decoration-color: #008000">'UniProtKB reviewed (Swiss-Prot)'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'primaryAccession'</span>: <span style="color: #008000; text-decoration-color: #008000">'A0A0C5B5G6'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'uniProtkbId'</span>: <span style="color: #008000; text-decoration-color: #008000">'MOTSC_HUMAN'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'entryAudit'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'annotationScore'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5.0</span>,
        <span style="color: #008000; text-decoration-color: #008000">'organism'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'proteinExistence'</span>: <span style="color: #008000; text-decoration-color: #008000">'1: Evidence at protein level'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'proteinDescription'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'genes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'comments'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'features'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'geneLocations'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'keywords'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'references'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'uniProtKBCrossReferences'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'sequence'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'extraAttributes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>
    <span style="font-weight: bold">}</span>,
    <span style="font-weight: bold">{</span>
        <span style="color: #008000; text-decoration-color: #008000">'entryType'</span>: <span style="color: #008000; text-decoration-color: #008000">'UniProtKB reviewed (Swiss-Prot)'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'primaryAccession'</span>: <span style="color: #008000; text-decoration-color: #008000">'A0A1B0GTW7'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'secondaryAccessions'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'uniProtkbId'</span>: <span style="color: #008000; text-decoration-color: #008000">'CIROP_HUMAN'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'entryAudit'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'annotationScore'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5.0</span>,
        <span style="color: #008000; text-decoration-color: #008000">'organism'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'proteinExistence'</span>: <span style="color: #008000; text-decoration-color: #008000">'1: Evidence at protein level'</span>,
        <span style="color: #008000; text-decoration-color: #008000">'proteinDescription'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'genes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'comments'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'features'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'keywords'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'references'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'uniProtKBCrossReferences'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'sequence'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>,
        <span style="color: #008000; text-decoration-color: #008000">'extraAttributes'</span>: <span style="color: #808000; text-decoration-color: #808000">...</span>
    <span style="font-weight: bold">}</span>
<span style="font-weight: bold">]</span>
</pre>



### ID Mapping

Unipressed also provides one other unique client, which is designed for mapping identifiers. You provide the source and destination database (both of which will autocomplete in VS Code), and a list of identifiers for the source database.


```python
from unipressed import IdMappingRequest
request = IdMappingRequest(
    source="UniProtKB_AC-ID", dest="Gene_Name", ids={"A1L190", "A0JP26", "A0PK11"}
).submit()
list(request.each_result())
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">
<span style="font-weight: bold">[</span>
    <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'from'</span>: <span style="color: #008000; text-decoration-color: #008000">'A0PK11'</span>, <span style="color: #008000; text-decoration-color: #008000">'to'</span>: <span style="color: #008000; text-decoration-color: #008000">'CLRN2'</span><span style="font-weight: bold">}</span>,
    <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'from'</span>: <span style="color: #008000; text-decoration-color: #008000">'A0JP26'</span>, <span style="color: #008000; text-decoration-color: #008000">'to'</span>: <span style="color: #008000; text-decoration-color: #008000">'POTEB3'</span><span style="font-weight: bold">}</span>,
    <span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'from'</span>: <span style="color: #008000; text-decoration-color: #008000">'A1L190'</span>, <span style="color: #008000; text-decoration-color: #008000">'to'</span>: <span style="color: #008000; text-decoration-color: #008000">'SYCE3'</span><span style="font-weight: bold">}</span>
<span style="font-weight: bold">]</span>
</pre>



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
