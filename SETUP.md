
# Setup Guide

This guide will help you set up the `monitoring/sensehat` and `monitoring/camera-pi` applications on your Raspberry Pi.

## Prerequisites

- A Raspberry Pi with Raspbian installed.
- The `monitoring/sensehat` and `monitoring/camera-pi` directories are located in your Raspberry Pi.

## Steps

1. **Open a Terminal:** You can do this by searching for "Terminal" in your applications menu or by using a keyboard shortcut (usually `Ctrl+Alt+T`).

2. **Navigate to the `monitoring/sensehat` directory:** Use the `cd` command to change directories. Replace `/path/to/your/project` with the actual path to your project.

```bash
cd /path/to/your/project/monitoring/sensehat
```

3. **Make the `setup.sh` script executable:** This step is necessary only if the script is not already executable.

```bash
chmod +x setup.sh
```

4. **Run the `setup.sh` script:**

```bash
./setup.sh
```

5. **Repeat the process for the `monitoring/camera-pi` directory:** Once the `setup.sh` script in the `monitoring/sensehat` directory has finished running, you can repeat the process for the `monitoring/camera-pi` directory.

```bash
cd /path/to/your/project/monitoring/camera-pi
chmod +x setup.sh
./setup.sh
```

Please note that these scripts should be run on your Raspberry Pi, not on your MacBook. Also, these scripts might require superuser permissions to run certain commands. If you encounter permission errors, try running the scripts with `sudo`:

```bash
sudo ./setup.sh
```

Remember to replace `/path/to/your/project` with the actual path to your project.
