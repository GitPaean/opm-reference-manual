### TRPLPORO -- Activate the Triple Porosity Model Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The TRPLPORO keyword activates the Triple Porosity Model option that models matrix, fractures and vuggy porosity for carbonate reservoirs, and specifies the number of matrix porosity systems

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | TRPLPORO | A positive integer value that specifies the number of matrix porosity systems in the model. TRPLPORO should be set to either:<br>1)  TRPLPORO set equal to 2, if the vugs are only connected to the fractures, so that the porosity system is matrix and connected vugs, or,<br>2)  TRPLPORO set equal to 3, if the vugs are connected to the fractures and the matrix, so that the porosity system is matrix, connected vugs, and isolated vugs. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.49: TRPLPORO Keyword Description

Note the keyword cannot be used in conjunction with the NMATRIX keyword, which is also in the RUNSPEC section.

#### Example

\--

\-- TRPLPORO

\-- OPTION

TRPLPORO

3 /

The above example activates the Triple Porosity Model option and specifies the porosity system is matrix, connected vugs, and isolated vugs.
