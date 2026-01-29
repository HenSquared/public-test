# Agent Session Task

## Overview

This implementation provides a simple yet functional agent session management system. It allows you to:
- Create and manage agent sessions
- Add and track tasks within sessions
- Monitor task completion status
- Generate session summaries

## Components

### AgentSession Class

Represents a single agent session with the following capabilities:
- Unique session ID generation
- Task management (add, complete, track)
- Session lifecycle management (active/closed status)
- Session summary reporting

### AgentSessionManager Class

Manages multiple agent sessions:
- Create new sessions
- Retrieve sessions by ID
- List all sessions (with optional filtering by agent ID)
- Close sessions

## Usage

### Running the Demo

```bash
python3 agent_session_task.py
```

This will run a demonstration showing:
1. Session creation
2. Task addition
3. Task completion
4. Session summary generation
5. Session listing
6. Session closure

### Using as a Library

```python
from agent_session_task import AgentSessionManager, AgentSession

# Create a manager
manager = AgentSessionManager()

# Create a session
session = manager.create_session("agent-001", "My Session")

# Add tasks
task_id = session.add_task("Complete code review", priority="high")

# Complete a task
session.complete_task(task_id)

# Get summary
summary = session.get_session_summary()
print(summary)

# Close session
manager.close_session(session.session_id)
```

## Features

- **UUID-based Identification**: Each session and task has a unique UUID
- **Timestamp Tracking**: Creation and completion times are tracked
- **Priority Levels**: Tasks can be assigned priority levels
- **Status Management**: Sessions and tasks have status tracking
- **Summary Reports**: Generate detailed summaries of session activity

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Example Output

```
============================================================
Agent Session Task Demo
============================================================

1. Creating a new agent session...
   Created session: abc123...
   Session name: Code Review Session

2. Adding tasks to the session...
   Added 3 tasks

3. Completing tasks...
   Completed 2 tasks

4. Session Summary:
   session_id: abc123...
   session_name: Code Review Session
   agent_id: agent-001
   status: active
   created_at: 2026-01-29T14:59:00
   total_tasks: 3
   completed_tasks: 2
   pending_tasks: 1

5. Listing all sessions:
   Total sessions: 1
   - Code Review Session (active)

6. Closing session...
   Session status: closed

============================================================
Demo completed successfully!
============================================================
```

## License

This is a test implementation for demonstration purposes.
