### LGRCOPY -- Activate Local Grid Refinement Inheritance

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [LGRCOPY](#__RefHeading___Toc236708_2843394514) keyword actives the Local Grid Refinement ("LGR") Inheritance option that allows the LGR to inherit the properties of the global or host cell containing an LGR grid block when it is defined, as opposed to the normal process of applying this transform at the end of the [GRID](#__RefHeading___Toc38674_784232322) section. [LGRCOPY](#__RefHeading___Toc236708_2843394514) can be used in the [RUNSPEC](#__RefHeading___Toc55591_1778172979), [GRID](#__RefHeading___Toc38674_784232322) and [EDIT](#__RefHeading___Toc40641_784232322) sections. If used in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section then the option is applied to all LGRs defined in the input file, whereas if used in the [GRID](#__RefHeading___Toc38674_784232322) or [EDIT](#__RefHeading___Toc40641_784232322) sections the keyword must be placed inside a [LGR](#__RefHeading___Toc55049_4106839650) definition section, that is between a [CARFIN](#__RefHeading___Toc150726_63720426) (Cartesian LGR grid) or [RADFIN](#__RefHeading___Toc76871_718313858)/[RADFIN4](#__RefHeading___Toc76873_718313858) (radial LGR grid) keyword and an [ENDFIN](#__RefHeading___Toc111797_332691817) keyword. In the latter case inheritance is applied on an individual LGR basis.

Currently, OPM Flow does not support the local grid refinement feature and therefore this keyword is ignored by the simulator.

#### Example

The following example activates the LGR Inheritance option for all LGRs in the model.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- ACTIVATE LOCAL GRID REFINEMENT INHERITANCE

\--

LGRCOPY
