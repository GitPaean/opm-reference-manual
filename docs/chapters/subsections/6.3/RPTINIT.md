### RPTINIT -- Define Output to the INIT File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the data in the [GRID](#__RefHeading___Toc38674_784232322) and [EDIT](#__RefHeading___Toc40641_784232322) sections that is to be written out to the [INIT](#__RefHeading___Toc45789_719036256) file (\*.INIT or \*.FINIT). The format consists of the keyword followed by a series of character strings that indicate the data to be written. In most cases the character string is the keyword used to load the data into the OPM Flow input deck, for example [PORO](#__RefHeading___Toc45797_719036256) for the porosity array in the [GRID](#__RefHeading___Toc38674_784232322) section. In addition, values either read or calculated by the simulator in the [EDIT](#__RefHeading___Toc40641_784232322) section can also be written to the [INIT](#__RefHeading___Toc45789_719036256) file. Again the keyword or property name is used as the mnemonic for the character string, for example the [PORV](#__RefHeading___Toc96547_718313858), [TRANX](#__RefHeading___Toc93085_718313858) keywords etc. If the [RPTINIT](#__RefHeading___Toc304364_516898843) keyword is not used in the input deck then a default set of data array are written to the file, in this case the actual data written is dependent on the model's configuration and the options being used.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
