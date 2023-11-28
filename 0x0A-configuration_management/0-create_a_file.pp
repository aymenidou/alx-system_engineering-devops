# Puppet script that create a file in /tmp called school and contains text
file{'/tmp/school':
    content => 'I love Puppet',
    mode    => '0744',
    owner   => www-data,
    group   => www-data,
}