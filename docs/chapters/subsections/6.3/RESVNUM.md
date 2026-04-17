### RESVNUM -- Define Reservoir Coordinate Data Set

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RESVNUM keyword is used to define the start of a reservoir coordinate data set and stipulates the reservoir number for the data set. The keyword is used in conjunction with the COORD keyword in the GRID section, that specifies a set of coordinate lines or pillars for a reservoir grid via an array. Note that the COORD keyword should immediately follow the RESVNUM keyword.

Although the keyword is processed by OPM Flow, the keyword is effectively ignored as only the default value of one is supported.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | RESVNUM | A positive integer values that defines the reservoir coordinate data set, or the independent reservoir, for which the subsequent COORD data is to be associated with.<br>RESVNUM should be less than or equal to NUMRES on the NUMRES keyword in the RUNSPEC section.<br>OPM Flow currently only accepts a single data set, that is the default value of one. | 1 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 6.114: RESVNUM Keyword Description

See the NUMRES keyword in the RUNSPEC section that defines the number of reservoir grids (COORD data sets) that the simulator should process.

The facility is useful to combine two separate reservoir grids into one model in the simulator.

#### Example

\--

\-- NUMRES

\-- NUMBER

RESVNUM

1 /

\--

\-- SPECIFY VERTICAL COORDINATE LINES FOR A REGULAR 3 x 2 GRID

\--(DX = 100 and DY = 200)

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

\--

\-- NUMRES

\-- NUMBER

RESVNUM

2 /

\--

\-- SPECIFY VERTICAL COORDINATE LINES FOR A REGULAR 3 x 2 GRID

\--(DX = 100 and DY = 200)

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
