import sys
from agents import Runner, RunContextWrapper
from context import UserSessionContext

try:
    from openai.types.responses import ResponseTextDeltaEvent
except ImportError:
    class ResponseTextDeltaEvent: pass

def _is_token_delta(ev) -> bool:
    return (
        ev.type == "raw_response_event"
        and isinstance(ev.data, ResponseTextDeltaEvent)
        and isinstance(ev.data.delta, str)
    )

async def stream_response(
    agent,
    prompt: str,
    ctx: RunContextWrapper[UserSessionContext],
) -> None:
    run_stream = Runner.run_streamed(agent, input=prompt, context=ctx)
    started = False

    async for ev in run_stream.stream_events():
        
        if _is_token_delta(ev):
            if not started:
                sys.stdout.write("\nAssistant: ")
                started = True
            sys.stdout.write(ev.data.delta)
            sys.stdout.flush()
            continue

        
        if ev.type == "raw_response_event":
            continue

        
        if ev.type == "run_item_stream_event":
            if ev.item.type == "message_output_item" and started:
                print()  # newline at end of assistant streaming
                started = False
            continue

        if ev.type == "agent_updated_stream_event":
            print(f"\n[Agent switched → {ev.new_agent.name}]")
