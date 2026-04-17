### NOGGF -- Deactivate Output of Grid Geometry File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword deactivates the output of a standard GRID or extended GRID file, as well as the extensible EGRID file for post-processing applications.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- DEACTIVATE GRID GEOMETRY OUTPUT

\--

NOGGF

The above example switches off the default behavior of writing out the grid geometry files.
