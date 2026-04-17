### SALTREST -- Define the Restart Salt Concentration for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SALTREST keyword defines restart salt concentration values for all grid cells in the model and should be used in runs that are using the RESTART facility, where the initial run has not used the Low Salt or Brine options. This allows for initial runs that have used the standard water PVT properties via the PVTW keyword in the PROPS section, to be restarted with salt dependent water properties. The keyword should only be used if the salt (brine) phase has been activated in the current restart run (not the initial run) via the BRINE keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SALTREST | SALTREST is an array of real positive numbers that are greater than or equal to zero assigning the restart salt concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*15.0. | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.39: SALTREST Keyword Description

See also the PVTWSALT keyword in the PROPS section and the RESTART keyword in the SOLUTION section.

#### Example

\--

\-- DEFINE RESTART SALTREST VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SALTREST

1000\*0.0000 1000\*0.0000 1000\*15.000 /

The above example defines the restart salt concentration values to be 0.0000 for all the cells in the first and second layers and finally 15.000 for all the cells in the third layer.
