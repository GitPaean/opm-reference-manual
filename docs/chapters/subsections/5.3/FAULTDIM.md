### FAULTDIM -- Define the Number of Fault Segments

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [FAULTDIM](#__RefHeading___Toc28917_1640804870) keyword defines the maximum number of records (or segments) that can be entered with the [FAULTS](#__RefHeading___Toc45779_719036256) keyword. The [FAULTS](#__RefHeading___Toc45779_719036256) keyword defines the faults in the grid than can be used for setting (or re-setting) transmissibility barriers across the fault planes.

+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name   | > Description                                                                                                                                   | > Default |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > MFSEGS | > A positive integer value that defines the maximum number of records (segments) for the [FAULTS](#__RefHeading___Toc45779_719036256) keyword.  | > 0       |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |          |                                                                                                                                                 |           |
|                                           |          |                                                                                                                                                 |           |
| 1)  The keyword is terminated by a "/".   |          |                                                                                                                                                 |           |
+-------------------------------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 5.13: FAULTDIM Keyword Description

#### Example

\--

\-- FAULT

\-- SEGMS

\--

FAULTDIM

10000 /

The above example defines the maximum number of records that can be entered using the FAULT keyword to be 10,000 segments.
