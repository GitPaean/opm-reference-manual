### HMMLT -- History Match Grid Permeability Gradient Cumulative Multipliers

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The HMMLT series of keywords defines the history match gradient cumulative permeability multipliers, for when the History Match Gradient option has been activated by the HMDIMS keyword in the RUNSPEC section. The keyword consists of the first five characters of "HMMLT" followed by a two or three character string shown in , that determines the permeability direction, for example, HMMLTPX.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| Grid<br>Keyword | HMMULT<br>Keyword | Grid<br>Keyword | HMMULT Keyword |  |
| --- | --- | --- | --- | --- |
| PX/PR | PERMX | HMMLTPX | PERMR | HMMLTPR |
| PXY | PERMXY | HMMLTPXY |  |  |
| PY/THT | PERMY | hMMLTPY | PERMTHT | HMMLTTH |
| PZ | PERMZ | HMMLTPZ | PERMZ | HMMLTPZ |

Table 6.45: HMMLT Keyword List

See also the HMMULT keyword in the EDIT section
