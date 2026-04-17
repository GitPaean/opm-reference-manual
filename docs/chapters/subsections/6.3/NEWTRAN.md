### NEWTRAN -- Activate Irregular Corner-Point Grid Transmissibilities

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on Irregular Corner-Point Grid geometry transmissibility calculation, which is the default option for this type of grid. Grids defined with the COORD and ZCORN keywords will always invoke this option by default.

For Cartesian Regular Grids defined by the DX, DY, and DZ series of keywords the block center geometry transmissibility calculations should be activated via the OLDTRAN keyword. Again this is automatically invoked if this type of grid is being employed.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE IRREGULAR CORNER-POINT GRID TRANSMISSIBILITIES

\--

NEWTRAN

The above example manually activates Irregular Corner-Point Grid transmissibility calculations.
