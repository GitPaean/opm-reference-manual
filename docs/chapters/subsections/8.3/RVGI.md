### RVGI -- Define Condensate-Gas Ratio versus Pressure and Gi Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RVGI](#__RefHeading___Toc335902_516898843) keyword specifies the saturated gas Condensate-Gas Ratio ("CGR") factors used to specify the variation of the maximum possible CGR of gas with respect to pressure and Gi values, for when the [GIMODEL](#__RefHeading___Toc383678_1414963541) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to activate the [GI](#__RefHeading___Toc372466_1414963541) Pseudo Compositional option for the run. See also the [GINODE](#__RefHeading___Toc389150_1414963541), [RSGI](#__RefHeading___Toc316970_516898843), [RVGI](#__RefHeading___Toc335902_516898843), [BGGI](#__RefHeading___Toc223319_1539708736) and [BOGI](#__RefHeading___Toc223321_1539708736) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section to describe the fluid properties for the [GI](#__RefHeading___Toc372466_1414963541) Pseudo Compositional option.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
