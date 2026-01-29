#!/usr/bin/env python3
"""
Agent Session Task
A simple implementation of an agent session management system.
"""

import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class TaskStatus(Enum):
    """Task status enumeration."""
    PENDING = "pending"
    COMPLETED = "completed"


class SessionStatus(Enum):
    """Session status enumeration."""
    ACTIVE = "active"
    CLOSED = "closed"


class TaskPriority(Enum):
    """Task priority enumeration."""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


class AgentSession:
    """Represents a single agent session."""
    
    def __init__(self, agent_id: str, session_name: str = ""):
        self.session_id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.session_name = session_name or f"Session-{self.session_id[:8]}"
        self.created_at = datetime.now().isoformat()
        self._tasks: List[Dict] = []
        self.status = SessionStatus.ACTIVE.value
    
    def add_task(self, task_description: str, priority: str = "normal") -> str:
        """Add a new task to the session."""
        # Validate priority
        valid_priorities = [p.value for p in TaskPriority]
        if priority not in valid_priorities:
            priority = TaskPriority.NORMAL.value
        
        task_id = str(uuid.uuid4())
        task = {
            "task_id": task_id,
            "description": task_description,
            "priority": priority,
            "status": TaskStatus.PENDING.value,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        self._tasks.append(task)
        return task_id
    
    def complete_task(self, task_id: str) -> bool:
        """Mark a task as completed."""
        for task in self._tasks:
            if task["task_id"] == task_id:
                task["status"] = TaskStatus.COMPLETED.value
                task["completed_at"] = datetime.now().isoformat()
                return True
        return False
    
    def get_tasks(self) -> List[Dict]:
        """Get a copy of all tasks."""
        return self._tasks.copy()
    
    def get_session_summary(self) -> Dict:
        """Get a summary of the session."""
        completed = sum(1 for task in self._tasks if task["status"] == TaskStatus.COMPLETED.value)
        pending = sum(1 for task in self._tasks if task["status"] == TaskStatus.PENDING.value)
        
        return {
            "session_id": self.session_id,
            "session_name": self.session_name,
            "agent_id": self.agent_id,
            "status": self.status,
            "created_at": self.created_at,
            "total_tasks": len(self._tasks),
            "completed_tasks": completed,
            "pending_tasks": pending
        }
    
    def close_session(self):
        """Close the session."""
        self.status = SessionStatus.CLOSED.value


class AgentSessionManager:
    """Manages multiple agent sessions."""
    
    def __init__(self):
        self.sessions: Dict[str, AgentSession] = {}
    
    def create_session(self, agent_id: str, session_name: str = "") -> AgentSession:
        """Create a new agent session."""
        session = AgentSession(agent_id, session_name)
        self.sessions[session.session_id] = session
        return session
    
    def get_session(self, session_id: str) -> Optional[AgentSession]:
        """Retrieve a session by ID."""
        return self.sessions.get(session_id)
    
    def list_sessions(self, agent_id: Optional[str] = None) -> List[AgentSession]:
        """List all sessions, optionally filtered by agent_id."""
        if agent_id:
            return [s for s in self.sessions.values() if s.agent_id == agent_id]
        return list(self.sessions.values())
    
    def close_session(self, session_id: str) -> bool:
        """Close a session."""
        session = self.get_session(session_id)
        if session:
            session.close_session()
            return True
        return False


def demo():
    """Demonstrate the agent session task system."""
    print("=" * 60)
    print("Agent Session Task Demo")
    print("=" * 60)
    
    # Create a session manager
    manager = AgentSessionManager()
    
    # Create a new session for an agent
    print("\n1. Creating a new agent session...")
    session = manager.create_session("agent-001", "Code Review Session")
    print(f"   Created session: {session.session_id}")
    print(f"   Session name: {session.session_name}")
    
    # Add tasks to the session
    print("\n2. Adding tasks to the session...")
    task1_id = session.add_task("Review pull request #123", "high")
    task2_id = session.add_task("Run automated tests", "high")
    task3_id = session.add_task("Update documentation", "normal")
    print(f"   Added {len(session.get_tasks())} tasks")
    
    # Complete some tasks
    print("\n3. Completing tasks...")
    session.complete_task(task1_id)
    session.complete_task(task2_id)
    print(f"   Completed 2 tasks")
    
    # Get session summary
    print("\n4. Session Summary:")
    summary = session.get_session_summary()
    for key, value in summary.items():
        print(f"   {key}: {value}")
    
    # List all sessions
    print("\n5. Listing all sessions:")
    all_sessions = manager.list_sessions()
    print(f"   Total sessions: {len(all_sessions)}")
    for s in all_sessions:
        print(f"   - {s.session_name} ({s.status})")
    
    # Close the session
    print("\n6. Closing session...")
    manager.close_session(session.session_id)
    print(f"   Session status: {session.status}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
