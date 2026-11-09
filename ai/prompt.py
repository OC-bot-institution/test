import json

def load_personality():
    with open(
        "character/personality.json",
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def create_system_prompt():
    p = load_personality()

    return f"""
あなたは「{p['name']}」というキャラクターです。

【人物紹介】
{p['description']}

【性格】
{chr(10).join(p['personality'])}

【話し方】
{chr(10).join(p['speech_style'])}

【価値観】
{chr(10).join(p['values'])}

【行動方針】
{chr(10).join(p['behavior'])}

常にこの人格を維持してください。
単なる質問応答ではなく、
一人のキャラクターとして会話してください。
"""