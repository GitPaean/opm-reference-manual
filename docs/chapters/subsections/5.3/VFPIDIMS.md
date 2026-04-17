### VFPIDIMS -- Injection Vertical Flow Performance Table Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

VFPIDIMS keyword defines the maximum dimensions of the injection well Vertical Lift Performance ("VFP") tables defined by VFPINJ keyword. The VFP tables for the producing wells are defined by the VFPPDIMS keyword.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MXMFLO | A positive integer that defines the maximum number of injection rate entries for the VFPINJ keyword. | 0 |
| 2 | MXMTHP | A positive integer that defines the maximum number of THP entries for the VFPINJ keyword. | 0 |
| 3 | MXVFPTAB | A positive integer that defines the maximum number of VFPINJ tables entered through the VFPINJ keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.56: VFPIDIMS Keyword Description

#### Example

\-- INJECTING VFP TABLES

\-- VFP VFP VFP

\-- MXMFLO MXMTHP NMMVFT

VFPIDIMS

10 10 12 /

The above example defines that the maximum number of injection rates and THP entries on the VFPINJ keyword is 10, and the number of VFPINJ tables is 12.
