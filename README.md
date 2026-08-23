# F60 Agentic Rehabilitation Planning

**Maturity:** L3 Gold Standard  
**Version:** 1.0

A six-agent reference architecture for governed rehabilitation planning support across goal organization, session planning, progress tracking, equipment and environment review, escalation, and qualified human approval.

F60 is designed as a reusable engineering reference for rehabilitation workflows in which physical therapy, occupational therapy, mobility support, assistive devices, home or facility environments, longitudinal observations, and clinical safety constraints must remain coordinated. The system supports organization and decision support around an existing clinician-directed rehabilitation plan. It does not diagnose, prescribe treatment, independently change therapy intensity, grant mobility clearance, or replace rehabilitation professionals.

Patient-specific use is fail-closed. Required governance evidence must be present before the workflow can be considered review-ready, and final patient-specific authority remains with an appropriately qualified human.

## Why rehabilitation planning needs explicit governance

Rehabilitation is inherently longitudinal. A plan that was appropriate last week may no longer be appropriate after a fall, surgery, new pain, new neurological symptoms, equipment change, medication change, hospitalization, change in weight-bearing status, or decline in mobility.

A useful rehabilitation support architecture therefore has to coordinate several different questions:

```text
clinician-confirmed rehabilitation goals
                |
                v
        Goal Organizer Agent
                |
                v
       Session Planner Agent
                |
                v
      Progress Tracker Agent
                |
                v
 Equipment & Environment Agent
                |
                v
        Escalation Agent
                |
                v
      Human Reviewer Agent
                |
                v
 qualified rehabilitation decision
```

The agents do not form an autonomous therapy team. They organize evidence so a qualified clinician can review the plan with clearer traceability and fewer missed operational or safety conditions.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Goal Organizer Agent | Organizes clinician-confirmed goals and measurable objectives | What outcomes are being pursued, and are they explicitly confirmed by the treating team? |
| Session Planner Agent | Structures sessions within approved scope and progression limits | What activities are already authorized, and how should they be organized without inventing new treatment? |
| Progress Tracker Agent | Tracks longitudinal measures, tolerance, and goal status | What changed over time, and is the observed trend reliable enough to review? |
| Equipment & Environment Agent | Reviews assistive devices and environmental safety considerations | Are equipment, setup, transfer conditions, and environment compatible with the current plan? |
| Escalation Agent | Detects red flags and conditions that require qualified review | Does the workflow need to stop, pause progression, or escalate? |
| Human Reviewer Agent | Enforces the qualified-human authority boundary | Has an authorized rehabilitation professional reviewed and approved the patient-specific plan? |

## Repository structure

