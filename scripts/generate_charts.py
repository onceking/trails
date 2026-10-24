import json
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("artifacts/file_generation/ttl=63d/intermediate", exist_ok=True)
os.makedirs("artifacts/file_generation/ttl=63d/output", exist_ok=True)

HIKES = [
    {
        "id": 1,
        "date": "Sun. Oct. 4, 2026",
        "title": "Fourteen Hills: A Circular",
        "region": "Harriman State Park, NY",
        "park_url": "https://www.palisadesparks.org/harriman",
        "leader": "Hugues",
        "pace": "Fast pace (Strenuous)",
        "duration": "7–8 hours",
        "distance_mi": 15.2,
        "elevation_gain_ft": 3450,
        "max_elev_ft": 1290,
        "min_elev_ft": 350,
        "route_type": "Out-and-Back / Circular",
        "map_ref": "NY-NJTC Map 118",
        "map_url": "https://www.nynjtc.org/",
        "summary": "From Sloatsburg station, use local streets to Pine Meadow Trail, thence to the Seven Hills Trail, which hike in its entirety to Lake Sebago. Then retrace! (Possible extensions depending on conditions.)",
        "trail_sequence": [
            "Sloatsburg Station & Local Streets (Eagle Valley Rd)",
            "Pine Meadow Trail (Red)",
            "Seven Hills Trail (Blue) — Ramapo Torne, Russian Bear, Torne View, West Mountain Peaks",
            "Diamond Mountain (1,290 ft) to Lake Sebago Boat Launch",
            "Retrace Seven Hills Trail & Pine Meadow Trail to Sloatsburg"
        ],
        "transit_start": {
            "station": "Sloatsburg, NY (Rt 17 & Mill St / Rail Station)",
            "mode": "Bus / Rail",
            "hub": "Port Authority Bus Terminal (Gate 408) or Penn Station",
            "details": "Coach USA ShortLine Hudson Bus from PABT Gate 408 to Rt 17 & Mill St, Sloatsburg (~61 min; schedule notes bus substitution), or NJ Transit Port Jervis Line via Secaucus Junction (~79 min).",
            "url": "https://www.google.com/maps/dir/Port+Authority+Bus+Terminal/Rt+17+%26+Mill+St+-+Sloatsburg/data=!4m5!4m4!2m2!6e0!8j1792868766!3e3",
            "agency_url": "https://www.njtransit.com/abc_PORT_JERVIS"
        },
        "transit_end": {
            "station": "Sloatsburg, NY (Rt 17 & Mill St / Rail Station)",
            "mode": "Bus / Rail",
            "hub": "Port Authority Bus Terminal or Penn Station",
            "details": "Return via Coach USA ShortLine Hudson Bus from Rt 17 & Mill St to PABT (~61 min) or NJ Transit Port Jervis Line from Sloatsburg Station to Secaucus / Penn Station (~79 min).",
            "url": "https://www.google.com/maps/dir/Penn+Station/Sloatsburg/data=!4m5!4m4!2m2!6e0!8j1792854245!3e3",
            "agency_url": "https://www.njtransit.com/abc_PORT_JERVIS"
        },
        "waypoints": [
            {"name": "Sloatsburg Station", "lat": 41.1565, "lon": -74.1912, "dist": 0.0, "elev": 350},
            {"name": "Pine Meadow Trailhead", "lat": 41.1585, "lon": -74.1780, "dist": 1.1, "elev": 460},
            {"name": "Seven Hills Jct", "lat": 41.1632, "lon": -74.1655, "dist": 2.2, "elev": 680},
            {"name": "Ramapo Torne", "lat": 41.1601, "lon": -74.1585, "dist": 3.1, "elev": 1120},
            {"name": "Russian Bear & Torne View", "lat": 41.1685, "lon": -74.1510, "dist": 4.3, "elev": 1080},
            {"name": "HTS Trail Crossing", "lat": 41.1740, "lon": -74.1450, "dist": 5.4, "elev": 820},
            {"name": "Diamond Mountain", "lat": 41.1865, "lon": -74.1360, "dist": 6.6, "elev": 1290},
            {"name": "Lake Sebago Turnaround", "lat": 41.1920, "lon": -74.1325, "dist": 7.6, "elev": 785},
            {"name": "Diamond Mtn (Return)", "lat": 41.1865, "lon": -74.1360, "dist": 8.6, "elev": 1290},
            {"name": "Torne View (Return)", "lat": 41.1685, "lon": -74.1510, "dist": 10.9, "elev": 1080},
            {"name": "Ramapo Torne (Return)", "lat": 41.1601, "lon": -74.1585, "dist": 12.1, "elev": 1120},
            {"name": "Pine Meadow Tr (Return)", "lat": 41.1585, "lon": -74.1780, "dist": 14.1, "elev": 460},
            {"name": "Sloatsburg Station", "lat": 41.1565, "lon": -74.1912, "dist": 15.2, "elev": 350}
        ]
    },
    {
        "id": 2,
        "date": "Sun. Oct. 11, 2026",
        "title": "Salt Hill State Forest: A Circular",
        "region": "Westchester County, NY",
        "park_url": "https://scenesfromthetrail.com/2020/06/07/salt-hill-state-forest/",
        "leader": "Chris",
        "pace": "Brisk pace",
        "duration": "7–8 hours",
        "distance_mi": 16.4,
        "elevation_gain_ft": 2150,
        "max_elev_ft": 700,
        "min_elev_ft": 15,
        "route_type": "Circular Loop",
        "map_ref": "Westchester Trails / Salt Hill SF",
        "map_url": "https://dec.ny.gov/places/montrose-point-state-forest",
        "summary": "From Croton-Harmon station follow Croton River Walk north to Brook Street. Climb to Upper Village Loop to Kaplan's Pond, Fox Road to Lytle Arboretum, Highland Trail to viewpoint, powerline to Colabaugh Pond Rd, Briarcliff-Peekskill Trailway to Valeria trails, and enter Salt Hill SF. Follow Leander's Way to former Nelson Mtn. fire tower; descend Fire Tower Trail to Rte. 129, cross Croton Dam, and return via Old Croton Aqueduct.",
        "trail_sequence": [
            "Croton-Harmon Station to Croton River Walk & Brook St",
            "Upper Village Loop, Kaplan's Pond & Jane E. Lytle Arboretum",
            "Highland Trail Viewpoint & Briarcliff-Peekskill Trailway (Valeria)",
            "Salt Hill State Forest — Leander's Way to Nelson Mtn Fire Tower Site (699 ft)",
            "Fire Tower Trail to Rte. 129, New Croton Dam & Old Croton Aqueduct"
        ],
        "transit_start": {
            "station": "Croton-Harmon Station, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North Hudson Line direct from Grand Central Terminal to Croton-Harmon (~49–54 min, departures every 18–30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Croton-Harmon/data=!4m5!4m4!2m2!6e0!8j1792848000!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "transit_end": {
            "station": "Croton-Harmon Station, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North Hudson Line direct from Croton-Harmon back to Grand Central Terminal (~50 min, departures every 20–30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Croton-Harmon/data=!4m5!4m4!2m2!6e0!8j1792848000!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "waypoints": [
            {"name": "Croton-Harmon Station", "lat": 41.1897, "lon": -73.8825, "dist": 0.0, "elev": 15},
            {"name": "Croton River Walk", "lat": 41.2010, "lon": -73.8810, "dist": 1.3, "elev": 60},
            {"name": "Kaplan's Pond", "lat": 41.2130, "lon": -73.8760, "dist": 2.8, "elev": 260},
            {"name": "Lytle Arboretum", "lat": 41.2215, "lon": -73.8695, "dist": 4.1, "elev": 380},
            {"name": "Highland Trail Viewpoint", "lat": 41.2310, "lon": -73.8740, "dist": 5.5, "elev": 520},
            {"name": "Valeria / BP Trailway", "lat": 41.2420, "lon": -73.8650, "dist": 7.4, "elev": 440},
            {"name": "Salt Hill SF (Leander's Way)", "lat": 41.2485, "lon": -73.8490, "dist": 9.2, "elev": 560},
            {"name": "Nelson Mtn Tower Site", "lat": 41.2510, "lon": -73.8420, "dist": 10.3, "elev": 699},
            {"name": "Rte 129 Descent", "lat": 41.2380, "lon": -73.8450, "dist": 11.8, "elev": 240},
            {"name": "New Croton Dam", "lat": 41.2265, "lon": -73.8560, "dist": 13.2, "elev": 210},
            {"name": "Old Croton Aqueduct", "lat": 41.2090, "lon": -73.8720, "dist": 14.9, "elev": 140},
            {"name": "Croton-Harmon Station", "lat": 41.1897, "lon": -73.8825, "dist": 16.4, "elev": 15}
        ]
    },
    {
        "id": 3,
        "date": "Sat. Oct. 17, 2026",
        "title": "Rye to Mamaroneck Along the Sound",
        "region": "Westchester Sound Shore, NY",
        "park_url": "https://parks.westchestercountyny.gov/marshlands-conservancy",
        "leader": "Ingrid (substituting for Zee)",
        "pace": "Moderate pace",
        "duration": "7–8 hours",
        "distance_mi": 13.0,
        "elevation_gain_ft": 420,
        "max_elev_ft": 85,
        "min_elev_ft": 5,
        "route_type": "Point-to-Point Coastal Walk",
        "map_ref": "Westchester County Parks Coastal Sanctuaries",
        "map_url": "https://parks.westchestercountyny.gov/read-wildlifesanctuary",
        "summary": "Saturday hike at a moderate pace. From Rye station, hike south to Rye Nature Preserve, then to Long Island Sound. Continue along the shore through Edith Read Preserve, Playland Beach, Oakland Beach, Rye Town Park, Marshlands Conservancy and Otter Creek Preserve to Mamaroneck.",
        "trail_sequence": [
            "Rye Metro-North Station to Rye Nature Center",
            "Edith G. Read Wildlife Sanctuary & Playland Lake",
            "Playland Beach, Oakland Beach & Rye Town Park",
            "Marshlands Conservancy Forest & Salt Marsh Trails",
            "Otter Creek Preserve to Mamaroneck Station"
        ],
        "transit_start": {
            "station": "Rye Station, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North New Haven Line direct from Grand Central Terminal (towards Stamford) to Rye (~49 min, departures every 30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Rye/data=!4m5!4m4!2m2!6e0!8j1792848960!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "transit_end": {
            "station": "Mamaroneck Station, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North New Haven Line direct from Mamaroneck back to Grand Central Terminal (~42 min, departures every 30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Mamaroneck/data=!4m5!4m4!2m2!6e0!8j1792848960!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "waypoints": [
            {"name": "Rye Station", "lat": 40.9856, "lon": -73.6836, "dist": 0.0, "elev": 65},
            {"name": "Rye Nature Center", "lat": 40.9740, "lon": -73.6940, "dist": 1.4, "elev": 85},
            {"name": "Edith Read Sanctuary", "lat": 40.9680, "lon": -73.6660, "dist": 4.2, "elev": 20},
            {"name": "Playland Beach", "lat": 40.9640, "lon": -73.6725, "dist": 5.5, "elev": 10},
            {"name": "Rye Town Park & Oakland Beach", "lat": 40.9605, "lon": -73.6810, "dist": 6.8, "elev": 25},
            {"name": "Marshlands Conservancy", "lat": 40.9520, "lon": -73.7005, "dist": 9.3, "elev": 45},
            {"name": "Otter Creek Preserve", "lat": 40.9415, "lon": -73.7195, "dist": 11.4, "elev": 15},
            {"name": "Mamaroneck Station", "lat": 40.9547, "lon": -73.7361, "dist": 13.0, "elev": 50}
        ]
    },
    {
        "id": 4,
        "date": "Sun. Oct. 25, 2026",
        "title": "Torrey Memorial",
        "region": "Bear Mountain State Park, NY",
        "park_url": "https://www.palisadesparks.org/bear-mountain",
        "leader": "Leah",
        "pace": "Brisk pace",
        "duration": "7–8 hours",
        "distance_mi": 14.7,
        "elevation_gain_ft": 3255,
        "max_elev_ft": 1280,
        "min_elev_ft": 160,
        "route_type": "Point-to-Point Ridge & Gorge Traverse",
        "map_ref": "NY-NJTC Map 119",
        "map_url": "https://www.nynjtc.org/",
        "summary": "Annual hike honoring Trail Conference visionary Raymond Torrey (1880–1938). From Rt 32 bus stop, walk east on Smith Clove Rd to seasonal Long Path through West Point property. Hike Long Path to Torrey Memorial on Long Mountain, descend to Popolopen Gorge Trail, then Anthony Wayne to Appalachian Trail, following AT over Bear Mountain to Bear Mountain Inn.",
        "trail_sequence": [
            "Route 32 & Smith Clove Rd (Highland Mills) to West Point Seasonal Long Path",
            "Long Path (Aqua) over Long Mountain to Torrey Memorial (1,060 ft)",
            "Descent into Popolopen Gorge Trail (Red)",
            "Anthony Wayne Recreation Area to Appalachian Trail (White)",
            "Bear Mountain South Side / Summit (1,280 ft) to Bear Mountain Inn"
        ],
        "transit_start": {
            "station": "Route 32 & Smith Clove Rd (Highland Mills / Central Valley, NY)",
            "mode": "Intercity Bus",
            "hub": "Port Authority Bus Terminal (Gate 405 / 409)",
            "details": "Coach USA ShortLine Hudson Bus (Route 32 corridor towards Newburgh via Central Valley) from Port Authority Bus Terminal to Rt 32 & Smith Clove Rd (~75 min).",
            "url": "https://web.coachusa.com/coachusaassets/files/98/hudsonl.pdf",
            "agency_url": "https://web.coachusa.com/coachusaassets/files/98/hudsonl.pdf"
        },
        "transit_end": {
            "station": "Bear Mountain Inn, Tomkins Cove, NY",
            "mode": "Intercity Bus",
            "hub": "Port Authority Bus Terminal (Gate 405)",
            "details": "Coach USA ShortLine Hudson Bus direct from Bear Mountain Inn back to Port Authority Bus Terminal (~94 min).",
            "url": "https://www.google.com/maps/dir/Port+Authority+Bus+Terminal/Bear+Mountain+Inn/data=!4m5!4m4!2m2!6e0!8j1792932066!3e3",
            "agency_url": "https://web.coachusa.com/coachusaassets/files/98/hudsonl.pdf"
        },
        "waypoints": [
            {"name": "Rt 32 & Smith Clove Rd", "lat": 41.3520, "lon": -74.1220, "dist": 0.0, "elev": 520},
            {"name": "Long Path Trailhead", "lat": 41.3480, "lon": -74.0950, "dist": 1.8, "elev": 790},
            {"name": "West Point Ridge (LP)", "lat": 41.3390, "lon": -74.0620, "dist": 4.4, "elev": 1150},
            {"name": "Torrey Memorial (Long Mtn)", "lat": 41.3250, "lon": -74.0350, "dist": 7.1, "elev": 1060},
            {"name": "Popolopen Gorge", "lat": 41.3195, "lon": -74.0190, "dist": 8.9, "elev": 540},
            {"name": "Anthony Wayne / AT Jct", "lat": 41.3020, "lon": -74.0280, "dist": 10.6, "elev": 820},
            {"name": "Bear Mtn South Shoulder", "lat": 41.3115, "lon": -74.0060, "dist": 12.8, "elev": 1240},
            {"name": "Bear Mountain Inn", "lat": 41.3128, "lon": -73.9889, "dist": 14.7, "elev": 160}
        ]
    },
    {
        "id": 5,
        "date": "Sat. Oct. 31, 2026",
        "title": "Manicure the Nurian Trail: Hike to Tuxedo Station",
        "region": "Harriman State Park, NY",
        "park_url": "https://www.palisadesparks.org/harriman",
        "leader": "Trails Committee Chair (Peter)",
        "pace": "Brisk pace (Trail Maintenance + Hike)",
        "duration": "7–8 hours",
        "distance_mi": 11.5,
        "elevation_gain_ft": 2150,
        "max_elev_ft": 1240,
        "min_elev_ft": 420,
        "route_type": "Point-to-Point Trail Work & Traverse",
        "map_ref": "NY-NJTC Map 119",
        "map_url": "https://scenesfromthetrail.com/tag/nurian-trail/",
        "summary": "Saturday volunteer trail maintenance & hike. Meet at Southfields bus stop on Rte. 17. Volunteers remove blowdowns and trim overgrown vegetation on the Nurian Trail in Harriman State Park, then hike out via White Bar and Ramapo-Dunderberg trails to Tuxedo Station.",
        "trail_sequence": [
            "Southfields Bus Stop (Rte. 17) to Nurian Trail Approach",
            "Nurian Trail (White) — Stahahe High Peak, Green Pond Mtn & Valley of Boulders",
            "Dunning Trail / White Bar Trail (White) Junction",
            "Ramapo-Dunderberg Trail (Red) over Claudius Smith Den",
            "Descent to Tuxedo Train Station"
        ],
        "transit_start": {
            "station": "Southfields, NY (Rt 17 & Old Orange Tpk)",
            "mode": "Intercity Bus",
            "hub": "Port Authority Bus Terminal (Gate 403 / 408)",
            "details": "Coach USA ShortLine Hudson Bus direct from Port Authority Bus Terminal to Rt 17 & Old Orange Tpk, Southfields (~57–64 min).",
            "url": "https://www.google.com/maps/dir/Port+Authority+Bus+Terminal/Rt+17+%26+Old+Orange+Tpk/data=!4m5!4m4!2m2!6e0!8j1792868766!3e3",
            "agency_url": "https://web.coachusa.com/coachusaassets/files/98/hudsonl.pdf"
        },
        "transit_end": {
            "station": "Tuxedo Station, Tuxedo Park, NY",
            "mode": "Commuter Rail",
            "hub": "Penn Station / Secaucus Junction",
            "details": "NJ Transit Port Jervis Line from Tuxedo Station to Secaucus Junction & NY Penn Station (~74–78 min) or Hoboken.",
            "url": "https://www.google.com/maps/dir/Penn+Station/Tuxedo/data=!4m5!4m4!2m2!6e0!8j1792847460!3e3",
            "agency_url": "https://www.njtransit.com/abc_PORT_JERVIS"
        },
        "waypoints": [
            {"name": "Southfields (Rt 17)", "lat": 41.2519, "lon": -74.1772, "dist": 0.0, "elev": 510},
            {"name": "Nurian Trailhead", "lat": 41.2500, "lon": -74.1620, "dist": 1.2, "elev": 740},
            {"name": "Stahahe High Peak", "lat": 41.2460, "lon": -74.1480, "dist": 2.8, "elev": 1180},
            {"name": "Valley of Boulders", "lat": 41.2435, "lon": -74.1320, "dist": 4.5, "elev": 960},
            {"name": "Black Ash Swamp / White Bar", "lat": 41.2395, "lon": -74.1220, "dist": 6.1, "elev": 1050},
            {"name": "Parker Cabin Mtn (R-D)", "lat": 41.2240, "lon": -74.1420, "dist": 8.0, "elev": 1240},
            {"name": "Claudius Smith Den", "lat": 41.2040, "lon": -74.1720, "dist": 9.8, "elev": 1020},
            {"name": "Tuxedo Station", "lat": 41.1942, "lon": -74.1847, "dist": 11.5, "elev": 420}
        ]
    },
    {
        "id": 6,
        "date": "Sat. Nov. 7, 2026",
        "title": "Hewitt to Wanaque",
        "region": "Norvin Green State Forest, NJ",
        "park_url": "https://dep.nj.gov/parksandforests/state-park/norvin-green-state-forest/",
        "leader": "Erik",
        "pace": "Fast pace (Strenuous)",
        "duration": "7–8 hours",
        "distance_mi": 15.6,
        "elevation_gain_ft": 3380,
        "max_elev_ft": 1315,
        "min_elev_ft": 260,
        "route_type": "Point-to-Point Highlands Traverse",
        "map_ref": "NY-NJTC Map 151 (formerly 115)",
        "map_url": "https://www.njhiking.com/best-hikes-in-nj-norvin-green/",
        "summary": "Saturday hike. From Hewitt, follow Highlands and Burnt Meadow trails to Tapawingo Trail over Long Hill to Overlook Rock Trail. Use Manaticut Trail to Manaticut Point, Pink Trail to Camp Wyanokie & Wyanokie Circular, connector to Macopin Trail, then Hewitt-Butler Trail over Wyanokie High Point, Yoo-Hoo Point and Carris Hill. Join Lower and Posts Brook trails past Chikahoki Falls and exit via Doty Road to Wanaque.",
        "trail_sequence": [
            "Hewitt (Lakeside Rd) to Highlands (Teal) & Burnt Meadow Trails",
            "Tapawingo Trail over Long Hill to Overlook Rock & Manaticut Point",
            "Pink Trail, Camp Wyanokie, Wyanokie Circular & Macopin Trail",
            "Hewitt-Butler Trail over Wyanokie High Point (1,145 ft), Yoo-Hoo Point & Carris Hill",
            "Lower & Posts Brook Trails via Chikahoki Falls to Doty Rd / Wanaque"
        ],
        "transit_start": {
            "station": "Hewitt, NJ (Lakeside Rd at Greenwood Lake Tpke)",
            "mode": "Intercity Bus",
            "hub": "Port Authority Bus Terminal (Platform 233_1)",
            "details": "NJ Transit Bus 197 (heading towards Warwick via Willowbrook) from PABT Platform 233_1 to Lakeside Rd N of Greenwood Lake Tpke (~105 min).",
            "url": "https://www.google.com/maps/dir/Port+Authority+Bus+Terminal/Lakeside+Rd+202'+N+of+Greenwood+Lake+Tpke./data=!4m5!4m4!2m2!6e0!8j1792848443!3e3",
            "agency_url": "https://www.njtransit.com/"
        },
        "transit_end": {
            "station": "Wanaque, NJ (Ringwood Ave at Father Hayes Dr)",
            "mode": "Intercity Bus",
            "hub": "Port Authority Bus Terminal (Platform 233_1)",
            "details": "NJ Transit Bus 197 direct from Ringwood Ave at Father Hayes Dr in Wanaque back to Port Authority Bus Terminal (~74 min, departures every 30–60 min).",
            "url": "https://www.google.com/maps/dir/Port+Authority+Bus+Terminal/Ringwood+Ave+at+Father+Hayes+Dr/data=!4m5!4m4!2m2!6e0!8j1792848443!3e3",
            "agency_url": "https://www.njtransit.com/"
        },
        "waypoints": [
            {"name": "Hewitt (Lakeside Rd)", "lat": 41.1480, "lon": -74.3540, "dist": 0.0, "elev": 640},
            {"name": "Long Hill (Tapawingo)", "lat": 41.1320, "lon": -74.3580, "dist": 2.4, "elev": 1120},
            {"name": "Overlook Rock", "lat": 41.1190, "lon": -74.3640, "dist": 4.2, "elev": 1315},
            {"name": "Manaticut Point", "lat": 41.1050, "lon": -74.3590, "dist": 6.1, "elev": 1060},
            {"name": "Camp Wyanokie / Macopin", "lat": 41.0920, "lon": -74.3450, "dist": 8.4, "elev": 780},
            {"name": "Wyanokie High Point", "lat": 41.0764, "lon": -74.3314, "dist": 10.6, "elev": 1145},
            {"name": "Yoo-Hoo Point & Carris Hill", "lat": 41.0680, "lon": -74.3240, "dist": 12.3, "elev": 1080},
            {"name": "Chikahoki Falls", "lat": 41.0620, "lon": -74.3160, "dist": 13.7, "elev": 620},
            {"name": "Wanaque (Ringwood Ave)", "lat": 41.0530, "lon": -74.2920, "dist": 15.6, "elev": 260}
        ]
    },
    {
        "id": 7,
        "date": "Sun. Nov. 15, 2026",
        "title": "Melzingah Reservoir",
        "region": "East Hudson Highlands, NY",
        "park_url": "https://en.wikipedia.org/wiki/Hudson_Highlands_State_Park",
        "leader": "Brian",
        "pace": "Fast pace (Strenuous)",
        "duration": "7–8 hours",
        "distance_mi": 15.5,
        "elevation_gain_ft": 3850,
        "max_elev_ft": 1540,
        "min_elev_ft": 15,
        "route_type": "Point-to-Point Ridge & Reservoir Traverse",
        "map_ref": "NY-NJTC Map 102 (East Hudson)",
        "map_url": "https://www.nynjtc.org/wp-content/uploads/2024/09/so03.pdf",
        "summary": "From Beacon station, follow Walcott Avenue to Casino Trail, ascend to Breakneck Ridge Trail past the Mount Beacon Fire Tower. Join Wilkinson Memorial Trail to Notch Trail, hike to Melzingah Reservoir and circle it. Return via woods roads to Notch Trail, Wilkinson Memorial, Connector to Breakneck Ridge Trail, then Cornish Trail to Rte. 9D and Cold Spring station.",
        "trail_sequence": [
            "Beacon Station along Walcott Ave to Mount Beacon Incline / Casino Trail (Red)",
            "South Beacon Mountain Fire Tower (1,540 ft) on Breakneck Ridge Trail (White)",
            "Wilkinson Memorial Trail (Yellow) & Notch Trail (Blue) to Melzingah Reservoir Loop",
            "Rejoin Wilkinson Memorial & Breakneck Ridge Trail over Sugarloaf North",
            "Cornish Estate Trail (Blue) to NY-9D & Cold Spring Metro-North Station"
        ],
        "transit_start": {
            "station": "Beacon Station, Beacon, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North Hudson Line direct from Grand Central Terminal to Beacon (~89–97 min, departures every 20–30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Beacon/data=!4m5!4m4!2m2!6e0!8j1792848000!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "transit_end": {
            "station": "Cold Spring Station, Cold Spring, NY",
            "mode": "Commuter Rail",
            "hub": "Grand Central Terminal",
            "details": "MTA Metro-North Hudson Line direct from Cold Spring back to Grand Central Terminal (~78–85 min, departures every 20–30 min).",
            "url": "https://www.google.com/maps/dir/Grand+Central/Cold+Spring/data=!4m5!4m4!2m2!6e0!8j1792848000!3e3",
            "agency_url": "https://www.mta.info/agency/metro-north-railroad"
        },
        "waypoints": [
            {"name": "Beacon Station", "lat": 41.5058, "lon": -73.9844, "dist": 0.0, "elev": 15},
            {"name": "Casino Trailhead", "lat": 41.4930, "lon": -73.9590, "dist": 1.9, "elev": 260},
            {"name": "Mt Beacon Fire Tower", "lat": 41.4815, "lon": -73.9445, "dist": 3.8, "elev": 1540},
            {"name": "Scofield Ridge (WMT)", "lat": 41.4720, "lon": -73.9490, "dist": 5.4, "elev": 1360},
            {"name": "Melzingah Reservoir", "lat": 41.4680, "lon": -73.9630, "dist": 7.6, "elev": 680},
            {"name": "Notch / WMT Climb", "lat": 41.4610, "lon": -73.9550, "dist": 9.8, "elev": 1220},
            {"name": "Breakneck Ridge Crest", "lat": 41.4480, "lon": -73.9690, "dist": 12.1, "elev": 1260},
            {"name": "Cornish Estate Ruins", "lat": 41.4360, "lon": -73.9680, "dist": 13.8, "elev": 340},
            {"name": "Cold Spring Station", "lat": 41.4153, "lon": -73.9581, "dist": 15.5, "elev": 20}
        ]
    },
    {
        "id": 8,
        "date": "Sun. Nov. 22, 2026",
        "title": "Long Island Sunken Meadow State Park Exploration: Circular",
        "region": "North Shore, Long Island, NY",
        "park_url": "https://en.wikipedia.org/wiki/Sunken_Meadow_State_Park",
        "leader": "Peter",
        "pace": "Brisk pace (Meet 10:10 AM at Kings Park)",
        "duration": "7–8 hours",
        "distance_mi": 15.0,
        "elevation_gain_ft": 1350,
        "max_elev_ft": 210,
        "min_elev_ft": 5,
        "route_type": "Circular Park, Beach & Bluff Loop",
        "map_ref": "LI Greenbelt Trail / Sunken Meadow SP",
        "map_url": "https://516update.com/p/best-hiking-trails-long-island",
        "summary": "From Kings Park LIRR station (10:10 AM meet), use village streets to join the trail network at the southern end of Sunken Meadow State Park. Cross Sunken Meadow Creek, complete an out-and-back of the Wetland Trail, walk east along the boardwalk and beach to the mouth of the Nissequogue River, recross SM Creek to ascend the bluff and explore the eastern side of the park, then return to Kings Park station.",
        "trail_sequence": [
            "Kings Park LIRR Station (10:10 AM) via Main St to Old Dock Rd Trailhead",
            "Sunken Meadow Creek Crossing & Western Wetland Trail Out-and-Back",
            "Sunken Meadow Boardwalk & Long Island Sound Beach to Nissequogue River Mouth",
            "Long Island Greenbelt Trail Glacial Bluffs (200+ ft) & Cardiac Hill",
            "Eastern Park Woodlands & Return to Kings Park LIRR Station"
        ],
        "transit_start": {
            "station": "Kings Park LIRR Station, NY",
            "mode": "Commuter Rail",
            "hub": "Penn Station / Grand Central Madison",
            "details": "MTA Long Island Rail Road (Port Jefferson Branch via Huntington transfer) from Penn Station to Kings Park (~95–99 min; arrives for 10:10 AM meet).",
            "url": "https://www.google.com/maps/dir/Penn+Station/Kings+Park/data=!4m5!4m4!2m2!6e0!8j1792850220!3e3",
            "agency_url": "https://www.mta.info/agency/long-island-rail-road"
        },
        "transit_end": {
            "station": "Kings Park LIRR Station, NY",
            "mode": "Commuter Rail",
            "hub": "Penn Station / Grand Central Madison",
            "details": "MTA Long Island Rail Road (Port Jefferson Branch via Huntington transfer) from Kings Park back to Penn Station (~95–99 min).",
            "url": "https://www.google.com/maps/dir/Penn+Station/Kings+Park/data=!4m5!4m4!2m2!6e0!8j1792856100!3e3",
            "agency_url": "https://www.mta.info/agency/long-island-rail-road"
        },
        "waypoints": [
            {"name": "Kings Park LIRR", "lat": 40.8836, "lon": -73.2564, "dist": 0.0, "elev": 175},
            {"name": "Southern Park Entry", "lat": 40.8980, "lon": -73.2550, "dist": 1.3, "elev": 60},
            {"name": "Sunken Meadow Creek", "lat": 40.9060, "lon": -73.2580, "dist": 2.4, "elev": 15},
            {"name": "Wetland Trail West End", "lat": 40.9095, "lon": -73.2740, "dist": 4.2, "elev": 25},
            {"name": "Sunken Meadow Boardwalk", "lat": 40.9105, "lon": -73.2520, "dist": 6.2, "elev": 10},
            {"name": "Nissequogue River Mouth", "lat": 40.9080, "lon": -73.2290, "dist": 8.0, "elev": 5},
            {"name": "Eastern Glacial Bluffs", "lat": 40.9045, "lon": -73.2350, "dist": 10.1, "elev": 210},
            {"name": "Cardiac Hill / Greenbelt", "lat": 40.9010, "lon": -73.2490, "dist": 12.4, "elev": 195},
            {"name": "Kings Park LIRR", "lat": 40.8836, "lon": -73.2564, "dist": 15.0, "elev": 175}
        ]
    },
    {
        "id": 9,
        "date": "Sun. Nov. 29, 2026",
        "title": "Tuxedo to Suffern, The Long Way",
        "region": "Harriman State Park, NY",
        "park_url": "https://www.palisadesparks.org/harriman",
        "leader": "Hugues",
        "pace": "Fast pace (Strenuous — Headlamps Required)",
        "duration": "7–8 hours",
        "distance_mi": 17.8,
        "elevation_gain_ft": 3950,
        "max_elev_ft": 1290,
        "min_elev_ft": 300,
        "route_type": "Point-to-Point Multi-Ridge Endurance Traverse",
        "map_ref": "NY-NJTC Map 118",
        "map_url": "https://www.nynjtc.org/",
        "summary": "Strenuous. From Tuxedo station, take Ramapo-Dunderberg Trail to Triangle Trail to White Bar Trail. Cross Rte. 106 to Nurian Trail, right onto RD recrossing 106 to White Cross Trail. Jog on Victory Trail back to White Bar, left on Tuxedo-Mt Ivy to Hillburn-Torne-Sebago, Seven Hills to Kakiat Trail, down to Torne Valley Rd, Pipeline access road, and Suffern-Bear Mountain Trail to Suffern.",
        "trail_sequence": [
            "Tuxedo Station to Ramapo-Dunderberg (Red), Triangle (Yellow) & White Bar (White)",
            "Rte. 106 Crossing, Nurian Trail (White), R-D & White Cross Trail",
            "Victory Trail (Blue), White Bar & Tuxedo-Mt Ivy Trail (Red)",
            "Hillburn-Torne-Sebago (Orange) & Seven Hills Trail (Blue)",
            "Kakiat Trail (White) to Torne Valley Rd, Pipeline & Suffern-Bear Mountain (Yellow) to Suffern"
        ],
        "transit_start": {
            "station": "Tuxedo Station, Tuxedo Park, NY",
            "mode": "Commuter Rail",
            "hub": "Penn Station / Secaucus Junction",
            "details": "NJ Transit Port Jervis Line from NY Penn Station (transfer at Secaucus Junction) to Tuxedo Station (~74–78 min).",
            "url": "https://www.google.com/maps/dir/Penn+Station/Tuxedo/data=!4m5!4m4!2m2!6e0!8j1792847460!3e3",
            "agency_url": "https://www.njtransit.com/abc_PORT_JERVIS"
        },
        "transit_end": {
            "station": "Suffern Station, Suffern, NY",
            "mode": "Commuter Rail",
            "hub": "Penn Station / Secaucus Junction",
            "details": "NJ Transit Main/Bergen/Port Jervis Line from Suffern Station back to Secaucus Junction & NY Penn Station (~60–64 min).",
            "url": "https://www.google.com/maps/dir/Penn+Station/Suffern/data=!4m5!4m4!2m2!6e0!8j1792847460!3e3",
            "agency_url": "https://www.njtransit.com/abc_PORT_JERVIS"
        },
        "waypoints": [
            {"name": "Tuxedo Station", "lat": 41.1942, "lon": -74.1847, "dist": 0.0, "elev": 420},
            {"name": "R-D / Triangle Trail", "lat": 41.2080, "lon": -74.1650, "dist": 2.2, "elev": 1060},
            {"name": "Rte 106 & Nurian Loop", "lat": 41.2290, "lon": -74.1420, "dist": 4.6, "elev": 1190},
            {"name": "White Cross & Victory", "lat": 41.2160, "lon": -74.1310, "dist": 6.8, "elev": 1140},
            {"name": "Tuxedo-Mt Ivy Jct", "lat": 41.1980, "lon": -74.1350, "dist": 9.1, "elev": 980},
            {"name": "HTS & Seven Hills", "lat": 41.1780, "lon": -74.1440, "dist": 11.4, "elev": 1290},
            {"name": "Kakiat Trail Ridge", "lat": 41.1580, "lon": -74.1420, "dist": 13.8, "elev": 1020},
            {"name": "Torne Valley / SBM Trail", "lat": 41.1390, "lon": -74.1460, "dist": 15.8, "elev": 520},
            {"name": "Suffern Station", "lat": 41.1144, "lon": -74.1578, "dist": 17.8, "elev": 300}
        ]
    }
]

