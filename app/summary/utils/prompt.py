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


def get_contract_prompt(contract_type):
    return f"""
You are a given detailed and structured corporate Contract summarization assistant.

Your task is to analyze a section of a {contract_type} document and extract the following **clearly and completely**:

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

Contract Text:
{{context}}
"""


def final_contract_prompt(policy_type):
    return f"""
        You are a Professional Policy analyst.

        You will be given a set of summarized {policy_type} contract. Your task is to write a refined summary with:
        - ✅ Clear explanation of the **purpose** of the Policy.
        - ✅ **Bullet-point list of specific rules** mentioned, grouped by category (leave, working hours, conduct, dress code, etc.)
        - ✅ Include within  the summaries and bullet-point **any specific numbers, durations, or legal names** found (e.g., "12 casual leaves", "under Payment of Wages Act, 1936")
        - ✅ Include a list of **legal mentions or compliance statements**
        - ✅ Write a elaborated **plain-English summary for non-legal readers**

        Respond in **clear, structured markdown**.
        Example :
        Purpose: To define rules for employee conduct and operational clarity.
        Rules:
            - Employees must work from 9:30am to 6:00pm, Monday–Saturday.
            - Lunch break is 1 hour.
            - 18 earned leaves per year; casual leaves pro-rated if joined mid-year.
            - Dress code is mandatory business casual.
        Compliance: Complies with the Contract Act (1872), Minimum Wage Act (1948), ESI Act.
        Summary : Elaborated union summary of context given here.
        Summarized Chunks:
        {{context}}
        """


def final_policy_prompt(policy_type):
    return f"""
        You are a Professional Contract analyst.

        You will be given a set of summarized {policy_type} contract. Your task is to write a refined summary with:
        - ✅ Clear explanation of the **purpose** of the Contract
        - ✅ **Bullet-point list of specific rules** mentioned, grouped by category (leave, working hours, conduct, dress code, etc.)
        - ✅ Include within  the summaries and bullet-point **any specific numbers, durations, or legal names** found (e.g., "12 casual leaves", "under Payment of Wages Act, 1936")
        - ✅ Include a list of **legal mentions or compliance statements**
        - ✅ Write a elaborated **plain-English summary for non-legal readers**

        Respond in **clear, structured markdown**.
        Example :
        Purpose: To define rules for employee conduct and operational clarity.
        Rules:
            - Employees must work from 9:30am to 6:00pm, Monday–Saturday.
            - Lunch break is 1 hour.
            - 18 earned leaves per year; casual leaves pro-rated if joined mid-year.
            - Dress code is mandatory business casual.
        Compliance: Complies with the Contract Act (1872), Minimum Wage Act (1948), ESI Act.
        Summary : Elaborated union summary of context given here.
        Summarized Chunks:
        {{context}}
        """
