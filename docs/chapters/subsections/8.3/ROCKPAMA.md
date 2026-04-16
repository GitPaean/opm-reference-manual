### ROCKPAMA -- Define Coal Palmer-Mansorri Rock Model Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[ROCKPAMA](#__RefHeading___Toc241588_516898843) defines the Palmer-Mansoori[^1] and [^2] parameters used for this rock model, for when the Coal Bed Methane option has been activated via the [COAL](#__RefHeading___Toc234580_3519154785) keyword, and PALM-MAN has been declared for the ROCKOPT variable on the [ROCKCOMP](#__RefHeading___Toc55593_1778172979) keyword; both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The Palmer-Mansoori rock model is used to calculate the impact on pore volume and permeability due to rock compaction.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Palmer, I. and Mansoori, J. "How Permeability Depends on Stress and Pore Pressure in Coalbeds: A New Model," paper SPE 52607, SPE Reservoir Evaluation & Engineering (1998) 1, No. 6, 539-544.

[^2]: Clarkson, C.R., Pan, Z., Palmer, I. and Harpalani, S. \"Predicting Sorption-Induced Strain and Permeability Increase With Depletion for Coalbed-Methane Reservoirs\", SPE 114778-PA, SPE Journal (2010) 15, No. 1, 152--159.
