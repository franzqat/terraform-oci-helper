# terraform-oci-helper
Tool for working with OCI resources in Terraform.
It helps you to create the yml file for configurating the OCI resources.
Check the file tab.md for more information.

Output will be processed in file outfile.yml.

Create config yml file from resources in tab.md file.
Copy the resources from the tab that you want to generate into tab.md, then launch the script selecting the correct type and the counter that you wish to start from.

Use "--type" argument for these instance types: volume, instance, security-list

Use the "-c" or "--count" parameter as a counter to start the instance number from. It's just a indicator in the yaml file. Not used in terraform. eg. #1

# To run
Simply run the helper.py script using python3.

Example:
> python3 helper.py --type instance --count 1

> python3 helper.py --type volume --count 1

> python3 helper.py --type security-list --count 1
