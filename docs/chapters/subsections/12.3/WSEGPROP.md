### WSEGPROP -- Modify Multi-Segment Wells and Their Segment Structure

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSEGPROP](#__RefHeading___Toc1056360_4263943340) keyword allows for the editing of exiting multi-segment wells created by [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section without having to re-define all the information that is on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword. Note that the well must have been previously define by both the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WELSEGS](#__RefHeading___Toc97661_3261743917) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to use the [WSEGPROP](#__RefHeading___Toc1056360_4263943340) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which a multi-segment well is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | ISEG1 | A positive integer greater than or equal to two and less than or equal to MXSEGS on [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the start of a segment | None |
| 3 | ISEG2 | A positive integer greater than or equal to two and less than or equal to ISEG1 on this record and MXSEGS on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the end of a segment. | None |
| 4 | ID | A real positive value that defines the tubing internal diameter of the segment for the well. | Previous Entered Value |
| feet | m | cm |  |
| 5 | EPSILON | A real positive value that defines the tubing absolute roughness of the segment for the well. | Previous Entered Value |
| feet | m | cm |  |
| 6 | XAREA | XAREA is real positive value equal to or greater than zero that defines the cross sectional area for fluid flow.<br>Currently this option is not supported by OPM Flow. | Previous Entered Value |
| ft^2^ | m^2^ | cm^2^ |  |
| 7 | VOLSEG | VOLSEG is a real positive value that defines the effective segment volume for the this segment.<br>Currently this option is not supported by OPM Flow. | Previous Entered Value |
| ft3 | m3 | cm3 |  |
| 8 | XAREAS | XAREAS is real positive value equal to or greater than zero that defines the cross sectional area of the pipe wall for this segment, that is used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>Currently this option is not supported by OPM Flow. | Previous Entered Value |
|  | ft^2^ | m^2^ | cm^2^ |
| 9 | VHEATCAP | VHEATCAP is real positive value equal to or greater than zero that defines the volumetric heat capacity of the pipe wall used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>Currently this option is not supported by OPM Flow. | Previous Entered Value |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| 10 | THCON | THCON is real positive value equal to or greater than zero that defines the thermal conductivity of the pipe wall used in thermal conductivity calculations for when the temperature calculation is activated by the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>Currently this option is not supported by OPM Flow. | Previous Entered Value |
| Btu/ft/day/°R | kJ/m/day/K | J/cm/hr/K |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.119: WSEGPROP Keyword Description

The total number of wells should be defined via the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword and the number of multi-segment wells should be declared on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword, both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define wells, the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define the well completions for both ordinary wells and multi-segment wells, and the [COMPSEGS](#__RefHeading___Toc316604_3519154785) keyword to define a multi-segment well segment completions. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example modifies two segments in well OP01 and one segment in well OP02.

\--

\-- WELL SEGMENT SPECIFICATION DATA

\--

\-- WELL SEG SEG TUBE TUBE XSEC VOL

\-- NAME ISTR IEND ID ROUGH AREA SEG

WSEGPROP

OPO1 12 14 0.3 0.00010 /

OP01 13 15 0.275 0.00010 /

OP02 14 14 0.275 0.00010 /

/

Note that the two multi-segment wells and their respective segments must have been previously defined by the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword.
