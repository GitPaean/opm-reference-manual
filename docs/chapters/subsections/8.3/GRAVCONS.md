### GRAVCONS -- Re-Define Gravity Constant

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GRAVCONS keyword re-defines the gravity constant used in various calculations from the default value used by the simulator. Normally this keyword should not be used.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | GRAVCONS | GRAVCONS is a positive real number number that defines the gravity constant used in various calculations. | Defined |
| ft^2^psi/lb<br>0.00694 | m^2^bars/kg<br>0.0000981 | cm^2^atm/gm<br>0.000968 |  |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.42: GRAVCONS Keyword Description

#### Example

\--

\-- RE-DEFINE GRAVITY CONSTANT

\--

GRAVITY

0.0000980665 /

The above example re-defines the gravity constant to be 0.0000980665 ft2psi/lb from the default value of 0.00694 ft2psi/lb.
