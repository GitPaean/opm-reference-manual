### HMMULT -- History Match Grid Transmissibility & Pore Volume Gradient Cumulative Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HMMULT series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The keyword consists of the first six characters of "HMMULT" followed by a one or two character string shown in , that determines the transmissibility direction, for example, HMMULTX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| Grid<br>Keyword | HMMULT<br>Keyword | Grid<br>Keyword | HMMULT Keyword |  |
| --- | --- | --- | --- | --- |
| X/R | MULTX | HMMULTX | MULTR | HMMULTR |
| XY |  | HMMULTXY |  |  |
| Y/HT | MULTY | hMMULTY | MULTTHT | HMMULTTH |
| z | MULTZ | HMMULTZ | MULTZ | HMMULTZ |
| PV | MULTPV | HMMULTPV | MULTPV | HMMULTPV |

Table 7.5: HMMULT Keyword List

See also the HMMLT keyword in the GRID section.
