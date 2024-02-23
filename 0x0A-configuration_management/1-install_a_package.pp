#  install puppet-lint.
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command  => '/usr/bin/pip3 install Flask==2.1.0',
  unless   => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  provider => 'shell',
  require  => Package['python3-pip'],
}
