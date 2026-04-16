### HBNUM -- Define Herschel-Bulkley Region Numbers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [HBNUM](#__RefHeading___Toc290467_870710203) keyword defines the Herschel-Bulkley rheological property table region numbers for each grid block, as such there must be one entry for each cell in the model. The region number specifies which table of Herschel-Bulkley rheological property data is assigned to a grid block, for when the Polymer option has been invoked via the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the Non-Newtonian Fluid phase has been declared active by the [NNEWTF](#__RefHeading___Toc267086_252421755) keyword, also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The [FHERCHBL](#__RefHeading___Toc285530_803326780) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section is used to specify the Herschel-Bulkley rheological property table data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
