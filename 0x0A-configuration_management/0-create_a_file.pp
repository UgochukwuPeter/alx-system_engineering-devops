# create a file in /tmp.
file { '/tmp/school':
ensure  =>'file',
path    =>'/tmp/school',
mode    =>'0744',
owner   =>'www-data',
group   =>'www-data',
content => 'I love Puppet'
}
