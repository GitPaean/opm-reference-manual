### FILLEPS -- Activate Saturation End-Point Export to the INIT File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on the export of the saturation end-point data ([SWL](#__RefHeading___Toc22881_7842323221), [SWCR](#__RefHeading___Toc27248_784232322), [SOWCR](#__RefHeading___Toc30436_784232322) array etc.) to the \*.INIT file so that the data can be viewed in post-processing software like OPM ResInsight.

There is no data required for this keyword.

#### Example

\--

\-- ACTIVATE SATURATION END-POINT EXPORT TO THE INIT FILE

\--

FILLEPS

The above example switches on the export of the end-point saturation data to the \*.INIT file.
