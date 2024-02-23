# changes to our configuration file ssh_config

file_line { 'IdentityFile':
line => 'IdentityFile ~/.ssh/holberton',
path => '/etc/ssh/ssh_config'
}

file_line { 'PasswordAuthentication':
line => 'PasswordAuthentication no',
path => '/etc/ssh/ssh_config'
}
