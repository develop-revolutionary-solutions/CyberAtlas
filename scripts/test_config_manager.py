from assistant.config.manager import ConfigManager


def main() -> None:
    ConfigManager.load()

    print("Configuration loaded successfully.")

    print(ConfigManager._config)


if __name__ == "__main__":
    main()
