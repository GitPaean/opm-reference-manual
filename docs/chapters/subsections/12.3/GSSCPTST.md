### GSSCPTST -- Perform Sustainable Capacity Test

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GSSCPTST](#__RefHeading___Toc218503_870710203) keyword instructs the simulator to perform a sustainable capacity test. This causes the model to be saved in it's current state via the [RESTART](#__RefHeading___Toc135629_1317547213) file, and the test performed by running the simulation under the current conditions combine with the parameters on this keyword. After the test is perform, the simulator will restart from the point prior to the test by loading in the [RESTART](#__RefHeading___Toc135629_1317547213) file. This type of testing is normally applied to gas fields for which the gas sales contracts stipulate that the gas sales rates are based on a sustainable capacity rate over a fixed period of time.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
