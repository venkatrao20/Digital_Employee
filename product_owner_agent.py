import ollama

print("=" * 60)
print("        PRODUCT OWNER AI AGENT")
print("=" * 60)

requirement = input("\nEnter BA analysis / requirements:\n")

print("\nCreating product backlog... Please wait...\n")

prompt = f"""
You are a professional Agile Product Owner.

Analyze the following Business Analyst requirements:

{requirement}

Your job is to convert the requirements into a clear and prioritized product backlog.

IMPORTANT RULES:
- Do not invent customer requirements.
- Use only information provided in the input.
- Clearly identify assumptions.
- If information is missing, create clarification questions.
- Keep the response concise.
- Do not provide unnecessary explanations.

OUTPUT:

1. PRODUCT SUMMARY
Briefly describe the product/feature.

2. EPIC
Create the main epic.

3. PRODUCT BACKLOG

For each backlog item provide:

Story ID:
Title:
User Story:
Priority: P0 / P1 / P2
Business Value: High / Medium / Low

4. MVP SCOPE
List the features that should be included in the Minimum Viable Product.

5. FUTURE SCOPE
List features that may be considered later, only if supported by the requirements.

6. SPRINT RECOMMENDATION
Suggest how the backlog could be divided into sprints.

7. ASSUMPTIONS
List assumptions separately.

8. CLARIFICATION QUESTIONS
List questions the Product Owner should ask.

9. PRODUCT OWNER NOTES
Mention risks, dependencies, or ambiguities.
"""

try:
    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 1000
        }
    )

    print("=" * 60)
    print("              PRODUCT BACKLOG")
    print("=" * 60)
    print()

    print(response["message"]["content"])

    print()
    print("=" * 60)
    print("          PRODUCT OWNER ANALYSIS COMPLETED")
    print("=" * 60)

except Exception as e:
    print("\nSomething went wrong:")
    print(e)