# Task Management Guide - Pomodoro Timer

[Versión en Español](docs/TASKS_es.md)

## Introduction

The task management feature allows you to record and track your pomodoros associated with specific tasks. Each task records the number of work pomodoros, short and long breaks, as well as total time invested.

## How to Use

### 1. Set a Task

1. In the central text field, click and write your task name
2. Press **Enter** to set the task
3. The "✓ Complete" button will activate

### 2. Work on the Task

1. Press "Start" to begin a pomodoro
2. Work until the timer reaches 00:00
3. The pomodoro counter will increment automatically
4. Take short or long breaks as needed
5. Breaks are also counted automatically

### 3. Complete a Task

1. When you finish the task, press the **"✓ Complete"** button
2. The task will be saved to the `tasks.txt` file
3. Counters will reset for the next task

## Task File Format

Completed tasks are saved in `tasks.txt` with the following format:

```
"Task name" | Pomodoros | Short breaks | Long breaks | Total time
```

### Examples:

```
"CCOO Assembly" | 1 | 0 | 0 | 00:25:00
"Example task" | 2 | 2 | 0 | 01:00:00
"Another example task" | 3 | 2 | 1 | 01:40:00
```

### Total Time Calculation

Total time is automatically calculated based on:
- **Pomodoros**: Each counts as configured time (25 min by default)
- **Short breaks**: Each counts as configured time (5 min by default)
- **Long breaks**: Each counts as configured time (15 min by default)

**Calculation example:**
- 3 pomodoros + 2 short breaks + 1 long break
- = (3 × 25) + (2 × 5) + (1 × 15)
- = 75 + 10 + 15
- = 100 minutes = 01:40:00

**Note:** If you modify times in `config.yaml`, the calculation will use your custom values.

## On-Screen Statistics

At the bottom of the window you'll see:
- **Pomodoros: X** - Number of pomodoros completed in current task
- **Short breaks: X** - Number of short breaks completed
- **Long breaks: X** - Number of long breaks completed
- **Work time: XX:XX** - Total accumulated work time
- **Break time: XX:XX** - Total accumulated break time

**Important:** Counters increment automatically when the timer reaches 00:00. Paused or reset periods before finishing are not counted.

## Recommended Workflow

### Complete Session Example

1. **Start session**
   - Write "Develop feature X"
   - Press Enter

2. **First pomodoro**
   - Press "Start"
   - Work 25 minutes until it reaches 00:00
   - Counter increments automatically: Pomodoros: 1

3. **Short break**
   - Switch to "Short Break"
   - Press "Start"
   - Rest 5 minutes until it reaches 00:00
   - Counter increments automatically: Short breaks: 1

4. **Continue working**
   - Repeat the cycle 3 more times
   - After the 4th pomodoro, take a long break

5. **Complete task**
   - Press "✓ Complete"
   - Task is saved with: name, counters and calculated total time
   - Example saved: "Develop feature X" | 4 | 3 | 1 | 02:15:00

## Tips

### Effective Task Names

✅ **Good examples:**
- "Study Python chapter 5"
- "Write monthly report"
- "Review pull request #123"

❌ **Avoid:**
- "Work" (too generic)
- "Task" (not descriptive)
- Very long names (more than 50 characters)

### Managing Interruptions

If you're interrupted during a pomodoro:
1. Pause the timer
2. Handle the interruption
3. Reset if the interruption was long
4. Continue if it was brief

### Productivity Analysis

Periodically review your `tasks.txt` file to:
- Identify how long similar tasks take
- Improve future estimates
- Detect productivity patterns

## Troubleshooting

### Task not saving

**Problem:** Nothing happens when pressing "✓ Complete"

**Solutions:**
1. Verify you set a task name (pressed Enter)
2. Check write permissions in the directory
3. Verify `tasks.txt` file is not open in another program

### Counter not incrementing

**Problem:** Pomodoros are not counted

**Solutions:**
1. Make sure you set a task first
2. Let the timer reach 00:00 (don't stop it before)
3. Counter only increments when a complete period finishes

## File Location

By default, tasks are saved in:
```
pomodoro-py/tasks.txt
```

You can change the location by editing `config.yaml`:

```yaml
tasks:
  file: "my_tasks.txt"
```

## Import/Export Tasks

### Backup

```bash
# Windows
copy tasks.txt tasks_backup.txt

# Linux/macOS
cp tasks.txt tasks_backup.txt
```

### Analyze with Excel/Calc

1. Open `tasks.txt` with a text editor
2. Copy the content
3. Paste in Excel/Calc
4. Use "Data > Text to Columns"
5. Select "|" as delimiter

## See Also

- [README.md](README.md) - General documentation
- [CONFIG.md](docs/CONFIG.md) - Configuration guide
