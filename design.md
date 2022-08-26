## Decisions

* Pure type annotations
  * Needs an additional runtime type checker `beartype`, `typeguard` anyway
  * Autocomplete doesn't work with `Unpack[]` yet
  * Without `Unpack[]`, would have to use heavily redundant `@overload`
* 