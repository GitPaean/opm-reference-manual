### WHEDREFD -- Define Well Hydraulic Head Reference Depth

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WHEDREFD](#__RefHeading___Toc1067814_487874538) keyword sets the hydraulic head reference depth for reporting the hydraulic head pressure for the well, for wells that have previously been defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-----------------------------------------------------------------------------------------------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                     | > WELNAME | > A character string of up to eight characters in length that defines the well name for which the well hydraulic head reference depth data is being defined.                                      | > None |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                     | > HYDREF  | > A real value that defines the hydraulic head reference depth for reporting the hydraulic head pressure for the well.                                                                            | > None |
|                                                                                                                                         |           |                                                                                                                                                                                                   |        |
|                                                                                                                                         |           | > HYDREF cannot be defaulted on the keyword; however if a well has not been set by this keyword HYDREF is set equal to the value on the [HYDRHEAD](#__RefHeading___Toc195463_2135714711) keyword. |        |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > feet                                                                                                                                  | > m       | > cm                                                                                                                                                                                              |        |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                |           |                                                                                                                                                                                                   |        |
|                                                                                                                                         |           |                                                                                                                                                                                                   |        |
| 1)  The keyword is followed by any number records with each record terminated by a "/" and the keyword should be terminated by a "/".   |           |                                                                                                                                                                                                   |        |
+-----------------------------------------------------------------------------------------------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.97: WHEDREFD Keyword Description

See also the [HYDRHEAD](#__RefHeading___Toc195463_2135714711) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The following example defines three wells hydraulic head reference depths for reporting, using the [WHEDREFD](#__RefHeading___Toc1067814_487874538) keyword

\--

\-- WELL HYDRAULIC HEAD REFERENCE DEPTH

\--

\-- WELL HYDREF

\-- NAME DEPTH

WHEDREFD

OP01 150.0 /

OP02 175.0 /

OP03 150.0 /

/

Here, well OP01 and OP03 have their hydraulic head reference depths set to 150.0 ft and well OP02's hydraulic head reference depth is set to 175.0 ft.
