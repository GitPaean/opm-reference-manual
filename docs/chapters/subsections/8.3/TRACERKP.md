### TRACERKP -- Standard Partitioned Tracer Option K(P) Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [TRACERKP](#__RefHeading___Toc1279807_4250154414), defines the Standard Partitioned Tracer option K(P) tables, for when the Partitioned Tracer option has been activate with the [PARTTRAC](#__RefHeading___Toc264979_2928331029) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Standard partitioned tracers only have a "free" and "solution" phases; whereas, Multi-partitioned tracers can partition into any number of phases (oil, water, gas etc.) and have adsorption, decay and diffusion parameters specific to each phase. For the [TRACERKP](#__RefHeading___Toc1279807_4250154414) keyword the K(P) tables relate the ratio of the reference phase (the "free" phase) to the solution phase versus pressure. So for example, given a standard partitioned tracer in oil and gas, with the oil phase acting as the reference phase, then [TRACERKP](#__RefHeading___Toc1279807_4250154414) would consist of columnar vectors of:

Where:

= standard partitioned K(P)

= oil concentration

= gas concentration

See also the [TRACERKM](#__RefHeading___Toc1279805_4250154414) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that provides similar data for tmulti-partitioned tracers.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
