### INSPEC -- Activate the INSPEC File Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword switches on the writing of the [INIT](#__RefHeading___Toc45789_719036256) Index file that specifies and defines the format and data type written to the \*.INIT data file. The \*.INIT data file contains the static data specified in the [GRID](#__RefHeading___Toc38674_784232322), [PROPS](#__RefHeading___Toc39329_784232322) and [REGIONS](#__RefHeading___Toc40648_784232322) sections. For example, the [PORO](#__RefHeading___Toc45797_719036256), PERM and [NTG](#__RefHeading___Toc33334_784232322) arrays from the [GRID](#__RefHeading___Toc38674_784232322) section. The data is used in post-processing software, for example OPM ResInsight, to visualize the static grid properties.

The [INIT](#__RefHeading___Toc45789_719036256) Index file can either be written out in formatted form as ASCII i.e. text files, if the [FMTOUT](#__RefHeading___Toc46651_1640804870) keyword has been activated (\*.FINSPEC), or binary format (\*.INSPEC) if the [FMTOUT](#__RefHeading___Toc46651_1640804870) keyword has not been activated. If the [INIT](#__RefHeading___Toc45789_719036256) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section has been used to switch on the writing of the \*. [INIT](#__RefHeading___Toc45789_719036256) data file then a binary [INIT](#__RefHeading___Toc45789_719036256) Index file is automatically written out as well, unless the [NOINSPEC](#__RefHeading___Toc70892_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section has been used to switch off the writing of the [INIT](#__RefHeading___Toc45789_719036256) Index file.

Note that most post-processing software require the \*.INSPEC file to load the \*.INIT data set, although OPM ResInsight does not require this file to be able to load the \*.INIT data file.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE WRITING THE INIT INDEX FILE FOR POST-PROCESSING

\--

INSPEC

The above example switches on the writing of the [INIT](#__RefHeading___Toc45789_719036256) Index file for post-processing in ResInsight.
