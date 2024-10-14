from Swarm import Agent
from .agents import neon_agent, sql_executor
from src.neon_swarm.tools import get_current_user_info, list_projects

def neon_agent_init() -> tuple[Agent, dict]:
    user_info = get_current_user_info()
    user_projects = list_projects()
    context_variables = {
        "user_info": f"""Here is what you know about the user's info:
        {user_info}
        """,
        "user_projects": f"""Here is what you know about the user's projects:
        {user_projects}
        """,
    }
    return neon_agent, context_variables


def sql_executor_init(connection_uri: str) -> tuple[Agent, dict]:
    context_variables = {
        "connection_uri": connection_uri
    }
    return sql_executor, context_variables

