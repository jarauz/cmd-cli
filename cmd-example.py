import cmd

class MyCMD(cmd.Cmd):
  intro = "Welcome to my CLI. Type 'help' or '?' for help."
  prompt = "> "

  def do_hello(self, arg):
    """Greets the user with a personalized message."""
    if arg:
      print(f"Hello, {arg}!")
    else:
      print("Hello!")

  def do_list(self, arg):
    """Lists available commands."""
    print("Available commands:")
    for cmd in self.get_names():
      if not cmd.startswith('do_'):
        continue
      print(f"- {cmd[3:]}")

  def do_quit(self, arg):
    """Exits the CLI."""
    print("Goodbye!!!!!!!")
    raise SystemExit

if __name__ == '__main__':
  MyCMD().cmdloop()
