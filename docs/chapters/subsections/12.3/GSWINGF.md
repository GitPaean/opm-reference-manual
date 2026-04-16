### GSWINGF -- Define Group Multiple Gas Contract Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [GSWINGF](#__RefHeading___Toc224004_870710203), defines the gas contract parameters, swing factor and the monthly seasonal profile factor, for when there are multiple gas contracts being used in the model. The keyword is used with the Gas Field Operations option which is activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Gas contracts are commonly based on a Daily Contract Quantity ("DCQ") that determines the gas rate that the field should be produced at, which is normally expressed as a multiple of the DCQ, for example 1.33, and is often referred to as the "swing factor". Some gas contracts also define a maximum DCQ ("Max DCQ") and/or a minimum take or pay DCQ ("Min DCQ"), as well as seasonal demand characteristics. For example, gas rates may be set higher in the winter months in order to meet heating demand compared with summer months in colder climates, and the opposite in warmer climates where air conditioning demand is high.

Thus, the DCQ must be calculated first over a contract period, where the contract period is commonly contract years, or in some instances contract quarters. This is performed by the simulator using the current DCQ and checking to see if the (DCQ x Swing Factor) can be satisfied throughout the current contract period, if not the DCQ is re-calculated so that the (DCQ x Swing Factor) condition is satisfied. Once this condition is met, the second and final pass uses the calculated DCQ in conjunction with the monthly scaling profile data to set the monthly gas rate for the field:

Where:

Qmonth = the monthly gas production target

DCQ = Daily Contract Quantity

[SWINGFAC](#__RefHeading___Toc1193036_4250154414)~month\ ~= monthly rate scaling factor that takes into account seasonal demand, etc.

Here the [GSWINGF](#__RefHeading___Toc224004_870710203) keyword allows for different gas contract parameters to be assign to different groups and is mutually exclusive to the [SWINGFAC](#__RefHeading___Toc1193036_4250154414) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, that sets the gas contract parameters for a single contract at the FIELD group level.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
