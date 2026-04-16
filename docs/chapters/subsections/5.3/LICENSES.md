### LICENSES -- Define Required Licenses for Run

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines the additional software licenses that are required to invoke various licensed options in the commercial simulator at the start of the run. The commercial simulator requests a license when keywords associated with a licensed option is encountered in the input deck, this may result in the license being unavailable at the time of request and after the simulation has been initiated, resulting in the run terminating. This keyword avoids this scenario by reserving the license at the start of the run.

OPM Flow is an open source project and therefore there is no license management of the various implemented options; hence this keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
