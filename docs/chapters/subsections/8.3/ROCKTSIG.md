### ROCKTSIG -- Rock Compaction Tables (Dual Porosity)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKTSIG keyword defines the rock compaction attributes to be applied for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section, and the either the Dual Permeability or Dual Porosity models are activated by the DUALPERM and DUALPORO keywords in the RUNSPEC section. ROCKTSIG specifies sigma multipliers versus pressure that are used in the dual porosity rock compaction calculations. The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the ROCKCOMP keyword to one of the available options.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
