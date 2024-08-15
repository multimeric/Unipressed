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

::: unipressed.dataset.core.DatasetClient
    options:
        show_bases: False

::: unipressed.dataset.core.FetchManyClient

::: unipressed.dataset.search.Search
    options:
        show_bases: False
        members:
            - each_response
            - each_page
            - each_record

::: unipressed.IdMappingClient

::: unipressed.id_mapping.core.IdMappingJob

::: unipressed.id_mapping.core.IdMappingResult

::: unipressed.ArbaClient
    options:
        members: None

::: unipressed.CitationsClient
    options:
        members: None

::: unipressed.DiseasesClient
    options:
        members: None

::: unipressed.KeywordsClient
    options:
        members: None

::: unipressed.LocationsClient
    options:
        members: None

::: unipressed.ProteomesClient
    options:
        members: None

::: unipressed.TaxonomyClient
    options:
        members: None

::: unipressed.UniparcClient
    options:
        members: None

::: unipressed.UniprotkbClient
    options:
        members: None

::: unipressed.UnirefClient
    options:
        members: None

::: unipressed.UniruleClient
    options:
        members: None

{% include-markdown "../CHANGELOG.md" %}