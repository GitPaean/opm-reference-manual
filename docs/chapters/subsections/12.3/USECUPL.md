### USECUPL -- Load a Reservoir Coupling File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [USECUPL](#__RefHeading___Toc1702367_4250154414) keyword causes the simulator to read a Reservoir Coupling file that has been previously created in a master run using the [DUMPCUPL](#__RefHeading___Toc246382_1772380413) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, for when reservoir coupling is invoked by the [GRUPMAST](#__RefHeading___Toc488185_1414963541) and [SLAVES](#__RefHeading___Toc1268538_516898843) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
