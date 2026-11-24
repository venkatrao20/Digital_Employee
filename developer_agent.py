import ollama
import re
from pathlib import Path


# ============================================================
# PYTHON DEVELOPER AI AGENT
# ============================================================

print("=" * 70)
print("              PYTHON DEVELOPER AI AGENT V1")
print("=" * 70)


# ============================================================
# MULTI-LINE INPUT
# ============================================================

def get_multiline_input(title):

    print("\n" + "-" * 70)
    print(title)
    print("Paste your content below.")
    print("Type END on a new line when finished.")
    print("-" * 70)

    lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)


# ============================================================
# GET PRODUCT OWNER BACKLOG
# ============================================================

backlog = get_multiline_input(
    "PRODUCT OWNER BACKLOG"
)


# ============================================================
# GET SOLUTION ARCHITECTURE
# ============================================================

architecture = get_multiline_input(
    "SOLUTION ARCHITECTURE"
)


# ============================================================
# PROJECT NAME
# ============================================================

project_name = input(
    "\nEnter project name "
    "(example: shopping-cart): "
).strip()


if not project_name:

    project_name = "generated-python-project"


# ============================================================
# PYTHON PACKAGE NAME
# ============================================================

package_name = re.sub(
    r"[^a-zA-Z0-9_]",
    "_",
    project_name
).lower()


# Prevent package starting with number

if package_name and package_name[0].isdigit():

    package_name = "app_" + package_name


# ============================================================
# DEVELOPER PROMPT
# ============================================================

prompt = f"""
You are a Senior Python Software Developer working inside
an AI-powered Software Development Life Cycle (SDLC).

Your job is to implement the confirmed requirements provided
by the Product Owner and Solution Architect.

============================================================
PRODUCT OWNER BACKLOG
============================================================

{backlog}

============================================================
SOLUTION ARCHITECTURE
============================================================

{architecture}

============================================================

YOUR TASK
============================================================

Generate a complete Python backend application.

The implementation MUST follow the Product Owner backlog
and Solution Architecture.

Do NOT invent requirements.

Do NOT implement functionality that is not requested.

============================================================
TECHNOLOGY
============================================================

Use the following technology stack when appropriate:

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- MySQL
- Pydantic
- pytest

Use REST APIs where required.

============================================================
ARCHITECTURE
============================================================

Follow a clean layered architecture.

Recommended structure:

app/
    main.py

    api/
        routes/

    models/

    schemas/

    services/

    repositories/

    database/

    exceptions/

    config/

tests/

Use the architecture provided by the Solution Architect.

Do not create unnecessary layers if they are not required.

============================================================
DEVELOPMENT RULES
============================================================

1. Implement ONLY confirmed requirements.

2. Do NOT invent business functionality.

3. Do NOT add authentication unless required.

4. Do NOT add payment functionality unless required.

5. Do NOT add microservices.

6. Do NOT add unnecessary technologies.

7. Use clean Python architecture.

8. Use dependency injection where appropriate.

9. Use SQLAlchemy models for database entities.

10. Use Pydantic schemas for API request/response validation.

11. Use meaningful REST endpoint names.

12. Use appropriate HTTP status codes.

13. Add validation where appropriate.

14. Add exception handling.

15. Use type hints.

16. Use readable Python code.

17. Follow PEP 8 style.

18. Avoid unnecessary complexity.

19. Every Python module must be represented as a separate file.

20. Do not put multiple unrelated modules into one file.

21. Do not use placeholders.

22. Every generated file must contain usable code.

23. Do not generate fake implementations.

24. Do not generate TODO-only functions.

25. Ensure imports are correct.

26. Ensure modules can import each other correctly.

============================================================
DATABASE
============================================================

Use MySQL when database persistence is required.

Use SQLAlchemy for database access.

Generate database models and relationships ONLY from
confirmed requirements.

Do not invent database entities.

============================================================
API
============================================================

Implement the REST APIs required by the Product Owner.

Use:

GET
POST
PUT
DELETE

only when appropriate.

Use FastAPI.

Use Pydantic schemas for request and response models.

============================================================
TESTING
============================================================

Generate pytest tests for the implemented business logic
and REST APIs where appropriate.

Tests must correspond to confirmed requirements.

Do not invent unrelated test cases.

============================================================
CONFIGURATION
============================================================

Use environment variables for configuration values such as:

DATABASE_URL

Do NOT hardcode production passwords.

Generate:

.env.example

instead of committing real credentials.

============================================================
PROJECT STRUCTURE
============================================================

Generate a professional Python project.

Example:

{project_name}/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes/
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── repositories/
│   │
│   ├── database/
│   │
│   ├── exceptions/
│   │
│   └── config/
│
├── tests/
│
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore

Adjust this structure according to the actual requirements.

============================================================
OUTPUT FORMAT
============================================================

VERY IMPORTANT.

For EVERY file use EXACTLY this format:

===FILE: requirements.txt===

<complete file content>

===END FILE===

For Python files:

===FILE: app/main.py===

<complete Python code>

===END FILE===

For example:

===FILE: app/models/product.py===

<complete Python code>

===END FILE===

============================================================
OUTPUT RULES
============================================================

1. Do NOT put explanations between files.

2. Generate COMPLETE file contents.

3. Do NOT use Markdown code fences.

4. Do NOT use placeholders.

5. Do NOT use:

# add implementation

# implementation here

pass

TODO

unless technically required.

6. All imports must be valid.

7. All generated files must work together.

8. The project must be runnable.

9. The project must follow the Product Owner backlog.

10. The project must follow the Solution Architecture.

============================================================
REQUIREMENT TRACEABILITY
============================================================

Every implemented requirement must be traceable to the
Product Owner backlog.

Before generating the files, internally verify:

- Which requirement is being implemented?
- Which API implements it?
- Which service implements it?
- Which database model is required?
- Which tests verify it?

Do not implement functionality without a corresponding
requirement.

============================================================
FINAL VALIDATION
============================================================

Before producing the final output, internally verify:

1. All requirements are implemented.

2. No unrelated features are implemented.

3. All imports are correct.

4. All Python modules are syntactically valid.

5. API routes are connected to FastAPI.

6. Database models are correctly connected.

7. Pydantic schemas are correct.

8. Service and repository dependencies are correct.

9. Tests reference existing code.

10. The project structure is consistent.

============================================================
FINAL OUTPUT
============================================================

Generate the complete Python project files now.

Return ONLY the structured files.

Do not provide explanations.
"""


