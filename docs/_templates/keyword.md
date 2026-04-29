# Keyword page template

This file is a reference template for the consistent layout we want every
keyword page in the OPM Flow Reference Manual to follow once the manual is
edited as Markdown directly. The `fodt2md` converter does not yet enforce
this template — it preserves the structure of the source FODT — but new
keyword pages added by hand should use the headings below.

```markdown
---
title: 'KEYWORD – Short description'
source: parts/chapters/subsections/4.3/KEYWORD.fodt
---

# KEYWORD – Short description

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |  ✓  |     |       |         |          |         |          |

## Synopsis

One-paragraph summary of what the keyword does.

## Description

Detailed explanation of the keyword and its parameters.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
|  1  | …    | …           | …       |

## Example

```eclipse
KEYWORD
   1*  /
```

## Notes

- Edge cases, restrictions, OPM-specific deviations from the reference
  semantics.

## See also

- [`OTHERKW`](OTHERKW.md)
```
