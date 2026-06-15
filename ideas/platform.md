---
type: ideas-log
domain: platform
---

# Platform Design Ideas Log

Learner-experience insights and design principles that surface during study. Captures the
"I would want this to work differently" observations in real time. No architecture specifics
here — this is a public research record. Implementation decisions go to the H&C hub.

---

### [2026-06-14 ~19:55] Unstructured online programs vs. H&C — the "read more" failure mode

**Domain:** platform
**Source:** M01 session calibration — prior linear algebra failure history
**Trigger:** Subject described being told "spend more time reading" as the only support offered by an online program instructor when requesting help with a concept

The failure mode: a learner with high conceptual motivation but format-incompatibility asks for help. The response is undifferentiated — more of the same format that isn't working, no diagnosis of what specifically isn't landing, no alternative representation offered.

The H&C design implication: when a learner signals confusion or requests help, "show more content" is never the right first response. The first response is diagnostic: what isn't landing and why? Is it the formalism density? The abstraction level? Missing prerequisite? The absence of a concrete example? The design question isn't "how much content?" but "which representation and at what altitude?"

**Follow-up needed:** yes — this is a direct design principle for the help/scaffolding system; track in hub when H&C architecture work resumes
**Related:** adaptive scaffolding design, T03 (H&C Architecture Spec), learner-profile-variables.md

---
