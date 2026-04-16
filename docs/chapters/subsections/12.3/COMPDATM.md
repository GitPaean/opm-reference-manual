### COMPDATM -- Define Well Connections to an Amalgamated LGR Grid

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [COMPDATM](#__RefHeading___Toc243247_1539708736) keyword is an alias for the [COMPDATL](#__RefHeading___Toc153110_63720426) keyword. [COMPDATM](#__RefHeading___Toc243247_1539708736) defines how a well in an amalgamated Local Grid Refinement ("LGR") is connected to the reservoir by declaring the [LGR](#__RefHeading___Toc55049_4106839650) and defining or modifying existing well connections. Ideally the connections should be declared in the correct sequence, starting with the connection nearest the well head and then working along the wellbore towards the bottom or toe of the well, however this may not be possible or convenient, for example when connections are added or removed from a well during the simulation (see the [COMPORD](#__RefHeading___Toc97657_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section for options regarding connection ordering).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
