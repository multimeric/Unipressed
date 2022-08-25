
## Changelog

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