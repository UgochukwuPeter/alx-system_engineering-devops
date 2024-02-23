# 0x0A Configuration management
This project shows what is configuration management about, how it works and how to implement with Puppet tool.

# Install puppet-lint
    $ apt-get install -y ruby
    $ gem install puppet-lint -v 2.1.1

# 0. Create a file
Using Puppet, create a file in /tmp.

Requirements:

* File path is /tmp/holberton
* File permission is 0744
* File owner is www-data
* File group is www-data
* File contains I love Puppet

Repo:
* File: 0-create_a_file.pp

# 1. Install a package
Using Puppet, install puppet-lint.

Requirements:

* Install puppet-lint
* Version must be 2.1.1

Repo:
* File: 1-install_a_package.pp


# 2. Execute a command
Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

* Must use the exec Puppet resource
* Must use pkill

Repo:
* File: 2-execute_a_command.pp


# AUTHOR

Pablo Andres Urbano -