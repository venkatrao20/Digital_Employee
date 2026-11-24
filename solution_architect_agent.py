import ollama

print("=" * 60)
print("       SOLUTION ARCHITECT AI AGENT")
print("=" * 60)

backlog = input("\nEnter Product Owner backlog / requirements:\n")

print("\nDesigning solution architecture... Please wait...\n")

prompt = f"""
You are a professional Senior Solution Architect.

Analyze the following Product Owner backlog:

{backlog}

Design a practical software architecture for the confirmed requirements.

IMPORTANT RULES:

- Do NOT invent business requirements.
- Do NOT add authentication unless the input requires it.
- Do NOT add payment, shipping, discounts, notifications, or other features
  unless they are explicitly present in the input.
- Clearly separate technical assumptions from confirmed requirements.
- Keep the architecture simple and suitable for an MVP.
- Use Java and Spring Boot for the backend.
- Use React for the frontend.
- Use MySQL for the database.
- Use REST APIs.
- Use a modular monolith architecture unless the requirements clearly justify
  another architecture.
- Do not recommend Kubernetes for this simple MVP.
- Do not recommend an API Gateway unless multiple independently deployed
  services are required.
- Do not invent exact performance numbers.
- Keep the response concise but technically useful.

OUTPUT:

1. SOLUTION OVERVIEW

Briefly explain the proposed technical solution.

2. ARCHITECTURE STYLE

Explain why Modular Monolith is appropriate.

3. SYSTEM COMPONENTS

List the components.

For each component provide:

Component:
Responsibility:

Consider:

- React Frontend
- Spring Boot Backend
- Controller Layer
- Service Layer
- Repository Layer
- MySQL Database

Only include components that are actually needed.

4. TECHNOLOGY STACK

Frontend:
Backend:
Programming Language:
Framework:
Database:
API:
Testing:
Version Control:
Build Tool:
Deployment:

5. HIGH-LEVEL ARCHITECTURE

Show the architecture using arrows.

The normal request flow should be:

User
→ React Frontend
→ REST Controller
→ Service Layer
→ Repository Layer
→ MySQL Database

For responses:

MySQL Database
→ Repository
→ Service
→ Controller
→ React Frontend
→ User

6. DATABASE DESIGN

Identify only the tables required by the confirmed requirements.

For each table provide:

Table:
Important Fields:
Purpose:

7. API DESIGN

Suggest REST APIs for the confirmed requirements.

For each API provide:

Method:
Endpoint:
Purpose:

8. DATA FLOW

Explain the data flow for:

- Adding a product to the cart
- Changing product quantity
- Removing a product
- Displaying the total price

9. PROJECT STRUCTURE

Suggest a Spring Boot project structure.

Example:

src/main/java
    controller
    service
    repository
    entity
    dto

Only include packages that are useful.

10. SECURITY CONSIDERATIONS

Only mention security considerations relevant to the current
requirements. Do not invent authentication requirements.

11. SCALABILITY CONSIDERATIONS

List simple and reasonable scalability considerations.

12. TECHNICAL ASSUMPTIONS

Clearly list assumptions made by the architect.

13. RISKS AND DEPENDENCIES

List technical risks and dependencies.

14. ARCHITECT RECOMMENDATION

Give a short final recommendation.
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
            "temperature": 0.1,
            "num_predict": 1200
        }
    )

    print("=" * 60)
    print("           SOLUTION ARCHITECTURE")
    print("=" * 60)
    print()

    print(response["message"]["content"])

    print()
    print("=" * 60)
    print("       ARCHITECTURE DESIGN COMPLETED")
    print("=" * 60)

except Exception as e:
    print("\nSomething went wrong:")
    print(e)
