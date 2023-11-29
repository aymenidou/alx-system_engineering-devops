# kills a process named killmenow
exec { 'install_flask':
  command => 'pkill --ns killmenow',
  path    => 'shell',
}
