### NOHMO -- Deactivate History Match Gradient Derivative Calculations (Alias)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [NOHMO](#__RefHeading___Toc262503_718033703) deactivates various history match gradient derivative calculations for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword consists of a series of character strings that define which derivative should be switch off based on the keyword that requested the derivatives to be calculated, for example [HMFAULTS](#__RefHeading___Toc254572_2135714711) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section. If an empty list is entered then all the gradient derivative calculations previously requested are switch off. The keyword is useful for changing from history matching runs to predication cases, as the prediction cases will be more computationally efficient without the burden of the gradient derivative calculations.

The keyword is an alias for the [NOHMD](#__RefHeading___Toc262487_718033703) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
