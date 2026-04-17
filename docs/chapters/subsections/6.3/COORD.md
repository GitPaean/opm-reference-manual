### COORD -- Define a Set of Coordinates Lines for a Reservoir Grid

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

COORD defines a set of coordinate lines or pillars for a reservoir grid via an array. A total of 6 x (NX+1) x (NY+1) values must be specified for each coordinate data set (or reservoir). For multiple reservoirs, where NUMRES is greater than one, there must be 6 x (NX+1) x (NY+1) x NUMRES values. In OPM Flow NUMRES can only be set to one.

For Cartesian geometry, each line is defined by the (x, y, z) coordinates of two distinct points on the line. The lines are entered with I cycling fastest then J. For radial geometry, each line is defined by the (r, theta, z) coordinates of two distinct points on the line. The lines are entered with R cycling fastest then THETA.

The keyword can only be used with Irregular Corner-Point Grids.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | X1-Column | Top X coordinate | None |
| 2 | Y1-Column | Top Y coordinate |  |
| 3 | Z1-Column | Top Z coordinate |  |
| 4 | X2-Column | Base X coordinate |  |
| 5 | Y2-Column | Base Y coordinate |  |
| 6 | Z2-Column | Base Z coordinate |  |
|  | feet | metres | cm |
| Notes:<br>1)  THETA values are in degrees for all units.<br>2)  Regular Cartesian and Radial grid keywords cannot be used with this keyword, that is: DR, DRV, DTHETA, DTHETAV, DX, DXV, DY, DYV, DZ, INRAD, and TOPS.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 6.14: COORD Keyword Description

See also the SPECGRID, COORDSYS and ZCORN keywords to fully define an Irregular Corner-Point Grid.

#### Example

\--

\-- SPECIFY VERTICAL COORDINATE LINES FOR A REGULAR 3 x 2 GRID

\-- (DX = 100 and DY = 200)

\--

\-- X1 Y1 Z1 X2 Y2 Z2

\-- \-\-- \-\-- \-\-\-- \-\-- \-\-- \-\-\--

COORD

0 0 1000 0 0 5000

100 0 1000 100 0 5000

200 0 1000 200 0 5000

300 0 1000 300 0 5000

0 200 1000 0 200 5000

100 200 1000 100 200 5000

200 200 1000 200 200 5000

300 200 1000 300 200 5000

0 400 1000 0 400 5000

100 400 1000 100 400 5000

200 400 1000 200 400 5000

300 400 1000 300 400 5000

/

The above example defines vertical coordinate lines for a regular 3 by 2 grid with DX equal to 100 and DY equal to 200.
