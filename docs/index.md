---
hide:
  - navigation
---
{% include-markdown "../README.md" %}

## Screenshots

<figure markdown>
![](media/query_keys.png){ width="400" }
<figcaption> Autocompletion for query keys</figcaption>
</figure>

<figure markdown>
![](media/enum_values.png){ width="400" }
<figcaption> Autocompletion for query values</figcaption>
</figure>

<figure markdown>
![](media/docstrings.png){ width="400" }
<figcaption>Documentation for almost all types</figcaption>
</figure>

<figure markdown>
![](media/field_completion.png){ width="400" }
<figcaption> Autocompletion for return fields</figcaption>
</figure>

## API

### `Search`
::: unipressed.base.Search

### `ArbaSearch`
::: unipressed.ArbaSearch
    options:
        members: None

### `CitationsSearch`
::: unipressed.CitationsSearch
    options:
        members: None

### `DiseasesSearch`
::: unipressed.DiseasesSearch
    options:
        members: None

### `KeywordsSearch`
::: unipressed.KeywordsSearch
    options:
        members: None

### `LocationsSearch`
::: unipressed.LocationsSearch
    options:
        members: None

### `ProteomesSearch`
::: unipressed.ProteomesSearch
    options:
        members: None

### `TaxonomySearch`
::: unipressed.TaxonomySearch
    options:
        members: None

### `UniparcSearch`
::: unipressed.UniparcSearch
    options:
        members: None

### `UniprotkbSearch`
::: unipressed.UniprotkbSearch
    options:
        members: None

### `UnirefSearch`
::: unipressed.UnirefSearch
    options:
        members: None

### `UniruleSearch`
::: unipressed.UniruleSearch
    options:
        members: None

## Changelog

### 0.1.2

#### Added
* Auto generated docstrings for all fields
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
* Add types for code generation API