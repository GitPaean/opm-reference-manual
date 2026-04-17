### NOHYST -- Deactivate the Hysteresis Option

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The NOHYST keyword deactivates the Hysteresis option and informs the simulator to ignore the IMBNUM array in the REGIONS section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE THE HYSTERESIS OPTION

\--

NOHYST

The above example switches off the default behavior of multiplying the fracture porosity by the fracture permeability to calculate the effective fracture permeability.
