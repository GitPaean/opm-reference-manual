### COMPFLSH -- Assign COMPDAT Differential-Flash Liberation Ratios

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[COMPFLSH](#__RefHeading___Toc403595_1535817064) is used to assign saturated PVT differential-flash liberation ratios to individual well completions for both the oil formation volume factor and the gas-oil ratio. Only the saturated oil properties are changed by this keyword, that is only data entered via the [PVCO](#__RefHeading___Toc325700_501926209) or [PVTO](#__RefHeading___Toc104062_57619843) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section will be used in the calculation. The other fluid PVT property keywords: [PVTW](#__RefHeading___Toc2086106_3315222525), [PVTG](#__RefHeading___Toc104060_57619843), [DENSITY](#__RefHeading___Toc45799_719036256), etc., are not used.

The differential liberation expansion ("DLE") experiment is designed to approximate the depletion process of an oil reservoir, and thereby provide suitable PVT data for calculating reservoir performance. This is then coupled with surface faculties via the multi-stage separator flash data. The multi-stage separator test is performed on an oil sample primarily to provide a basis for converting differential liberation data from a residual oil to a stock-tank oil basis. Occasionally, several separator tests are run to help choose separator conditions that maximize stock-tank oil production. Usually two or three stages of separation are used, with the last stage being at atmospheric pressure and near-ambient temperature (60 to 80 ^o^F).

Note, normally the data on the [PVCO](#__RefHeading___Toc325700_501926209) and [PVTO](#__RefHeading___Toc104062_57619843) keywords should have already taken the two datasets into account and therefore this keyword should not normally be used in practice, unless there is a specific requirement to adjust the oil PVT data on a well connection basis.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
