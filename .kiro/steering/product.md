# Product: NAS — National Address System

A national address standardization system for Malaysia. Government agencies submit raw address files (CSV, Excel, JSON) through a web portal or API. An ETL pipeline normalizes, parses, validates, and enriches addresses using reference lookups and PostGIS spatial boundaries, then loads canonical rows into a PostGIS database and OpenSearch index that serves autocomplete and lookup APIs.

## Core Capabilities

- File ingestion via direct upload or S3 multipart upload
- Address parsing: extracts premise_no, lot_no, street_name, locality, postcode, state, district, mukim
- Enrichment: postcode-based locality/state lookup, fuzzy district/mukim matching (Levenshtein), spatial boundary assignment via PostGIS
- Validation: splits rows into success/failed based on confidence score, postcode conflicts, missing fields
- Stable identity: each canonical address gets a NASKod (e.g. `NAS-KL-01-R000123`) that persists through admin changes
- Autocomplete search via OpenSearch
- Admin APIs for managing lookup tables and boundary geometries
- Multi-agency tenancy with API key and JWT authentication

## Domain Context

- Addresses are Malaysian; field names may be in Malay (alamat, negeri, daerah, mukim, poskod, bandar)
- Administrative hierarchy: State → District → Mukim → Locality/Sublocality
- Boundary layers: state, district, mukim, postcode, PBT (local authority)
- Reference data lives in the `nas_lookup` schema; application data in the `nas` schema
