from pathlib import Path

def compose_prompt(
    configuration: str,
    prompt_dir: Path = Path("../prompts"),
    input_file: Path = None,
    placeholder: str = "{input}"
) -> str:
    """
    Compose a prompt by selecting a template based on configuration
    and injecting the input content.

    configuration: "BASELINE" | "GUIDED"
    prompt_dir: directory containing prompt templates
    input_file: file containing the input to inject
    placeholder: placeholder used inside the prompt template
    """

    configuration = configuration.upper()
    if configuration not in {"BASELINE", "GUIDED"}:
        raise ValueError(f"Invalid configuration: {configuration}")

    prompt_file = {
        "BASELINE": prompt_dir / "baseline_prompt.txt",
        "GUIDED": prompt_dir / "guided_prompt.txt"
    }[configuration]

    if not prompt_file.exists():
        raise FileNotFoundError(prompt_file)

    if not input_file.exists():
        raise FileNotFoundError(input_file)

    prompt_template = prompt_file.read_text(encoding="utf-8")
    input_text = input_file.read_text(encoding="utf-8")

    if placeholder not in prompt_template:
        raise ValueError(
            f"Placeholder '{placeholder}' not found in {prompt_file}"
        )

    return prompt_template.replace(placeholder, input_text)
