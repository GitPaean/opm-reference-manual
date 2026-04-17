### WRFT -- Activate Well RFT Reporting to the RFT File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates reporting of a well's pressure and saturation profile versus depth for the connected grid blocks, to the RFT file for the requested wells at the time the keyword is activated. Data written out by OPM Flow is used to match the field measured data collected from a Repeat Formation Tester ("RFT") tool.

The RFT tool is an open hole device which is an updated version of the Formation Interval Tester ("FIT"), both of which are run on wire line. Both tools take multiple pressure readings (at various depths) thus enabling a pressure depth profile to be obtained from the formation, and, in addition, they can also take fluid samples from the formation. The latest tool available from Schlumberger is the Modular Formation Dynamics Tester ("MDT"), which, as its name suggests, is a modular tool that can be assembled in different configurations depending on what are the objectives for running the tool. Note other vendors have similar wire line logging tools with alternative names for the tools. Throughout this section the term RFT applies to all tools that measure a pressure profile versus depth (RFT/FIT/MDT etc.).

| 1 | WELNAME | A columnar vector of character strings of up to eight characters in length for each item, that defines the well name for which the RFT data should be written to the RFT file.<br>Note that the WELNAME must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur.<br>If the WELNAME is left blank then the data is written out for all wells at the time they are first opened to flow.<br>If the WELNAME is given, then the RFT data for the well at the time step the keyword is invoked is written out. | None |
| --- | --- | --- | --- |
| Notes:<br>1)  The keyword is followed by any number of records.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.115: WRFT Keyword Description

See also the WRFTPLT keyword in the SCHEDULE section that has more flexible reporting options.

#### Examples

The first example activates RFT reporting for all wells at the time a well is first opened to flow:

\--

\-- ACTIVATE WELL RFT REPORTING TO THE RFT FILE

\--

\-- WELL

\-- NAME

WRFT

/

Ideally, this version of the keyword should be place at the beginning of the SCHEDULE section to obtain the data for the wells in the run before they are opened up through time.

The next example shows how to use the keyword to request the output for several wells at different reporting time steps.

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- 01 JAN 2000 START OF SCHEDULE SECTION

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

DATES

15 JAN 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.5E3 0.0 1550 10 1\* 900.0 1\* /

OP02 SHUT /

/

\--

\-- ACTIVATE WELL RFT REPORTING TO THE RFT FILE

\--

\-- WELL

\-- NAME

WRFT

OP01 /

OP02 /

/

DATES

01 FEB 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.5E3 0.0 1550 10 1\* 900.0 1\* /

OP02 SHUT /

/ \--

\-- ACTIVATE WELL RFT REPORTING TO THE RFT FILE

\--

\-- WELL

\-- NAME

WRFT

OP01 /

OP02 /

/

DATES

01 MAR 2000 /

/

\--

\-- WELL HISTORICAL PRODUCTION CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS VFP VFP THP BHP

\-- NAME SHUT MODE RATE RATE RATE TABLE ALFQ PRES PRES

WCONHIST OP01 OPEN ORAT 15.5E3 0.0 1550 10 1\* 900.0 1\* /

OP02 OPEN ORAT 10.5E3 0.0 1000 10 1\* 900.0 1\* /

/

In this example, both well's have their RFT written out on February 1 and March 1 2000.