```text
AGENTS/
├── goal_organizer_agent.py
├── session_planner_agent.py
├── progress_tracker_agent.py
├── equipment_environment_agent.py
├── escalation_agent.py
└── human_reviewer_agent.py

SKILLS/
├── goal_organization.py
├── session_planning.py
├── progress_tracking.py
├── equipment_environment_review.py
└── escalation_review.py

TOOLS/
├── goal_tracker.py
├── session_schedule_tool.py
├── progress_metrics.py
├── environment_checklist.py
└── escalation_router.py

benchmarks/
├── benchmark.py
└── RESULTS.md

evals/
├── evaluator.py
└── heldout_suite.py

orchestration/
memory/
observability/
schemas/
prompts/
config/
safety/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The design intentionally separates reasoning agents from deterministic tracking, validation, safety, state, and evaluation layers.

## Goal organization

The Goal Organizer Agent starts from goals that are already established or confirmed by the appropriate rehabilitation professional.

A goal record can include:

```text
goal_id
patient_reference
discipline
functional_domain
baseline
objective
target_measure
target_date
clinician_confirmation
status
last_reviewed
```

Examples of functional domains may include mobility, transfers, gait, balance, strength, range of motion, activities of daily living, endurance, upper-extremity function, communication, cognition, or participation depending on the clinical discipline and plan.

The system should not invent goals solely from diagnosis labels or informal observations.

`TOOLS/goal_tracker.py` provides the reference structure for maintaining goal state.

## Session planning

The Session Planner Agent organizes activities that are already inside the approved rehabilitation scope.

A session plan can include:

- approved goal references
- scheduled activities
- duration or sequence where already authorized
- required assistive devices
- supervision level
- environmental setup
- known precautions
- progression ceiling
- documentation expectations

`TOOLS/session_schedule_tool.py` provides deterministic support for session organization.

### Treatment authority boundary

F60 must not autonomously:

- prescribe a new therapeutic exercise program
- increase resistance or intensity without an approved progression rule
- change weight-bearing status
- discontinue an assistive device
- advance a patient from walker to cane or unassisted ambulation
- alter transfer assistance level
- introduce unsupervised balance training
- clear a patient for stairs, driving, work, or independent mobility
- recommend return to sport or other high-risk activity as clinical clearance

Those decisions require qualified professional assessment.

## Progress tracking

The Progress Tracker Agent organizes longitudinal evidence without converting observations into unsupported clinical conclusions.

`TOOLS/progress_metrics.py` can represent measures such as:

```text
measure_id
metric_name
value
unit
timestamp
source
assessor
context
assistive_device
support_level
quality_flag
```

Useful observations can include clinician-recorded or otherwise authorized measures related to:

- mobility distance
- transfer assistance
- gait speed
- repetition counts
- task completion
- range-of-motion measurements
- balance measures
- endurance measures
- pain or exertion ratings
- session tolerance
- functional-assistance level

A change in a metric is not by itself evidence that treatment should progress.

## Measurement provenance

Rehabilitation measurements are context-sensitive. Ten meters walked with a walker and close supervision is not equivalent to ten meters walked independently.

Production implementations should preserve:

- who collected the measure
- device or equipment used
- assistance level
- environmental context
- protocol or test method
- timestamp
- whether the measure was clinician-entered, patient-reported, caregiver-reported, or sensor-derived

The system should not combine incomparable measurements into a false trend.

## Equipment and assistive-device review

The Equipment & Environment Agent supports structured review of mobility and rehabilitation equipment.

Examples include:

- walkers
- canes
- wheelchairs
- transfer devices
- shower chairs
- grab bars
- orthoses
- braces
- gait belts
- lift systems
- exercise equipment
- adaptive utensils
- home modifications

The agent can check whether an expected device is documented and whether a setup review is complete. It cannot independently fit, prescribe, discontinue, or clinically approve an assistive device.

## Environment safety

`TOOLS/environment_checklist.py` provides a deterministic reference checklist for environmental factors.

Depending on the use case, review items can include:

- floor surface
- loose rugs
- clutter
- lighting
- stairs
- handrails
- bathroom access
- bed height
- chair height
- transfer space
- wheelchair clearance
- device charging or storage
- trip hazards
- caregiver access

Environmental review should be adapted to the real setting and the patient's current functional status.

## Fall-risk safeguards

Fall risk is a cross-cutting safety concern rather than a single score.

F60 requires explicit fall-risk safeguards before patient-specific progression. Relevant evidence can include:

- current mobility status
- recent falls
- transfer assistance
- balance status
- assistive-device status
- supervision requirements
- environment hazards
- orthostatic or other clinician-identified precautions

A system-generated low-risk label should never override clinician-identified fall precautions.

## Contraindications and precautions

Patient-specific workflow must include a current contraindication and precaution review.

Examples may involve clinician-documented restrictions related to:

- surgery
- weight bearing
- fractures
- wounds
- cardiovascular status
- neurological status
- pain
- dizziness
- orthostasis
- fatigue
- infection
- implanted devices
- lines or tubes
- activity restrictions

F60 organizes these restrictions. It does not infer that a restriction has expired merely because time has passed.

## Pain and symptom review

Pain, unusual fatigue, dizziness, shortness of breath, weakness, acute neurological change, or other symptoms can change whether a planned rehabilitation activity should proceed.

F60 therefore requires symptom review as part of patient-specific readiness.

The system can surface a new or worsening symptom and route it for review. It must not independently diagnose the cause or reassure the user that a symptom is safe.

## Acute escalation

The Escalation Agent is intended to fail closed on acute or potentially unsafe conditions.

Examples include:

- new fall with possible injury
- new severe or unexplained pain
- new neurological deficit
- sudden functional decline
- loss of consciousness
- acute breathing difficulty
- chest symptoms
- new inability to bear weight
- equipment failure creating immediate risk
- contradiction between the current plan and a new medical restriction

Institutional emergency procedures and clinical escalation pathways remain authoritative.

`TOOLS/escalation_router.py` provides the routing abstraction.

## Therapy-scope confirmation

Different disciplines have different scopes, and scope also varies by licensure, jurisdiction, institution, and plan of care.

A production implementation should identify the responsible discipline and authorized reviewer, for example:

- physical therapist
- occupational therapist
- speech-language pathologist
- rehabilitation physician
- rehabilitation nurse
- other qualified clinician

The system should not treat all rehabilitation decisions as interchangeable.

## Progression limits

One of the most important F60 controls is the prohibition on autonomous progression.

A progression rule should be explicit, bounded, clinician-approved, and linked to measurable criteria when progression is allowed at all.

For example, a structured rule can represent:

```text
progression_rule_id
activity_id
current_level
maximum_authorized_level
criteria
stop_conditions
approving_clinician
approval_date
```

If the requested change exceeds the authorized progression ceiling, F60 should return a review-required state rather than generating a new treatment plan.

## Documentation completeness

Rehabilitation support is only as useful as the evidence attached to it.

A patient-specific plan should preserve, as applicable:

- patient identity
- current plan version
- goal confirmation
- responsible clinician
- restrictions and precautions
- current mobility status
- assistive-device state
- session history
- progress measures
- pain/symptom observations
- fall events
- environment review
- escalation history
- human approval state

Missing critical documentation should block the workflow from appearing complete.

## Privacy and authorization

Rehabilitation records can contain sensitive health and functional information.

Production systems should implement:

- authenticated identity
- authorized patient access
- role-based or attribute-based access
- minimum-necessary data use
- encryption
- audit logging
- retention controls
- consent or authorization where applicable

Test and benchmark environments should use synthetic or appropriately governed data.

## Shared state and provenance

The `memory/` layer preserves structured workflow evidence between agents.

Useful state includes:

```text
patient_reference
goals
plan_version
restrictions
mobility_state
equipment_state
session_state
progress_metrics
symptoms
fall_risk_state
environment_state
escalations
unresolved_questions
human_review_state
```

Updates should preserve history rather than overwriting previous measurements or restrictions without traceability.

## Observability

The `observability/` layer supports workflow-level tracing.

Useful metrics include:

- incomplete-governance-gate count
- missing-goal-confirmation count
- contraindication-review failures
- escalation count
- new-fall events
- assistive-device review gaps
- environment-checklist failures
- attempted unauthorized progression
- missing-human-approval count
- data-quality issues

Workflow telemetry should be used for system reliability and safety review, not as a substitute for clinical outcomes research.

## Fail-closed governance

F60 requires the following patient-specific governance evidence before a plan can be considered review-ready:

- patient identity verification
- clinician-confirmed rehabilitation goals
- contraindication and precaution review
- fall-risk safeguards
- current mobility status
- assistive-device safety review
- current pain and symptom review
- therapy-scope confirmation
- explicit progression limits
- environment safety review
- complete required documentation
- privacy and authorization controls
- an escalation path
- explicit qualified-human approval

Potential failure states include:

```text
PATIENT IDENTITY UNVERIFIED
GOALS NOT CLINICIAN CONFIRMED
CONTRAINDICATION REVIEW REQUIRED
FALL RISK SAFEGUARDS INCOMPLETE
MOBILITY STATUS UNKNOWN
ASSISTIVE DEVICE REVIEW REQUIRED
PAIN/SYMPTOM REVIEW REQUIRED
THERAPY SCOPE UNCONFIRMED
PROGRESSION LIMIT NOT DEFINED
ENVIRONMENT REVIEW INCOMPLETE
DOCUMENTATION INCOMPLETE
PRIVACY/AUTHORIZATION INCOMPLETE
ESCALATION REQUIRED
QUALIFIED HUMAN APPROVAL REQUIRED
```

A human approval flag does not erase an unresolved blocker. The underlying issue must be resolved or explicitly handled under the applicable clinical process.

## Human authority boundary

F60 must not independently:

- diagnose a rehabilitation condition
- prescribe treatment
- change a plan of care
- progress therapy beyond approved rules
- assign or remove clinical precautions
- determine weight-bearing status
- determine fall-risk clearance
- approve independent ambulation
- clear transfers or stairs
- change assistive-device recommendations
- certify medical necessity
- determine discharge readiness
- replace emergency response

Final decisions remain with the appropriate qualified clinicians and care organization.

## End-to-end reference workflow

A typical patient-specific workflow follows this sequence:

1. Verify patient identity and authorization.
2. Load the current clinician-confirmed rehabilitation goals.
3. Confirm discipline and responsible reviewer.
4. Review contraindications, precautions, and current mobility state.
5. Review pain, symptoms, falls, and other new events.
6. Confirm assistive devices and environmental setup.
7. Organize an in-scope session using only approved activities and progression rules.
8. Record observations and progress measures with provenance.
9. Compare new evidence with prior measurements without overstating trend certainty.
10. Route red flags or conflicting evidence for escalation.
11. Verify all fail-closed governance gates.
12. Require explicit qualified-human approval for patient-specific plan changes or progression.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run static checks and tests:

```bash
ruff check .
python -m pytest -q
```

Run the held-out evaluation:

```bash
python evals/heldout_suite.py
```

Run the example:

```bash
python examples/example_run.py
```

Run the main entry point:

```bash
python run.py
```

## Verification gates

CI runs across Python 3.10, 3.11, and 3.12 and executes:

```bash
ruff check .
python -m pytest -q
python evals/heldout_suite.py
python examples/example_run.py
python run.py
```

The test suite verifies fail-closed governance, every required gate, acute red-flag escalation, prohibition of autonomous treatment progression, prohibition of new treatment prescription, mandatory qualified-human approval, specialist coverage, approval-contract consistency, patient-specific fail-closed behavior, and absence of autonomous treatment authority.

## Benchmarks and evaluation

The repository includes deterministic benchmark and held-out evaluation paths under:

```text
benchmarks/benchmark.py
benchmarks/RESULTS.md
evals/evaluator.py
evals/heldout_suite.py
```

Useful evaluation dimensions include:

- identity-gate enforcement
- clinician-goal confirmation
- contraindication detection
- fall-risk safeguard enforcement
- mobility-status completeness
- assistive-device review
- pain and symptom review
- therapy-scope enforcement
- progression-limit enforcement
- environment-safety detection
- documentation completeness
- escalation behavior
- human-approval enforcement

Strong cases should intentionally include unsafe requests such as autonomous therapy progression, undocumented mobility changes, missing clinician approval, acute red flags, or conflicts between equipment state and the rehabilitation plan.

## L3 Gold Standard

F60 is labeled **L3 Gold Standard** based on its explicit specialist-agent architecture, deterministic tools, patient-specific fail-closed controls, qualified-human gate, safety tests, held-out evaluation, observability, examples, and multi-version CI.

This maturity designation describes the repository architecture and its internal verification criteria. It is not clinical validation, medical-device authorization, professional licensure, reimbursement approval, or evidence that the system can autonomously manage rehabilitation.

## Extending F60

Common extensions include:

- EHR integration
- rehabilitation documentation systems
- PT/OT/SLP scheduling systems
- home-health platforms
- wearable sensor integration
- gait and mobility sensors
- smart walkers or wheelchairs
- fall-detection systems
- remote therapeutic monitoring platforms
- patient-reported outcome systems
- assistive-device inventories
- home-environment assessment tools
- caregiver portals
- rehabilitation dashboards

New integrations should preserve patient identity, provenance, current-plan versioning, clinician authority, safety gates, least privilege, and explicit escalation paths.

## Example applications

F60 can serve as a reference architecture for:

- inpatient rehabilitation workflow support
- outpatient rehabilitation coordination
- home-health rehabilitation
- post-surgical rehabilitation tracking
- mobility and fall-risk programs
- assistive-device follow-up
- caregiver-supported rehabilitation routines
- remote rehabilitation research
- rehabilitation engineering education

Higher-risk or regulated applications require additional clinical, quality, regulatory, cybersecurity, and human-factors controls.

## Design principles

1. Start from clinician-confirmed goals, not inferred treatment objectives.
2. Keep session organization separate from treatment prescription.
3. Preserve measurement context and provenance.
4. Treat current mobility and fall risk as dynamic safety state.
5. Review assistive devices and the physical environment together.
6. Define progression ceilings explicitly.
7. Escalate new symptoms, falls, and conflicting restrictions.
8. Preserve privacy and authorization boundaries.
9. Fail closed when patient-specific evidence is incomplete.
10. Keep rehabilitation decisions with qualified humans.

## Repository identity

- Library ID: **F60**
- Repository: **agentic_rehabilitation_planning**
- Standard: **L3 Gold Standard**
- Version: **1.0**

## Documentation

Additional architecture documentation is available in `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository's citation metadata when referencing this implementation. The repository is intended to function as a reusable technical reference for governed multi-agent rehabilitation architecture.

## Responsible use

Use F60 to support rehabilitation workflow organization, evidence tracking, environment review, progress documentation, and governed escalation. Validate every patient-specific workflow against the current plan of care, current clinical status, applicable professional scope, and real institutional policy. Final treatment, progression, equipment, mobility, discharge, and emergency decisions remain with appropriately qualified and authorized professionals.