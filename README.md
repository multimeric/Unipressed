# Unipressed

Unipressed (Uniprot REST) is an API client for the protein database [Uniprot](Unipy).
It provides thoroughly typed and documented code to ensure your use of the library is clear, type safe and statically analysable.

## Example


## Decisions

* Pure type annotations
  * Needs an additional runtime type checker `beartype`, `typeguard` anyway
  * Autocomplete doesn't work with `Unpack[]` yet
  * Without `Unpack[]`, would have to use heavily redundant `@overload`
* 