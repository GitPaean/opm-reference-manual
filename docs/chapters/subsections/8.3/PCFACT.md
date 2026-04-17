### PCFACT -- Capillary Pressure Multiplication Factor as a Function of Porosity Change

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PCFACT defines the capillary pressure multiplication factor due to a change in porosity. Currently the keyword is used in conjunction with OPM Flow's Salt Precipitation model, in which the pore space is reduced due to salt precipitating in the pore space, causing a reduction in porosity and an associated increase in capillary pressure.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | POROFAC | A real monotonically increasing positive columnar vector that defines the porosity factor () for the corresponding PCFAC vector.<br>In the simulator's Salt Precipitation model, the maximum value of is , implying a maximum value of one for POROFAC. | None |
| dimensionless | dimensionless | dimensionless |  |
| 2 | PCFAC | A real positive monotonically decreasing columnar vector that defines the capillary pressure () multiplier associated with POROFAC and used to scale a grid block\'s capillary pressure due to the reduction in pore volume caused by salt precipitation. Where: | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  There must be same number of entries for each column.<br>4)  Each table is terminated by a single "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.3.199.1: PCFACT Keyword Description

The porosity reduction is a function of the volume fraction of salt () precipitated out of the vaporized water phase, that is:

The capillary pressure factor data can be estimated from the permeability and porosity factors defined by the PERMFACT keyword in the PROPS section using the Leverett J-function, for example:

Where:

, = the initial and scaled porosity,

, = the initial and scaled permeability, and

, = the initial and scaled capillary pressure.

#### Example

The example below defines two PCFACT tables assuming NTSFUN equals two and NSSFUN is greater than or equal to five on the TABDIMS keyword in the RUNSPEC section.

\--

\-- CAPILLARY PRESSURE FACTOR INCREASE DUE TO SALT PRECIPITATION

\-- (OPM FLOW KEYWORD)

\--

PCFACT

\-- PORO PC

\-- FACTOR FACTOR

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 2.0000

0.25 2.0000

0.50 1.4142

0.75 1.1547

1.00 1.0000 / TABLE NO. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.00 2.0000

0.25 2.0000

0.50 1.4142

0.75 1.1547

1.00 1.0000 / TABLE NO. 02

Note that the capillary pressure factor has been capped for POROFAC less than 0.25.
