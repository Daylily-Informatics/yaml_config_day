import os
import yaml

class ProjectConfigManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.config_file_path = os.path.expanduser(f"~/.config/{self.project_name}.yml")

    def get_config(self):
        """
        Load the project configuration from the YAML file.
        """
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, "r") as file:
                return yaml.safe_load(file)
        else:
            return {}

    def set_config(self, username, access_key, secret_access_key):
        """
        Save the project configuration to the YAML file.
        """
        config = {
            "username": username,
            "access_key": access_key,
            "secret_access_key": secret_access_key,
        }

        with open(self.config_file_path, "w") as file:
            yaml.dump(config, file, default_flow_style=False)

    def clear_config(self):
        """
        Remove the project configuration file.
        """
        if os.path.exists(self.config_file_path):
            os.remove(self.config_file_path)

def main():
    project_name = "my_project"
    config_manager = ProjectConfigManager(project_name)

    while True:
        print("1. Set project configuration")
        print("2. Get project configuration")
        print("3. Clear project configuration")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            access_key = input("Enter access key: ")
            secret_access_key = input("Enter secret access key: ")
            config_manager.set_config(username, access_key, secret_access_key)
            print("Configuration saved.")
        elif choice == "2":
            config = config_manager.get_config()
            if config:
                print("Project Configuration:")
                print(f"Username: {config['username']}")
                print(f"Access Key: {config['access_key']}")
                print(f"Secret Access Key: {config['secret_access_key']}")
            else:
                print("No configuration found.")
        elif choice == "3":
            config_manager.clear_config()
            print("Configuration cleared.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
