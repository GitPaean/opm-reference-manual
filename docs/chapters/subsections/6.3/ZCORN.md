### ZCORN -- Define the Depth of Each Corner-Point of a Grid Block

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ZCORN defines the depth of each corner point of a grid block on the pillars defining the reservoir grid. A total of 8 x NX x NY x NZ values are needed to fully define all the depths in the model. The depths specifying the top of the first layer are entered first with one point for each pillar for each grid block. The points are entered with the X axis cycling fastest. Next come the depths of the bottom of the first layer. The top of layer two follows etc.

The keyword can be only used be used with Irregular Corner-Point Grids.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ZCORN | An array of depths with 8 depths for each cell, for a total of 8 x Nx x NY x NZ entries | None |
| feet | metres | cm |  |
| Notes:<br>1)  Regular Cartesian and Radial grid keywords cannot be used with this keyword, that is: DR, DRV, DTHETA, DTHETAV, DX, DXV, DY, DYV, DZ, DZV, INRAD, and TOPS.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.131: ZCORN Keyword Description

See also the SPECGRID, COORD and COORDSYS keywords to fully define an Irregular Corner-Point Grid.

#### Example

\--

\-- SPECIFY CORNER-POINT DEPTHS FOR A 3 x 2 x 2 GRID,

\-- WITH CONSTANT SLOPE IN THE X AND Y DIRECTIONS

\-- SUCH THAT ALL CORNER POINTS OF NEIGHBOURING BLOCKS ALIGN

ZCORN

\--

\-- top of layer 1

\--

1450 1500 1500 1550 1550 1600

1500 1550 1550 1600 1600 1650

1500 1550 1550 1600 1600 1650

1550 1600 1600 1650 1650 1700

\--

\-- bottom of layer 1

\--

1460 1510 1510 1560 1560 1610

1510 1560 1560 1610 1610 1660

1510 1560 1560 1610 1610 1660

1560 1610 1610 1660 1660 1710

\--

\-- top of layer 2

\--

1460 1510 1510 1560 1560 1610

1510 1560 1560 1610 1610 1660

1510 1560 1560 1610 1610 1660

1560 1610 1610 1660 1660 1710

\--

\-- bottom of layer 2

\--

1470 1520 1520 1570 1570 1620

1520 1570 1570 1620 1620 1670

1520 1570 1570 1620 1620 1670

1570 1620 1620 1670 1670 1720

/

The above example defines depths of the vertical coordinate lines for a regular 3 by 2 by 2 grid with a constant slope in the x and y directions such that all the corner points of neighboring blocks are aligned.
