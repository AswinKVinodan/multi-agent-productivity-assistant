# Multi-Agent Productivity Assistant

A multi-agent AI assistant built using multiple lightweight agents coordinated by a central orchestrator.

## Features
- Task prioritization  
- Habit and routine coaching  
- Productivity pattern analysis  
- Goal breakdown  
- Session memory + long-term user profile  
- Optional Gemini 2.5 model flash support  

## Structure

multi-agent-productivity-assistant/
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── task_priority_agent.py
│   ├── habit_coach_agent.py
│   ├── productivity_insights_agent.py
│   └── goal_escalation_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── task_database.py
│   ├── schedule_manager.py
│   ├── productivity_tracker.py
│   └── reflection_logger.py
│
├── memory/
│   ├── __init__.py
│   ├── session_memory.py
│   └── long_term_memory.py
│
├── orchestrator/
│   ├── __init__.py
│   └── lifestyle_coordinator.py
│
├── chat_demo/
│   ├── __init__.py
│   └── chat_console.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE (optional)
