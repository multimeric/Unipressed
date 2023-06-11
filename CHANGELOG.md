
## Changelog

### 1.2.0

#### Added
* `DatasetClient.search()` now has an `include_isoform` parameter, which specifies if you want isoforms to be returned [[#27](https://github.com/multimeric/Unipressed/pull/27), @godotgildor]
* Python 3.11 is now officially supported

#### Changed
* Auto-generated type definitions have been regenerated [[#28](https://github.com/multimeric/Unipressed/pull/28)]. This pulls upstream changes from Uniprot which are description-only:
    * All the `cc_` query fields for `Arba` and `Unirule` such as `cc_cofactor` and `cc_domain` hav updated descriptions
    * `Uniparc`'s list of databases has increased in the `database` query field

### 1.1.0

#### Changed
* `unipressed.IdMappingClient.get_status()` now returns a `Literal`, which gives your type checker/IDE access to the possible return values.

#### Fixed
* `unipressed.IdMappingClient.get_status()` now wraps a bug in the UniProt API ([#293](https://github.com/ebi-uniprot/uniprot-rest-api/issues/293)), ensuring that it will return a valid job status even when the API itself does not. [[#21](https://github.com/multimeric/Unipressed/issues/21)]

### 1.0.0

#### Changed

* **Breaking**: Reworked the search API. Broadly this means that rather than using `unipressed.UniprotkbSearch`, you should now use the `unipressed.UniprotkbClient` class, which encapsulates the dataset's APIs. You can then perform a search query using `Uniprotkb.search()`.
* **Breaking**: Restructured the Python package. Most imports have changed.

#### Added

* The new client objects support `.fetch_one()` and `.fetch_many()` which can be used to look up one or more database entries using their IDs
* An ID mapping client. This can be accessed as `unipressed.IdMappingClient`

### 0.2.0

**Note, if you are using Visual Studio Code, please update Pylance to at least version 2022.8.20.
A bug in earlier versions will give you false errors with this new release of `unipressed`**.

#### Added
* Also allow strings within the query dictionary, so that e.g. this is now allowed:
    ```python
    {
        "and_": [
            "foo*",
            "*bar"
        ]
    }
    ```
    This will search for all proteins that have any field that starts with `foo` and any field that ends with `bar`.

* Auto generated docstrings for all fields
* Examples to the documentation of each field
* Certain missing query fields for the `arba` dataset:
    * `cc_scl_term`
* Certain missing query fields for the `proteomes` dataset:
    * `organism_id`
    * `taxonomy_id`
* Certain missing query fields for the `unirule` dataset:
    * `cc_scl_term`
* Certain missing query fields for the `uniparc` dataset:
    * `taxonomy_id`
* Certain missing query fields for the `uniprotkb` dataset:
    * `organism_id`
    * `taxonomy_id`
    * `virus_host_id`

#### Removed
* Uniprot seem to have removed certain `uniprokb` query fields, so these are now not part of the accepted query type:
    * `ft_metal`
    * `ftlen_metal`
    * `ft_ca_bind`
    * `ftlen_ca_bind`
    * `ft_np_bind`
    * `ftlen_np_bind`
* Likewise, some `uniprotkb` return fields have been removed:
    * `ft_ca_bind`
    * `ft_metal`
    * `ft_np_bind`

#### Internal
* Move from `pyhumps` to `inflection` for code generation
* Add a test for the date field
* Added tests for all datasets
* Add types for code generation API