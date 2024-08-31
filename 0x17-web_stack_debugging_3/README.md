# Web Stack Debugging Task

This project involves debugging an Apache 500 Internal Server Error using `strace` and automating the fix using Puppet.

## Steps Taken

1. Used `strace` to attach to the Apache process and identify the cause of the 500 error.
2. Diagnosed the issue and manually fixed it to confirm the solution.
3. Automated the fix using Puppet to ensure it persists and can be reapplied as necessary.

## Files

- `0-strace_is_your_friend.pp`: Puppet manifest to fix the identified issue.

