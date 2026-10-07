"""Lesson-range check. Classifies a question as IN scope, LATER content (outside this version), or OTHER (not about physical activity coaching)."""

from typing import Any

ALLOWED_TOPICS = """Physical activity: what it is, types and intensities (light, moderate-to-vigorous, strength, balance), walking, cycling, swimming, gardening, active travel.
Lesson 1 (Is it ever too late): the four pillars of a strong exercise program (stability, resistance, cardiovascular, nutrition).\nGuidelines: 150 minutes of moderate-to-vigorous activity a week, strength twice a week, sitting time, the 24-hour movement guidelines.
Benefits in Lessons 1-2 and Science 1: physical health, chronic disease and mortality risk, falls and balance, mood, anxiety and depression, stress, well-being types (physical, cognitive, emotional, self-esteem), cognitive function (attention, memory, executive function), dementia risk, Canadian statistics.
Motivation in general terms (why it matters, how it feels; not low-motivation coping, which is Lesson 6). Lesson 3: social connection, loneliness, belonging, being welcomed, confidence and self-efficacy, the success cycle, small wins, enjoyment and why it matters, feelings and activity.
Science 1 (WHY): the reflective process of M-PAC (instrumental attitude, perceived capability, perceived opportunity, affective judgement, intention), MET, strength-promoting exercise research, physical activity and mood in the short term."""

BANNED_TOPICS = """Anything in Lessons 4-10 or Science 2-3, including: goal setting and goal choice, what makes a goal effective, weekly goals, action planning, coping planning, if-then plans, planning for enjoyment, self-monitoring, social monitoring, activity tracking tools, emotion regulation and coping tools (reframing, attention deployment, response modulation, traffic light, mindfulness, breathing for activity), barriers and 'don't feel like it' strategies, habits, cues, routines as a habit recipe, habit formation, habit disruption, the 66-day question, automaticity, identity (physical activity identity, building blocks, identity agents, active self), values as identity, social appraisals and attachment ties, Acceptance and Commitment Therapy (ACT), defusion, committed action, self-as-context, the regulatory and reflexive processes of M-PAC, the intention-behaviour gap, hedonic motivation, valence and arousal, feeling-state theory, the Science Behind Lessons 4-10, the weekly focus, and what a later week or lesson covers.
Sleep, sleep quality, sleep duration and sleep advice are never in scope for this version. Also out of scope generally: diet, medical advice, and anything not about physical activity (the base prompt rules still apply)."""

ERROR_DECLINES_KEYWORD_HITS = True

SYSTEM_PROMPT = (
    "You classify one user message for a physical activity coach that may only use the lesson content listed as ALLOWED. "
    "Reply with exactly one word.\n"
    "IN: the message's main topic is covered by ALLOWED, or it is a greeting, a short reply, or a question about the coach itself.\n"
    "LATER: the main topic is covered by BANNED (content from lessons or science modules outside this version). "
    "Also LATER if the message asks what a later lesson covers, or asks about a later week.\n"
    "OTHER: the message is not about physical activity or healthy aging.\n\n"
    "ALLOWED:\n" + ALLOWED_TOPICS + "\n\nBANNED:\n" + BANNED_TOPICS
)


def classify_scope(client: Any, model: str, question: str) -> str:
    """Return IN, LATER, OTHER or ERROR. ERROR is returned when the call fails."""
    try:
        completion = client.chat.completions.create(
            model=model,
            temperature=0,
            max_tokens=3,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
        )
        word = (completion.choices[0].message.content or "").strip().upper()
    except Exception:
        return "ERROR"
    if word.startswith("LATER"):
        return "LATER"
    if word.startswith("OTHER"):
        return "OTHER"
    return "IN"
