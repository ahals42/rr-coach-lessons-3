"""Lesson-range decline patterns. Any match gets the out-of-range decline."""

import re

DECLINE_PATTERNS = [re.compile(p) for p in [
    '(?i)\\b(sleep|sleeping|insomnia|bedtime|naps?)\\b',
    '(?i)\\bhabits?\\b',
    '(?i)\\b(cues?|instigation|execution habits?|if[- ]then|implementation intentions?)\\b',
    '(?i)\\b(cue|trigger)s?\\b.{0,20}\\b(routine|habit|repeat|behaviou?r)\\b',
    '(?i)\\bcue,?\\s*routine,?\\s*(and\\s+)?repeat\\b',
    '(?i)\\b(66|sixty[- ]six)[- ]?days?\\b',
    '(?i)\\bhow (long|many (days|weeks)) (does it|do i|will it|would it|to) (take|form|make|become)\\b',
    '(?i)\\b(automaticity|automatic(ally)?|on autopilot|second nature|without (having to )?think(ing)? about it)\\b',
    '(?i)\\b(goals?|goal[- ]setting|smart goals?)\\b',
    '(?i)\\b(action|coping|back-?up|contingency)\\s+plan\\w*\\b',
    '(?i)\\bplan(ning)? (ahead|for (enjoyment|enjoying|when|bad|rainy|busy|days?))\\b',
    "(?i)\\bwhat (do|should) i (do|try) (if|when) (i )?(miss|skip|can'?t|cannot|forget|get sick)\\b",
    '(?i)\\b(self[- ]?monitor\\w*|social monitoring|monitor(ing)? (my |your |the )?(activity|steps|progress|behaviou?r|walks))\\b',
    '(?i)\\b(track\\w*|log\\w*|journal\\w*|record\\w*)\\s+(my |your |the |their )?(steps|activity|progress|sessions|walks|workouts?|minutes|exercise|days)\\b',
    '(?i)\\b(pedometer|step counter|fitness tracker|activity tracker|wearable|fitbit|apple watch|activity journal|fridge calendar|pathverse|thermostat|garden club)\\b',
    '(?i)\\b(stay(ing)?|keep(ing)?|get(ting)?|back|on)\\s+(on\\s+)?track\\b',
    '(?i)\\bcheck(ing)? off\\b',
    "(?i)\\b(can'?t|cannot) be (bothered|arsed)\\b",
    '(?i)\\bfeel(ing)? like (quitting|giving up|skipping|stopping)\\b',
    '(?i)\\b(quit|quitting|give up|giving up|keep at it|keep it up|stick with it|sticking with it|stick to it|sticking to it|push myself|pushing myself|lazy|procrastinat\\w*|slipp\\w*|fall(ing)? off|restart\\w*)\\b',
    '(?i)\\bmotivat\\w*\\s+(myself|yourself|on\\s+(low|bad|hard|tough)\\s+days)\\b',
    "(?i)\\b(don'?t|do not|dont)\\s+feel(ing)?\\s+(like|up to)\\b",
    '(?i)\\b(?:emotion|emotional)\\s+regulat\\w*\\b|\\bregulat\\w*\\s+(?:my |your )?(?:emotions?|feelings?|mood)\\b',
    '(?i)\\b(traffic light|red,? amber,? (and )?green|mindful\\w*|breathing exercises?|reframe\\w*|reframing|self[- ]talk|distract\\w*|distraction|attention deployment|cognitive change|response modulation)\\b',
    '(?i)\\b(barriers?|obstacles?|setbacks?|missed days?|intention[- ]behaviou?r gap|intention)\\b',
    '(?i)\\b(regulatory|reflexive)\\s+process\\b|\\breflexive\\b',
    '(?i)\\breactive regulation\\b',
    '(?i)\\bidentit(y|ies)\\b',
    '(?i)\\b(active self|active person|someone who (moves|is active|exercises|walks))\\b',
    '(?i)\\b(self-?(image|view|perception|concept|theor(y|ies)|verification)|see (myself|yourself) as)\\b',
    '(?i)\\b(possible (future )?(active )?self|future (active )?self|building blocks?|behavio(u)?ral blocks?|cognitive blocks?|social blocks?|social identit\\w*|identity agents?|attachment ties?|social appraisals?|imaginal)\\b',
    '(?i)\\bvalues? (as|are|define|shape|guide|drive|make up) (who|my identity|your identity|me|you)\\b',
    '(?i)\\b(acceptance (and|&) commitment|ACT therapy|defusion|defuse|committed action|self-as-context|psychological flexibility|present[- ]moment awareness)\\b',
    '(?-i:\\bACT\\b)',
    '(?i)\\b(valence|arousal|hedonic|feeling states?|affect (theory|research|states?))\\b',
    '(?i)\\b(lessons? ?(4|5|6|7|8|9|10)|science ?(2|3)|weeks? ?(4|5|6|7|8|9|10))\\b',
    '(?i)\\bsleep\\b',
]]

# Concept-specific phrasings that are declined outright, without asking the classifier.
HARD_DECLINE_PATTERNS = [re.compile(p) for p in [
    '(?i)\\bsleep\\b',
    '(?i)\\bemotion(al)? regulat\\w*|\\bregulat\\w* (my |your )?(emotions?|feelings?|mood)\\b',
    '(?i)\\bplan\\w*\\b.{0,30}\\b(when|where|for (my|the|a) week|something fun|fun|enjoy)\\b|\\bmake (me )?a plan\\b',
    '(?i)\\b(getting|get|gets|in the way|miss\\w*)\\b.{0,25}\\b(rain\\w*|way|my walk|my exercise|my plan)\\b|\\bmiss(ed|ing)? my walk\\b',
    '(?i)\\bcoping (tools?|strateg\\w*|plan\\w*)\\b|\\bcalm (down|myself)\\b.{0,30}\\b(workout|exercis\\w*|walk)\\b|\\bstress (tools?|management)\\b',
    '(?i)\\bthermostat\\b',
    '(?i)\\b(pleasure|hedonic)\\b.{0,30}\\b(motivat\\w*|exercis\\w*|activ\\w*|walk\\w*)\\b|\\bis pleasure a motivator\\b',
    '(?i)\\b(life|move|moving|transition)\\w*\\b.{0,25}\\b(keep|stay|still)\\b.{0,15}\\b(exercis\\w*|active|moving)\\b|\\bafter a move\\b|\\bwhen my life changes\\b',
    '(?i)\\btrack\\w*\\b.{0,30}\\b(friends?|others?|people)\\b.{0,20}\\bactive\\b',
    '(?i)\\bkeep (moving|going|exercising)\\b.{0,30}\\bnot (motivated|feeling it)\\b|\\bnot motivated\\b',

]]
