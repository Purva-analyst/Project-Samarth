# very small planner: decides datasets to query based on parsed intent

def plan(parsed):
    intent = parsed.get('intent')
    if intent == 'compare_rainfall_and_crops':
        return ['imd_rainfall_norm', 'crop_production_norm']
    return []
