### EQLDIMS -- Define the Equilibration Data Dimensions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The EQLDIMS keyword defines the maximum number of properties associated with equilibrating the model, that is initializing the model. A reservoir grid can be separated into separate regions in order to apply different pressure regimes and/or fluid contacts. Care should be taken that the different regions are not in communication if the pressures or fluid contacts are different for the various regions, as this would lead to an unstable initialization and would also imply errors in the model description as implemented.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NTEQUL | A positive integer value that defines the number of equilibration regions entered using the EQLNUM keyword in the REGIONS section and the number of entries associated with the EQUIL keyword in the SOLUTION section. | 1 |
| 2 | NPRSVD | A positive integer value setting the number of pressure versus depth entries used by OPM Flow in determining equilibration parameters.<br>Unless there is a requirement for a very fine equilibration this parameter should be defaulted. | 100 |
| 3 | NDRXVD | A positive integer value that defines the maximum number of depth entries in equilibration property versus depth tables (RSVD, RVVD, PBVD or PDVD etc.) as defined in the SOLUTION section. | 20 |
| 4 | NTTRVD | A positive integer that defines the maximum number of TVDP tables that describe the initial tracer concentration versus depth. | 1 |
| 5 | NSTRVD | A positive integer that defines the maximum number of depth entries in the TVDP tables as described in (4) | 20 |
| Notes:<br>1)  NTEQUL is the exact number of entries must be entered on the EQUIL keyword, otherwise OPM Flow will report an error. It is not a maximum number as for the other region arrays.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.11: EQLDIMS Keyword Description

It is common that the EQLNUM and FIPNUM arrays are identical so that the fluid in-place reporting matches the equilibration regions. Thus, in order to avoid errors in this case, one should just use one array (say the FIPNUM property array) and use the COPY keyword to generate the EQLNUM array.

#### Example

\--

\-- MAX MAX RSVD TVDP TVDP

\-- EQLNUM DEPTH NODES TABLE NODES

EQLDIMS

9 1\* 20 1\* 1\* /

The above example defines nine equilibration regions the default values for the remaining parameters on the EQLDIMS keyword.
