### ENDBOX -- Define the End of the BOX Defined Grid

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword marks the end of a previously defined [BOX](#__RefHeading___Toc42110_3671211675) sub-grid as defined by a previously entered [BOX](#__RefHeading___Toc42110_3671211675) keyword. The keyword resets the input grid to be the full grid as defined by the NX, NY, and NZ variables on the [DIMENS](#__RefHeading___Toc20387_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

There is no data required for this keyword.

#### Example

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

10 10 1 6 1 1 / DEFINE BOX AREA

\--

\--

\-- DEFINE GRID BLOCK PERMZ DATA FOR THE INPUT BOX

\--

PERMZ

6\*0.01 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX

The above example defines a subset of the grid and sets the cells [PERMZ](#__RefHeading___Toc45795_719036256) values to 0.01 for that area. After which the [ENDBOX](#__RefHeading___Toc88719_1778172979) keyword resets the input to be the full grid.
