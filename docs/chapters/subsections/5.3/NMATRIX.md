### NMATRIX -- Activate the Discretized Matrix Dual Porosity Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NMATRIX keyword activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid blocks. See also the NMATOPS keyword in the GRID section that defines various parameters for this option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | NMATRIX | A positive integer value that specifies the number of sub-grid blocks in the actual matrix grid blocks. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 5.26: NMATRIX Keyword Description

Note the keyword cannot be used in conjunction with the TRPLPORO keyword, which is also in the RUNSPEC section.

#### Example

\--

\-- SUB-GRIDS

\-- NMATRIX

NMATRIX

4 /

The above example activates the Discretized Matrix Dual Porosity option and specifies the number of sub-grid blocks in the actual matrix grid block to be four.
