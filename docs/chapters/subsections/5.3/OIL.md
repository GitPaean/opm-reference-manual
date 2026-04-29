---
title: 'OIL – Activate the Oil Phase in the Model'
source: parts/chapters/subsections/5.3/OIL.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc97439-1778172979"></a>OIL – Activate the Oil Phase in the Model

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc14499-3701168388312"></a>Description

This keyword indicates that the oil phase is present in the model and must be used for oil\-gas, oil\-water, oil\-water\-gas input decks that contain the oil phase. The keyword will also invoke data input file checking to ensure that all the required oil phase input parameters are defined in the input deck.
There is no data required for this keyword and there is no terminating “/” for this keyword.

#### <a id="-refheading-toc14501-3701168388313"></a>Example

```eclipse
--
--       OIL PHASE IS PRESENT IN THE RUN
--
OIL
```

The above example declares that the oil phase is active in the model.
