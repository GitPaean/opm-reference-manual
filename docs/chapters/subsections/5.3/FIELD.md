### FIELD -- Activate the Oil Field System of Units for the Model

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the oil FIELD system of units for the model.

OPM Flow has three sets of units, namely: METRIC, FIELD and LAB and one of these keyword should be invoked in the RUNSPEC section to avoid any ambiguity. Both the simulator input and output units are controlled by including one of the METRIC, FIELD or LAB keywords in the RUNSPEC section of the input file.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- SWITCH ON THE FIELD SYSTEM OF UNITS FOR BOTH INPUT AND OUTPUT

\--

FIELD

The above example switches on the FIELD system of units for the model.
