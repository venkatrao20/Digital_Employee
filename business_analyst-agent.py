"""Multi-agent business analyst workflow orchestrated with LangGraph."""

import os
from typing import TypedDict

import ollama
from langgraph.graph import END, START, StateGraph


class AnalysisState(TypedDict, total=False):
    requirement: str
    requirements_analysis: str
    stories_analysis: str
    quality_analysis: str
    final_analysis: str


MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")


def ask_agent(role: str, task: str, requirement: str) -> str:
    """Run one specialist against the same source requirement."""
    prompt = f"""You are {role}, working as part of a Senior Business Analyst team.

Customer requirement:
{requirement}

Your task:
{task}

Do not invent facts. Mark assumptions clearly and identify missing information.
Return concise, professional markdown that another BA can use."""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


def intake_node(state: AnalysisState) -> AnalysisState:
    requirement = state.get("requirement", "").strip()
    if not requirement:
        raise ValueError("A customer requirement is required.")
    return {"requirement": requirement}


def requirements_node(state: AnalysisState) -> AnalysisState:
    return {
        "requirements_analysis": ask_agent(
            "the requirements analyst",
            "Extract the requirement summary, actors, functional and non-functional requirements, and explicit business rules.",
            state["requirement"],
        )
    }


def stories_node(state: AnalysisState) -> AnalysisState:
    return {
        "stories_analysis": ask_agent(
            "the product and user-story analyst",
            "Create prioritized user stories with Given/When/Then acceptance criteria. Keep each story traceable to the customer wording.",
            state["requirement"],
        )
    }


def quality_node(state: AnalysisState) -> AnalysisState:
    return {
        "quality_analysis": ask_agent(
            "the BA quality reviewer",
            "Identify assumptions, dependencies, ambiguities, risks, clarification questions, and a justified overall priority.",
            state["requirement"],
        )
    }


def synthesis_node(state: AnalysisState) -> AnalysisState:
    prompt = f"""You are the lead business analyst. Synthesize the three specialist reports below.

Source requirement:
{state['requirement']}

Requirements report:
{state['requirements_analysis']}

User stories report:
{state['stories_analysis']}

Quality report:
{state['quality_analysis']}

Produce one cohesive BA analysis with these headings:
1. Requirement Summary
2. Actors
3. User Stories
4. Acceptance Criteria
5. Functional Requirements
6. Non-Functional Requirements
7. Business Rules
8. Assumptions
9. Dependencies
10. Clarification Questions
11. Priority
12. BA Notes

Resolve duplication, preserve uncertainty, and never turn an assumption into a confirmed requirement."""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return {"final_analysis": response["message"]["content"]}


def build_graph():
    """Build a fan-out/fan-in workflow of specialist agents."""
    graph = StateGraph(AnalysisState)
    graph.add_node("intake", intake_node)
    graph.add_node("requirements_analyst", requirements_node)
    graph.add_node("stories_analyst", stories_node)
    graph.add_node("quality_reviewer", quality_node)
    graph.add_node("synthesizer", synthesis_node)

    graph.add_edge(START, "intake")
    graph.add_edge("intake", "requirements_analyst")
    graph.add_edge("intake", "stories_analyst")
    graph.add_edge("intake", "quality_reviewer")
    graph.add_edge("requirements_analyst", "synthesizer")
    graph.add_edge("stories_analyst", "synthesizer")
    graph.add_edge("quality_reviewer", "synthesizer")
    graph.add_edge("synthesizer", END)
    return graph.compile()


def run_analysis(requirement: str) -> str:
    """Run the multi-agent workflow and return the synthesized analysis."""
    result = build_graph().invoke({"requirement": requirement})
    return result["final_analysis"]


if __name__ == "__main__":
    print("=" * 60)
    print("       BUSINESS ANALYST MULTI-AGENT SYSTEM")
    print("=" * 60)
    requirement = input("\nEnter customer requirement:\n")
    try:
        print("\nRunning specialist agents and synthesizing their findings...\n")
        print(run_analysis(requirement))
        print("\n" + "=" * 60)
        print("             ANALYSIS COMPLETED")
        print("=" * 60)
    except Exception as error:
        print(f"\nSomething went wrong: {error}")

