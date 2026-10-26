# hookline-sources

Block lists for [Hookline](https://github.com/SpecSierra/hookline), the Sailfish OS 5 call blocker.

## Lists

- **Index:** [`blocklists/index.json`](blocklists/index.json), read by the app every day.
- **Defaults:** each list is on by default in its own country.

## Add a list

- **Index entry:** `id`, `country`, `name`, `description`, `license`, `attribution`, `attribution_url`
- **Number format:** `country_code`, `trunk_prefix` (national form, e.g. `0`)
- **`urls`:** JSON lines files, one `{"name": "…", "pattern": "34400######"}` per line, each `#` = any digit
- **Sources:** official ones (a regulator or a law) or openly licensed lists only

## Old lookup robots

- **Where:** `files/`, the Phonehook website lookup robots, no longer used by Hookline.
- **Origin:** [omnight/phonehook-sources](https://github.com/omnight/phonehook-sources).
