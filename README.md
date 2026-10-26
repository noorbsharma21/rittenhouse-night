# Watch Rittenhouse Square close

An interactive map of every establishment with published hours in the Rittenhouse
Square study area, Philadelphia. Drag through the night — or press play — and see
which kinds of business stay open, on any night of the week.

**Live page: https://noorbsharma21.github.io/rittenhouse-night/**

Built for CPLN 6890 *The City at Night*, Area Study 2, Brief 7: Business Activity
(University of Pennsylvania, Weitzman School of Design).

## What you are looking at

- Each icon is one establishment, placed at its address. The icon says what kind of
  business it is; a filled icon is trading in the hour shown, a faded one has closed.
- Hollow icons are the eight places that publish no hours — four hotels, the Square
  itself, two residential buildings and one store.
- Each night runs 6am to 5am the following morning, so a Friday 1am closing counts
  against Friday night rather than Saturday.
- Click a row in the legend to isolate or hide a kind of business.

## Linking to one moment

Add `?day=` and `?h=` to open the page already set to a particular hour, which is
useful from a printed report:

- <https://noorbsharma21.github.io/rittenhouse-night/?day=Fri&h=22> — Friday 10pm, 17 open
- <https://noorbsharma21.github.io/rittenhouse-night/?day=Fri&h=0> — Friday midnight, 7 open
- <https://noorbsharma21.github.io/rittenhouse-night/?day=Tue&h=22> — Tuesday 10pm, for contrast

`h` is a 24-hour clock value; anything from 6 (6am) round to 5 (5am) lands in the
same night.

## Source and method

Google Places extract (August 2026), joined to the 2026 study-area polygon with a
strict spatial join: 67 of 707 citywide points fall inside, 59 of them with
published hours.

Opening hours were rebuilt from the raw `weekday_text` strings rather than taken
from the supplied hour columns, which disagreed with the source text for 27% of
place-days. Categories were corrected against Philadelphia L&I business licences
and PLCB liquor licences, and by hand where the source tags did not match the
business.

Noor Sharma, October 2026.
