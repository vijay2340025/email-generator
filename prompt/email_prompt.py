def build_email_prompt(
    purpose: str,
    tone: str,
    recipient: str,
    key_points: str,
    length: str,
    language: str,
) -> tuple[str, str]:
    system_prompt = (
        "You are an email expert that you can writes clear, natural, "
        "ready-to-send emails.\n"
        "Rules:\n"
        "- Output ONLY the email (start with 'Subject: ...' followed by the body).\n"
        "- Match the requested tone, recipient relationship, length, and language.\n"
        "- Do not add outside facts or assumptions.\n"
        "- Use the provided key details accurately without providing any additional information."
    )

    LENGTH_GUIDANCE = {
        "Short": "Keep it concise around 3 to 5 sentences in the body.",
        "Medium": "Keep it clear and well-structured 1 to 3 short paragraphs.",
        "Detailed": "Provide thorough context, clear structure, and explicit next steps where helpful.",
    }

    details_block = key_points.strip() if key_points.strip() else "None provided."
    length_instruction = LENGTH_GUIDANCE.get(length, LENGTH_GUIDANCE["Medium"])

    user_prompt = (
        f"Write an email with the following specifications:\n"
        f"- Purpose: {purpose or 'General communication'}\n"
        f"- Tone: {tone}\n"
        f"- Recipient Type: {recipient}\n"
        f"- Language: {language}\n"
        f"- Length Guidance: {length_instruction}\n"
        f"- Key Details to Include:\n{details_block}"
    )

    return system_prompt, user_prompt
