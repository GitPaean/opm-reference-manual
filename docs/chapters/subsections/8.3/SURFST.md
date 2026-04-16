### SURFST -- Surfactant Water-Oil Surface Tension versus Surfactant Concentration

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SURFST](#__RefHeading___Toc1173151_4250154414) keyword defines surfactant water-oil surface tension versus surfactant concentration in the water phase tables, used in adjusting the pressure independent capillary pressure vectors in the [SWFN](#__RefHeading___Toc106882_335817223) or [SWOF](#__RefHeading___Toc45811_7190362561) saturation tables, entered by their respective keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section. [SURFST](#__RefHeading___Toc1173151_4250154414) is also used to adjust the relative permeability curves on the aforementioned tables via the capillary number. The Surfactant option must have been activated by the SURFACTANT keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to use this keyword and either this keyword or the [SURFSTES](#__RefHeading___Toc1173153_4250154414) keyword, also in the [PROPS](#__RefHeading___Toc39329_784232322) section, is obligatory in this case.

See also the [SURFSTES](#__RefHeading___Toc1173153_4250154414) that defines the surfactant water-oil surface tension as a function of surfactant concentration in the water phase and salt concentration or the effective salinity.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
