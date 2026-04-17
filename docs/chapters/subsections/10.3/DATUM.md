### DATUM -- Define the Datum Depth for the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DATUM keyword defines the datum depth for the model. This allows for all grid block potentials (depth corrected pressures) to be calculated at a common depth.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DATUM | DATUM is a single positive value that defines the datum depth for the model. | None |
| feet | m | cm |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 10.11: DATUM Keyword Description

See also the DATUMR and DATUMRX keywords in the SOLUTION section that also define the datum depth for the model.

#### Example

\-- DATUM

\-- DEPTH

\-- \-\-\-\-\--

DATUM

5000.0 / DATUM DEPTH FOR REPORTING

The above example defines the datum for the model to be 5000.0
