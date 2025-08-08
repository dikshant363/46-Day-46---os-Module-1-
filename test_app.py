import subprocess
import time
import os
import json

def test_app():
    # Clean up previous test runs
    if os.path.exists('assistant/tasks.json'):
        os.remove('assistant/tasks.json')

    # --- First run: Add a task ---
    print("--- Running Test: First Run (Add Task) ---")
    process1 = subprocess.Popen(
        ['python3', '-m', 'assistant.main'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1, # line buffered
        universal_newlines=True
    )

    # Interaction: list (empty), add task, list, exit
    commands1 = [
        '2', # list
        '1', # add
        'Test Task 1', # title
        'Testing', # category
        'High', # priority
        '2', # list
        '3'  # exit
    ]
    for cmd in commands1:
        process1.stdin.write(cmd + '\n')
        process1.stdin.flush()
        time.sleep(0.2)


    stdout1, stderr1 = process1.communicate(timeout=10)
    print("--- STDOUT ---")
    print(stdout1)
    print("--- STDERR ---")
    print(stderr1)

    if process1.returncode != 0:
        print("Test failed: Process returned non-zero exit code.")
        return

    # --- Verification 1: Check tasks.json ---
    print("\n--- Running Test: Verify tasks.json ---")
    if not os.path.exists('assistant/tasks.json'):
        print("Test failed: tasks.json was not created.")
        return

    with open('assistant/tasks.json', 'r') as f:
        tasks_data = json.load(f)

    if len(tasks_data) != 1:
        print(f"Test failed: Expected 1 task in tasks.json, but found {len(tasks_data)}.")
        return

    if tasks_data[0]['title'] != 'Test Task 1':
        print(f"Test failed: Unexpected task title '{tasks_data[0]['title']}'.")
        return

    print("tasks.json verification successful.")


    # --- Second run: Load task ---
    print("\n--- Running Test: Second Run (Load Task) ---")
    process2 = subprocess.Popen(
        ['python3', '-m', 'assistant.main'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    # Interaction: list (should show task), exit
    commands2 = [
        '2', # list
        '3'  # exit
    ]
    for cmd in commands2:
        process2.stdin.write(cmd + '\n')
        process2.stdin.flush()
        time.sleep(0.2)

    stdout2, stderr2 = process2.communicate(timeout=10)
    print("--- STDOUT ---")
    print(stdout2)
    print("--- STDERR ---")
    print(stderr2)

    if process2.returncode != 0:
        print("Test failed: Process returned non-zero exit code during second run.")
        return

    if "Test Task 1" not in stdout2:
        print("Test failed: Task was not loaded and listed in the second run.")
        return

    print("\n--- All tests passed! ---")


if __name__ == "__main__":
    test_app()
