### QMOBIL -- Activate or Deactivate LGR End-Point Mobility Correction

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [QMOBIL](#__RefHeading___Toc630861_501926209) keyword activates or deactivates the end-point mobility correction for Local Grid Refinements ("LGR"), for when LGRs have been activated for the input deck using the [LGR](#__RefHeading___Toc55049_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [QMOBIL](#__RefHeading___Toc630861_501926209) should be placed in between the [LGR](#__RefHeading___Toc55049_4106839650) definition keywords [CARFIN](#__RefHeading___Toc150726_63720426), or RADIN (or RAFDIN4) and the [ENDFIN](#__RefHeading___Toc111797_332691817) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