# ============================================================
# CALL OLLAMA
# ============================================================

print("\n")
print("=" * 70)
print("Generating Python project...")
print("Model: qwen2.5:3b")
print("Please wait...")
print("=" * 70)


try:

    response = ollama.chat(

        model="qwen2.5:3b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        options={
            "temperature": 0.1,
            "num_predict": 6000
        }
    )


    generated_code = response["message"]["content"]


    # ========================================================
    # DISPLAY OUTPUT
    # ========================================================

    print("\n")
    print("=" * 70)
    print("              GENERATED PYTHON PROJECT")
    print("=" * 70)

    print(generated_code)


    # ========================================================
    # CREATE PROJECT DIRECTORY
    # ========================================================

    output_directory = (
        Path("generated_projects")
        / project_name
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )


    # ========================================================
    # SAVE RAW AI OUTPUT
    # ========================================================

    raw_file = (
        output_directory
        / "developer_output.txt"
    )

    raw_file.write_text(
        generated_code,
        encoding="utf-8"
    )


    # ========================================================
    # REMOVE ACCIDENTAL MARKDOWN FENCES
    # ========================================================

    generated_code = re.sub(
        r"```(?:python|text|yaml|json|ini|toml|bash|shell)?\s*",
        "",
        generated_code,
        flags=re.IGNORECASE
    )

    generated_code = generated_code.replace(
        "```",
        ""
    )


    # ========================================================
    # EXTRACT FILES
    # ========================================================

    pattern = (
        r"===FILE:\s*(.*?)===\s*"
        r"(.*?)"
        r"===END FILE==="
    )

    matches = re.findall(
        pattern,
        generated_code,
        re.DOTALL
    )


    if not matches:

        print("\n")
        print("=" * 70)
        print("WARNING")
        print("=" * 70)

        print(
            "No structured files were detected."
        )

        print(
            f"Raw output saved at:\n"
            f"{raw_file.resolve()}"
        )


    else:

        print("\n")
        print("=" * 70)
        print("Creating Python project files...")
        print("=" * 70)


        created_files = []


        # ====================================================
        # CREATE FILES
        # ====================================================

        for filename, content in matches:

            filename = filename.strip()

            content = content.strip()


            # Normalize Windows path

            filename = filename.replace(
                "\\",
                "/"
            )


            # Prevent absolute paths

            if filename.startswith("/"):

                filename = filename.lstrip("/")


            # Prevent drive paths

            if re.match(
                r"^[A-Za-z]:",
                filename
            ):

                print(
                    f"Skipped unsafe file path: {filename}"
                )

                continue


            file_path = (
                output_directory
                / filename
            )


            # =================================================
            # SECURITY CHECK
            # =================================================

            try:

                file_path.resolve().relative_to(
                    output_directory.resolve()
                )

            except ValueError:

                print(
                    f"Skipped unsafe file path: {filename}"
                )

                continue


            # =================================================
            # CREATE PARENT DIRECTORIES
            # =================================================

            file_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )


            # =================================================
            # REMOVE EXTRA CODE FENCES
            # =================================================

            content = re.sub(
                r"^```[a-zA-Z0-9_-]*\s*",
                "",
                content
            )

            content = re.sub(
                r"\s*```$",
                "",
                content
            )


            # =================================================
            # WRITE FILE
            # =================================================

            file_path.write_text(
                content.strip() + "\n",
                encoding="utf-8"
            )


            created_files.append(
                filename
            )


            print(
                f"Created: {filename}"
            )


        # ====================================================
        # SUMMARY
        # ====================================================

        print("\n")
        print("=" * 70)
        print("       PYTHON DEVELOPER AGENT COMPLETED")
        print("=" * 70)


        print(
            f"\nProject created at:\n"
            f"{output_directory.resolve()}"
        )


        print(
            f"\nFiles created: "
            f"{len(created_files)}"
        )


        print("\nGenerated files:")


        for filename in created_files:

            print(
                f"  ✓ {filename}"
            )


        print("\n")
        print("=" * 70)
        print("NEXT STEP")
        print("=" * 70)


        print(
            "\nSend this generated project "
            "to the QA Agent."
        )


except Exception as e:

    print("\n")
    print("=" * 70)
    print("ERROR")
    print("=" * 70)

    print(
        f"\n{type(e).__name__}: {e}"
    )