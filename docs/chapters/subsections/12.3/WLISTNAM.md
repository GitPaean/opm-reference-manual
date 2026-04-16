### WLISTNAM -- Define Well Lists (WLISTARG)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WLISTNAM](#__RefHeading___Toc592907_4263943340) declares a group of wells to belong to a named [WLISTARG](#__RefHeading___Toc585895_4263943340) well list for use with the [WLISTARG](#__RefHeading___Toc585895_4263943340) keyword. Only the [WLISTARG](#__RefHeading___Toc585895_4263943340) keyword can be used with this type of well list, and therefore it is better to use the [WLIST](#__RefHeading___Toc179534_3325167686) keyword instead, that defines a static well list but offers more flexibility than a [WLISTNAM](#__RefHeading___Toc592907_4263943340) well list.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 2-51 | WELNAMES | A character string of up to eight characters in length that defines the well name that belongs to the named well list ([WLIST](#__RefHeading___Toc179534_3325167686)). A total of 50 well names can be added to [WLISTNAM](#__RefHeading___Toc592907_4263943340) at a time.<br>If the first well name in the list is the default value ("\*1"), then the list is first cleared of all wells, before adding the subsequent wells in WELLNAMES.<br>Well names roots may all be used in WELLNAMES as long as they are enclosed in quotes and end with an asterisk ("\*"). In this case all wells that match the specification will be added to the list. For example, wells named OP01, OP02 and OP03, can be added as group by using "OP\*" as the well name.<br>Note that the well names must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | 1\* |
| --- | --- | --- | --- |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.106: WLISTNAM Keyword Description

Note that named well list production data in the [SUMMARY](#__RefHeading___Toc43949_784232322) file is well dependent, that is, if the wells belonging to a named well list is changed through time, the [SUMMARY](#__RefHeading___Toc43949_784232322) data will be based on the wells in the named well list group at the end of the run. Thus, if there are three wells in a named well list called \*PROD1 at the beginning of a run; OP01, OP02 and OP03, and during the run OP03 is moved to a well named list called \*PROD2, then the [SUMMARY](#__RefHeading___Toc43949_784232322) data for \*PROD1will only contain the production data for wells OP01 and OP02 and \*PROD2 will only contain the [SUMMARY](#__RefHeading___Toc43949_784232322) data for OP03 from the start to the end of the run.

#### Example

The following example defines two named well lists using the [WLISTNAM](#__RefHeading___Toc592907_4263943340) keyword.

\--

\-- WELL LIST SPECIFICATION

\--

\-- LIST WELL NAME LIST

\-- NAME

WLISTNAM

\'\*BLK-1\' WEL-01M WEL-02M WEL-03M WEL-04M WEL-05M WEL-06M WEL-07M /

\'\*BLK-1\' WEL-08M WEL-09M WEL-10M WEL-11M WEL-12M WEL-13M WEL-14M /

\'\*BLK-1\' WEL-15M WEL-16M WEL-17M WEL-18M WEL-19M WEL-20M WEL-23M /

\'\*BLK-1\' WEL-24M WEL-25M WEL-26M WEL-28M /

\'\*BLK-2\' 1\* WEL-03U WEL-05U WEL-06U WEL-10U WEL-11U WEL-13U WEL-14U /

\'\*BLK-2\' WEL-15U WEL-16U WEL-17U WEL-18U WEL-19U WEL-25U WEL-27U /

/

Here well list \''\*BLK-1' contains 28 wells, that is wells WEL-01M to WEL-28M. For the \'\*BLK-2\' well list all wells are first deleted due to the "1\*" default value and then wells WEL-03U to WEL-27U are added to the list.
