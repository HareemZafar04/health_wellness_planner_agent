<<<<<<< HEAD
from agents import RunHooks, AgentHooks
from context import UserSessionContext

class LoggingRunHooks(RunHooks):
    def on_agent_start(self, agent, context):
        print(f"[HOOK] {agent.name} starting")

    def on_tool_end(self, tool, output, context):
        print(f"[HOOK] {tool.name} returned {output}")

class LoggingAgentHooks(AgentHooks):
    def on_start(self, agent, input, context):
        print(f"[AGENT HOOK] Received: {input}")

    def on_end(self, agent, response, context):
        print(f"[AGENT HOOK] Responded: {response}")
=======
from agents import RunHooks, AgentHooks
from context import UserSessionContext

class LoggingRunHooks(RunHooks):
    def on_agent_start(self, agent, context):
        print(f"[HOOK] {agent.name} starting")

    def on_tool_end(self, tool, output, context):
        print(f"[HOOK] {tool.name} returned {output}")

class LoggingAgentHooks(AgentHooks):
    def on_start(self, agent, input, context):
        print(f"[AGENT HOOK] Received: {input}")

    def on_end(self, agent, response, context):
        print(f"[AGENT HOOK] Responded: {response}")
>>>>>>> faa8bc7afdfe6f43f8569794d231ee58b8d13116
