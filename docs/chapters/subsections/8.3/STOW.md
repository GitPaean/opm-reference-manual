### STOW -- Define Capillary Pressure Oil-Water Surface Tension versus Pressure

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [STOW](#__RefHeading___Toc850688_4250154414) keyword defines capillary pressure oil-water surface tension versus pressure tables used in adjusting the pressure independent capillary pressure vectors in the [SWFN](#__RefHeading___Toc106882_335817223) or [SWOF](#__RefHeading___Toc45811_7190362561) saturation tables, entered by their respective keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section. The [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should state the SURFTENS character string to activate the Capillary Pressure Surface Tension Pressure Dependency option. If the [STOW](#__RefHeading___Toc850688_4250154414) keyword is not supplied then no capillary pressure surface tension pressure scaling will occur and the capillary pressure values on the [SWFN](#__RefHeading___Toc106882_335817223) or SWOF saturation tables will be used directly.

Capillary pressure surface tension pressure scaling can also be used with multi-segment wells, but this facility has not been incorporated in OPM Flow's multi-segment well implementation.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
