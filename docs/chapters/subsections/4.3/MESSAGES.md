### MESSAGES -- Define Message Print Limits and Stop Limits

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [MESSAGES](#__RefHeading___Toc61634_2479612490) keyword defines the print and stops levels for various messages. The "print limits" set the maximum number of messages that will be printed, after which no more messages will be printed and the "stop limits" terminate the run when these limits are exceeded. There are six levels of message that increase in severity from informative all the way to programming errors, as outlined in [Table 4.5](#anchor-2).

| 1 | PRTSMESG | An integer defining the maximum number of MESSAGE type messages to be printed after which this type of message stops printing. | 1,000,000 |
| --- | --- | --- | --- |
| 2 | PRTSCOMT | An integer defining the maximum number of COMMENT type messages be printed after which this type of message stops printing. | 1,000,000 |
| 3 | PRTSWARN | An integer defining the maximum number of WARNING type messages be printed after which this type of message stops printing. | 10,000 |
| 4 | PRTSPROB | An integer defining the maximum number of PROBLEM type messages to be printed after which this type of message stops printing. | 100 |
| 5 | PRTSERRS | An integer defining the maximum number of ERROR type messages to be printed after which this type of message stops printing. | 100 |
| 6 | PRTSBUGS | An integer defining the maximum number of BUG type messages to be printed after which this type of message stops printing. | 100 |
| 7 | STOPMESG | An integer defining the maximum number of MESSAGE type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 1,000,000 |
| 8 | STOPCOMT | An integer defining the maximum number of COMMENT type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 1,000,000 |
| 9 | STOPWARN | An integer defining the maximum number of WARNING type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 10,000 |
| 10 | STOPPROB | An integer defining the maximum number of PROBLEM type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 100 |
| 11 | STOPERRS | An integer defining the maximum number of ERROR type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 10 |
| 12 | STOPBUGS | An integer defining the maximum number of BUG type messages to be printed after which OPM Flow terminates the run.<br>Not used by OPM Flow. | 1 |
| 13 | PRTGRPMS | An integer defining the maximum number of GROUP MESSAGE type messages to be printed after which this type of message stops printing.<br>Not used by OPM Flow. | 10 |
| Notes:<br>1)  MESSAGE type messages are informative messages.<br>2)  COMMENT type messages are probably not data errors.<br>3)  WARNING type message are possible data errors and should be investigated.<br>4)  PROBLEM type errors messages are associated with numerical problems.<br>5)  ERROR type messages are errors that need to be fixed before the simulator can run the input deck.<br>6)  BUG type of messages are potential programming errors.<br>7)  The keyword is terminated by a "/". |  |  |  |

Table 4.5: MESSAGES Keyword Description

#### Example

\--

\-- MESS COMMT WARN PROBL ERROR BUG MESS COMMT WARN PROBL ERROR BUG

\-- LIMIT LIMIT LIMIT LIMIT LIMIT LIMIT STOP STOP STOP STOP STOP STOP

MESSAGES

1\* 1\* 1\* 1500 1\* 1\* 1\* 1\* 1\* 1000 1\* 1\* /

The above example sets the PROBLEM type message print limit to 1,500 and the stop limit to 1,000.
