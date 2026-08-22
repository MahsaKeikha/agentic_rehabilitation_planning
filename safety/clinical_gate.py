def allow_patient_specific_use(approved: bool) -> bool:
    """Fail closed unless a qualified human explicitly approved patient-specific use."""
    return approved is True
