### TIGHTEN -- Tighten and Relax Numerical Controls

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [TIGHTEN](#__RefHeading___Toc1239635_4250154414) keyword tightens up or slackens the numerical controls for the linear, non-linear and material balance convergence targets and also tightens or relaxes the maximum values for the aforementioned parameters. The keyword should be used with caution as it may result in significantly increasing the run times.

Note that any subsequent use of the [TUNING](#__RefHeading___Toc146744_4203985108) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section will result in resetting the numerical controls. See also the [TIGHTENP](#__RefHeading___Toc1239637_4250154414) in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that allows for greater flexibility in modifying the numerical controls.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
