### HMPROPS -- History Match End-Point Section Start

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[HMPROPS](#__RefHeading___Toc235727_373485663) defines the start of a history match end-points section, for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition, the End-Point Scaling option must also be activated by the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword which is also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword allows for the [BOX](#__RefHeading___Toc42110_3671211675), [EQUALS](#__RefHeading___Toc296597_1576177388), [COPY](#__RefHeading___Toc45761_719036256), [MINVALUE](#__RefHeading___Toc296605_1576177388), [MAXVALUE](#__RefHeading___Toc296601_1576177388) and [ADD](#__RefHeading___Toc4412_421927891) keywords to be used with the [HA](#__RefHeading___Toc279266_870710203) and [HM](#__RefHeading___Toc267495_373485663) series of keywords that reference the end-point scaling arrays, that is: HMKRG, HMKRGR, HMKRO, HMKRORG, HMKRORW, HMKRW, HMKRWR, HMPCW, HMPCG, HMSGCR, HMSOWCR, HMSOGCR, HMSWCR, and HMSWL keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
