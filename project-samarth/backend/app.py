from fastapi import FastAPI
from pydantic import BaseModel
from query_planner import plan
from assemble import assemble_compare

app = FastAPI()

class Query(BaseModel):
    question: str

# very small LLM-free parser: naive extraction for demo
def naive_parse(question: str):
    q = question.lower()
    # this is minimal: expects "state1 and state2" and a year range like 2010-2019
    import re
    states = re.findall(r"([A-Za-z]+) and ([A-Za-z]+)", question)
    years = re.findall(r"(\d{4})\s*[-to]+\s*(\d{4})", question)
    if states:
        s1, s2 = states[0]
    else:
        s1 = s2 = None
    if years:
        y1, y2 = map(int, years[0])
    else:
        y1, y2 = 2018, 2019
    return {'intent':'compare_rainfall_and_crops', 'state_x':s1, 'state_y':s2, 'year_from':y1, 'year_to':y2}

@app.post('/ask')
async def ask(q: Query):
    parsed = naive_parse(q.question)
    plan1 = plan(parsed)
    # only supporting compare intent in this minimal prototype
    result = assemble_compare([parsed['state_x'], parsed['state_y']], parsed['year_from'], parsed['year_to'], topn=3)
    # simple textual answer
    text = ''
    for s, v in result['rainfall'].items():
        text += f"Average annual rainfall ({parsed['year_from']}-{parsed['year_to']}) in {s}: {v['avg_mm']} mm. Source(s): {v['source']}\n"
    for s, top in result['topcrops'].items():
        text += f"Top crops in {s} (by volume): " + ', '.join([f"{t['crop']} ({t['tons']} t)" for t in top]) + "\n"
    return {'answer': text, 'raw': result}
