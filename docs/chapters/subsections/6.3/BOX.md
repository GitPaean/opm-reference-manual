### BOX -- Define a Range of Grid Blocks to Enter Property Data

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[BOX](#__RefHeading___Toc42110_3671211675) defines a range of grid blocks for which subsequent data is assigned for all the cells in the defined [BOX](#__RefHeading___Toc42110_3671211675). Values are set for cells within the defined box grid using natural reading order, initially along the I-direction then J-direction and finally the K-direction. If fewer values are assigned than exist within the defined block space, then subsequent values are set starting from the next block that was not previously assigned for that property. This is the same behavior as applies to setting grid properties for an unboxed grid.

Note that the [BOX](#__RefHeading___Toc42110_3671211675) grid is reset by the keyword [ENDBOX](#__RefHeading___Toc88719_1778172979) by resetting the current defined [BOX](#__RefHeading___Toc42110_3671211675) to be the whole grid. The keyword can be used for any array and for all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | I1 | A positive integer that defines the lower bound of the array in the I-direction to be modified must be greater than or equal 1 and less than or equal to I2 and NX. | 1 |
| 2 | I2 | A positive integer that defines the upper bound of the array in the I-direction to be modified must be greater than or equal to II and less than or equal to NX | NX |
| 3 | J1 | A positive integer that defines the lower bound of the array in the J-direction to be modified must be greater than or equal 1 and less than or equal to J2 and NY. | 1 |
| 4 | J2 | A positive integer that defines the upper bound of the array in the J-direction to be modified must be greater than or equal to JI and less than or equal to NY. | NY |
| 5 | K1 | A positive integer that defines the lower bound of the array in the K-direction to be modified must be greater than or equal to one and less than or equal to K2 and NZ. | 1 |
| 6 | K2 | A positive integer that defines the upper bound of the array in the K-direction to be modified must be greater than or equal to KI and less than or equal to NZ. | NZ |
| Notes:<br>1)  Where NX, NY and NZ are the dimensions of the model as defined on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.11: BOX Keyword Description

See also the [ADD](#__RefHeading___Toc4412_421927891), [COPY](#__RefHeading___Toc45761_719036256), [ENDBOX](#__RefHeading___Toc88719_1778172979), [EQUALS](#__RefHeading___Toc296597_1576177388), and [MULTIPLY](#__RefHeading___Toc296609_1576177388) keywords can also be used to enter data in a subset of the model.

#### Examples

\--

\-- DEFINE A BOX GRID FOR THE BOTTOM LAYER OF A 100 X 100 X 20 MODEL

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 20 20 / SELECT THE BOTTOM LAYER

\--

\-- DEFINE THE POROSITY AND OTHER PROPERTIES ON THE BOX GRID

\--

PORO

10000\*0.300 /

PERMX

5000\*100.0 5000\*75.0 /

NTG

10000\*0.500 /

\--

\-- RESET THE INPUT BOX TO BE THE FULL MODEL

\--

ENDBOX

The above example set the [BOX](#__RefHeading___Toc42110_3671211675) grid to be the last layer in the model which means that 100 x 100, that is 10,000 values need to entered for each property.

Alternatively, one could use the [EQUALS](#__RefHeading___Toc296597_1576177388) keyword to accomplish the same thing.

\-- \-- ARRAY CONSTANT \-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

\'PORO' 0.3000 1\* 1\* 1\* 1\* 20 20 / PORO TO 0.30 IN LAYER 20

\'PERMX\' 100.00 1\* 1\* 1 50 20 20 / PERMX TO 100. IN LAYER 20

\'PERMX\' 75.00 1\* 1\* 51 100 20 20 / PERMX TO 75.0 IN LAYER 20

\'NTG' 0.5000 1\* 1\* 1\* 1\* 20 20 / NTG TO 0.50 IN LAYER 20

/
