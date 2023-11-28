#  install flask from pip3 using puppet
# Define a class for installing Flask
class install_flask {
  package { 'python3-pip':
    ensure => installed,
  }

  exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => ['/usr/bin'],
    require => Package['python3-pip'],
  }
}

# Include the class in the main manifest
include install_flask