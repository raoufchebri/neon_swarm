# Neon Swarm

Neon Swarm is a set of tools and agents for interacting with Neon PostgreSQL databases. It leverages the power of [OpenAI Swarm Framework](https://github.com/openai/swarm) to simplify database operations, query generation, and project management.

## Features

- AI-powered database interaction
- Project management (create, list, delete projects)
- Branch management (create, list, delete branches)
- SQL query execution and generation
- Database schema retrieval
- Secure connection handling

## Installation

You can install Neon Swarm using pip:

```bash
pip install neon-swarm
```

## Agents

Neon Swarm provides three main agents:

1. **Neon Agent**: Handles project and branch management tasks.
2. **SQL Executor**: Executes SQL queries on your Neon databases.

## Usage

### Set up API keys

Before using Neon Swarm, make sure to set up your Neon and OpenAI API keys as environment variables:

```bash
export NEON_API_KEY='your_neon_api_key'
export OPENAI_API_KEY='your_openai_api_key'
```

### Initialize the Neon Agent

First, you can initialize the agent and provide the necessary context variables:

```python
from neon_swarm import neon_agent_init
from swarm.repl import run_demo_loop

neon_agent, context_variables = neon_agent_init()
run_demo_loop(agent=neon_agent, context_variables=context_variables, debug=True)

```

### Query PostgreSQL database outside of Neon

```python
from neon_swarm import sql_executor_agent_init
from swarm.repl import run_demo_loop

sql_executor_agent, context_variables = sql_executor_agent_init(connection_uri="your_connection_uri")
run_demo_loop(agent=sql_executor_agent, context_variables=context_variables, debug=True)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please file an issue on the [GitHub issue tracker](https://github.com/raoufchebri/neon_swarm/issues).

## Acknowledgements

- [Swarm](https://github.com/openai/swarm) for the Swarm Framework
- [OpenAI](https://openai.com) for the AI models powering the agents
- [Neon](https://neon.tech) for providing the serverless PostgreSQL platform
