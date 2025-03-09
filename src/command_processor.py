#!/usr/bin/env python3

class CommandProcessor:
    """Processes and executes voice commands"""
    
    def __init__(self):
        self.commands = {}
        self._register_default_commands()
    
    def _register_default_commands(self):
        """Register default system commands"""
        self.commands = {
            "open": self._handle_open,
            "search": self._handle_search,
            "play": self._handle_play,
            "stop": self._handle_stop,
            "help": self._handle_help
        }
    
    def register_command(self, command_name, handler_function):
        """Register a new command with a handler function"""
        self.commands[command_name] = handler_function
    
    def process_command(self, command_text):
        """Process a text command and execute the associated action"""
        # Simple command parsing logic
        words = command_text.lower().split()
        if not words:
            return "No command received"
        
        command = words[0]
        args = words[1:]
        
        if command in self.commands:
            return self.commands[command](args)
        else:
            return f"Unknown command: {command}"
    
    # Default command handlers
    def _handle_open(self, args):
        return f"Opening {' '.join(args)}"
    
    def _handle_search(self, args):
        return f"Searching for {' '.join(args)}"
    
    def _handle_play(self, args):
        return f"Playing {' '.join(args)}"
    
    def _handle_stop(self, args):
        return f"Stopping {' '.join(args) if args else 'current task'}"
    
    def _handle_help(self, args):
        return f"Available commands: {', '.join(self.commands.keys())}"
