This is an example template. Please overwrite **this entire file, header included**, with the content that you need to format respecting the tab pattern below
### Instance example
| NAME           | IP        | PublicIP | Shape               | OCPU count | Memory | AD   | FD   | DISK(GB) | Tag         |
| -------------- | --------- | :------: | ------------------- | ---------- | ------ | ---- | ---- | -------- | ----------- |
| instance-name1 | 0.0.0.101 |   TBD    | VM.Standard.E3.Flex | 2          | 4      | AD-1 | FD-1 | 100      | example-tag |
| instance-name2 | 0.0.0.102 |   TBD    | VM.Standard.E3.Flex | 4          | 8      | AD-2 | FD-2 | 100      | example-tag |
| instance-name3 | 0.0.0.103 |   TBD    | VM.Standard.E4.Flex | 8          | 16     | AD-1 | FD-1 | 200      | example-tag |
| instance-name4 | 0.0.0.104 |   TBD    | VM.Standard.E4.Flex | 16         | 32     | AD-2 | FD-2 | 300      | example-tag |
### Volume example
| NAME        | SIZE | VPUs/GB | Filesystem | Attached instance | Application |
| ----------- | ---- | ------- | ---------- | ----------------- | ----------- |
| volume-name | 100  | 10      | xfs        | instance-name1    | example-app |
| volume-name | 100  | 10      | xfs        | instance-name2    | example-app |
| volume-name | 100  | 10      | xfs        | instance-name3    | example-app |
| volume-name | 100  | 10      | xfs        | instance-name4    | example-app |
### Security list Example
| DESCRIPTION | SOURCE         | TCP PORT MIN | TCP PORT MIN |
| ----------- | -------------- | ------------ | ------------ |
| rule-name   | 123.123.0.0/24 | 1234         | 1234         |
| rule-name   | 123.123.0.0/24 | 2222         | 2222         |
| rule-name   | 123.123.0.0/24 | 1111         | 1111         |
| rule-name   | 123.123.0.0/24 | 4444         | 4444         |