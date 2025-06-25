def get_policy_prompt(policy_type):
    return f'''
You are an assistant summarizing a corporate {policy_type}.
Summarize the key points in the following areas:
- Purpose of the policy
- Rules mentioned (leave, work hours, conduct, etc.)
- Any compliance/legal mentions
- Summary in plain English

Text:
{{context}}
'''


def get_contract_prompt():
    return f"""
You are a legal assistant analyzing a corporate contract.

Please identify:
- Type of contract
- Key clauses (termination, IP, payment, etc.)
- Missing or vague sections
- Summarize everything in bullet points.

Text:
{context}
"""
