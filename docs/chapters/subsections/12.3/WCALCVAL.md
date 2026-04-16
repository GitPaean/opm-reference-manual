### WCALCVAL -- Define Gas Well Calorific Value

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines a gas well's calorific value for when the Gas Calorific Value option has been activated by specifying a target calorific value for a group via the [GCONCAL](#__RefHeading___Toc254086_1190369742) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. If this option is invoked then the gas calorific value must be set either by this keyword for a well by well allocation of the calorific value, or by using the Tracer Tracking option (activated by the [TRACER](#__RefHeading___Toc121485_83452205) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section) combined with [CALTRAC](#__RefHeading___Toc229773_3519154785) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that defines the tracer for the calorific value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
