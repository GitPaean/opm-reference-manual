### WLIST -- Define Well Lists (Static)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

WLIST declares a group of wells to belong to a named static well list. Wells in a named well list are treated as a group of wells for which the standard well keywords can be applied. For example, instead of repeating a well keyword for each well, the keyword only needs to have the named well list instead, for the action to be applied to all wells in the named well list. In general any well keyword that allows well name roots as a well name, for example, PROD\*, can use a named well list.

| 2 | ACTION | A defined character string that determines how the WELNAMES should be handled with respect to the named well list (WLIST). ACTION should be set to one of the following::<br>1)  ADD: Add the WELNAMES to an existing WLIST.<br>2)  DEL; Delete WELNAMES from an existing WLIST.<br>3)  MOV: WELNAMES from another existing named well list and ADD them to WLIST.<br>4)  NEW: Define a new named well list and add the WELNAMES to WLIST. |  |
| --- | --- | --- | --- |
| 3-52 | WELNAMES | A character string of up to eight characters in length that defines the well name that belongs to the named well list (WLIST). A total of 50 well names can be added to WLIST at a time. If additional wells are needed to added then use the ADD option of ACTION to add additional wells.<br>Well names roots may all be used in WELNAMES as long as they are enclosed in quotes and end with an asterisk ("\*"). In this case all wells that match the specification will be added to the list. For example, wells named OP01, OP02 and OP03, can be added as group by using "OP\*" as the well name.<br>Note that the well names must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.104: WLIST Keyword Description

Note that named well list production data in the SUMMARY file is well dependent, that is, if the wells belonging to a named well list is changed through time, the SUMMARY data will be based on the wells in the named well list group at the end of the run. Thus, if there are three wells in a named well list called \*PROD1 at the beginning of a run; OP01, OP02 and OP03, and during the run OP03 is moved to a well named list called \*PROD2, then the SUMMARY data for \*PROD1will only contain the production data for wells OP01 and OP02 and \*PROD2 will only contain the SUMMARY data for OP03 from the start to the end of the run.

#### Example

The following example defines two named well lists using the WLIST keyword.

\--

\-- WELL LIST SPECIFICATION

\--

\-- LIST OPER WELL NAME LIST

\-- NAME

WLIST

\'\*BLK-1\' NEW WEL-01M WEL-02M WEL-03M WEL-04M WEL-05M WEL-06M WEL-07M /

\'\*BLK-1\' ADD WEL-08M WEL-09M WEL-10M WEL-11M WEL-12M WEL-13M WEL-14M /

\'\*BLK-1\' ADD WEL-15M WEL-16M WEL-17M WEL-18M WEL-19M WEL-20M WEL-23M /

\'\*BLK-1\' ADD WEL-24M WEL-25M WEL-26M WEL-28M /

\'\*BLK-2\' NEW WEL-03U WEL-05U WEL-06U WEL-10U WEL-11U WEL-13U WEL-14U /

\'\*BLK-2\' ADD WEL-15U WEL-16U WEL-17U WEL-18U WEL-19U WEL-25U WEL-27U /

/

DATES

1 JAN 2020 /

/

\--

\-- DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS

\--

\-- WELL WELL \--LOCATION\-- COMPLETION

\-- NAME STAT I J K FIRST LAST

WELOPEN

\'\*BLK-1\' OPEN /

\'\*BLK-1\' OPEN 0 0 0 0 0 /

/

DATES

1 JAN 2021 /

1 JLY 2021 /

1 OCT 2021 /

/

\--

\-- DEFINE WELL AND WELL CONNECTIONS FLOWING STATUS

\--

\-- WELL WELL \--LOCATION\-- COMPLETION

\-- NAME STAT I J K FIRST LAST

WELOPEN

\'\*BLK-2\' OPEN /

\'\*BLK-2\' OPEN 0 0 0 0 0 /

/

In this example the wells in named well list ''\*BLK-1" are opened on January 1, 2020 and wells in named well list '\*BLK-2" are opened October 1, 2021.
