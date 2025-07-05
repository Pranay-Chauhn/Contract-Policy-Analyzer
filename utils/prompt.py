def get_policy_prompt(policy_type):
    return f"""
You are a detailed and structured corporate policy summarization assistant.

Your task is to analyze a section of a {policy_type} document and extract the following **clearly and completely**:

---

### 1. 📌 Purpose (if applicable)
- What is the purpose or intent described in this section?

### 2. 📋 Rules / Guidelines
- Extract **all specific rules, procedures, and processes**
- Use bullet points
- Include any **quantitative values** like:
  - Number of leaves
  - Working hours
  - Allowed lateness
  - Notice periods
  - Salary deductions
  - Attendance rules
- If something is vague, note it as such (e.g., “notice period mentioned, but duration not specified”)

### 3. ⚖️ Legal / Compliance Mentions
- List any legal references (e.g., “Contract Act, 1872”, “Minimum Wages Act, 1948”)
- Mention statutory guidelines if any
- Say “None mentioned” if not found

### 4. 📝 Extra Notes (optional)
- Anything important like values, mission statements, ethics, or onboarding steps

---

**Respond in markdown format.**
Use clear bullet points and subheadings where necessary.

Policy Text:
{{context}}
"""



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
