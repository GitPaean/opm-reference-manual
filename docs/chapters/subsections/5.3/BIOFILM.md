### BIOFILM -- Activate the Biofilm Model

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) keyword activates the biofilm model for the run. Biofilm-related effects in subsurface applications such as hydrogen storage include reduced injectivity and hydrogen loss. The conceptual model includes the following mechanisms: (1) Biofilm is present in the storage site prior to injection and (2) the biofilm consumes injected H~2~/CO~2~, leading to clogging effects.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE THE BIOFILM MODEL

\--

BIOFILM

\--

\-- ACTIVATE THE H2STORE MODEL

\--

WATER

GAS

H2STORE

The above example declares that the [BIOFILM](#REF_HEADING_KEYWORD_BIOFILM) model is active for the run and activates the [H2STORE](#REF_HEADING_KEYWORD_H2STORE) model. For a complete example of this model, see [H2STORE_BIOFILM.DATA](https://github.com/OPM/opm-tests/blob/master/h2store/H2STORE_BIOFILM.DATA).
