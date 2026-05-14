# Troubleshooting Episode 1

pyATS and SSH are powerful, but the first connection can fail for very ordinary reasons. Start simple and check one thing at a time.

## Wrong IP Address

If Avi cannot reach the device, confirm that the IP address in `testbed.yaml` is correct.

Try:

```bash
ping 192.168.1.10
```

Replace `192.168.1.10` with your device IP.

## SSH Is Not Enabled

The device must accept SSH connections from your computer.

Try connecting manually:

```bash
ssh admin@192.168.1.10
```

If manual SSH does not work, pyATS will not work yet either.

## Wrong Username or Password

Check the `credentials.default` section in `testbed.yaml`.

```yaml
credentials:
  default:
    username: admin
    password: cisco123
```

Make sure these match your lab device.

## Enable Password Problems

Some IOS-XE devices require enable mode before running certain commands. Episode 1 includes an enable password in the example testbed.

Check:

```yaml
credentials:
  enable:
    password: cisco123
```

If your device does not use an enable password, adjust your local `testbed.yaml` for your lab.

## Hostname Learning Issues

Episode 1 uses:

```python
learn_hostname=True
```

This lets Unicon learn the real device hostname after login. If the prompt is unusual, hostname learning can fail.

Things to check:

- Does the device prompt look normal?
- Are you landing in the expected CLI mode?
- Can you SSH manually and run `show ip interface brief`?

## Wrong `os` Value

For Cisco IOS-XE, the testbed should use:

```yaml
os: iosxe
```

If the `os` value is wrong, pyATS/Unicon may use the wrong connection behavior.

## Testbed YAML Indentation Problems

YAML is indentation-sensitive. Spaces matter.

Run:

```bash
pyats validate testbed testbed.yaml
```

If validation fails, compare your local file with `testbed.example.yaml`.

## Device Prompt Issues

Unicon expects to recognize the device prompt. If your device has banners, unusual login messages, or a custom prompt, the connection may need extra tuning later.

For Episode 1, keep the lab device as standard as possible.

## Basic Checklist

Try these in order:

```bash
ping 192.168.1.10
ssh admin@192.168.1.10
pyats validate testbed testbed.yaml
python avi_pilot_01_pyats.py
```

If the manual SSH test fails, fix SSH access first. If the pyATS validation fails, fix the YAML next. If both pass but the script fails, read the error and check the device prompt or credentials.
