from agents import *
from swarm.repl import run_demo_loop

if __name__ == "__main__":
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
    run_demo_loop(neon_agent, context_variables=context_variables, debug=True)