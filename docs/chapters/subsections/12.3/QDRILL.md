### QDRILL -- Define Sequential Drilling Queue Wells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [QDRILL](#__RefHeading___Toc614222_501926209) keyword places previously defined wells in the Sequential Drilling Queue. Wells in this type of queue will be automatically drilled and completed in the sequence entered in order to satisfy group targets, as defined by the [GCONPROD](#__RefHeading___Toc146746_4203985108), [GCONINJE](#__RefHeading___Toc134874_2055188184) and [GCONSALE](#__RefHeading___Toc178287_2026549522) keywords. or a group's production potential as per the GDRILLPOT keyword. All the previously mentioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
