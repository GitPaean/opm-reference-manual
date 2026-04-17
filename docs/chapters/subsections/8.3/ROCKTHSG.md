### ROCKTHSG -- Rock Compaction Hysteresis Tables (Dual Porosity)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ROCKTHSG keyword defines the rock compaction hysteresis attributes to be applied for when the rock compaction option has been invoked by the ROCKCOMP keyword in the RUNSPEC section and the either the Dual Permeability or Dual Porosity models are activated by the DUALPERM and DUALPORO keywords in the RUNSPEC section. ROCKTHSG specifies sigma multipliers versus pressure that are used in the dual porosity rock compaction calculations. The keyword should only be used if the Rock Compaction Hysteresis option has been activated by either setting the ROCKOPT parameter on the ROCKCOMP keyword to one of the available options.

Each data set consists of columnar vectors of sigma multipliers versus pressure that specify the elastic contraction and expansion and of the reservoir rock. The deflation curve is derived from the first data elements on each elastic curve. If the ROCKOPT parameter on the ROCKCOMP keyword has been set to HYSTER, then the dilation curves are extrapolated to infinite pressure, that is the curves are unbounded. However, if ROCKCOMP is set to BOBERG the last points of each elastic curve are used as the dilation curves.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
