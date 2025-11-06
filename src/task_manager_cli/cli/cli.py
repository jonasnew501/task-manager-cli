import argparse

from src.task_manager_cli.core.taskRepository import TaskRepository
from src.task_manager_cli.core.taskManager import TaskManager



class CLI:
    def __init__(self) -> None:
        self.taskManager = TaskManager(taskRepository=TaskRepository())



    def run(self):
        self._print_welcome_message()

        while True:
            user_input = self.get_user_input_clean()

            if user_input in ["quit"]:
                print("Goodbye!")
                break

            self._handle_command(user_input)
    
    def _handle_command(self, user_input: str):
        pass

    

    def get_user_input_clean(self):
        user_input_raw = self._get_raw_user_input()
        user_input_stripped = self._remove_leading_and_trailing_whitespaces_string(string=user_input_raw)
        user_input_stripped_and_lowercase = self._turn_string_lowercase(string=user_input_stripped)

        return user_input_stripped_and_lowercase


    def _get_raw_user_input(self) -> str:
        user_input = input(">> ")
        return user_input
    
    def _remove_leading_and_trailing_whitespaces_string(self, string: str) -> str:
        return string.strip()

    def _turn_string_lowercase(self, string: str) -> str:
        return string.lower()
    
    
    def _print_welcome_message(self):
        print("Welcome to Task Manager CLI! Type 'help' for commands, 'quit' to exit.")





def main():
    # Setup the argument parser
    parser = argparse.ArgumentParser(
        description="Simple CLI tool to create text files with rollback on error."
    )

    # Define command-line arguments
    parser.add_argument(
        "--text", required=True, help="The text content to write into the file"
    )
    parser.add_argument(
        "--filename",
        required=True,
        help="Name of the text file to create (e.g. output.txt)",
    )

    args = parser.parse_args()

    # Calling the class
    TextfileWriter.process_textfile(text_to_write=args.text, file_path=args.filename)

    # (optionally): Printing the output of the method-call
    # print(f"✅ File processed successfully: {result}")


if __name__ == "__main__":
    main()
