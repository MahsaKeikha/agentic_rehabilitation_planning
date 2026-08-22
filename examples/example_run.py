from orchestration.orchestrator import run_workflow


if __name__ == "__main__":
    result = run_workflow(
        {
            "goals": [],
            "sessions": [],
            "progress": {},
            "flags": [],
            "human_approved": False,
        }
    )
    print(result)
