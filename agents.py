from swarm import Agent
from tools import list_projects, list_projects_with_details, get_project, create_project, delete_project, get_connection_uri, create_project_branch, list_project_branches, get_project_branch, delete_project_branch, get_current_user_info

def triage_instructions(context_variables):
    user_info = context_variables.get("user_info", None)
    user_projects = context_variables.get("user_projects", None)
    return f"""You are to triage a users request, and call a tool to transfer to the right intent.
    Once you are ready to transfer to the right intent, call the tool to transfer to the right intent.
    You dont need to know specifics, just the topic of the request.
    When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
    Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of user.
    The customer context is here: {user_info}, and their projects are here: {user_projects}"""

neon_agent = Agent(
    name="Neon Agent",
    instructions=triage_instructions,
    functions=[list_projects_with_details, get_project, create_project, delete_project, get_connection_uri, create_project_branch, list_project_branches, get_project_branch, delete_project_branch],
)