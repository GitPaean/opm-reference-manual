### GRIDUNIT -- Define the Grid Units

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GRIDUNIT keyword defines the units of the grid data. It is usually output by pre-processing software when exporting the grid geometry. The data is not used by OPM Flow intrinsically, but is merely written to the output EGRID file, as specified by the GRIDFILE keyword, for the use of post-processing software like OPM ResInsight.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | GRIDUNIT | A character string that defines the units of the coordinates stated on the MAPAXES keyword, and should be set to:<br>1)  FEET for field units,<br>2)  METRES for metric units, or<br>3)  CM for laboratory units. | METRES |
| 2 | MAPOPT | A character string that defines if the grid data are measured relative to the map, or relative to the origin as stated on the MAPAXES keyword. MAPOPT should either be left blank (the default) indicating the origin is relative to the origin on the MAPAXES keyword, or set equal to MAP measured relative to the map. | 1\* |
| Notes:<br>1)  Note the alternative spelling METRES, that is METERS is not recognized.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.42: GRIDUNIT Keyword Description

#### Example

\--

\-- SET THE GRID UNITS FOR THE GRID

\--

GRIDUNIT

METRES /

The above example defines that the GRID units to be metric.
