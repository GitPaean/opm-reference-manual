<a id="__RefHeading___Toc4410_421927891"></a>

### ACTNUM -- Set the Status of a Grid Block To Active or Inactive

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The ACTNUM keyword specifies which grid blocks are either active or inactive. A grid block is automatically set to inactive if its pore volume is less than the value entered using the MINPV keyword. The ACTNUM keyword can be used to also make blocks with pore volumes greater than MINPV inactive.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ACTNUM | An array of integers equal to either 0 or 1 that define the activity of each cell in the model. A value of 0 indicates the cell is inactive.<br>Grid blocks are ordered with the I index cycling fastest, followed by the J and K indices.<br>Repeat counts may be used, for example 20\*1. | 1 |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX keyword.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.2: ACTNUM Keyword Description

#### Examples

The example below sets several cells to be inactive for a 4 x 5 x 2 model.

ACTNUM

\-- Layer 1

0 0 1 1

0 0 1 1

1 1 1 1

1 1 1 1

1 1 1 1

\-- Layer 2

1 1 1 1

1 1 1 1

1 1 1 1

1 1 1 1

0 0 0 0

/

Alternatively the EQUALS keyword could be employed to accomplish the same task, that is:

\-- \-- ARRAY CONSTANT \-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

\'ACTNUM' 1.0000 1\* 1\* 1\* 1\* 1\* 1\* / SET ACTIVE CELLS

\'ACTNUM' 0.0000 1 2 1 2 1 1 / SET INACTIVE CELLS

\'ACTNUM' 0.0000 1 4 5 5 2 2 / SET INACTIVE CELLS

/
