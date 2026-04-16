### INIT -- Activate the INIT File Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on the writing of the [INIT](#__RefHeading___Toc45789_719036256) file that contains the static data specified in the [GRID](#__RefHeading___Toc38674_784232322), [PROPS](#__RefHeading___Toc39329_784232322) and [REGIONS](#__RefHeading___Toc40648_784232322) sections. For example, the [PORO](#__RefHeading___Toc45797_719036256), PERM and [NTG](#__RefHeading___Toc33334_784232322) arrays from the [GRID](#__RefHeading___Toc38674_784232322) section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The [INIT](#__RefHeading___Toc45789_719036256) file can either be written out in formatted form as ASCII i.e. text files, if the [FMTOUT](#__RefHeading___Toc46651_1640804870) keyword has been activated, or binary format if the [FMTOUT](#__RefHeading___Toc46651_1640804870) keyword has not been activated. Normally, this option is always activated by the user and when activated the binary form of the file is used.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE WRITING THE INIT FILE FOR POST-PROCESSING

INIT

The above example switches on the writing of the [INIT](#__RefHeading___Toc45789_719036256) file for post-processing in ResInsight.
