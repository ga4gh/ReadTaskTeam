.. _metadata:

***************************
Metadata API (stub)
***************************

For the Metadata schema definitions, see the `Metadata schema <schemas/metadata.html>`_

------------------
Metadata
------------------

`FIXME: Stub here for time format submission; to be extended...`

* standardized use of common attributes/values
* a schema of how objects relate to each other


-----------------------------------
Date and Time Format Specifications
-----------------------------------

`FIXME: Move date/time to separate document?`
`FIXME: Add examples for time attributes as when such are implemented 
in the schema.`

Date and time formats are specified as ISO8601 compatible strings, both for
time points as well as for intervals and durations.
The required granularity have to be specified as part of the respective
attributes' documentations.


===========
Time points
===========

The specification of a time point is given through the concatenation of
* a date in YYYY-MM-DD
* the designator "T" indicating a following time description
* the time of day in HH:MM:SS.SSS form, where "SSS" represents a decimal
fraction of a second
* a time zone offset in relation to UTC

**Examples**

* year (YYYY)
    2015

* date (e.g. date of birth) in YYYY-MM-DD
    2015-02-10

* time stamp in milliseconds in YYYY-MM-DDTHH:MM:SS.SSS
    2015-02-10T00:03:42.123Z


===========
Durations
===========

Durations are a specific form of intervals, without reference to time points.
They are indicated with a leading "P", followed by unit delimited
quantifiers. A leading "T" is required before the start of the time components.
Durations do not have to be normalized; "PT50H" is equally valid as "P2T2H".

**Examples**

* age in years in PnY
    P44Y

* age in years and months in PnYnM
    P44Y08M

* short time interval (e.g. 30min in experimental time series) in PTnM
    PT30M


==============
Time intervals
==============

Time intervals consist of a combination of two time designators. These can be
either two time points for start and end, or one time point and a leading
(time point indicates end) or trailing (time point indicates start) duration.
The time elements are separated by a forward slash "/".

**Examples**

* age with date of birth in YYYY-MM-DD/PnYnMnD
    1967-11-21/P40Y10M05D

* anchored 3 month interval, e.g. a therapy cycle in YYYY-MM-DD/YYYY-MM-DD
    2015-04-18/2015-07-17

* experimental intervention of 30min in YYYY-MM-DDTHH:MM/YYYY-MM-DDTHH:MM
    2014-12-31T23H45M/2015-01-01T00H15M
