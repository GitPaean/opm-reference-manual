### FBHPDEF -- Define Well Default BHP Target and Constraints

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, FBHPDEF, defines the default well BHP target for production wells and the default BHP constraint for injection wells.

| 1 | TARGET_BHP | A real positive value that defines the default well BHP target for production wells. | 1.01325 barsa |
| --- | --- | --- | --- |
| psia | barsa | atma |  |
| 2 | LIMIT_BHP | A real positive value that defines the default well BHP limit for injection wells. | 6895 barsa |
| psia | barsa | atma |  |
| Notes:<br>1)  The values defined by the FBHPDEF keyword will be used when a well BHP target or limit is later defaulted using one of the well control keywords in the SCHEDULE section (e.g. WCONPROD, WCONHIST, WCONINJE and WCONINJH). Well BHP targets or limits defaulted prior to the FBHPDEF keyword will not be affected.<br>2)  The keyword should be terminated by a "/". |  |  |  |

*Table 12.3.72.1: FBHPDEF Keyword Description*
See also the WELTARG keyword in the SCHEDULE section that modifies a well's target and constraint values.

#### Example

The following examples sets the default BHP target for production wells to 1.01325, and the default BHP limit for injection wells to 6895:

\--

\-- DEFAULT BHP TARGET AND CONSTRAINTS

\--

FBHPDEF

1.01325 6895. /
