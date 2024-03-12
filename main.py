import subprocess


def run_pytest():
    try:
        # 在这里执行 Pytest
        subprocess.run(["pytest", "tests/"])  # 替换为你的测试文件或目录路径
    except Exception as e:
        print(f"Error running Pytest: {e}")


def main():
    # 在这里执行你的主要操作
    print("Running main function")

    # 启动 Pytest
    run_pytest()


if __name__ == "__main__":
    main()