with open("artifacts/file_generation/ttl=63d/intermediate/hikes_data.json", "w") as f:
    json.dump(HIKES, f, indent=2)

# Generate high-resolution side-by-side Trail Map & Elevation Profile PNG for each hike for the PDF
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 0.8

for hike in HIKES:
    fig, (ax_map, ax_elev) = plt.subplots(1, 2, figsize=(11.8, 3.35), dpi=180, gridspec_kw={'width_ratios': [1.05, 1.25]})
    fig.patch.set_facecolor('#FAF9F6')

    wps = hike["waypoints"]
    lats = [w["lat"] for w in wps]
    lons = [w["lon"] for w in wps]
    dists = [w["dist"] for w in wps]
    elevs = [w["elev"] for w in wps]

    # Smooth interpolation for visual trail & elevation profile
    t_orig = np.linspace(0, 1, len(wps))
    t_fine = np.linspace(0, 1, 200)
    lons_fine = np.interp(t_fine, t_orig, lons)
    lats_fine = np.interp(t_fine, t_orig, lats)
    dists_fine = np.interp(t_fine, t_orig, dists)
    elevs_fine = np.interp(t_fine, t_orig, elevs)
    # Add subtle natural topographic roughness to elevation profile between waypoints
    np.random.seed(hike["id"] * 42)
    roughness = np.sin(t_fine * 28) * (hike["elevation_gain_ft"] * 0.012) * np.sin(t_fine * np.pi)
    elevs_smooth = np.maximum(hike["min_elev_ft"], elevs_fine + roughness)

    # --- LEFT PANEL: TRAIL ROUTE MAP ---
    ax_map.set_facecolor('#F1F5F2')
    ax_map.grid(True, linestyle='--', alpha=0.45, color='#94A3B8', linewidth=0.6)

    # Pad bounding box
    lon_span = max(max(lons) - min(lons), 0.018)
    lat_span = max(max(lats) - min(lats), 0.018)
    ax_map.set_xlim(min(lons) - lon_span * 0.22, max(lons) + lon_span * 0.22)
    ax_map.set_ylim(min(lats) - lat_span * 0.22, max(lats) + lat_span * 0.22)

    # Plot route shadow and main trail line
    ax_map.plot(lons_fine, lats_fine, color='#1B4332', linewidth=3.5, alpha=0.25, zorder=2)
    ax_map.plot(lons_fine, lats_fine, color='#1B4332', linewidth=2.2, linestyle='-', zorder=3, label='Trail Route')

    # Directional arrows along route
    for idx in [40, 100, 160]:
        dx = lons_fine[idx+2] - lons_fine[idx-2]
        dy = lats_fine[idx+2] - lats_fine[idx-2]
        if abs(dx) + abs(dy) > 1e-5:
            ax_map.annotate('', xy=(lons_fine[idx+1], lats_fine[idx+1]),
                            xytext=(lons_fine[idx-1], lats_fine[idx-1]),
                            arrowprops=dict(arrowstyle='->', color='#D97706', lw=1.6), zorder=4)

    # Plot waypoints
    for i, w in enumerate(wps):
        if i == 0:
            ax_map.scatter(w["lon"], w["lat"], color='#16A34A', s=75, zorder=6, edgecolors='white', linewidth=1.5, label='Start')
        elif i == len(wps) - 1:
            if abs(w["lon"] - wps[0]["lon"]) < 1e-4 and abs(w["lat"] - wps[0]["lat"]) < 1e-4:
                ax_map.scatter(w["lon"], w["lat"], color='#16A34A', s=85, zorder=6, edgecolors='#DC2626', linewidth=1.8, label='Start / Finish')
            else:
                ax_map.scatter(w["lon"], w["lat"], color='#DC2626', s=75, zorder=6, edgecolors='white', linewidth=1.5, label='Finish')
        else:
            ax_map.scatter(w["lon"], w["lat"], color='#D97706', s=32, zorder=5, edgecolors='white', linewidth=0.9)

    # Annotate select non-overlapping waypoints on map
    labeled_coords = []
    for i, w in enumerate(wps):
        is_endpoint = (i == 0 or i == len(wps) - 1)
        is_peak = (w["elev"] == hike["max_elev_ft"])
        if is_endpoint or is_peak or (i % 2 == 0 and i < len(wps) - 1):
            # check distance to existing labels
            too_close = False
            for (lx, ly) in labeled_coords:
                if abs(w["lon"] - lx) < lon_span * 0.16 and abs(w["lat"] - ly) < lat_span * 0.14:
                    too_close = True
                    break
            if not too_close:
                labeled_coords.append((w["lon"], w["lat"]))
                offset_y = 7 if (i % 2 == 0) else -11
                font_w = 'bold' if (is_endpoint or is_peak) else 'normal'
                color_t = '#0F172A' if (is_endpoint or is_peak) else '#334155'
                ax_map.annotate(
                    w["name"],
                    (w["lon"], w["lat"]),
                    textcoords="offset points",
                    xytext=(4, offset_y),
                    fontsize=7.2,
                    fontweight=font_w,
                    color=color_t,
                    bbox=dict(boxstyle='round,pad=0.18', facecolor='white', edgecolor='none', alpha=0.82),
                    zorder=7
                )

    ax_map.set_title(f"Trail Route Map ({hike['route_type']})", fontsize=10, fontweight='bold', color='#1B4332', pad=8)
    ax_map.set_xlabel("Longitude (°W)", fontsize=8, color='#475569')
    ax_map.set_ylabel("Latitude (°N)", fontsize=8, color='#475569')
    ax_map.tick_params(axis='both', labelsize=7, colors='#475569')
    ax_map.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{abs(x):.2f}°W"))
    ax_map.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.2f}°N"))

    # --- RIGHT PANEL: ELEVATION PROFILE CHART ---
    ax_elev.set_facecolor('#FFFFFF')
    ax_elev.grid(True, linestyle=':', alpha=0.55, color='#CBD5E1', linewidth=0.7)

    ax_elev.fill_between(dists_fine, elevs_smooth, hike["min_elev_ft"] * 0.85, color='#1B4332', alpha=0.16, zorder=2)
    ax_elev.plot(dists_fine, elevs_smooth, color='#1B4332', linewidth=2.2, zorder=3)

    # Highlight waypoints on elevation profile
    for i, w in enumerate(wps):
        c = '#16A34A' if i == 0 else ('#DC2626' if i == len(wps) - 1 else '#D97706')
        ax_elev.scatter(w["dist"], w["elev"], color=c, s=30, zorder=5, edgecolors='white', linewidth=0.8)

    # Annotate key peaks/milestones on elevation profile
    peak_idx = int(np.argmax(elevs))
    for i in set([0, peak_idx, len(wps)//2, len(wps)-1]):
        w = wps[i]
        y_off = 8 if w["elev"] < hike["max_elev_ft"] * 0.88 else -13
        ax_elev.annotate(
            f"{w['name']}\n({w['elev']} ft)",
            (w["dist"], w["elev"]),
            textcoords="offset points",
            xytext=(0, y_off),
            ha='center',
            fontsize=6.8,
            fontweight='bold' if i == peak_idx else 'normal',
            color='#1E293B',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#FAF9F6', edgecolor='#CBD5E1', lw=0.5, alpha=0.9),
            zorder=6
        )

    y_min = max(0, hike["min_elev_ft"] - 80)
    y_max = hike["max_elev_ft"] * 1.18 + 60
    ax_elev.set_ylim(y_min, y_max)
    ax_elev.set_xlim(-0.3, hike["distance_mi"] + 0.4)

    ax_elev.set_title(
        f"Elevation Profile — {hike['distance_mi']} mi | +{hike['elevation_gain_ft']:,} ft Gain (Max {hike['max_elev_ft']:,} ft)",
        fontsize=10, fontweight='bold', color='#1B4332', pad=8
    )
    ax_elev.set_xlabel("Cumulative Trail Distance (Miles)", fontsize=8, color='#475569')
    ax_elev.set_ylabel("Elevation (Feet above Sea Level)", fontsize=8, color='#475569')
    ax_elev.tick_params(axis='both', labelsize=7.5, colors='#475569')

    plt.tight_layout(pad=1.4)
    out_img = f"artifacts/file_generation/ttl=63d/intermediate/hike_{hike['id']}_chart.png"
    plt.savefig(out_img, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Generated {out_img}")
