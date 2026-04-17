### WSCCLENL -- Well Deposited Scale Adjustment (LGR)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WSCCLENL keyword adjusts the amount of scale currently accumulated around a well's well connections for wells located in a Local Grid Refinement (\"LGR\"). For example, if a workover has been performed on a well to remove (or reduce) the deposited scale over the perforations, then this keyword can be used to implement the effects of the workover. Scale deposits reduce the productivity of well and this relationship is defined in the SCDPTAB and SCDATAB keywords in SCHEDULE section. The tables are allocated to a well via the WSCTAB keyword, which is also in the SCHEDULE section. Note that the Scale Deposition option must have been activated by declaring the dimensions of the scaling deposition tables using the SCDPDIMS keyword in the RUNSPEC section.

See also the WSCCLEAN keyword in the SCHEDULE section that performs similar functionality for wells located in the global grid.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
