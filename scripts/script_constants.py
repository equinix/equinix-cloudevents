import re

RELEASED = "released"
PREVIEW = "preview"

# Schemas live in versioned directories (v1, v2, ...). Anything else under
# jsonschema/ (catalog.json, sloCategories.json, examples, ...) is not a schema.
VERSION_DIR = re.compile(r'^v\d+$')

# Versions published to catalog.json and the README event catalog. Schemas in
# other version directories are still validated, just not published.
PUBLISHED_VERSIONS = {"v2"}

EVENTS = "cloudeventTypes"
METRICS = "metricNames"
ALERTS = "alertNames"

README = {
    EVENTS: "Events",
    METRICS: "Metrics",
    ALERTS: "Alerts"    
}
