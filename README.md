# NY Ramblers Hiking Trails — Maps, Elevation Profiles & NYC Transit Guide

> **Attribution Notice**: All hike schedules, route descriptions, and club information are sourced from the [New York Ramblers Hiking Club](https://www.nyramblers.org/schedule/) (© 2026 The New York Ramblers, Inc. All rights reserved) and volunteer hike leaders (Hugues, Chris, Ingrid, Leah, Peter, Erik, and Brian). Trail map references are credited to the [New York–New Jersey Trail Conference](https://www.nynjtc.org/), [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, and [OpenTopoMap](https://opentopomap.org/). See [`ATTRIBUTION.md`](./ATTRIBUTION.md) for full details.

## Overview

This private repository stores extracted hiking routes from [nyramblers.org/schedule](https://www.nyramblers.org/schedule/), complete with GPS trail waypoints, 3D GeoJSON route geometry, side-by-side trail maps and elevation charts, and NYC public transportation connections.

## Repository Structure

- `ATTRIBUTION.md` — Complete credits to The New York Ramblers, Inc., volunteer hike leaders, NY-NJ Trail Conference, OpenStreetMap/OpenTopoMap, and regional transit agencies.
- `data/hikes.json` — Structured metadata, attribution header, turn-by-turn trail sequences, elevation profiles, and NYC transit itineraries for all 9 scheduled hikes.
- `data/trails.geojson` — Standard GeoJSON `FeatureCollection` (3D `LineString` routes and `Point` waypoints with elevation in feet) compatible with GitHub's native GeoJSON map viewer, CalTopo, and Gaia GPS.
- `charts/hike_1_chart.png` .. `charts/hike_9_chart.png` — High-resolution (180 DPI) side-by-side trail route maps and elevation profiles.
- `docs/index.html` — Self-contained interactive web application (Leaflet topographic maps + Chart.js elevation profiles).
- `docs/ny_ramblers_hiking_guide.pdf` — Printable 12-page PDF trail guide.
- `scripts/update_trails.py` & `.github/workflows/update-trails.yml` — Automated weekly GitHub Action that checks `https://www.nyramblers.org/schedule/` every Monday at 12:00 UTC (8:00 AM EDT) and commits any schedule updates with full attribution.

## Included Hikes (Fall 2026 Schedule)

| # | Date | Hike Title | Region & Map Ref | Distance | Elev. Gain | Start Transit | End Transit | Leader |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Sun. Oct. 4 | **Fourteen Hills: A Circular** | Harriman SP (NY-NJTC 118) | 15.2 mi | +3,450 ft | Sloatsburg (ShortLine Bus / NJT) | Sloatsburg (ShortLine Bus / NJT) | Hugues |
| 2 | Sun. Oct. 11 | **Salt Hill State Forest: A Circular** | Westchester, NY | 16.4 mi | +2,150 ft | Croton-Harmon (MNR Hudson) | Croton-Harmon (MNR Hudson) | Chris |
| 3 | Sat. Oct. 17 | **Rye to Mamaroneck Along the Sound** | Westchester Sound Shore | 13.0 mi | +420 ft | Rye (MNR New Haven) | Mamaroneck (MNR New Haven) | Ingrid |
| 4 | Sun. Oct. 25 | **Torrey Memorial** | Bear Mountain SP (NY-NJTC 119) | 14.7 mi | +3,255 ft | Rt 32 & Smith Clove Rd (ShortLine) | Bear Mountain Inn (ShortLine) | Leah |
| 5 | Sat. Oct. 31 | **Manicure the Nurian Trail** | Harriman SP (NY-NJTC 119) | 11.5 mi | +2,150 ft | Southfields Rt 17 (ShortLine) | Tuxedo Station (NJT Port Jervis) | Peter |
| 6 | Sat. Nov. 7 | **Hewitt to Wanaque** | Norvin Green SF, NJ (Map 151) | 15.6 mi | +3,380 ft | Hewitt Lakeside Rd (NJT Bus 197) | Wanaque Ringwood Ave (NJT Bus 197) | Erik |
| 7 | Sun. Nov. 15 | **Melzingah Reservoir** | East Hudson Highlands (Map 102) | 15.5 mi | +3,850 ft | Beacon (MNR Hudson) | Cold Spring (MNR Hudson) | Brian |
| 8 | Sun. Nov. 22 | **Sunken Meadow State Park Circular** | Long Island, NY | 15.0 mi | +1,350 ft | Kings Park (LIRR Port Jefferson) | Kings Park (LIRR Port Jefferson) | Peter |
| 9 | Sun. Nov. 29 | **Tuxedo to Suffern, The Long Way** | Harriman SP (NY-NJTC 118) | 17.8 mi | +3,950 ft | Tuxedo Station (NJT Port Jervis) | Suffern Station (NJT Main/Bergen) | Hugues |
