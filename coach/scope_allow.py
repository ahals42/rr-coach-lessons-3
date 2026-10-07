"""In-scope topic patterns. A match skips the scope classifier; decline patterns still run first."""

import re

ALLOW_PATTERNS = [re.compile(p) for p in [
    '(?i)\\bstretch\\w*',
    '(?i)\\bmoving\\b',
    '(?i)\\bevery move\\b',
    '(?i)\\b(physical|physically)\\s+(activity|activities|active|fitness)\\b',
    '(?i)\\b(exercise|exercises|exercising|workouts?)\\b',
    '(?i)\\b(get|be|stay|getting|being|staying)\\s+(more\\s+)?active\\b',
    '(?i)\\bhow (much|many)\\s+(exercise|activity|minutes|physical activity)\\b',
    '(?i)\\b(150 minutes|two and a half hours|2\\.5 hours)\\b',
    '(?i)\\b(guidelines?|recommendations?)\\b.{0,30}\\b(activity|exercise|moving|movement|active)\\b',
    '(?i)\\bmovement\\b',
    '(?i)\\bmove often\\b',
    '(?i)\\bevery move counts?\\b',
    '(?i)\\b(sitting|sedentary|sit all day|too much sitting)\\b',
    '(?i)\\b(light|moderate|vigorous|brisk|easy|intense)\\s+(activity|activities|intensity|exercise|walking|effort|pace)\\b',
    '(?i)\\b(talk test|out of breath|heart pumping|breathe harder)\\b',
    '(?i)\\b(strength|strengthening|muscles?|bone[- ]strengthening)\\b',
    '(?i)\\b(balance|falls?|falling|fall[- ]prevention|steady on my feet)\\b',
    '(?i)\\b(walk|walks|walking|cycle|cycling|biking|bike|swim|swimming|gardening|dance|dancing|yoga|tai chi|pickleball|golf|hiking)\\b',
    '(?i)\\b(four pillars|is it (ever )?too late)\\b',
    '(?i)\\b(mood|moods|anxiety|anxious|depression|depressed|stress|stressed|worry|worried)\\b',
    '(?i)\\bfeel(ing|s)?\\s+(better|happier|brighter|sharper|calmer|down)\\b',
    '(?i)\\b(brain|memory|memories|attention|concentration|dementia|cognitive|cognition|think(ing)? (sharper|clearer))\\b',
    '(?i)\\b(health|healthy aging|healthier|heart|chronic (disease|conditions?)|diabetes|blood pressure|mortality|live longer|life expectancy)\\b',
    '(?i)\\b(well-?being|life satisfaction|quality of life|self-esteem)\\b',
    '(?i)\\b(retire|retired|retirement|retiree|retirees)\\b',
    '(?i)\\b(lonely|loneliness|isolat\\w*|alone|friends?|friendships?|social|companions?|neighbou?rs?|community|belong\\w*|meet(ing)? (new )?people|welcom\\w*)\\b',
    '(?i)\\b(confiden(ce|t)|self-?efficacy|believe (i|you) can|capable|success cycle|small wins?)\\b',
    '(?i)\\b(enjoy|enjoys|enjoyed|enjoyment|enjoyable|fun|pleasure|pleasant)\\b',
    '(?i)\\bmotivat\\w*\\b',
    '(?i)\\bwhy (it|this|being active|moving|staying active|physical activity|exercise) (still )?matters?\\b',
    '(?i)\\bfeelings? (and|about|from) (physical )?(activity|exercise|moving|walking)\\b',
    '(?i)\\b(canad(a|ian|ians)|statistics|stats)\\b',
    '(?i)\\b(perceived (capability|opportunit(y|ies))|instrumental attitude|affective judgements?|reflective process|M-PAC|METs?)\\b',
    '(?i)\\b(framingham|cardiovascular|cardiorespiratory|heart disease)\\b',
]]


def is_allowed(text: str) -> bool:
    return any(p.search(text or '') for p in ALLOW_PATTERNS)
