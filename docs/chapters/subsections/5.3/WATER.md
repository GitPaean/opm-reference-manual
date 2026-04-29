---
title: 'WATER – Activate the Water Phase in the Model'
source: parts/chapters/subsections/5.3/WATER.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

### <a id="-refheading-toc38611-2267116897"></a>WATER – Activate the Water Phase in the Model

| [RUNSPEC](#3runspec-section) | [GRID](#4grid-section) | [EDIT](#5edit-section) | [PROPS](#6props-section) | [REGIONS](#7regions-section) | [SOLUTION](#8solution-section) | [SUMMARY](#9summary-section) | [SCHEDULE](#10schedule-section) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### <a id="-refheading-toc14499-370116838832"></a>Description

This keyword indicate that the water phase is present in the model and must be used for gas\-water, oil\-water, oil\-water\-gas input decks that contain the water phase. The keyword will also invoke data input file checking to ensure that all the required water phase input parameters are defined in the input deck.
There is no data required for this keyword and there is no terminating “/” for this keyword.

#### <a id="-refheading-toc14501-370116838832"></a>Example

```eclipse
--
--       WATER PHASE IS PRESENT IN THE RUN
--
WATER
```

The above example declares that the water phase is active in the model.
