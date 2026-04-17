### FAULTDIM -- Define the Number of Fault Segments

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The FAULTDIM keyword defines the maximum number of records (or segments) that can be entered with the FAULTS keyword. The FAULTS keyword defines the faults in the grid than can be used for setting (or re-setting) transmissibility barriers across the fault planes.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | MFSEGS | A positive integer value that defines the maximum number of records (segments) for the FAULTS keyword. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.13: FAULTDIM Keyword Description

#### Example

\--

\-- FAULT

\-- SEGMS

\--

FAULTDIM

10000 /

The above example defines the maximum number of records that can be entered using the FAULT keyword to be 10,000 segments.
