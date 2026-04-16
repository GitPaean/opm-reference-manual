### GRUPMAST -- Define Master and Slave Groups

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [GRUPMAST](#__RefHeading___Toc488185_1414963541) keyword defines master groups and their associated slave groups for when the Reservoir Coupling option as been activated by the [GRUPMAST](#__RefHeading___Toc488185_1414963541) and [SLAVES](#__RefHeading___Toc1268538_516898843) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Reservoir coupling allows for independent reservoir simulation decks ([SLAVES](#__RefHeading___Toc1268538_516898843)) to be controlled by a separate master run file. For example, if there are five separate reservoir models each representing one field, one of the four would be used as the master and the other four would be the subordinate [SLAVES](#__RefHeading___Toc1268538_516898843).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
